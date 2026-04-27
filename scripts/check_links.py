#!/usr/bin/env python3
"""Check external URLs in Markdown files are reachable."""

import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib.discovery import iter_md_files
TIMEOUT = 10
# Domains/patterns to skip: badges, placeholders, and bot-blocking hosts
SKIP_DOMAINS = {
    "shields.io",
    "img.shields.io",
    "star-history.com",
    "api.star-history.com",
    "example.com",
    "localhost",
    "127.0.0.1",
    "my-webhook.example.com",
    "git.internal",
    # Wikipedia blocks HEAD requests — GET also unreliable in CI without network
    "en.wikipedia.org",
    "wikipedia.org",
    # GitHub API requires auth — unauthenticated requests return 404 for protected endpoints
    "api.github.com",
}
SKIP_DOMAIN_SUFFIXES = (".example.com", ".example.org", ".internal")
# Placeholder/template URLs that are intentionally non-resolvable
SKIP_URL_PATTERNS = {
    "github.com/org/",
    "github.com/user/",
    "github.com/your-org/",
    "docs.example.com",
}

URL_RE = re.compile(r"https?://[a-zA-Z0-9][a-zA-Z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+")


def is_skipped(url: str) -> bool:
    try:
        domain = url.split("/", maxsplit=3)[2].split(":", maxsplit=1)[0]
    except IndexError:
        return True  # malformed URL
    # Repository may be private or unpublished — do not fail link check on GitHub 404.
    if "github.com/evoveotech/cursor-howto" in url:
        return True
    if any(skip == domain or domain.endswith("." + skip) for skip in SKIP_DOMAINS):
        return True
    if any(domain.endswith(suffix) for suffix in SKIP_DOMAIN_SUFFIXES):
        return True
    return any(pattern in url for pattern in SKIP_URL_PATTERNS)


def check_url(url: str, _depth: int = 0) -> tuple[str, bool, str]:
    if _depth > 8:
        return url, False, "too many redirects"
    if is_skipped(url):
        return url, True, "skipped"
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; link-check/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:  # nosec B310
            code = getattr(resp, "status", 200)
            if code in (200, 203, 204, 206):
                return url, True, "ok"
            return url, True, f"http {code}"
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 405, 429):
            return url, True, f"http {e.code} (ignored)"
        # urllib may not follow every 308; chase Location manually.
        if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):
            next_url = urllib.parse.urljoin(url, e.headers["Location"])
            return check_url(next_url, _depth + 1)
        return url, False, f"HTTP {e.code}"
    except Exception as e:
        return url, False, str(e)


def main(strict: bool = False) -> int:
    urls: dict[str, list[str]] = {}  # url -> [file, ...]

    md_files = iter_md_files()

    for file_path in md_files:
        content = file_path.read_text(encoding="utf-8")
        for raw_url in URL_RE.findall(content):
            # Strip trailing Markdown/punctuation characters the regex may over-capture
            # from link syntax like [text](https://url/) or **https://url)**
            clean_url = raw_url.rstrip(")>*_`':.,;").split("#")[0]
            urls.setdefault(clean_url, []).append(str(file_path))

    if not urls:
        print("OK: No external URLs found")
        return 0

    errors = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(check_url, url): url for url in urls}
        for future in as_completed(futures):
            url, ok, reason = future.result()
            if not ok:
                errors.extend(f"{f}: dead link -> {url} ({reason})" for f in urls[url])

    if errors:
        print("Dead links found:")
        for e in sorted(errors):
            print(f"  - {e}")
        # In non-strict mode (pre-commit), report but don't block the commit.
        # Set LINK_CHECK_STRICT=1 (as CI does) to enforce failures.
        return 1 if strict else 0

    print(f"OK: All external URLs reachable ({len(urls)} checked)")
    return 0


if __name__ == "__main__":
    import os

    sys.exit(main(strict=os.environ.get("LINK_CHECK_STRICT") == "1"))
