#!/usr/bin/env python3
"""Klien LibGen (libgen.li dkk.) untuk korpus PDF lokal.

Skrip ini tanpa dependensi (hanya pustaka standar Python 3). LibGen tidak
menyediakan API resmi dan sering membalas galat ``max_user_connections``;
karena itu setiap permintaan dicoba ulang pada beberapa mirror dan baris
provenance ``# backend: libgen`` dicetak ke stderr agar stdout tetap TSV murni.

Contoh:
    python3 tools/libgen.py search "theory of international politics" --kind book
    python3 tools/libgen.py search "vaccine diplomacy" --kind article --limit 5
    python3 tools/libgen.py search "soft power Nye" --json
    python3 tools/libgen.py fetch

PERINGATAN: jangan pernah mengarang PDF, DOI, atau metadata. Catatan yang
keluar dari skrip ini berasal dari hasil pencarian nyata; bila semua mirror
gagal, keluaran kosong (bukan data palsu).

# backend: libgen
"""

import argparse
import html
import json
import os
import random
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

BACKEND = "libgen"

UA = "Mozilla/5.0 (X11; Linux x86_64)"
MIRRORS = ["libgen.li", "libgen.la", "libgen.vg", "libgen.bz", "libgen.gl"]
TOPICS = {"article": "a", "book": "l"}
KINDS = ("book", "article")
RETRIES = 3
SLEEP = 3
TIMEOUT = 45

MANIFEST = "docs/libgen-corpus/manifest.tsv"
OUTDIR = "docs/libgen-corpus"
HEADER = ["slug", "kind", "title", "year", "md5", "doi"]

GET_RE = re.compile(r"get\.php\?md5=[a-f0-9]{32}&key=[A-Za-z0-9]+")
MD5_RE = re.compile(r"ads\.php\?md5=([a-f0-9]{32})")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
YEAR_RE = re.compile(r"(1[89]\d{2}|20\d{2})")
ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
CELL_RE = re.compile(r"<td[^>]*>(.*?)</td>", re.S)

_ANCHOR_RE = re.compile(r'edition\.php\?id=\d+"[^>]*>(.*?)</a>', re.S)
_TITLE_ATTR_RE = re.compile(r'title="([^"]*)"')
_DOWNLOADNAME_RE = re.compile(r'downloadname=([^"&]+)')


# ---------------------------------------------------------------------------
# Utilitas umum
# ---------------------------------------------------------------------------

def _log_provenance(name: str, to_stderr: bool = False) -> None:
    """Cetak baris provenance (``# backend: <name>``)."""
    stream = sys.stderr if to_stderr else sys.stdout
    print(f"# backend: {name}", file=stream)


def _http_get(url: str) -> tuple[int, bytes]:
    """GET ``url`` -> (status, body). (0, b"") bila koneksi gagal."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        try:
            return exc.code, exc.read()
        except Exception:
            return exc.code, b""
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, b""


def _strip_tags(s: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", text).strip()


def _slug(text: str) -> str:
    """ASCII-fold -> lowercase -> ``[^a-z0-9]+`` -> ``-`` -> strip ``-``."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def _row_title(row: str) -> str:
    """Ambil judul dari anchor ``edition.php?id=...`` atau atribut ``title``."""
    anchors = [a for a in _ANCHOR_RE.findall(row) if "<font" not in a]
    for raw in reversed(anchors):
        title = _strip_tags(raw)
        if title:
            return title
    for attr in _TITLE_ATTR_RE.findall(row):
        if "<br>" in attr:
            title = _strip_tags(attr.split("<br>")[-1])
            if title:
                return title
    return ""


def _row_year(row: str) -> str:
    """Tahun 4 digit dari sel tabel; utamakan sel yang persis setahun."""
    cells = CELL_RE.findall(row)
    for cell in cells:
        text = _strip_tags(cell)
        if re.fullmatch(r"(1[89]\d{2}|20\d{2})", text):
            return text
    for cell in cells:
        match = YEAR_RE.search(_strip_tags(cell))
        if match:
            return match.group(1)
    return ""


def _parse_rows(body: str, kind: str, limit: int) -> list[dict]:
    results: list[dict] = []
    seen: set[str] = set()
    prefix = "book" if kind == "book" else "art"
    for row in ROW_RE.findall(body):
        if "ads.php?md5=" not in row:
            continue
        md5_match = MD5_RE.search(row)
        if not md5_match:
            continue
        md5 = md5_match.group(1)
        if md5 in seen:
            continue
        title = _row_title(row)
        if not title:
            continue
        doi = ""
        dn = _DOWNLOADNAME_RE.search(row)
        if dn and DOI_RE.match(dn.group(1)):
            doi = dn.group(1)
        slug = "lg-" + prefix + "-" + _slug(title[:60])
        results.append({
            "slug": slug,
            "kind": kind,
            "title": title,
            "year": _row_year(row),
            "md5": md5,
            "doi": doi,
        })
        seen.add(md5)
        if len(results) >= limit:
            break
    return results


# ---------------------------------------------------------------------------
# Pencarian
# ---------------------------------------------------------------------------

def search(query: str, kind: str, limit: int) -> list[dict]:
    """Cari di LibGen (``kind`` = book/article). Kembalikan <= ``limit`` dict."""
    if kind not in TOPICS:
        raise ValueError(f"kind tidak dikenal: {kind}")
    order = list(MIRRORS)
    random.shuffle(order)
    for mirror in order:
        url = (
            f"https://{mirror}/index.php?req={urllib.parse.quote_plus(query)}"
            f"&topics%5B%5D={TOPICS[kind]}"
        )
        status, body = _http_get(url)
        if status != 200:
            continue
        text = body.decode("utf-8", "replace")
        if "<tr" not in text or "ads.php?md5=" not in text:
            continue
        results = _parse_rows(text, kind, limit)
        if results:
            return results
    return []


# ---------------------------------------------------------------------------
# Unduhan
# ---------------------------------------------------------------------------

def fetch_one(md5: str, dest: str) -> str | None:
    """Unduh satu PDF berdasarkan ``md5``. Kembalikan nama mirror atau None."""
    order = list(MIRRORS)
    random.shuffle(order)
    for mirror in order:
        ads = f"https://{mirror}/ads.php?md5={md5}"
        for _ in range(RETRIES):
            status, body = _http_get(ads)
            if status != 200 or b"max_user_connections" in body:
                time.sleep(SLEEP)
                continue
            match = GET_RE.search(body.decode("utf-8", "replace"))
            if not match:
                break
            getlink = match.group(0)
            status, data = _http_get(f"https://{mirror}/{getlink}")
            if status == 200 and data[:5] == b"%PDF-":
                try:
                    with open(dest, "wb") as fh:
                        fh.write(data)
                except OSError:
                    return None
                return mirror
            time.sleep(SLEEP)
    return None


# ---------------------------------------------------------------------------
# Perintah
# ---------------------------------------------------------------------------

def cmd_search(args) -> int:
    _log_provenance(BACKEND, to_stderr=True)
    results = search(args.query, args.kind, args.limit)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0
    print("\t".join(HEADER))
    for rec in results:
        print("\t".join(str(rec.get(col, "")) for col in HEADER))
    return 0


def cmd_fetch(args) -> int:
    if not os.path.exists(MANIFEST):
        print("GAGAL: manifest.tsv tidak ditemukan")
        return 1
    os.makedirs(OUTDIR, exist_ok=True)
    with open(MANIFEST, encoding="utf-8") as fh:
        lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
    ok = failed = 0
    for line in lines[1:]:
        cells = line.split("\t")
        if len(cells) < 5:
            continue
        slug, _kind, _title, _year, md5 = cells[:5]
        dest = os.path.join(OUTDIR, f"{slug}.pdf")
        mirror = fetch_one(md5, dest)
        if mirror:
            print(f"{slug} OK (mirror={mirror})")
            ok += 1
        else:
            print(f"{slug} FAILED")
            failed += 1
    print(f"OK={ok} FAILED={failed}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="libgen",
        description="Klien LibGen: cari kandidat PDF dan unduh korpus lokal.",
    )
    sub = parser.add_subparsers(dest="command")

    p_search = sub.add_parser("search", help="cari kandidat (TSV ke stdout)")
    p_search.add_argument("query")
    p_search.add_argument("--kind", choices=KINDS, default="book")
    p_search.add_argument("--limit", type=int, default=10)
    p_search.add_argument("--json", action="store_true", help="keluarkan JSON")
    p_search.set_defaults(func=cmd_search)

    p_fetch = sub.add_parser("fetch", help="unduh PDF dari manifest.tsv")
    p_fetch.set_defaults(func=cmd_fetch)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        args = parser.parse_args(["fetch"])
    try:
        return args.func(args)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
