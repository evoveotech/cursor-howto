#!/usr/bin/env python3
"""Validate Mermaid diagram syntax in Markdown files using mmdc."""

import json
import os
import re
import shutil
import subprocess  # nosec B404
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib.discovery import iter_md_files


def main() -> int:
    if not shutil.which("mmdc"):
        print(
            "WARN: mmdc not found - skipping Mermaid validation (install @mermaid-js/mermaid-cli)"
        )
        return 0

    errors = []
    checked = 0

    # On GitHub Actions Linux runners, Chrome/Puppeteer requires --no-sandbox.
    # Write a temporary puppeteer config when MERMAID_PUPPETEER_NO_SANDBOX is set.
    puppeteer_config_path = None
    extra_args: list[str] = []
    if os.environ.get("MERMAID_PUPPETEER_NO_SANDBOX") == "true":
        with tempfile.NamedTemporaryFile(
            suffix=".json", mode="w", delete=False
        ) as pcfg:
            json.dump({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}, pcfg)
            puppeteer_config_path = pcfg.name
        extra_args = ["-p", puppeteer_config_path]

    md_files = iter_md_files()

    try:
        for file_path in md_files:
            content = file_path.read_text(encoding="utf-8")
            blocks = re.findall(r"```mermaid\n(.*?)```", content, re.DOTALL)
            for i, block in enumerate(blocks):
                tmp_path: str | None = None
                out_path: str | None = None
                try:
                    with tempfile.NamedTemporaryFile(
                        suffix=".mmd", mode="w", delete=False
                    ) as tmp:
                        tmp.write(block)
                        tmp_path = tmp.name
                    out_path = str(Path(tmp_path).with_suffix(".svg"))
                    result = subprocess.run(  # nosec B603 B607
                        ["mmdc", "-i", tmp_path, "-o", out_path, *extra_args],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    if result.returncode != 0:
                        errors.append(
                            f"{file_path} (block {i + 1}): {result.stderr.strip()}"
                        )
                    else:
                        checked += 1
                finally:
                    if tmp_path is not None:
                        Path(tmp_path).unlink(missing_ok=True)
                    if out_path is not None:
                        Path(out_path).unlink(missing_ok=True)
    finally:
        if puppeteer_config_path:
            Path(puppeteer_config_path).unlink(missing_ok=True)

        print(f"OK: Checked {checked} Mermaid diagram(s)")
    if errors:
        print("\nMermaid errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
