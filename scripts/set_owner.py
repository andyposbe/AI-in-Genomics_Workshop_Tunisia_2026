#!/usr/bin/env python3
"""Point every link in the repository at a different GitHub account or repo name.

    python3 scripts/set_owner.py <account> [repo-name]

Run it after moving the repository, for example to a GetGenome organisation.
"""
import pathlib, re, sys

OLD_OWNER = "andyposbe"
OLD_REPO = "AI-in-Genomics_Workshop_Tunisia_2026"
SKIP_DIRS = {".git", "assets", "_site", "vendor"}
SUFFIXES = {".md", ".yml", ".yaml", ".html"}


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    owner = sys.argv[1]
    repo = sys.argv[2] if len(sys.argv) > 2 else OLD_REPO
    root = pathlib.Path(__file__).resolve().parent.parent
    changed = 0
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        s = p.read_text()
        new = s.replace(OLD_OWNER + ".github.io", owner + ".github.io")
        new = new.replace("github.com/" + OLD_OWNER, "github.com/" + owner)
        new = new.replace(OLD_REPO, repo)
        if new != s:
            p.write_text(new)
            changed += 1
            print("updated", p.relative_to(root))
    print("%d files updated. Check _config.yml, then commit." % changed)


if __name__ == "__main__":
    main()
