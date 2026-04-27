"""Shared markdown file discovery utilities.

All scripts that scan the repository for markdown files should use this module
to ensure consistent ignore patterns and reduce duplication.
"""

from __future__ import annotations

from pathlib import Path

# Directories that should be excluded from all repository scans.
# Keep this as the single source of truth.  If a new directory type is added
# to the repo (e.g. ``.agents``, ``blog-posts``) it should be listed here so
# that *every* check script and the build pipeline skip it automatically.
DEFAULT_IGNORE_DIRS: frozenset[str] = frozenset({
    ".venv",
    "node_modules",
    ".git",
    "blog-posts",
    "openspec",
    "prompts",
    ".agents",
    ".cursor",
    ".github",
    "scripts",
    "assets",
    "resources",
    "slides",
})

# Files that should be excluded from scans.
DEFAULT_IGNORE_FILES: frozenset[str] = frozenset({
    "README.backup.md",
})


def is_ignored_path(path: Path, extra_ignore_dirs: set[str] | None = None) -> bool:
    """Return *True* if *path* should be ignored by repository scanners.

    A path is ignored when any of its parts matches ``DEFAULT_IGNORE_DIRS``
    (or the caller-supplied *extra_ignore_dirs*), or when its file name is
    in ``DEFAULT_IGNORE_FILES``.

    Parameters
    ----------
    path:
        The ``Path`` to evaluate (absolute or relative).
    extra_ignore_dirs:
        Additional directory names to ignore on top of the defaults.
    """
    ignore_dirs = DEFAULT_IGNORE_DIRS | (extra_ignore_dirs or set())
    if any(part in ignore_dirs for part in path.parts):
        return True
    if path.name in DEFAULT_IGNORE_FILES:
        return True
    return False


def iter_md_files(
    root: Path | None = None,
    extra_ignore_dirs: set[str] | None = None,
) -> list[Path]:
    """Return all markdown files under *root*, respecting ignore rules.

    Parameters
    ----------
    root:
        Directory to scan.  Defaults to the current working directory.
    extra_ignore_dirs:
        Additional directory names to ignore.

    Returns
    -------
    list[Path]
        Sorted list of markdown file paths (relative to *root*).
    """
    root = root or Path()
    results: list[Path] = []
    for f in root.rglob("*.md"):
        if is_ignored_path(f, extra_ignore_dirs):
            continue
        results.append(f)
    results.sort()
    return results


def iter_numbered_dirs(root: Path | None = None) -> list[Path]:
    """Return numbered tutorial directories (``01-*``, ``02-*``, …) under *root*.

    These are the top-level content modules such as ``01-slash-commands``,
    ``02-memory``, etc.
    """
    root = root or Path()
    results: list[Path] = []
    for i in range(0, 100):
        prefix = f"{i:02d}-"
        for d in root.iterdir():
            if d.is_dir() and d.name.startswith(prefix):
                results.append(d)
    results.sort(key=lambda p: p.name)
    return results
