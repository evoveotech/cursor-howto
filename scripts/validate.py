#!/usr/bin/env python3
"""Unified validation runner for the cursor-howto repository.

Replaces the fragmented ``check_*.py`` scripts with a single orchestrated entry
point that produces consistent, machine-readable output.

Checks run (in order)::

    1. manifest     -- generate and validate content-manifest.json
    2. structure    -- validate directory / file conventions
    3. markdown     -- lint via markdownlint-cli (external tool)
    4. links        -- check external URL reachability
    5. cross-refs   -- validate internal markdown links and anchors
    6. mermaid      -- validate Mermaid diagram syntax via mmdc
    7. build        -- ensure EPUB can be built end-to-end

Usage::

    python scripts/validate.py              # run all checks
    python scripts/validate.py --checks=manifest,structure  # subset
    python scripts/validate.py --ci       # CI mode (strict, no mermaid build)

Exit codes::

    0   all checks passed
    1   one or more checks failed
"""

from __future__ import annotations

import argparse
import importlib
import shutil
import subprocess  # nosec B404
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib.discovery import iter_numbered_dirs
from lib.reporter import Reporter


# ---------------------------------------------------------------------------
# Check definitions
# ---------------------------------------------------------------------------

CHECKS = {
    "manifest",
    "structure",
    "markdown",
    "links",
    "cross-refs",
    "mermaid",
    "build",
}


def check_manifest(reporter: Reporter, _ci: bool) -> None:
    from generate_manifest import generate, validate

    manifest = generate()
    errors = validate(manifest)
    if errors:
        reporter.fail("manifest", f"{len(errors)} validation error(s)")
        for e in errors:
            print(f"  - {e}")
    else:
        reporter.ok(
            "manifest",
            f"valid ({len(manifest.items)} items, {manifest.total_modules} modules)",
        )


def check_structure(reporter: Reporter, _ci: bool) -> None:
    errors: list[str] = []
    root = Path()

    # Every numbered dir must have README.md
    for d in iter_numbered_dirs(root):
        if not (d / "README.md").exists():
            errors.append(f"Missing README.md in {d.name}")

    # Every skill dir must have SKILL.md
    skills_dir = root / "03-skills"
    if skills_dir.exists():
        for d in sorted(skills_dir.iterdir()):
            if d.is_dir() and not d.name.startswith("."):
                if not (d / "SKILL.md").exists():
                    errors.append(f"Missing SKILL.md in {d.name}")

    # Every plugin dir must have README.md
    plugins_dir = root / "07-plugins"
    if plugins_dir.exists():
        for d in sorted(plugins_dir.iterdir()):
            if d.is_dir() and not d.name.startswith(".") and d.name != "README.md":
                if not (d / "README.md").exists():
                    errors.append(f"Missing README.md in plugin {d.name}")

    if errors:
        reporter.fail("structure", f"{len(errors)} convention error(s)")
        for e in errors:
            print(f"  - {e}")
    else:
        reporter.ok("structure", "directory conventions valid")


def check_markdown(reporter: Reporter, _ci: bool) -> None:
    mdl = shutil.which("markdownlint")
    if not mdl:
        reporter.ok("markdown", "markdownlint not installed — skipped")
        return
    result = subprocess.run(  # nosec B603
        [
            mdl,
            "**/*.md",
            "--ignore",
            "node_modules",
            "--ignore",
            ".venv",
            "--config",
            ".markdownlint.json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        reporter.fail("markdown", f"lint errors\n{result.stdout}{result.stderr}")
    else:
        reporter.ok("markdown", "all files pass markdownlint")


def check_links(reporter: Reporter, ci: bool) -> None:
    strict = ci or False
    # Import lazily so that the shared lib path setup above is honoured.
    import check_links

    rc = check_links.main(strict=strict)
    if rc != 0:
        reporter.fail("links", "dead or unreachable external URLs")
    else:
        reporter.ok("links", "all external URLs reachable")


def check_cross_refs(reporter: Reporter, _ci: bool) -> None:
    import check_cross_references

    rc = check_cross_references.main()
    if rc != 0:
        reporter.fail("cross-refs", "broken internal links or anchors")
    else:
        reporter.ok("cross-refs", "all cross-references valid")


def check_mermaid(reporter: Reporter, _ci: bool) -> None:
    if not shutil.which("mmdc"):
        reporter.ok("mermaid", "mmdc not installed — skipped")
        return
    import check_mermaid

    rc = check_mermaid.main()
    if rc != 0:
        reporter.fail("mermaid", "Mermaid syntax errors")
    else:
        reporter.ok("mermaid", "all diagrams valid")


def check_build(reporter: Reporter, ci: bool) -> None:
    if ci:
        # In CI the full build job already exists; skip here to avoid duplication.
        reporter.ok("build", "skipped in CI mode")
        return
    uv = shutil.which("uv")
    if not uv:
        reporter.ok("build", "uv not installed — skipped")
        return
    result = subprocess.run(  # nosec B603
        [uv, "run", "scripts/build_epub.py"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        reporter.fail("build", f"EPUB build failed\n{result.stderr}")
    else:
        reporter.ok("build", "EPUB builds successfully")


CHECK_RUNNERS: dict[str, type] = {
    "manifest": check_manifest,
    "structure": check_structure,
    "markdown": check_markdown,
    "links": check_links,
    "cross-refs": check_cross_refs,
    "mermaid": check_mermaid,
    "build": check_build,
}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Unified repository validator")
    parser.add_argument(
        "--checks",
        default=",".join(CHECKS),
        help=f"Comma-separated checks to run (default: all). Available: {', '.join(CHECKS)}",
    )
    parser.add_argument("--ci", action="store_true", help="CI mode: strict, skip build")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    requested = set(args.checks.split(","))
    invalid = requested - CHECKS
    if invalid:
        print(f"Unknown checks: {', '.join(invalid)}")
        return 2

    reporter = Reporter(verbose=args.verbose)
    for name in CHECK_RUNNERS:
        if name not in requested:
            continue
        runner = CHECK_RUNNERS[name]
        runner(reporter, args.ci)

    reporter.print_summary()
    return reporter.exit_code()


if __name__ == "__main__":
    sys.exit(main())
