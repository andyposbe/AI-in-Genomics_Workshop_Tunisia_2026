#!/usr/bin/env python3
"""Check a participant laptop is ready for the AI in Genomics 2026 workshop.

Run this from the root of the repository:

    python3 scripts/check_setup.py

It prints one line per requirement. Anything marked FAIL needs fixing before
Day 1. Bring the output with you if you cannot resolve something.

Deliberately dependency-free: standard library only, so it runs on whatever
Python a participant already has.
"""

import os
import platform
import shutil
import socket
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

PASS, WARN, FAIL = "PASS", "WARN", "FAIL"
results = []


def record(status, name, detail=""):
    results.append((status, name, detail))


# --- checks ----------------------------------------------------------------

def check_python():
    v = sys.version_info
    version = f"{v.major}.{v.minor}.{v.micro}"
    if v >= (3, 9):
        record(PASS, "Python", version)
    elif v >= (3, 7):
        record(WARN, "Python", f"{version} — old but workable. 3.9+ preferred.")
    else:
        record(FAIL, "Python", f"{version} — install Python 3.9 or newer from python.org")


def check_disk():
    try:
        free_gb = shutil.disk_usage(REPO_ROOT).free / 1024**3
    except OSError as exc:
        record(WARN, "Disk space", f"could not measure ({exc})")
        return
    if free_gb >= 5:
        record(PASS, "Disk space", f"{free_gb:.1f} GB free")
    else:
        record(FAIL, "Disk space", f"{free_gb:.1f} GB free — clear space, 5 GB needed")


def check_repo_files():
    expected = [
        "README.md",
        "docs/setup.md",
        "docs/practicals/01-predict.md",
        "data",
    ]
    missing = [p for p in expected if not (REPO_ROOT / p).exists()]
    if missing:
        record(FAIL, "Workshop files", f"missing: {', '.join(missing)} — re-download the repository")
    else:
        record(PASS, "Workshop files", f"found in {REPO_ROOT}")


def check_chimerax():
    """ChimeraX rarely lands on PATH, so look in the usual install locations too."""
    if shutil.which("chimerax") or shutil.which("ChimeraX"):
        record(PASS, "UCSF ChimeraX", "on PATH")
        return

    system = platform.system()
    candidates = []
    if system == "Darwin":
        candidates = list(Path("/Applications").glob("ChimeraX*.app"))
    elif system == "Windows":
        for base in (os.environ.get("ProgramFiles", ""), os.environ.get("ProgramFiles(x86)", "")):
            if base:
                candidates += list(Path(base).glob("ChimeraX*"))
    elif system == "Linux":
        candidates = [p for p in (Path("/usr/bin/chimerax"), Path("/opt/UCSF")) if p.exists()]

    if candidates:
        record(PASS, "UCSF ChimeraX", str(candidates[0]))
    else:
        record(
            FAIL,
            "UCSF ChimeraX",
            "not found — install from https://www.cgl.ucsf.edu/chimerax/download.html",
        )


def check_internet():
    for host, port in (("alphafoldserver.com", 443), ("github.com", 443)):
        try:
            socket.create_connection((host, port), timeout=6).close()
            record(PASS, f"Reach {host}", "ok")
        except OSError:
            record(
                WARN,
                f"Reach {host}",
                "unreachable — check your firewall or proxy; you will need this on the day",
            )


def check_terminal():
    record(PASS, "Terminal", f"{platform.system()} {platform.release()}")


# --- output ----------------------------------------------------------------

def main():
    print()
    print("  AI in Genomics 2026 — setup check")
    print("  " + "-" * 52)
    print()

    for check in (
        check_python,
        check_terminal,
        check_disk,
        check_repo_files,
        check_chimerax,
        check_internet,
    ):
        check()

    width = max(len(name) for _, name, _ in results)
    for status, name, detail in results:
        print(f"  [{status}]  {name.ljust(width)}   {detail}")

    failures = sum(1 for s, _, _ in results if s == FAIL)
    warnings = sum(1 for s, _, _ in results if s == WARN)

    print()
    if failures:
        print(f"  {failures} thing(s) to fix before Day 1. See docs/setup.md.")
        print("  Stuck? Open an issue on the repository or email getgenome@tsl.ac.uk")
    elif warnings:
        print(f"  Ready, with {warnings} warning(s). Worth a look, but not blocking.")
    else:
        print("  All set. See you in Tunisia.")
    print()

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
