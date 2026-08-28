"""Verify internal Markdown links and Python syntax for this repository."""

from __future__ import annotations

import compileall
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def internal_link_errors() -> list[str]:
    errors: list[str] = []
    for markdown_file in ROOT.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split("#", maxsplit=1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (markdown_file.parent / unquote(target)).resolve()
            if not resolved.exists():
                errors.append(f"{markdown_file.relative_to(ROOT)} -> {raw_target}")
    return errors


def main() -> None:
    errors = internal_link_errors()
    compiled = compileall.compile_dir(ROOT / "examples" / "python", quiet=1)

    if errors:
        print("Broken internal Markdown links:")
        for error in errors:
            print(f"- {error}")
    if not compiled:
        print("Python compilation failed")

    if errors or not compiled:
        raise SystemExit(1)
    print("Repository verification passed")


if __name__ == "__main__":
    main()
