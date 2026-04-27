#!/usr/bin/env python3
"""Validate cross-references, anchors, and code fences in Markdown files."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib.discovery import iter_md_files
from lib.markdown import heading_to_anchor, strip_code_blocks




def main() -> int:
    errors = []

    for file_path in iter_md_files():
        content = file_path.read_text(encoding="utf-8")
        # Strip code blocks before scanning for links/anchors to avoid false positives
        # from documentation examples inside code fences.
        scannable = strip_code_blocks(content)

        # Relative .md links must resolve
        errors.extend(
            f"{file_path}: broken cross-reference -> '{link_path}'"
            for link_path in re.findall(r"\[[^\]]+\]\(([^)#]+\.md)[^)]*\)", scannable)
            if not (file_path.parent / link_path).resolve().exists()
        )

        # In-page anchors must match a real heading
        anchors = re.findall(r"\[[^\]]+\]\(#([^)]+)\)", scannable)
        if anchors:
            headings = re.findall(r"^#{1,6}\s+(.+)$", content, re.MULTILINE)
            valid_anchors = {heading_to_anchor(h) for h in headings}
            errors.extend(
                f"{file_path}: broken anchor -> '#{anchor}'"
                for anchor in anchors
                if anchor not in valid_anchors
            )

        # Unmatched code fences (only count fences at start of line)
        if len(re.findall(r"^```", content, re.MULTILINE)) % 2 != 0:
            errors.append(f"{file_path}: unmatched code fences")

    # All numbered lesson dirs must have README.md
    for i in range(1, 11):
        errors.extend(
            f"{d}: missing README.md"
            for d in Path().glob(f"{i:02d}-*")
            if d.is_dir() and not (d / "README.md").exists()
        )

    if errors:
        print("Cross-reference errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    md_count = sum(1 for _ in iter_md_files())
    print(f"OK: All cross-references valid ({md_count} files checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
