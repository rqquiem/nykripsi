#!/usr/bin/env python3
"""Akuisisi full-text untuk Nykripsi v2 (tangga F1-F8).

Skrip ini tanpa dependensi (hanya pustaka standar Python 3). Ia memakai
tangga sumber legal berurutan: OpenAlex, Unpaywall, CORE (rung 1-3), lalu
shadow library sebagai upaya terakhir (rung 5). Baris provenance
``# backend: <name>`` dicetak ke stderr agar stdout tetap bersih.

Contoh:
    python3 tools/fulltext.py resolve --doi 10.xxxx/yyyy
    python3 tools/fulltext.py fetch --doi 10.xxxx/yyyy
    python3 tools/fulltext.py verify docs/fulltext-corpus/<slug>.pdf
    python3 tools/fulltext.py shadow --doi 10.xxxx/yyyy

PERINGATAN: jangan pernah mengarang PDF, hash, jumlah halaman, atau URL. Bila
tidak ada akses legal, statusnya ``inaccessible`` — bukan data palsu. PDF tetap
git-ignored; hanya catatan/manifest yang dilacak.

# backend: fulltext
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

BACKEND = "fulltext"

UA = "Mozilla/5.0 (X11; Linux x86_64) (Nykripsi research; mailto:research@example.com)"
TIMEOUT = 45
EMAIL = "research@example.com"

OPENALEX_WORK = "https://api.openalex.org/works/https://doi.org/"
UNPAYWALL = "https://api.unpaywall.org/v2/"
CORE_SEARCH = "https://api.core.ac.uk/v3/search/works"

OUTDIR = "docs/fulltext-corpus"

SHA_RE = re.compile(r"^[0-9a-f]{64}$")
PAGES_RE = re.compile(r"Pages:\s+(\d+)", re.I)
BODY_RE = re.compile(r"PENDAHULUAN|INTRODUCTION|METHOD|METODE|RESULTS|REFERENCES|DAFTAR PUSTAKA",
                     re.I)
PAYWALL_RE = re.compile(r"purchase|subscribe|access denied|paywall", re.I)

# ---------------------------------------------------------------------------
# Utilitas umum
# ---------------------------------------------------------------------------

def _log_provenance(name: str, to_stderr: bool = True) -> None:
    """Cetak baris provenance ``# backend: <name>``."""
    stream = sys.stderr if to_stderr else sys.stdout
    print(f"# backend: {name}", file=stream)


def _http_get(url: str, accept: str | None = None) -> tuple[int, bytes, str]:
    """GET ``url`` -> (status, body, content_type). (0, b"", "") bila gagal."""
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.read(), resp.headers.get("Content-Type", "")
    except urllib.error.HTTPError as exc:
        try:
            return exc.code, exc.read(), exc.headers.get("Content-Type", "")
        except Exception:
            return exc.code, b"", ""
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, b"", ""


def _json_get(url: str) -> dict | None:
    """GET JSON; ``None`` bila gagal atau bukan JSON valid."""
    status, body, _ctype = _http_get(url, accept="application/json")
    if status != 200:
        return None
    try:
        return json.loads(body.decode("utf-8", "replace"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None


def _slug(text: str) -> str:
    """ASCII-fold -> lowercase -> ``[^a-z0-9]+`` -> ``-`` -> strip ``-``."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


# ---------------------------------------------------------------------------
# Tangga resolusi (rung 1-3): OpenAlex -> Unpaywall -> CORE
# ---------------------------------------------------------------------------

def _openalex_candidates(doi: str) -> list[str]:
    data = _json_get(OPENALEX_WORK + urllib.parse.quote(doi))
    if not isinstance(data, dict):
        return []
    out: list[str] = []
    best = data.get("best_oa_location") or {}
    if isinstance(best, dict) and best.get("pdf_url"):
        out.append(best["pdf_url"])
    oa = data.get("open_access") or {}
    if isinstance(oa, dict) and oa.get("oa_url"):
        out.append(oa["oa_url"])
    return out


def _unpaywall_candidates(doi: str, email: str) -> list[str]:
    url = UNPAYWALL + urllib.parse.quote(doi) + "?" + urllib.parse.urlencode({"email": email})
    data = _json_get(url)
    if not isinstance(data, dict):
        return []
    out: list[str] = []
    best = data.get("best_oa_location") or {}
    if isinstance(best, dict) and best.get("url_for_pdf"):
        out.append(best["url_for_pdf"])
    return out


def _core_candidates(doi: str) -> list[str]:
    """CORE opsional; kegagalan (401/429) tidak fatal."""
    url = CORE_SEARCH + "?" + urllib.parse.urlencode({"q": f'doi:"{doi}"', "limit": "1"})
    data = _json_get(url)
    if not isinstance(data, dict):
        return []
    results = data.get("results") or []
    out: list[str] = []
    for item in results:
        if isinstance(item, dict) and item.get("downloadUrl"):
            out.append(item["downloadUrl"])
    return out


def resolve_candidates(doi: str, title: str | None = None, email: str = EMAIL) -> list[tuple[str, str]]:
    """Kembalikan daftar ``(backend, url)`` unik dari rung 1-3."""
    found: list[tuple[str, str]] = []
    for backend, urls in (
        ("openalex", _openalex_candidates(doi)),
        ("unpaywall", _unpaywall_candidates(doi, email)),
        ("core", _core_candidates(doi)),
    ):
        for u in urls:
            if u and all(u != prev for _b, prev in found):
                found.append((backend, u))
    return found


# ---------------------------------------------------------------------------
# Verifikasi PDF (aturan F2-F4)
# ---------------------------------------------------------------------------

def _pdfinfo_pages(path: str) -> int | None:
    try:
        proc = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    match = PAGES_RE.search(proc.stdout or "")
    return int(match.group(1)) if match else None


def _pdftotext(path: str) -> str | None:
    try:
        proc = subprocess.run(["pdftotext", "-q", path, "-"],
                              capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout or ""


def verify_pdf(path: str) -> tuple[bool, str | None, int | None, str]:
    """Verifikasi ``path`` -> (ok, sha256, pages, alasan)."""
    if not os.path.exists(path):
        return False, None, None, f"file tidak ditemukan: {path}"
    try:
        sha = _sha256(path)
    except OSError as exc:
        return False, None, None, f"tidak dapat membaca file ({exc})"

    pages = _pdfinfo_pages(path)
    if pages is None:
        return False, sha, None, "pdfinfo gagal / jumlah halaman tidak terbaca"
    if pages < 2:
        return False, sha, pages, f"halaman < 2 ({pages})"

    text = _pdftotext(path)
    if text is None:
        return False, sha, pages, "pdftotext gagal / teks tidak terbaca"
    if PAYWALL_RE.search(text):
        return False, sha, pages, "halaman paywall terdeteksi"
    if not BODY_RE.search(text):
        return False, sha, pages, "penanda isi tidak ditemukan"
    return True, sha, pages, ""


# ---------------------------------------------------------------------------
# Perintah: resolve
# ---------------------------------------------------------------------------

def cmd_resolve(args) -> int:
    _log_provenance(BACKEND, to_stderr=True)
    if not args.doi:
        print("GAGAL: --doi wajib diisi", file=sys.stderr)
        return 2
    email = args.email or EMAIL
    candidates = resolve_candidates(args.doi, args.title, email)
    if not candidates:
        print("inaccessible: tidak ada kandidat full-text (OpenAlex/Unpaywall/CORE)")
        return 1
    backend, url = candidates[0]
    _log_provenance(backend, to_stderr=True)
    print(url)
    for backend, url in candidates[1:]:
        print(f"# cadangan ({backend}): {url}", file=sys.stderr)
    return 0


# ---------------------------------------------------------------------------
# Perintah: fetch
# ---------------------------------------------------------------------------

def _download(url: str, dest: str) -> bool:
    status, body, _ctype = _http_get(url, accept="application/pdf")
    if status != 200 or body[:5] != b"%PDF-":
        return False
    try:
        with open(dest, "wb") as fh:
            fh.write(body)
    except OSError:
        return False
    return True


def cmd_fetch(args) -> int:
    _log_provenance(BACKEND, to_stderr=True)
    if not args.doi:
        print("GAGAL: --doi wajib diisi", file=sys.stderr)
        return 2
    email = args.email or EMAIL
    candidates = resolve_candidates(args.doi, args.title, email)
    if not candidates:
        print(json.dumps({
            "access_level": "inaccessible", "fulltext_url": None,
            "fulltext_sha256": None, "fulltext_pages": None,
            "fulltext_verified": False,
        }, ensure_ascii=False))
        return 1

    os.makedirs(args.out, exist_ok=True)
    slug = _slug(args.title or args.doi)
    dest = os.path.join(args.out, f"{slug}.pdf")

    for backend, url in candidates:
        _log_provenance(backend, to_stderr=True)
        if not _download(url, dest):
            continue
        ok, sha, pages, reason = verify_pdf(dest)
        if ok:
            print(json.dumps({
                "access_level": "fulltext",
                "fulltext_url": url,
                "fulltext_sha256": sha,
                "fulltext_pages": pages,
                "fulltext_verified": True,
            }, ensure_ascii=False))
            return 0
        print(f"# backend: {backend} gagal verifikasi: {reason}", file=sys.stderr)
        try:
            os.remove(dest)
        except OSError:
            pass

    print(json.dumps({
        "access_level": "inaccessible", "fulltext_url": None,
        "fulltext_sha256": None, "fulltext_pages": None,
        "fulltext_verified": False,
    }, ensure_ascii=False))
    return 1


# ---------------------------------------------------------------------------
# Perintah: verify
# ---------------------------------------------------------------------------

def cmd_verify(args) -> int:
    ok, sha, pages, reason = verify_pdf(args.file)
    if ok:
        print(f"FULLTEXT: OK sha256={sha} pages={pages}")
        return 0
    print(f"FULLTEXT: GAGAL {reason}")
    return 1


# ---------------------------------------------------------------------------
# Perintah: shadow (rung 5, upaya terakhir)
# ---------------------------------------------------------------------------

def cmd_shadow(args) -> int:
    _log_provenance(BACKEND, to_stderr=True)
    if not args.doi:
        print("inaccessible: --doi wajib diisi")
        return 1
    doi = args.doi.strip()
    urls = [
        f"https://sci-hub.se/{doi}",
        f"https://annas-archive.org/scidb/{doi}",
    ]
    print("PERINGATAN: shadow library adalah upaya TERAKHIR (rung 5). Skrip ini "
          "TIDAK melewati captcha dan TIDAK mengunduh; PDF apa pun tetap "
          "git-ignored. Bila akses gagal, statusnya 'inaccessible'.",
          file=sys.stderr)
    for url in urls:
        print(url)
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fulltext",
        description="Akuisisi full-text legal (OpenAlex/Unpaywall/CORE) + verifikasi PDF.",
    )
    sub = parser.add_subparsers(dest="command")

    p_resolve = sub.add_parser("resolve", help="cari kandidat URL full-text (rung 1-3)")
    p_resolve.add_argument("--doi", required=False)
    p_resolve.add_argument("--title", default=None)
    p_resolve.add_argument("--email", default=None)
    p_resolve.set_defaults(func=cmd_resolve)

    p_fetch = sub.add_parser("fetch", help="unduh + verifikasi PDF kandidat")
    p_fetch.add_argument("--doi", required=False)
    p_fetch.add_argument("--title", default=None)
    p_fetch.add_argument("--email", default=None)
    p_fetch.add_argument("--out", default=OUTDIR)
    p_fetch.set_defaults(func=cmd_fetch)

    p_verify = sub.add_parser("verify", help="verifikasi PDF lokal")
    p_verify.add_argument("file")
    p_verify.set_defaults(func=cmd_verify)

    p_shadow = sub.add_parser("shadow", help="URL shadow library (upaya terakhir, rung 5)")
    p_shadow.add_argument("--doi", required=False)
    p_shadow.set_defaults(func=cmd_shadow)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 0
    try:
        return args.func(args)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
