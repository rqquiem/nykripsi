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
  "subject": null,
  "channel": null,
  "access_level": "fulltext|abstract-only|inaccessible",
  "fulltext_url": null,
  "fulltext_sha256": null,
  "fulltext_pages": null,
  "fulltext_verified": false,
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

## Subject and channel

Every record also carries **`subject`** and **`channel`** for the subject sweep
(provenance). Both default to `null` and are filled when a source is gathered
for a named research subject:

- `subject` — the research subject the source belongs to (a company, actor,
  institution, or state). `null` when the source is not tied to a swept subject.
- `channel` — the sweep channel the source came from, one of
  `press` (first-party press release), `news`, `article`, `official` (official
  or company documents), or `web` (general web). `null` when not swept.

Both are set from the CLI with `--subject` / `--channel` (see the `search.py`
subcommands) and are preserved for existing records. The subject registry
(`subjects/registry.json`) counts sources per channel and per subject. See
[`docs/subject-framework.md`](../docs/subject-framework.md) for the full
framework.

## Full-text access level

Every record also carries an **`access_level`** describing how much of the
source's body text is actually available to the writer. It is one of
`fulltext`, `abstract-only`, or `inaccessible`; the default is the most
conservative value, `inaccessible`. Only a **verified** full text may be
recorded as `fulltext`. See
[`docs/fulltext-framework.md`](../docs/fulltext-framework.md) for the full
framework.

- `fulltext` — a real PDF body was obtained and verified (page count ≥ 2,
  contains a body marker such as `PENDAHULUAN`/`INTRODUCTION`/`METHOD`/`RESULTS`
  /`REFERENCES`, and is not a paywall page). Records at this level MUST carry
  `fulltext_url` (non-empty string), `fulltext_sha256` (64-char hex digest),
  `fulltext_pages` (integer ≥ 2), and `fulltext_verified: true`.
- `abstract-only` — only the abstract/metadata is reachable; the body text is
  not available.
- `inaccessible` — no lawful access (paywalled, dead link, or credential
  required). Never fabricate a file or URL to fill this gap.

The F1–F8 rules enforced here and by `tools/validators/sources.py`:

- **F1** — every record must have `access_level` ∈ {`fulltext`,
  `abstract-only`, `inaccessible`}; the default is `inaccessible`.
- **F2** — `fulltext` may be claimed only after verification of the downloaded
  PDF (pages ≥ 2, body marker present, not a paywall page).
- **F3** — a `fulltext` record must have `fulltext_url` (non-empty string),
  `fulltext_sha256` (64-hex), `fulltext_pages` (int ≥ 2), and
  `fulltext_verified: true`; any missing/invalid field is a validation failure.
- **F4** — `fulltext_sha256` is computed from the PDF actually downloaded; the
  PDF itself stays local and git-ignored, only the record/manifest is tracked.
- **F5** — `abstract-only` means only abstract/metadata is available; no body
  text was obtained.
- **F6** — `abstract-only` and `inaccessible` records MUST NOT be used as the
  basis for substantive conclusions or claims; they may only be cited for their
  existence/metadata.
- **F7** — `inaccessible` means no lawful access; never invent a PDF, hash,
  page count, or URL.
- **F8** — shadow libraries (Sci-Hub / Anna's Archive) are a last resort only,
  must not bypass captchas, and any retrieved PDF remains git-ignored.

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
