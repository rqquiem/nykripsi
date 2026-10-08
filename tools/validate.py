#!/usr/bin/env python3
"""Verifikator alur kerja + validator korpus untuk Nykripsi v2.

Stdlib saja. Contoh:
    python3 tools/validate.py                 # semua validator
    python3 tools/validate.py journals doi    # sebagian saja
    python3 tools/validate.py --offline       # lewati pemeriksaan jaringan
    python3 tools/validate.py --agent         # tambah tinjauan ulang oleh agen
    python3 tools/validate.py --list          # daftar validator
    python3 tools/validate.py --json          # keluaran mesin
"""

import argparse
import json
import os
import sys

# Bootstrap path agar ``from validators import base`` bekerja saat dijalankan
# sebagai ``python3 tools/validate.py``.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from validators import base  # noqa: E402
import validators.workflow  # noqa: E402,F401
import validators.journals  # noqa: E402,F401
import validators.papers  # noqa: E402,F401
import validators.research_notes  # noqa: E402,F401
import validators.ir_journals  # noqa: E402,F401
import validators.ir_research_notes  # noqa: E402,F401
import validators.libgen_corpus  # noqa: E402,F401
import validators.doi  # noqa: E402,F401
import validators.sources  # noqa: E402,F401
import validators.research  # noqa: E402,F401

LABEL = {"ok": "OK", "warn": "PERINGATAN", "fail": "GAGAL"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="validate.py",
        description="Verifikator alur kerja + validator korpus Nykripsi v2.",
    )
    parser.add_argument(
        "names",
        nargs="*",
        help="nama validator (default: semua, sesuai urutan registrasi)",
    )
    parser.add_argument("--agent", action="store_true", help="aktifkan tinjauan ulang oleh agen")
    parser.add_argument("--offline", action="store_true", help="lewati pemeriksaan jaringan")
    parser.add_argument("--list", action="store_true", help="daftar validator lalu keluar")
    parser.add_argument("--json", action="store_true", help="keluarkan JSON")
    args = parser.parse_args(argv)

    registry = base.VALIDATORS

    if args.list:
        for name, (subject, _fn) in registry.items():
            print(f"{name}\t{subject}")
        return 0

    if args.agent and base.shutil.which("claude") is None:
        print("GAGAL: agen tidak tersedia (pasang CLI 'claude' atau jalankan tanpa --agent)")
        return 2

    names = args.names or list(registry.keys())
    for n in names:
        if n not in registry:
            print(f"GAGAL: validator tidak dikenal: {n}")
            return 2

    ctx = base.Context(root=base.REPO, offline=args.offline, agent=args.agent)

    results: dict[str, list[base.Finding]] = {}
    failed_total = 0
    for name in names:
        _subject, fn = registry[name]
        findings = fn(ctx)
        results[name] = findings
        failed_total += sum(1 for f in findings if f.level == "fail")

    if args.json:
        payload = {
            "validators": {
                name: [{"level": f.level, "message": f.message} for f in findings]
                for name, findings in results.items()
            },
            "failed": failed_total,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 1 if failed_total > 0 else 0

    for name in names:
        findings = results[name]
        for f in findings:
            label = LABEL[f.level]
            prefix = f"{label}: {name}: "
            msg = f.message if f.message.startswith(prefix) else prefix + f.message
            print(msg)
        n_ok = sum(1 for f in findings if f.level == "ok")
        n_warn = sum(1 for f in findings if f.level == "warn")
        n_fail = sum(1 for f in findings if f.level == "fail")
        print(f"{name}: {n_ok} ok, {n_warn} peringatan, {n_fail} gagal")

    if failed_total > 0:
        print(f"VALIDASI: GAGAL ({failed_total} galat).")
        return 1
    print("VALIDASI: LULUS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
