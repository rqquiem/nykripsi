# `sources/` — Multi-source search store

This folder is the on-disk store for every source retrieved by
`.claude/skills/nykripsi/scripts/search.py` (Workflow C). It holds the raw
records and a generated human-readable index.

| File | Role |
| --- | --- |
| `sources/registry.json` | The machine-readable store: a JSON **array** of records. Edit this, never `index.md`. |
| `sources/index.md` | Generated index (`search.py render` / `make sources`). Regenerated from the registry — do not hand-edit. |
| `sources/interview-<slug>.md` | Interview templates written by `search.py interview --template NAME`. Not registry records (no retrievable URL). |

## Record schema

Every record carries **every** key below; unknown values are `[]` (authors) or
`null` (year/doi/publisher).

```json
{
  "id": "news-2026-10-08-<slug-of-title>",
  "type": "news|article|book|interview|dataset|publicdata|company|pdf|web|forum|video",
  "title": "...",
  "authors": ["..."],
  "year": 2026,
  "publisher": "...",
  "url": "https://...",
  "doi": "10.xxxx/...",
  "accessed": "2026-10-08",
  "query": "...",
  "backend": "gdelt|googlenews|scholar|crossref|openalex|openlibrary|googlebooks|datacite|zenodo|worldbank|wikidata|sec-edgar|openalex-oa|core|duckduckgo|ddg-instant|wikipedia|stackexchange|hackernews|invidious|piped",
  "source_class": "primary|secondary",
  "class_origin": "auto|manual",
  "notes": "",
  "cite_key": null
}
```

Rules enforced by the writer and by `tools/validators/sources.py`:

- `id` = `<type>-<accessed>-<slug(title)>`; the slug ASCII-folds the title and
  keeps only `[a-z0-9-]`. On collision the writer appends `-1`, `-2`, ….
- `accessed` = local date `YYYY-MM-DD`.
- `authors` is `[]`; `year` / `doi` / `publisher` are `null` when unknown.
- Every record MUST have a non-empty `url`.
- `source_class` is required and is `primary`/`secondary` (default:
  `interview` -> `primary`, every other `type` -> `secondary`);
  `class_origin` is `auto`/`manual`.
- Records are de-duplicated by `url` (case-insensitive) or `doi` before appending.

## Source classification

Each record carries a **source class**: `primary` (subject truth — a direct
interview of the company / main actor / main subject) or `secondary` (supporting
truth — the subject's press release, plus news, articles, and all other
mediated/third-party material). The class defaults from `type`
(`interview` -> `primary`, else `secondary`) and can be overridden with
`--class {primary,secondary}` or recomputed with the `classify` subcommand. See
[`docs/source-classification.md`](../docs/source-classification.md) for the full
framework.

## Subcommands

```
python3 .claude/skills/nykripsi/scripts/search.py <subcommand> QUERY [options]
```

| Subcommand | What it gathers |
| --- | --- |
| `news` | GDELT DOC 2.0 + Google News RSS. |
| `article` | Academic articles via `scholar.py` (Scholar/Crossref/OpenAlex). |
| `book` | OpenLibrary, then Google Books (best-effort). |
| `interview` | GDELT + Google News RSS, plus an optional `--template NAME` skeleton. |
| `dataset` | DataCite + Zenodo datasets. |
| `publicdata` | World Bank indicator catalog + Wikidata. |
| `company` | SEC EDGAR full-text search + Wikidata entity lookup. |
| `pdf` | OpenAlex OA (`is_oa:true`) + CORE (best-effort). |
| `web` | General website / web results: DuckDuckGo, DDG Instant Answer, Wikipedia. |
| `forum` | Q&A / discussion: Stack Exchange, Hacker News. |
| `video` | Video: Invidious, Piped (best-effort). |
| `classify` | Recompute each record's source class from its type (or force one with `--class`). |
| `render` | Regenerate `sources/index.md` from the registry. |

Common flags on every search subcommand: `--limit N` (default 10),
`--registry PATH`, `--index PATH`, `--json`, `--no-save`, `--class
{primary,secondary}` (override the record's source class; marks it `manual`),
and `--email ADDR` (polite pool / SEC User-Agent; falls back to
`$SCHOLAR_EMAIL`, default `research@example.com`). `render` takes only
`--registry` / `--index`.

## Keyless backends

All backends below work **without an API key** (a polite `User-Agent` /
mailto is sent where the provider asks for one):

| Backend | Subcommand(s) |
| --- | --- |
| `gdelt` | `news`, `interview` |
| `googlenews` | `news`, `interview` |
| `scholar` / `crossref` / `openalex` | `article` (via `scholar.py`) |
| `openlibrary` | `book` |
| `googlebooks` | `book` |
| `datacite` | `dataset` |
| `zenodo` | `dataset` |
| `worldbank` | `publicdata` |
| `wikidata` | `publicdata`, `company` |
| `sec-edgar` | `company` |
| `openalex-oa` | `pdf` |
| `core` | `pdf` |
| `duckduckgo` | `web` |
| `ddg-instant` | `web` |
| `wikipedia` | `web` |
| `stackexchange` | `forum` |
| `hackernews` | `forum` |
| `invidious` | `video` |
| `piped` | `video` |

## Requires a key / may be unavailable

- **CORE** (`pdf`): the public v3 endpoint may return `401`/`429` without a key;
  errors are non-fatal and the subcommand simply skips CORE.
- **Google Books** (`book`): may return `429`; a non-200 response is skipped
  silently and never fails the run.
- **Invidious / Piped** (`video`): the `invidious` and `piped` backends are
  best-effort and rely on public instances that may be down or rate-limited;
  errors are non-fatal and the subcommand simply skips the failing backend.
- **Google News RSS / GDELT** (`news`, `interview`): GDELT is rate-limited to
  one request per 5 s; the script sleeps 5 s before each call and retries once
  after a 10 s backoff on `429`.
- Any backend may be unreachable from a given network. The script then reports
  `GAGAL: ...` and leaves the registry unchanged.

## Provenance rule

**Never invent a record.** Every record in `sources/registry.json` must come from
a live retrieval by `search.py` in this session. If a backend returns nothing or
is unreachable, report which backend failed — do **not** fill the gap by hand.
