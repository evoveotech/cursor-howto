"""Shared Markdown parsing utilities used by check and build scripts."""

from __future__ import annotations

import re


def heading_to_anchor(heading: str) -> str:
    """Convert a Markdown heading to its GitHub-style anchor ID.

    GitHub's algorithm: strip non-ASCII (including emoji), strip punctuation,
    lower-case, replace spaces with hyphens, strip leading/trailing hyphens.

    Examples
    --------
    >>> heading_to_anchor("Hello World!")
    'hello-world'
    >>> heading_to_anchor("  Leading Space ")
    'leading-space'
    """
    heading_ascii = heading.encode("ascii", "ignore").decode()
    return re.sub(r"[^\w\s-]", "", heading_ascii.lower()).replace(" ", "-").rstrip("-")


def strip_code_blocks(content: str) -> str:
    """Remove fenced code blocks and inline code spans from Markdown content.

    Useful when scanning for links/anchors so that example URLs or placeholder
    syntax inside documentation examples are not treated as real references.

    Parameters
    ----------
    content:
        Raw Markdown text.

    Returns
    -------
    str
        Content with code fences and inline spans removed.
    """
    # Strip fenced code blocks (``` ... ```)
    content = re.sub(r"```[^\n]*\n.*?```", "", content, flags=re.DOTALL)
    # Strip inline code spans (` ... `)
    content = re.sub(r"`[^`\n]+`", "", content)
    return content
