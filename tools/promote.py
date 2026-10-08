#!/usr/bin/env python3
"""Promosikan draf menjadi bab skripsi yang sudah dikenal.

Stdlib saja. Draf di ``content/drafts/`` adalah bahan kerja yang dikecualikan
dari ``make check``. Nama berkas draf HARUS sama dengan nama berkas bab tujuan,
mis. ``content/drafts/10-bab-01-pendahuluan.md`` -> ``content/skripsi/10-bab-01-pendahuluan.md``.

Alur:
  1. ``--draft`` harus ada dan berakhiran ``.md``.
  2. Target ``<skripsi-dir>/<basename>`` harus sudah ada (mencegah bab baru
     yang terbentuk karena salah ketik).
  3. Target saat ini dicadangkan ke ``--backup-dir`` dengan cap waktu.
  4. Isi draf disalin menimpa target secara atomik (``.tmp`` + ``os.replace``).
"""

import argparse
import os
import shutil
import sys
from datetime import datetime


def _unique_backup_path(backup_dir: str, basename: str) -> str:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = os.path.join(backup_dir, f"{basename}.{stamp}")
    if not os.path.exists(candidate):
        return candidate
    n = 1
    while True:
        candidate = os.path.join(backup_dir, f"{basename}.{stamp}-{n}")
        if not os.path.exists(candidate):
            return candidate
        n += 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Promosikan draf menjadi bab skripsi yang sudah dikenal."
    )
    parser.add_argument("--draft", required=True, help="path berkas draf (.md)")
    parser.add_argument(
        "--skripsi-dir", default="content/skripsi", help="direktori bab skripsi"
    )
    parser.add_argument(
        "--backup-dir", default=".promote-backups", help="direktori cadangan"
    )
    args = parser.parse_args(argv)

    draft = args.draft
    if not os.path.isfile(draft) or not draft.endswith(".md"):
        print(f"GAGAL: draft tidak ditemukan: {draft}", file=sys.stderr)
        return 1

    target = os.path.join(args.skripsi_dir, os.path.basename(draft))
    if not os.path.isfile(target):
        print(
            f"GAGAL: target bukan berkas skripsi yang dikenal: {target}",
            file=sys.stderr,
        )
        return 1

    os.makedirs(args.backup_dir, exist_ok=True)
    backup = _unique_backup_path(args.backup_dir, os.path.basename(target))
    shutil.copyfile(target, backup)

    with open(draft, "rb") as fh:
        data = fh.read()
    tmp = target + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, target)

    print(f"PROMOSI: {draft} -> {target}")
    print(f"BACKUP: {backup}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
