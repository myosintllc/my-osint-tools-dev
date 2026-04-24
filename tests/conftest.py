"""
conftest.py
Scrapes the live tools.myosint.training page to discover all bookmarklets,
then loads their corresponding expectation files. Tests are parametrized
from this combined data so the test suite always reflects what's live.
"""

import json
import os
import re
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright


# Raw GitHub URL avoids Cloudflare challenges that would block GitHub Actions IPs.
# This always reflects the latest committed version of index.html on main.
TOOLS_URL = "https://raw.githubusercontent.com/myosintllc/my-osint-tools-dev/refs/heads/main/index.html"
EXPECTATIONS_DIR = Path(__file__).parent / "expectations"

# ── Scrape source HTML ────────────────────────────────────────────────────────

def scrape_bookmarklets() -> list[dict]:
    """
    Fetch index.html from the raw GitHub URL and parse all bookmarklet rows.
    Uses Python's html.parser rather than a full browser since the raw file
    is static HTML -- no JS rendering needed.

    Each <tr id="bm-*"> row gives us: slug, name, js, type, platform, last_updated.
    """
    import urllib.request
    from html.parser import HTMLParser

    # Fetch the raw HTML
    req = urllib.request.Request(TOOLS_URL, headers={"User-Agent": "myosint-healthcheck/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw_html = resp.read().decode("utf-8")

    class BookmarkletParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.results = []
            self._in_bm_row = False
            self._current = {}
            self._cell_index = 0
            self._in_cell = False
            self._in_link = False
            self._depth = 0          # track nesting inside the <tr>
            self._cell_text = ""
            self._link_href = ""
            self._link_text = ""

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == "tr" and attrs.get("id", "").startswith("bm-"):
                self._in_bm_row = True
                self._current = {"slug": attrs["id"].removeprefix("bm-")}
                self._cell_index = 0
                self._depth = 0
                return

            if not self._in_bm_row:
                return

            if tag == "tr":
                self._depth += 1

            if tag == "td":
                self._in_cell = True
                self._cell_text = ""

            if tag == "a" and self._in_cell:
                href = attrs.get("href", "")
                if href.startswith("javascript:"):
                    self._in_link = True
                    self._link_href = href
                    self._link_text = ""

        def handle_endtag(self, tag):
            if not self._in_bm_row:
                return

            if tag == "a" and self._in_link:
                self._in_link = False
                # Store name and JS from the bookmarklet anchor
                self._current["name"] = self._link_text.strip()
                self._current["js"]   = self._link_href

            if tag == "td" and self._in_cell:
                self._in_cell = False
                text = self._cell_text.strip()
                # Column order: 0=drag button (has the <a>), 1=description, 2=type, 3=platform, 4=last_updated
                if self._cell_index == 2:
                    self._current["type"] = text
                elif self._cell_index == 3:
                    self._current["platform"] = text
                elif self._cell_index == 4:
                    self._current["last_updated"] = text
                self._cell_index += 1

            if tag == "tr" and self._in_bm_row:
                if self._depth == 0:
                    # Closing the bm- row itself
                    if self._current.get("js"):
                        self.results.append(self._current)
                    self._in_bm_row = False
                    self._current = {}
                else:
                    self._depth -= 1

        def handle_data(self, data):
            if self._in_link:
                self._link_text += data
            elif self._in_cell:
                self._cell_text += data

    parser = BookmarkletParser()
    parser.feed(raw_html)
    return parser.results


def load_expectation(slug: str) -> dict | None:
    """Load the JSON expectation file for a given slug, or return None if missing."""
    path = EXPECTATIONS_DIR / f"{slug}.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


# ── Pytest fixtures & parametrize ─────────────────────────────────────────────

def pytest_configure(config):
    """Scrape once per session and stash results."""
    config._bookmarklets = scrape_bookmarklets()


def pytest_generate_tests(metafunc):
    """
    Dynamically parametrize any test that accepts the 'bookmarklet' fixture.
    Each parameter is a merged dict of scraped data + expectation file.
    Bookmarklets with no expectation file, or with skip=true, are xfail/skipped.
    """
    if "bookmarklet" not in metafunc.fixturenames:
        return

    scraped = metafunc.config._bookmarklets
    params = []
    ids = []

    for item in scraped:
        slug = item["slug"]
        expectation = load_expectation(slug)

        merged = {**item}
        if expectation:
            merged.update(expectation)

        mark = None
        if not expectation:
            mark = pytest.mark.skip(reason=f"No expectation file: expectations/{slug}.json")
        elif merged.get("skip"):
            reason = merged.get("skip_reason", "Marked skip=true in expectation file")
            mark = pytest.mark.skip(reason=reason)
        elif merged.get("requires_auth"):
            mark = pytest.mark.skip(reason="Requires authentication - skipped in CI")

        param = pytest.param(merged, marks=[mark] if mark else [])
        params.append(param)
        ids.append(slug)

    metafunc.parametrize("bookmarklet", params, ids=ids)


@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser_instance):
    context = browser_instance.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    pg = context.new_page()
    yield pg
    pg.close()
    context.close()