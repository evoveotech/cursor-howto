"""Tests for utility scripts: check_links.py and check_mermaid.py."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from check_links import check_url, is_skipped, main as links_main

# =============================================================================
# check_links.py Tests
# =============================================================================


class TestIsSkipped:
    """Tests for URL skip logic."""

    @pytest.mark.parametrize(
        "url,expected",
        [
            ("https://img.shields.io/badge/test", True),
            ("https://api.star-history.com/svg", True),
            ("https://example.com/page", True),
            ("https://localhost:8080/api", True),
            ("https://en.wikipedia.org/wiki/Python", True),
            ("https://api.github.com/repos/evoveotech/cursor-howto", True),
            ("https://github.com/evoveotech/cursor-howto/issues", True),
            ("https://docs.example.com/guide", True),
            ("https://my-app.example.com/page", True),
            ("https://git.internal/repo", True),
            ("https://real-website.com/page", False),
            ("https://cursor.com/docs", False),
        ],
    )
    def test_skip_patterns(self, url: str, expected: bool) -> None:
        """Test that skip patterns match expected URLs."""
        assert is_skipped(url) is expected

    def test_malformed_url(self) -> None:
        """Malformed URLs should be skipped."""
        assert is_skipped("not-a-url") is True


class TestCheckUrl:
    """Tests for URL reachability checking."""

    def test_skipped_url(self) -> None:
        """Skipped URLs should return success immediately."""
        url = "https://img.shields.io/badge/test"
        result_url, ok, reason = check_url(url)
        assert result_url == url
        assert ok is True
        assert reason == "skipped"

    @patch("urllib.request.urlopen")
    def test_successful_request(self, mock_urlopen: MagicMock) -> None:
        """Successful HTTP 200 should return ok."""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        url = "https://example.org/test"
        _result_url, ok, reason = check_url(url)
        assert ok is True
        assert reason == "ok"

    @patch("urllib.request.urlopen")
    def test_http_error_ignored(self, mock_urlopen: MagicMock) -> None:
        """HTTP 403/429 should be treated as ok (ignored)."""
        from urllib.error import HTTPError

        mock_urlopen.side_effect = HTTPError(
            "https://example.org/test", 403, "Forbidden", {}, None  # type: ignore[arg-type]
        )

        url = "https://example.org/test"
        _result_url, ok, reason = check_url(url)
        assert ok is True
        assert "403" in reason

    @patch("urllib.request.urlopen")
    def test_http_error_failure(self, mock_urlopen: MagicMock) -> None:
        """HTTP 404 should be treated as failure."""
        from urllib.error import HTTPError

        mock_urlopen.side_effect = HTTPError(
            "https://example.org/test", 404, "Not Found", {}, None  # type: ignore[arg-type]
        )

        url = "https://example.org/test"
        _result_url, ok, reason = check_url(url)
        assert ok is False
        assert "404" in reason

    def test_redirect_loop_protection(self) -> None:
        """Too many redirects should be caught."""
        url = "https://example.org/loop"
        _result_url, ok, reason = check_url(url, _depth=9)
        assert ok is False
        assert "too many redirects" in reason


class TestLinksMain:
    """Tests for the link check main function."""

    def test_no_markdown_files(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Empty directory should return 0 with no URLs found."""
        monkeypatch.chdir(tmp_path)
        result = links_main(strict=True)
        assert result == 0

    def test_all_links_skipped(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Directory with only skipped URLs should pass."""
        md_file = tmp_path / "README.md"
        md_file.write_text("[badge](https://img.shields.io/badge/test)")
        monkeypatch.chdir(tmp_path)
        result = links_main(strict=True)
        assert result == 0

    def test_dead_link_strict(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Dead link in strict mode should return 1."""
        md_file = tmp_path / "README.md"
        md_file.write_text("[link](https://httpstat.us/404)")
        monkeypatch.chdir(tmp_path)
        result = links_main(strict=True)
        assert result == 1

    def test_dead_link_non_strict(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Dead link in non-strict mode should return 0 (reports but doesn't fail)."""
        md_file = tmp_path / "README.md"
        md_file.write_text("[link](https://httpstat.us/404)")
        monkeypatch.chdir(tmp_path)
        result = links_main(strict=False)
        assert result == 0


# =============================================================================
# check_mermaid.py Tests
# =============================================================================


class TestMermaidMain:
    """Tests for Mermaid validation main function."""

    @patch("shutil.which")
    def test_mmdc_not_found(self, mock_which: MagicMock, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """If mmdc is not installed, should exit gracefully with 0."""
        mock_which.return_value = None
        monkeypatch.chdir(tmp_path)
        from check_mermaid import main as mermaid_main

        result = mermaid_main()
        assert result == 0

    @patch("shutil.which")
    @patch("subprocess.run")
    @patch("os.environ.get")
    def test_valid_mermaid(
        self,
        mock_env_get: MagicMock,
        mock_subprocess: MagicMock,
        mock_which: MagicMock,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Valid Mermaid diagram should pass validation."""
        mock_which.return_value = "/usr/bin/mmdc"
        mock_env_get.return_value = None

        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_subprocess.return_value = mock_result

        md_file = tmp_path / "test.md"
        md_file.write_text("# Test\n\n```mermaid\ngraph TD\n    A --> B\n```\n")
        monkeypatch.chdir(tmp_path)
        from check_mermaid import main as mermaid_main

        result = mermaid_main()
        assert result == 0
        assert mock_subprocess.call_count == 1

    @patch("shutil.which")
    @patch("subprocess.run")
    @patch("os.environ.get")
    def test_invalid_mermaid(
        self,
        mock_env_get: MagicMock,
        mock_subprocess: MagicMock,
        mock_which: MagicMock,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Invalid Mermaid diagram should fail validation."""
        mock_which.return_value = "/usr/bin/mmdc"
        mock_env_get.return_value = None

        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stderr = "Syntax error in graph"
        mock_subprocess.return_value = mock_result

        md_file = tmp_path / "test.md"
        md_file.write_text("# Test\n\n```mermaid\ngraph TD\n    A --\n```\n")
        monkeypatch.chdir(tmp_path)
        from check_mermaid import main as mermaid_main

        result = mermaid_main()
        assert result == 1

    @patch("shutil.which")
    @patch("subprocess.run")
    @patch("os.environ.get")
    def test_puppeteer_no_sandbox(
        self,
        mock_env_get: MagicMock,
        mock_subprocess: MagicMock,
        mock_which: MagicMock,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """MERMAID_PUPPETEER_NO_SANDBOX=true should add puppeteer config."""
        mock_which.return_value = "/usr/bin/mmdc"
        mock_env_get.side_effect = lambda key, default=None: "true" if key == "MERMAID_PUPPETEER_NO_SANDBOX" else default

        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_subprocess.return_value = mock_result

        md_file = tmp_path / "test.md"
        md_file.write_text("# Test\n\n```mermaid\ngraph TD\n    A --> B\n```\n")
        monkeypatch.chdir(tmp_path)
        from check_mermaid import main as mermaid_main

        result = mermaid_main()
        assert result == 0

        # Verify that the subprocess call included puppeteer config
        call_args = mock_subprocess.call_args
        assert call_args is not None
        cmd = call_args[0][0]
        assert "-p" in cmd


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
