#!/usr/bin/env python3
"""Cari referensi (Google Scholar / Crossref / OpenAlex) dan hasilkan BibTeX.

Skrip ini tanpa dependensi (hanya pustaka standar Python 3). Google Scholar
tidak menyediakan API resmi dan dapat memblokir akses otomatis; karena itu
skrip melaporkan backend yang dipakai pada baris provenance ``# backend: ...``
di stdout dan otomatis beralih ke Crossref lalu OpenAlex bila Scholar diblokir.

Contoh:
    python3 .claude/skills/nykripsi/scripts/scholar.py search "random forest" --limit 5
    python3 .claude/skills/nykripsi/scripts/scholar.py search "random forest" --json
    python3 .claude/skills/nykripsi/scripts/scholar.py bib "random forest" --out assets/refs.bib
    python3 .claude/skills/nykripsi/scripts/scholar.py bib --doi 10.1016/j.cmet.2018.04.010

PERINGATAN: jangan pernah mengarang sitasi atau DOI. Catatan yang keluar dari
skrip ini berasal dari hasil pencarian nyata.
"""

import argparse
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

UA_SCHOLAR = "Mozilla/5.0 (X11; Linux x86_64)"
UA_POLITE = "Mozilla/5.0 (X11; Linux x86_64)"

SCHOLAR_URL = "https://scholar.google.com/scholar"
CROSSREF_URL = "https://api.crossref.org/works"
OPENALEX_URL = "https://api.openalex.org/works"

BACKENDS = ("auto", "scholar", "crossref", "openalex")

# Tipe Crossref/OpenAlex yang bukan karya sitasi yang layak -> dilewati.
SKIP_TYPES = {
    "component", "dataset", "peer-review", "grant", "figure", "table",
    "posted-content",
}

# ---------------------------------------------------------------------------
# Utilitas umum
# ---------------------------------------------------------------------------


def _log_provenance(name: str, to_stderr: bool = False) -> None:
    """Cetak baris provenance (``# backend: <name>``).

    Ke stdout secara bawaan; ke stderr saat mode ``--json`` agar stdout tetap
    berupa JSON yang valid.
    """
    stream = sys.stderr if to_stderr else sys.stdout
    print(f"# backend: {name}", file=stream)


def _user_agent(mailto: str | None) -> str:
    if mailto:
        return f"{UA_POLITE} (mailto:{mailto})"
    return UA_POLITE


def _get(url: str, headers: dict[str, str] | None = None, timeout: int = 25):
    """GET ``url`` -> (status, text). Melempar ``Blocked`` bila 403/429."""
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            status = getattr(resp, "status", 200)
            charset = resp.headers.get_content_charset() or "utf-8"
            return status, raw.decode(charset, errors="replace")
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 429):
            raise Blocked(f"HTTP {exc.code}") from exc
        raise


class Blocked(Exception):
    """Akses otomatis diblokir (Scholar captcha / 403 / 429)."""


# ---------------------------------------------------------------------------
# Backend: Google Scholar
# ---------------------------------------------------------------------------

_SCHOLAR_BLOCK_MARKERS = ("gs_captcha", "unusual traffic", "sorry/index")
_MARKER_RE = re.compile(
    r"^(?:\s*\[(?:PDF|HTML|BOOK|B|CITATION|DOC)\])+\s*", re.IGNORECASE
)
_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def _clean(fragment: str) -> str:
    text = _TAG_RE.sub("", fragment)
    text = html.unescape(text)
    return _WS_RE.sub(" ", text).strip()


def _parse_scholar_authors_venue(line: str) -> tuple[list[str], str, str | None]:
    """Pecah baris ``gs_a`` -> (authors, venue, year)."""
    line = line.replace("\xa0", " ")
    line = _WS_RE.sub(" ", line).strip()

    year = None
    m_year = re.search(r"\b(1[89]\d{2}|20\d{2})\b", line)
    if m_year:
        year = m_year.group(1)

    # Bagian penulis adalah sebelum pemisah " - " pertama.
    parts = re.split(r"\s+-\s+", line, maxsplit=1)
    authors_part = parts[0]
    venue_part = parts[1] if len(parts) > 1 else ""

    authors: list[str] = []
    for chunk in authors_part.split(","):
        name = chunk.strip().rstrip("…").strip()
        if not name or name in ("…", "…"):
            continue
        # "AB Shaik" tetap dipertahankan apa adanya (inisial gaya Scholar).
        authors.append(name)

    # Venue: buang tahun dan domain di ujung.
    venue = re.sub(r"\b(1[89]\d{2}|20\d{2})\b", "", venue_part).strip(" ,-")
    venue = re.sub(r"-\s*[\w.-]+\.[a-z]{2,}\s*$", "", venue).strip(" ,-")
    return authors, venue, year


def scholar_search(query: str, limit: int) -> list[dict]:
    """Cari di Google Scholar. Melempar ``Blocked`` bila diblokir."""
    url = SCHOLAR_URL + "?" + urllib.parse.urlencode({"hl": "en", "q": query})
    status, text = _get(url, {"User-Agent": UA_SCHOLAR})

    low = text.lower()
    if status in (403, 429) or any(m in low for m in _SCHOLAR_BLOCK_MARKERS):
        raise Blocked("captcha/unusual traffic")
    if "gs_rt" not in text:
        raise Blocked("tidak ada blok hasil")

    records: list[dict] = []
    pattern = re.compile(
        r'<div class="gs_r gs_or gs_scl"[^>]*data-cid="([^"]*)"[^>]*>(.*?)'
        r'(?=<div class="gs_r gs_or gs_scl"|<div id="gs_res_ccl_bot)',
        re.DOTALL,
    )
    for cid, block in pattern.findall(text):
        m_title = re.search(r'<h3 class="gs_rt[^"]*"[^>]*>(.*?)</h3>', block, re.DOTALL)
        if not m_title:
            continue
        title = _clean(m_title.group(1))
        title = _MARKER_RE.sub("", title).strip()
        if not title:
            continue

        m_a = re.search(r'<div class="gs_a">(.*?)</div>', block, re.DOTALL)
        authors, venue, year = ([], "", None)
        if m_a:
            authors, venue, year = _parse_scholar_authors_venue(_clean(m_a.group(1)))

        m_link = re.search(r'<h3 class="gs_rt[^"]*"[^>]*>.*?<a[^>]+href="([^"]+)"', block, re.DOTALL)
        link = html.unescape(m_link.group(1)) if m_link else ""

        records.append({
            "title": title,
            "authors": authors,
            "year": year,
            "venue": venue,
            "doi": None,
            "url": link or (f"https://scholar.google.com/scholar?q={urllib.parse.quote(title)}"),
            "source": "scholar",
            "cid": cid,
        })
        if len(records) >= limit:
            break

    if not records:
        raise Blocked("hasil kosong")
    return records


# ---------------------------------------------------------------------------
# Backend: Crossref
# ---------------------------------------------------------------------------


def _crossref_record(item: dict) -> dict | None:
    if item.get("type") in SKIP_TYPES:
        return None
    title_list = item.get("title") or []
    title = (title_list[0] if title_list else "").strip()
    if not title:
        return None

    authors = []
    for a in item.get("author", []) or []:
        name = " ".join(p for p in (a.get("given"), a.get("family")) if p).strip()
        if name:
            authors.append(name)

    year = None
    parts = (item.get("issued", {}) or {}).get("date-parts") or []
    if parts and parts[0] and parts[0][0]:
        year = str(parts[0][0])

    venue_list = item.get("container-title") or []
    venue = (venue_list[0] if venue_list else "").strip()
    doi = item.get("DOI")

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "venue": venue,
        "doi": doi,
        "url": f"https://doi.org/{doi}" if doi else "",
        "source": "crossref",
        "type": item.get("type") or "",
    }


def _rank(record: dict) -> tuple:
    """Skor kelengkapan: dahulukan catatan berpenulis, bervenue, dan bertahun."""
    return (
        1 if record.get("authors") else 0,
        1 if record.get("venue") else 0,
        1 if record.get("year") else 0,
        1 if record.get("doi") else 0,
    )


def _prefer_complete(records: list[dict], limit: int) -> list[dict]:
    """Urutkan menurut kelengkapan (stabil) lalu ambil ``limit`` teratas."""
    ranked = sorted(records, key=_rank, reverse=True)
    return ranked[:limit]


def crossref_search(query: str, limit: int, mailto: str | None = None) -> list[dict]:
    params = urllib.parse.urlencode({
        "query.bibliographic": query,
        "rows": max(limit * 4, 20),
        "select": "DOI,title,author,issued,container-title,type",
    })
    status, text = _get(CROSSREF_URL + "?" + params, {"User-Agent": _user_agent(mailto)})
    data = json.loads(text)
    records = []
    for item in data.get("message", {}).get("items", []):
        rec = _crossref_record(item)
        if rec:
            records.append(rec)
    return _prefer_complete(records, limit)


def crossref_by_doi(doi: str, mailto: str | None = None) -> dict | None:
    url = CROSSREF_URL + "/" + urllib.parse.quote(doi, safe="")
    status, text = _get(url, {"User-Agent": _user_agent(mailto)})
    data = json.loads(text)
    return _crossref_record(data.get("message", {}))


# ---------------------------------------------------------------------------
# Backend: OpenAlex
# ---------------------------------------------------------------------------


def _openalex_record(work: dict) -> dict | None:
    title = (work.get("title") or "").strip()
    if not title:
        return None
    authors = []
    for a in work.get("authorships", []) or []:
        name = ((a.get("author") or {}).get("display_name") or "").strip()
        if name:
            authors.append(name)

    venue = ""
    src = (work.get("primary_location") or {}).get("source") or {}
    if src:
        venue = (src.get("display_name") or "").strip()

    doi_raw = work.get("doi")
    doi = None
    if doi_raw:
        doi = re.sub(r"^https?://doi\.org/", "", doi_raw)

    year = work.get("publication_year")
    return {
        "title": title,
        "authors": authors,
        "year": str(year) if year else None,
        "venue": venue,
        "doi": doi,
        "url": doi_raw or "",
        "source": "openalex",
        "type": work.get("type") or "",
    }


def openalex_search(query: str, limit: int, mailto: str | None = None) -> list[dict]:
    params = {"search": query, "per-page": max(limit, 5)}
    if mailto:
        params["mailto"] = mailto
    status, text = _get(OPENALEX_URL + "?" + urllib.parse.urlencode(params),
                        {"User-Agent": _user_agent(mailto)})
    data = json.loads(text)
    records = []
    for work in data.get("results", []):
        rec = _openalex_record(work)
        if rec:
            records.append(rec)
        if len(records) >= limit:
            break
    return records


# ---------------------------------------------------------------------------
# Resolusi backend (auto + fallback)
# ---------------------------------------------------------------------------


def resolve(query: str, limit: int, backend: str, mailto: str | None,
            to_stderr: bool = False) -> list[dict]:
    """Selesaikan ``query`` -> daftar catatan; cetak provenance ke stdout."""
    def prov(name: str) -> None:
        _log_provenance(name, to_stderr)

    if backend == "scholar":
        prov("scholar")
        try:
            return scholar_search(query, limit)
        except (Blocked, urllib.error.URLError, TimeoutError, OSError) as exc:
            print(f"# scholar tidak tersedia ({exc})", file=sys.stderr)
            return []

    if backend == "crossref":
        prov("crossref")
        return crossref_search(query, limit, mailto)

    if backend == "openalex":
        prov("openalex")
        return openalex_search(query, limit, mailto)

    # auto: scholar -> crossref -> openalex
    try:
        records = scholar_search(query, limit)
        if records:
            prov("scholar")
            return records
        raise Blocked("hasil kosong")
    except (Blocked, urllib.error.URLError, TimeoutError, OSError):
        pass

    try:
        records = crossref_search(query, limit, mailto)
        if records:
            prov("scholar (blocked -> crossref)")
            return records
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        pass

    records = openalex_search(query, limit, mailto)
    if records:
        prov("scholar (blocked -> openalex)")
        return records
    prov("none")
    return []


# ---------------------------------------------------------------------------
# BibTeX
# ---------------------------------------------------------------------------

_STOPWORDS = {
    "a", "an", "the", "of", "on", "in", "for", "and", "to", "with", "using",
    "via", "at", "by", "from", "as", "is", "are",
}


def _ascii_slug(text: str) -> str:
    """ASCII-fold -> lowercase -> hanya ``[a-z0-9]``."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    return re.sub(r"[^a-z0-9]", "", text)


def _first_author_last(name: str) -> str:
    name = name.strip()
    if not name:
        return "anon"
    if "," in name:  # "Family, Given"
        return name.split(",", 1)[0].strip()
    parts = name.split()
    return parts[-1] if parts else "anon"


def _significant_word(title: str) -> str:
    for word in re.findall(r"[A-Za-z0-9]+", title):
        if word.lower() not in _STOPWORDS:
            return word
    return ""


def make_key(record: dict) -> str:
    authors = record.get("authors") or []
    last = _first_author_last(authors[0]) if authors else "anon"
    year = record.get("year") or "n"
    word = _significant_word(record.get("title") or "")
    key = _ascii_slug(last) + _ascii_slug(str(year)) + _ascii_slug(word)
    return key or "ref"


def _entry_type(record: dict) -> str:
    raw = (record.get("type") or "").lower()
    venue = (record.get("venue") or "").lower()
    if raw in ("book", "monograph", "edited-book", "reference-book"):
        return "book"
    if raw in ("proceedings-article", "conference-paper", "proceedings",
               "paper-conference") or "proceeding" in venue or "conference" in venue:
        return "inproceedings"
    if raw in ("journal-article", "article", "review", "review-article"):
        return "article"
    if raw in ("posted-content", "report"):
        return "misc"
    if raw:
        return "misc"
    # Scholar: tebak dari venue.
    if "proceeding" in venue or "conference" in venue or "seminar" in venue:
        return "inproceedings"
    if "journal" in venue or "jurnal" in venue:
        return "article"
    return "misc"


def _bib_escape(value: str) -> str:
    return value.replace("{", "(").replace("}", ")").replace("\\", "")


def format_bibtex(record: dict, key: str) -> str:
    etype = _entry_type(record)
    authors = " and ".join(a for a in (record.get("authors") or []) if a) or "Tanpa Penulis"
    title = _bib_escape((record.get("title") or "").strip())
    year = record.get("year") or "n.d."
    venue = _bib_escape((record.get("venue") or "").strip())

    fields: list[tuple[str, str]] = []
    if etype == "article":
        fields.append(("author", authors))
        fields.append(("title", title))
        fields.append(("journal", venue or "Tanpa Jurnal"))
        fields.append(("year", str(year)))
    elif etype == "book":
        fields.append(("author", authors))
        fields.append(("title", title))
        fields.append(("publisher", venue or "Tanpa Penerbit"))
        fields.append(("year", str(year)))
    elif etype == "inproceedings":
        fields.append(("author", authors))
        fields.append(("title", title))
        fields.append(("booktitle", venue or "Tanpa Prosiding"))
        fields.append(("year", str(year)))
    else:
        fields.append(("author", authors))
        fields.append(("title", title))
        fields.append(("year", str(year)))
        if venue:
            fields.append(("howpublished", venue))

    doi = record.get("doi")
    if doi:  # hanya DOI nyata yang pernah diambil
        fields.append(("doi", _bib_escape(doi)))
    url = record.get("url")
    if url and not doi:
        fields.append(("url", _bib_escape(url)))

    width = max(len(name) for name, _ in fields)
    lines = [f"@{etype}{{{key},"]
    for name, value in fields:
        lines.append(f"  {name.ljust(width)} = {{{value}}},")
    # Buang koma pada baris terakhir.
    lines[-1] = lines[-1].rstrip(",")
    lines.append("}")
    return "\n".join(lines)


def _existing_keys(path: str) -> set[str]:
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    return set(re.findall(r"^@\w+\{([^,]+),", text, re.MULTILINE))


def _dedupe_keys(records: list[dict], taken: set[str]) -> list[tuple[str, dict]]:
    """Pasangkan catatan dengan kunci unik.

    Catatan yang kunci dasarnya sudah ada di ``taken`` (mis. sudah ada di berkas
    tujuan) dilewati. Kunci yang bertabrakan antar catatan baru diberi akhiran
    ``a``, ``b``, ``c``, …
    """
    out: list[tuple[str, dict]] = []
    used = set(taken)
    for rec in records:
        base = make_key(rec)
        if base in taken:
            continue  # sudah ada di berkas tujuan -> lewati
        key = base
        suffix = "a"
        while key in used:
            key = base + suffix
            suffix = chr(ord(suffix) + 1)
        used.add(key)
        out.append((key, rec))
    return out


# ---------------------------------------------------------------------------
# Perintah
# ---------------------------------------------------------------------------


def cmd_search(args) -> int:
    query = args.query
    mailto = os.environ.get("SCHOLAR_EMAIL")
    records = resolve(query, args.limit, args.backend, mailto, to_stderr=args.json)

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0 if records else 1

    if not records:
        print("GAGAL: tidak ada hasil", file=sys.stderr)
        return 1

    for i, rec in enumerate(records, start=1):
        authors = ", ".join(rec.get("authors") or []) or "Tanpa Penulis"
        year = rec.get("year") or "n.d."
        venue = rec.get("venue") or "-"
        ident = rec.get("doi") and f"https://doi.org/{rec['doi']}" or rec.get("url") or "-"
        print(f"[{i}] {authors} ({year}). {rec['title']}. {venue}. {ident}")
        if i < len(records) and rec.get("source") == "scholar":
            time.sleep(1 + (i % 3))  # 1-3 detik antar permintaan Scholar
    return 0


def _emit(records: list[dict], out: str | None) -> int:
    if not records:
        print("GAGAL: tidak ada hasil", file=sys.stderr)
        return 1

    if out is None:
        pairs = _dedupe_keys(records, set())
        for i, (key, rec) in enumerate(pairs):
            if i:
                print()
            print(format_bibtex(rec, key))
        return 0

    existing = _existing_keys(out)
    pairs = _dedupe_keys(records, existing)
    added: list[str] = []
    blocks: list[str] = []
    for key, rec in pairs:
        if key in existing:
            continue
        blocks.append(format_bibtex(rec, key))
        added.append(key)

    if not blocks:
        print("# tidak ada entri baru (semua kunci sudah ada)")
        return 0

    prefix = ""
    if os.path.exists(out) and os.path.getsize(out) > 0:
        with open(out, encoding="utf-8") as fh:
            tail = fh.read()
        prefix = "" if tail.endswith("\n\n") else ("\n" if tail.endswith("\n") else "\n\n")

    with open(out, "a", encoding="utf-8") as fh:
        fh.write(prefix + "\n\n".join(blocks) + "\n")

    for key in added:
        print(key)
    return 0


def cmd_bib(args) -> int:
    mailto = os.environ.get("SCHOLAR_EMAIL")

    if args.doi:
        rec = crossref_by_doi(args.doi, mailto)
        if rec is None:
            print("GAGAL: tidak ada hasil", file=sys.stderr)
            return 1
        rec["doi"] = rec.get("doi") or args.doi
        return _emit([rec], args.out)

    records = resolve(args.query, args.limit, args.backend, mailto)
    return _emit(records, args.out)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scholar.py",
        description="Cari referensi (Google Scholar/Crossref/OpenAlex) dan hasilkan BibTeX.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p):
        p.add_argument("query", help="kueri pencarian")
        p.add_argument("--limit", type=int, default=5, help="jumlah maksimum hasil (default: 5)")
        p.add_argument("--backend", choices=BACKENDS, default="auto",
                       help="backend pencarian (default: auto)")

    p_search = sub.add_parser("search", help="cari referensi dan tampilkan hasil")
    add_common(p_search)
    p_search.add_argument("--json", action="store_true", help="keluarkan JSON")
    p_search.set_defaults(func=cmd_search)

    p_bib = sub.add_parser("bib", help="cari referensi dan hasilkan BibTeX")
    p_bib.add_argument("query", nargs="?", default=None, help="kueri pencarian")
    p_bib.add_argument("--limit", type=int, default=5, help="jumlah maksimum hasil (default: 5)")
    p_bib.add_argument("--backend", choices=BACKENDS, default="auto",
                       help="backend pencarian (default: auto)")
    p_bib.add_argument("--doi", default=None, help="selesaikan satu DOI via Crossref")
    p_bib.add_argument("--out", default=None, help="berkas BibTeX tujuan (append, de-duplikat)")
    p_bib.set_defaults(func=cmd_bib)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "bib" and not args.doi and not args.query:
        parser.error("bib memerlukan QUERY atau --doi")
    try:
        return args.func(args)
    except urllib.error.URLError as exc:
        print(f"GAGAL: jaringan tidak tersedia ({exc})", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
