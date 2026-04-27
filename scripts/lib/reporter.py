"""Unified reporting / CLI output helpers.

Provides a consistent look-and-feel for all check scripts so that CI logs and
local pre-commit output are easy to read and programmatically parse.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class CheckResult:
    """Result of a single validation check."""

    tool: str
    ok: bool
    message: str
    files: list[Path] = field(default_factory=list)

    def __str__(self) -> str:
        status = "✅" if self.ok else "❌"
        return f"{status} {self.tool}: {self.message}"


class Reporter:
    """Collect results from multiple checks and print a unified summary."""

    def __init__(self, verbose: bool = False) -> None:
        self.results: list[CheckResult] = []
        self.verbose = verbose

    def add(self, result: CheckResult) -> None:
        """Record a check result."""
        self.results.append(result)
        if self.verbose or not result.ok:
            print(result, file=sys.stderr if not result.ok else sys.stdout)

    def ok(self, tool: str, message: str, files: list[Path] | None = None) -> None:
        """Shorthand for recording a passing check."""
        self.add(CheckResult(tool, True, message, files or []))

    def fail(self, tool: str, message: str, files: list[Path] | None = None) -> None:
        """Shorthand for recording a failing check."""
        self.add(CheckResult(tool, False, message, files or []))

    def exit_code(self) -> int:
        """Return ``1`` if any check failed, ``0`` otherwise."""
        return 1 if any(not r.ok for r in self.results) else 0

    def summary(self) -> str:
        """Human-readable summary of all recorded checks."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.ok)
        failed = total - passed
        lines = [
            "",
            "─" * 50,
            f"Validation Summary: {passed}/{total} passed",
        ]
        if failed:
            lines.append(f"  ❌ {failed} check(s) failed")
        lines.append("─" * 50)
        return "\n".join(lines)

    def print_summary(self) -> None:
        """Print the summary to stdout."""
        print(self.summary())
