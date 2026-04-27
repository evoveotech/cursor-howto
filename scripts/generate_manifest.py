#!/usr/bin/env python3
"""Generate a machine-readable content manifest for the cursor-howto repository.

The manifest captures every module, skill, plugin, command, and resource with
metadata (title, level, estimated time, dependencies).  It is the single source
of truth for:

* Build pipelines (EPUB, future HTML/PDF)
* Validation scripts (structure, freshness)
* Contributor tooling ("what's missing?")
* Future search / website generation

Usage::

    python scripts/generate_manifest.py              # write to content-manifest.json
    python scripts/generate_manifest.py --check      # validate existing manifest
    python scripts/generate_manifest.py --pretty     # indented JSON output
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from lib.discovery import iter_md_files, iter_numbered_dirs


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class ContentItem:
    """A single piece of content (file or directory entry)."""

    id: str
    title: str
    path: str
    type: str  # 'module', 'skill', 'plugin', 'command', 'resource', 'doc'
    level: str | None = None  # 'beginner', 'intermediate', 'advanced'
    estimated_minutes: int | None = None
    depends_on: list[str] = field(default_factory=list)
    has_mermaid: bool = False
    has_code_blocks: bool = False


@dataclass
class Manifest:
    """Root manifest object."""

    schema_version: str = "1.0"
    total_modules: int = 0
    total_skills: int = 0
    total_plugins: int = 0
    total_commands: int = 0
    items: list[ContentItem] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "total_modules": self.total_modules,
            "total_skills": self.total_skills,
            "total_plugins": self.total_plugins,
            "total_commands": self.total_commands,
            "items": [asdict(i) for i in self.items],
        }


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------


def extract_title(content: str, fallback: str) -> str:
    """First H1 heading, or *fallback*."""
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def extract_level(content: str) -> str | None:
    """Infer difficulty level from content keywords."""
    lowered = content.lower()
    if "advanced" in lowered or "expert" in lowered:
        return "advanced"
    if "intermediate" in lowered:
        return "intermediate"
    if "beginner" in lowered or "getting started" in lowered:
        return "beginner"
    return None


def extract_time(content: str) -> int | None:
    """Look for ``~N hours`` or ``~N min`` patterns and return minutes."""
    m = re.search(r"[~≈]?\s*(\d+(?:\.\d+)?)\s*hours?", content, re.IGNORECASE)
    if m:
        return int(float(m.group(1)) * 60)
    m = re.search(r"[~≈]?\s*(\d+)\s*min", content, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def scan_file(path: Path, content_type: str) -> ContentItem:
    """Create a ``ContentItem`` by scanning a single markdown file."""
    content = path.read_text(encoding="utf-8")
    rel = str(path.relative_to(Path()))
    return ContentItem(
        id=path.stem,
        title=extract_title(content, path.stem.replace("-", " ").title()),
        path=rel,
        type=content_type,
        level=extract_level(content),
        estimated_minutes=extract_time(content),
        has_mermaid="```mermaid" in content,
        has_code_blocks="```" in content,
    )


# ---------------------------------------------------------------------------
# Scanners
# ---------------------------------------------------------------------------


def scan_modules(root: Path) -> list[ContentItem]:
    """Scan numbered tutorial directories ``01-*`` … ``10-*``."""
    items: list[ContentItem] = []
    for d in iter_numbered_dirs(root):
        readme = d / "README.md"
        if readme.exists():
            item = scan_file(readme, "module")
            item.id = d.name
            items.append(item)
        # Scan sub-files
        for sub in sorted(d.rglob("*.md")):
            if sub.name == "README.md":
                continue
            if any(part.startswith(".") for part in sub.relative_to(root).parts):
                continue
            item = scan_file(sub, "module_section")
            item.id = f"{d.name}/{sub.stem}"
            items.append(item)
    return items


def scan_skills(root: Path) -> list[ContentItem]:
    """Scan ``03-skills/`` sub-directories."""
    items: list[ContentItem] = []
    skills_dir = root / "03-skills"
    if not skills_dir.exists():
        return items
    for d in sorted(skills_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        skill_md = d / "SKILL.md"
        if skill_md.exists():
            item = scan_file(skill_md, "skill")
            item.id = f"skill:{d.name}"
            items.append(item)
    return items


def scan_plugins(root: Path) -> list[ContentItem]:
    """Scan ``07-plugins/`` sub-directories."""
    items: list[ContentItem] = []
    plugins_dir = root / "07-plugins"
    if not plugins_dir.exists():
        return items
    for d in sorted(plugins_dir.iterdir()):
        if not d.is_dir() or d.name.startswith(".") or d.name == "README.md":
            continue
        readme = d / "README.md"
        if readme.exists():
            item = scan_file(readme, "plugin")
            item.id = f"plugin:{d.name}"
            items.append(item)
    return items


def scan_commands(root: Path) -> list[ContentItem]:
    """Scan ``01-slash-commands/`` for individual command definitions."""
    items: list[ContentItem] = []
    cmds_dir = root / "01-slash-commands"
    if not cmds_dir.exists():
        return items
    for f in sorted(cmds_dir.glob("*.md")):
        if f.name == "README.md":
            continue
        item = scan_file(f, "command")
        item.id = f"cmd:{f.stem}"
        items.append(item)
    return items


def scan_root_docs(root: Path) -> list[ContentItem]:
    """Scan top-level documentation files (README, LEARNING-ROADMAP, etc.)."""
    items: list[ContentItem] = []
    for name in ("README.md", "LEARNING-ROADMAP.md", "QUICK_REFERENCE.md",
                 "CATALOG.md", "INDEX.md", "cursor_concepts_guide.md",
                 "CONTRIBUTING.md", "SECURITY.md", "resources.md"):
        path = root / name
        if path.exists():
            item = scan_file(path, "doc")
            item.id = path.stem
            items.append(item)
    return items


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def generate(root: Path | None = None) -> Manifest:
    root = root or Path()
    manifest = Manifest()
    manifest.items.extend(scan_root_docs(root))
    manifest.items.extend(scan_modules(root))
    manifest.items.extend(scan_skills(root))
    manifest.items.extend(scan_plugins(root))
    manifest.items.extend(scan_commands(root))

    manifest.total_modules = sum(1 for i in manifest.items if i.type == "module")
    manifest.total_skills = sum(1 for i in manifest.items if i.type == "skill")
    manifest.total_plugins = sum(1 for i in manifest.items if i.type == "plugin")
    manifest.total_commands = sum(1 for i in manifest.items if i.type == "command")
    return manifest


def validate(manifest: Manifest, root: Path | None = None) -> list[str]:
    """Return a list of structural errors in the manifest."""
    errors: list[str] = []
    root = root or Path()

    # Every numbered dir must have README.md
    for d in iter_numbered_dirs(root):
        if not (d / "README.md").exists():
            errors.append(f"Module directory missing README.md: {d}")

    # Every module must have at least one item
    module_ids = {i.id for i in manifest.items if i.type == "module"}
    for d in iter_numbered_dirs(root):
        if d.name not in module_ids:
            errors.append(f"Unindexed module directory: {d}")

    # Every skill must have SKILL.md
    skills_dir = root / "03-skills"
    if skills_dir.exists():
        for d in sorted(skills_dir.iterdir()):
            if d.is_dir() and not d.name.startswith("."):
                if not (d / "SKILL.md").exists():
                    errors.append(f"Skill directory missing SKILL.md: {d}")

    return errors


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate content manifest")
    parser.add_argument("--output", "-o", default="content-manifest.json")
    parser.add_argument("--check", action="store_true",
                        help="Validate existing manifest against repo structure")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    args = parser.parse_args(argv)

    manifest = generate()

    if args.check:
        errors = validate(manifest)
        if errors:
            print("Manifest validation errors:")
            for e in errors:
                print(f"  - {e}")
            return 1
        print(f"OK: Manifest valid ({len(manifest.items)} items)")
        return 0

    indent = 2 if args.pretty else None
    Path(args.output).write_text(
        json.dumps(manifest.to_dict(), indent=indent, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote manifest: {args.output} ({len(manifest.items)} items)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
