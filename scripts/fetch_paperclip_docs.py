#!/usr/bin/env python3
"""Fetch official Paperclip docs or repository documentation into a local cache."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

DOCS_HOME = "https://docs.paperclip.ing/"
DOCS_HOST = "docs.paperclip.ing"
RAW_HOST = "raw.githubusercontent.com"
RAW_PREFIX = "/paperclipai/paperclip/"
DEFAULT_REPO_PATH = "docs/docs.json"
REF_PATTERN = re.compile(r"^[A-Za-z0-9._/-]+$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a live Paperclip docs page or an official repository doc."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--page", help="docs.paperclip.ing URL or relative route")
    group.add_argument("--repo-path", help="path inside paperclipai/paperclip")
    parser.add_argument("--ref", default="master", help="repository branch, tag, or commit")
    parser.add_argument("--cache-dir", type=Path, help="cache directory")
    parser.add_argument(
        "--max-age", type=int, default=86400, help="reuse cache for this many seconds"
    )
    parser.add_argument("--refresh", action="store_true", help="ignore cached content")
    return parser.parse_args()


def validate_ref(value: str) -> str:
    if not REF_PATTERN.fullmatch(value) or value.startswith("/") or ".." in value.split("/"):
        raise ValueError("invalid repository ref")
    return value


def validate_repo_path(value: str) -> str:
    path = value.strip("/")
    if not path or ".." in path.split("/"):
        raise ValueError("invalid repository path")
    return path


def resolve_url(args: argparse.Namespace) -> str:
    if args.repo_path or not args.page:
        ref = urllib.parse.quote(validate_ref(args.ref), safe="._-/")
        path = validate_repo_path(args.repo_path or DEFAULT_REPO_PATH)
        return f"https://{RAW_HOST}{RAW_PREFIX}{ref}/{path}"

    value = args.page.strip()
    if value.startswith("/"):
        value = urllib.parse.urljoin(DOCS_HOME, value.lstrip("/"))
    elif not urllib.parse.urlparse(value).scheme:
        value = urllib.parse.urljoin(DOCS_HOME, value)
    parsed = urllib.parse.urlparse(value)
    if parsed.scheme != "https" or parsed.hostname != DOCS_HOST:
        raise ValueError(f"only https://{DOCS_HOST} pages are allowed")
    return urllib.parse.urlunparse(parsed._replace(fragment=""))


def cache_root(explicit: Path | None) -> Path:
    if explicit:
        return explicit.expanduser()
    base = os.environ.get("TMPDIR") or tempfile.gettempdir()
    return Path(base) / "paperclip-docs-cache"


def destination(root: Path, url: str) -> Path:
    parsed = urllib.parse.urlparse(url)
    name = Path(parsed.path.rstrip("/")).name or "index"
    if "." not in name:
        name = f"{name}.md"
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
    return root / f"{digest}-{name}"


def fetch(url: str, target: Path, max_age: int, refresh: bool) -> tuple[str, str]:
    if target.exists() and not refresh:
        age = time.time() - target.stat().st_mtime
        if age <= max(0, max_age):
            return "cache", "cached"
    request = urllib.request.Request(
        url,
        headers={"Accept": "text/markdown,text/plain;q=0.9,text/html;q=0.5", "User-Agent": "paperclip-docs-skill/1"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read()
        content_type = response.headers.get_content_type()
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_bytes(body)
    temporary.replace(target)
    return "network", content_type


def main() -> int:
    args = parse_args()
    try:
        url = resolve_url(args)
        root = cache_root(args.cache_dir)
        target = destination(root, url)
        source, content_type = fetch(url, target, args.max_age, args.refresh)
    except (ValueError, OSError, urllib.error.URLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(
        json.dumps(
            {
                "url": url,
                "path": str(target.resolve()),
                "source": source,
                "content_type": content_type,
                "fetched_at": int(target.stat().st_mtime),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
