---
name: nykripsi
description: "Author and build the Nykripsi v2 skripsi (undergraduate thesis) and Sinta-targeted journal article in this Markdown+Pandoc workspace. Use when asked to author or draft a skripsi/thesis chapter (BAB I–VI), scaffold BAB I–VI from the Sinta-derived templates, write or revise content/skripsi/*.md or content/artikel/artikel-sinta.md, build the skripsi PDF or the Sinta article, search Google Scholar or find references/papers for a topic, add BibTeX citations to assets/refs.bib, resolve a DOI, run make check/validate, or follow the Indonesian academic register (ragam bahasa ilmiah) and the STMIK Triguna Dharma pedoman. Covers the whole workspace: chapter scaffolding, Google Scholar / Crossref / OpenAlex reference gathering into BibTeX, citation [@key] wiring, and validation of citations, DOIs, journals, and workflow."
argument-hint: "<topik skripsi atau kueri referensi>"
user-invocable: true
---

# Nykripsi v2 — Skripsi & Sinta Article Authoring

Author a **skripsi** and a **Sinta-targeted journal article** from a single set of
Markdown sources in the Nykripsi v2 workspace. This skill gathers real references
from Google Scholar (falling back to Crossref/OpenAlex), writes them to
`assets/refs.bib`, scaffolds the BAB I–VI skeleton from the repo's Sinta-derived
templates, and drives the Pandoc build and validator suite to completion.

## When to use this skill

Use it when the user asks to:

- **Search Google Scholar** or find papers/references for a topic.
- **Add citations** / build a bibliography / resolve a DOI into `assets/refs.bib`.
- **Scaffold** the skripsi skeleton (BAB I–VI) or write/revise a chapter
  (`content/skripsi/*.md`) or the Sinta article (`content/artikel/artikel-sinta.md`).
- **Build** the thesis or article (`make skripsi`, `make artikel`) or **validate**
  them (`make check`, `make validate`).
- Follow the **Indonesian academic register** and the STMIK Triguna Dharma
  pedoman while writing.

Do **not** use it to fabricate a citation or DOI, or to write chapters that
violate the register rules — `make check` will reject them.

## Workspace map

| Path | Role |
| --- | --- |
| `content/skripsi/*.md` | Skripsi chapters + front matter (00–06, 10–15, 90), concatenated in filename order |
| `content/artikel/artikel-sinta.md` | The Sinta journal article source |
| `assets/refs.bib` | BibTeX database (all citations resolve against this file) |
| `assets/bahasa/kamus-id.yaml` | Structure + diction dictionary (`kepala_bagian`, `formula`, `kosakata_baku`, `rangkai_argumen`) |
| `assets/csl/apa.csl` | CSL style used by `--citeproc` (default APA 7) |
| `templates/` | `skripsi-preamble.tex`, `artikel-preamble.tex`, `artikel-meta.yaml`, `journal-reference.docx` |
| `docs/skripsi-pedoman.md` | STMIK Triguna Dharma pedoman (layout, typography, ≥ 20 references, BAB sub-sections) |
| `docs/sinta-reference.md` | Sinta ranking / ARJUNA notes and journal requirements |
| `docs/conversion-skripsi-to-article.md` | Skripsi → Sinta article mapping and rewrite rules |
| `docs/bahasa-artikel.md` | Sourced Indonesian register rules |
| `docs/kamus-bahasa-artikel.md` | Generated human-readable dictionary |
| `docs/kamus-riset-korpus.md` | Corpus research notes (29 Sinta PDFs) |
| `docs/workflow.md` | Numbered build walkthrough |
| `sources/registry.json` | Multi-source search store (JSON array of source records) |
| `sources/index.md` | Generated index of the registry (`make sources`) |
| `research/judul.json` | Judul-availability registry (title verdicts: `available`/`too-similar`/`duplicate`) |
| `research/gap-<slug>.md` | Research-gap report scaffold (weakness dimensions + angle + novelty) |
| `research/index.md` | Generated index of the judul registry (`make research`) |
| `content/drafts/` | Staging folder for draft material before promotion |
| `tools/validate.py` + `tools/validators/` | Validator suite (`workflow`, `journals`, `papers`, `research_notes`, `doi`, `sources`, `research`) |
| `tools/check.sh`, `tools/check-bahasa.sh` | Build + register linters run by `make check` |

**Make targets:** `setup`, `skripsi`, `artikel`, `check`, `kamus`, `corpus`,
`check-drafts`, `promote`, `sources`, `research`, `validate`, `validate-agent`,
`validate-offline`, `clean`.

Chapter skeleton spec: [`references/skripsi-structure.md`](references/skripsi-structure.md).

## Non-negotiable rules

1. **Never fabricate a reference or DOI.** Every record written to
   `assets/refs.bib` must come from a tool call in this session. If it was not
   retrieved, do not write it.
2. **Respect the Indonesian academic register.** No first/second-person pronouns
   (`saya`, `aku`, `kami`, `kita`, `anda`, `kamu`, `kalian`); use passive forms
   and baku diction (EYD Edisi V). Enforced by `make check` via
   `tools/check-bahasa.sh`.
3. **Write BAB headings in ALL-CAPS** in Markdown (`# PENDAHULUAN`), e.g. `#
   TINJAUAN PUSTAKA`, `# METODOLOGI PENELITIAN`.
4. **Keep the abstract free of citations** (and of abbreviations and footnotes) —
   enforced by the `papers` validator.
5. **Run `make check` before declaring anything done**, and keep
   `python3 tools/validate.py` green.

## Workflow A — Google Scholar references

### 1. Search

```bash
python3 .claude/skills/nykripsi/scripts/scholar.py search "<query>" --limit 5
python3 .claude/skills/nykripsi/scripts/scholar.py search "<query>" --json
```

### 2. Emit BibTeX (appends, de-duplicated)

```bash
python3 .claude/skills/nykripsi/scripts/scholar.py bib "<query>" --limit 5 --out assets/refs.bib
python3 .claude/skills/nykripsi/scripts/scholar.py bib --doi 10.xxxx/yyyy
```

With `--out assets/refs.bib` the script **appends** new entries, skipping any key
already present in the file, and prints the added keys. Without `--out` it prints
BibTeX to stdout.

### 3. Cite and verify

Cite in Markdown as `[@key]`, then verify:

```bash
python3 tools/validate.py papers
python3 tools/validate.py doi
# or: make validate
```

`papers` checks that every `[@key]` exists in `assets/refs.bib` and that every
bib entry is cited; `doi` checks DOI structure and (online) resolvability.

### Backends (read this before trusting the output)

Google Scholar has **no API** and may block automated access; the script reports
`# backend: scholar|crossref|openalex` on stdout and falls back automatically
(`# backend: scholar (blocked -> crossref)` when it does). Crossref and OpenAlex
return **real DOIs**; Scholar records have no DOI. Set `SCHOLAR_EMAIL` to join
the polite Crossref/OpenAlex pools. **NEVER invent a citation or DOI** — if the
script returns nothing, say so; do not fill the gap by hand.

## Workflow B — create the skripsi

### 1. Scaffold the BAB I–VI skeleton

```bash
python3 .claude/skills/nykripsi/scripts/scaffold.py \
  --out content/skripsi --title "…" --author "…" --nim "…" --year 2026
```

See [`references/skripsi-structure.md`](references/skripsi-structure.md) for the
generated 14-file layout, the BAB I–VI sub-sections, and the `<!-- kamus:f id=… -->`
formula ids.

### 2. Fill the `<!-- TODO -->` markers

Replace each `<!-- TODO: … -->` with prose that follows the `formula:` entries in
`assets/bahasa/kamus-id.yaml` (the `<!-- kamus:f id=… -->` marker names the
formula). Keep the register rules from *Non-negotiable rules* above.

### 3. Cite with `[@key]`

Add references first (Workflow A), then cite with `[@key]` in the chapter text.

### 4. Build and check

```bash
make skripsi   # -> out/skripsi.pdf
make check     # build + register linter + validator suite
```

Follow [`docs/skripsi-pedoman.md`](../../../docs/skripsi-pedoman.md) for layout,
typography, the ≥ **20 references** rule (last 5 years, ≥ 30% international), and
the required BAB sub-sections. To turn the finished skripsi into the Sinta
article, follow [`docs/conversion-skripsi-to-article.md`](../../../docs/conversion-skripsi-to-article.md).

## Workflow C — multi-source search

Gather non-BibTeX source material (news, articles, books, datasets, public
data, company filings, open-access PDFs, interview leads, general web/website
results, forum/Q&A discussion, and video) into `sources/registry.json`, with a
generated `sources/index.md`. `search.py` exposes **11 search subcommands**
plus `classify` and `render` (13 total). Every record is classified as
**primary** (kebenaran subjek — a direct interview of the company / main actor /
main subject) or **secondary** (kebenaran pendukung — the subject's press
release, plus news, articles, and other mediated/third-party material); the
class defaults from `type` (`interview` -> `primary`, else `secondary`) and can
be overridden per record with `--class {primary,secondary}`. See
[`docs/source-classification.md`](../../../docs/source-classification.md) for the
full framework.

```bash
S=.claude/skills/nykripsi/scripts/search.py

python3 $S news       "Indonesia nation branding" --limit 5
python3 $S article    "nation branding"            --limit 5
python3 $S book       "nation branding"            --limit 5
python3 $S interview  "UMKM digital"  --template "Pemilik UMKM"
python3 $S dataset    "tourism"                    --limit 5
python3 $S publicdata "tourism"                    --limit 5
python3 $S company    "Pertamina"                  --limit 5
python3 $S pdf        "nation branding"            --limit 5
python3 $S web        "nation branding"            --limit 5
python3 $S forum      "nation branding"            --limit 5
python3 $S video      "nation branding"            --limit 5
python3 $S classify        # recompute classes from type; --class X forces all
python3 $S render          # or: make sources
```

Each subcommand writes new records to `sources/registry.json` (de-duplicated by
`url`/`doi`) and prints human lines plus `TAMBAH: <n> baru, <m> duplikat
dilewati`. Common flags: `--limit N` (default 10), `--registry PATH`,
`--index PATH`, `--json`, `--no-save`, `--class {primary,secondary}` (override
the record's source class; marks it `manual`), and `--email ADDR` (polite pool /
SEC User-Agent; falls back to `$SCHOLAR_EMAIL`). `classify` recomputes every
non-manual record's class from its `type` (or forces all records with
`--class X`). `render` (or `make sources`) regenerates `sources/index.md` from
the registry — never hand-edit the index.

`interview --template NAME` writes a `sources/interview-<slug>.md` skeleton and
adds **no** registry record (a template has no retrievable URL).

**Keyless backends:** `gdelt`, `googlenews`, `scholar`/`crossref`/`openalex`
(via `scholar.py`), `openlibrary`, `googlebooks`, `datacite`, `zenodo`,
`worldbank`, `wikidata`, `sec-edgar`, `openalex-oa`, `core`, `duckduckgo`,
`ddg-instant`, `wikipedia`, `stackexchange`, `hackernews`, `invidious`,
`piped`. The `web` backends are `duckduckgo`, `ddg-instant`, `wikipedia`; the
`forum` backends are `stackexchange`, `hackernews`; the `video` backends are
`invidious` and `piped`, which are **best-effort** public instances that may be
down (errors are non-fatal). CORE and Google
Books may return `429`/`401`; those errors are non-fatal and the subcommand
skips them. GDELT is rate-limited to 1 req/5 s — the script sleeps and retries
once. If a backend is unreachable the script prints `GAGAL: ...` and leaves the
registry unchanged.

**Provenance rule:** never invent a record — every registry entry must come from
a live retrieval by `search.py`. Validate with `python3 tools/validate.py
sources` (or `make validate`).

### Draft-folder flow

Stage prose in `content/drafts/`, lint it with `make check-drafts`, and promote
a finished draft with `make promote` (`DRAFT=<file>`); the numbered walkthrough
lives in [`docs/workflow.md`](../../../docs/workflow.md).

## Workflow D — judul availability & research gap

Check whether a thesis **judul** is still available, cross-check it in a browser,
and scaffold the research-gap report. Full framework:
[`docs/research-gap.md`](../../../docs/research-gap.md).

**Rule:** a *selected* judul whose verdict is `duplicate` or `too-similar` is
**BLOCKED** by the `research` validator (wired into `make check`). A normalized
**exact** title match is `duplicate`; token-Jaccard similarity **≥ 0.80** is
`too-similar`; otherwise `available`. The threshold is overridable with
`--threshold`.

**Keyless `check`** searches Crossref + OpenAlex + Google Scholar (via
`scholar.py`) + the local registry, computes the verdict, and appends a judul
record to `research/judul.json`:

```bash
R=.claude/skills/nykripsi/scripts/research_gap.py
python3 $R check "Judul Penelitian" --limit 10 --threshold 0.80
python3 $R check "Judul Penelitian" --json --no-save
```

**Mandated browser pass (not build-gated).** After the keyless check, cross-check
manually over **Google Scholar**
(`https://scholar.google.com/scholar?q=<urlencoded judul>`) and a **normal search**,
then ingest each finding with `browser-record` (the verdict is recomputed):

```bash
python3 $R browser-record "Judul Penelitian" \
  --title "Karya yang ditemukan" --url "https://..." --year 2024 --backend scholar
```

**Gap scaffold.** Write `research/gap-<slug>.md`, then regenerate the index with
`render` (or `make research`):

```bash
python3 $R gap "Judul Penelitian" --prior "Judul Terdahulu|https://...|kelemahan|angle"
python3 $R render
```

**Method summary:** (a) collect prior works; (b) analyse their **weakness** across
the fixed dimensions `ruang lingkup, metode, data, populasi/konteks, rentang
waktu, variabel, teori, tingkat analisis`; (c) choose a **different angle** by
picking at least two dimensions on which the new study deliberately differs;
(d) formulate the **gap + novelty**. Never invent a match — every match comes
from a live retrieval or the agent's browser pass.

## Scripts

| Script | Purpose |
| --- | --- |
| [`scripts/scholar.py`](scripts/scholar.py) | Search Google Scholar / Crossref / OpenAlex; emit or append BibTeX to `assets/refs.bib`; resolve a DOI |
| [`scripts/search.py`](scripts/search.py) | Multi-source search into `sources/registry.json`; render `sources/index.md` (news, article, book, interview, dataset, publicdata, company, pdf, web, forum, video) |
| [`scripts/scaffold.py`](scripts/scaffold.py) | Scaffold the BAB I–VI skripsi skeleton (14 files) from the Sinta-derived templates |
| [`scripts/research_gap.py`](scripts/research_gap.py) | Judul availability check (Crossref/OpenAlex/Scholar + local registry) + browser-record ingest + gap-report scaffold; render `research/index.md` |

All scripts are dependency-free (Python 3 standard library only).

## Verification

Run after any edit:

```bash
python3 .claude/skills/nykripsi/scripts/scholar.py --help
python3 .claude/skills/nykripsi/scripts/scholar.py search "<query>" --limit 3
python3 .claude/skills/nykripsi/scripts/scholar.py search "<query>" --limit 3 --json
python3 .claude/skills/nykripsi/scripts/scholar.py bib "<query>" --limit 3 --backend crossref
python3 .claude/skills/nykripsi/scripts/search.py --help
python3 .claude/skills/nykripsi/scripts/search.py book "<query>" --limit 3
python3 .claude/skills/nykripsi/scripts/search.py render
python3 .claude/skills/nykripsi/scripts/research_gap.py --help
python3 .claude/skills/nykripsi/scripts/research_gap.py render
python3 tools/validate.py papers
python3 tools/validate.py doi
python3 tools/validate.py sources
python3 tools/validate.py research
make check
```

## Output format

When reporting back:

```markdown
## References added
| Key | Title | Year | DOI/URL | Backend |
| --- | --- | --- | --- | --- |

## Chapters / files changed
- <path> — <what changed>

## Validation
- `python3 tools/validate.py papers` → <result>
- `python3 tools/validate.py doi` → <result>
- `make check` → <result>
```

State the **backend** that served each query, and never present a record that no
tool call retrieved.
