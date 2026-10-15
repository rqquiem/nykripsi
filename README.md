# Nykripsi v2

A Markdown + Pandoc workspace that produces **two deliverables from a single set
of source files**:

1. a **skripsi** (Indonesian undergraduate thesis) PDF, following the
   *STMIK Triguna Dharma* — Hubungan Internasional pedoman, and
2. a **Sinta-targeted journal article** (`content/artikel/artikel-sinta.md`),
   built as a DOCX + PDF draft.

The workspace is opinionated: it ships a **Claude Code workspace skill** for
authoring, an **Indonesian academic-register linter** (`ragam bahasa ilmiah`),
and a **validator suite** that enforces citations ↔ `assets/refs.bib`, corpus
manifests, research notes, sources, and the overall workflow. Everything is
plain text and reproducible — no proprietary word processor in the loop.

## The study

The current thesis is:

> **Analisis Strategi Diplomasi Publik Tiongkok terhadap Indonesia melalui
> Diplomasi Vaksin pada Masa Pandemi Covid-19 Tahun 2020–2022**

It analyses China's vaccine diplomacy towards Indonesia as a case of public
diplomacy, using a qualitative case-study method and a Foreign Policy Analysis
(FPA) framework. The theoretical framework harmonises three lenses — public
diplomacy, soft power & nation branding, and FPA — into one integrated
public-diplomacy/soft-power lens with FPA as a cross-stage level of analysis.

## Outputs

| Path | What it is |
| --- | --- |
| `out/skripsi.pdf` | The full skripsi PDF. |
| `out/artikel-sinta.docx` | The Sinta article draft (content-and-style draft). |
| `out/artikel-sinta.pdf` | The Sinta article PDF. |
| `out/artikel-datacenter.docx` | The `artikel-datacenter` article draft (content-and-style draft). |
| `out/artikel-datacenter.pdf` | The `artikel-datacenter` article PDF. |

`out/` is build output and is **not** tracked.

## Repository layout

| Path | Role |
| --- | --- |
| `content/skripsi/*.md` | Skripsi chapters + front matter (`00`–`06`, `10`–`15`, `90`), concatenated in filename order. |
| `content/artikel/artikel-sinta.md` | The Sinta journal article source. |
| `content/drafts/` | Work-in-progress chapters; **excluded** from `make check`. |
| `assets/refs.bib` | BibTeX database — every `[@key]` citation resolves against this file. |
| `assets/bahasa/kamus-id.yaml` | Structure + diction dictionary (headings, formulas, standard vocabulary, argument phrasing, `istilah_asing`, `singkatan`, `istilah_teknis`, `tanda_pisah`). |
| `assets/csl/apa.csl` | CSL style used by `--citeproc` (default APA 7). |
| `assets/figures/` | Figures referenced by the chapters. |
| `templates/` | LaTeX preambles, article metadata, and the reference DOCX. |
| `tools/` | Build/validation scripts (`check.sh`, `check-bahasa.sh`, `gen_kamus.py`, `validate.py`, `promote.py`, `libgen.py`, `table.py`, corpus fetchers). |
| `tools/pandoc_filters/` | Pandoc Lua filters (`sinta_layout.lua`, `figure_table.lua`, `bilingual.lua`, `table.lua`). |
| `tools/validators/` | Individual validators (papers, sources, research, journals, corpora, workflow, …). |
| `docs/` | Project documentation, plus the downloaded research corpora. |
| `research/` | Title-availability registry (`judul.json`) and research-gap reports. |
| `sources/` | Multi-source search store (`registry.json`) + generated index. |
| `.claude/skills/nykripsi/` | The Claude Code workspace skill (scripts, references, `SKILL.md`). |

## Requirements

- **Pandoc** (with `--citeproc`) and a **XeLaTeX** engine for PDF output.
- **Python 3** (standard library) plus `python-docx` and `pyyaml` for the
  DOCX/DOCX-reference and dictionary tooling.
- `make`.
- Optional: the `claude` CLI for the LLM re-read pass (`make validate-agent`).

On Arch Linux the one-shot setup target installs the toolchain:

```bash
make setup
```

If `pandoc-cli` is unavailable, download the static release from
<https://github.com/jgm/pandoc/releases/latest> into `~/.local/bin/pandoc` and
make it executable:

```bash
chmod +x ~/.local/bin/pandoc
```

## Make targets

| Target | Purpose |
| --- | --- |
| `make setup` | Prepare the toolchain (run once). |
| `make skripsi` | Build `out/skripsi.pdf`. |
| `make artikel` | Build the Sinta article (`out/artikel-sinta.docx` + `.pdf`). |
| `make artikel-datacenter` | Build `artikel-datacenter.md` → `out/artikel-datacenter.docx` + `.pdf`. |
| `make artikel-hi` | Build the Indonesian HI/IR article → `out/artikel-hi.docx` + `.pdf`. |
| `make artikel-hi-en` | Build the English HI/IR article → `out/artikel-hi-en.docx` + `.pdf`. |
| `make all` | Build both (default target). |
| `make check` | Build both, then run every check below (the main gate). |
| `make check-bab1` | Validate the BAB I framework (`10-bab-01-pendahuluan.md`). |
| `make validate` | Run the validator suite (`tools/validate.py`). |
| `make validate-agent` | Same, plus an LLM re-read pass confirming each claim (needs the `claude` CLI). |
| `make validate-offline` | Validator suite without network access. |
| `make check-drafts` | Lint the Indonesian register of drafts in `content/drafts/`. |
| `make promote` | Promote a finished draft (`DRAFT=<file>`) into its final location. |
| `make sources` | Regenerate `sources/index.md` from `sources/registry.json`. |
| `make subjects` | Regenerate `subjects/index.md` from `subjects/registry.json`. |
| `make scrape` | Sweep secondary channels for a subject (`S=<nama>`) into `subjects/registry.json`. |
| `make research` | Regenerate `research/index.md` (title availability + research-gap index). |
| `make corpus` | Download the Sinta journal study corpus into `docs/sinta-corpus/`. |
| `make corpus-hi` | Download the Hubungan Internasional journal corpus into `docs/ir-corpus/`. |
| `make corpus-libgen` | Download the LibGen reference corpus into `docs/libgen-corpus/`. |
| `make webgrab` | Fetch one URL (`URL=<url>`) into the git-ignored web corpus (`docs/web-corpus/`). |
| `make webdiscover` | Discover candidate URLs for a query (`Q="<q>"`) and fetch them. |
| `make kamus` | Regenerate structure & documents from the dictionary (`assets/bahasa/kamus-id.yaml`). |
| `make tables` | Render `.table` blocks (`tools/table.py`) into native tables. |
| `make clean` | Remove build artifacts. |

## Validation

`make check` is the single source of truth. It runs:

1. `tools/check.sh` — workflow/structure checks.
2. `tools/check-bahasa.sh` — the **Indonesian register linter**. It rejects
   first/second-person pronouns (`saya`, `kami`, `kita`, `anda`, …),
   non-standard vocabulary (EYD Edisi V), and generic AI filler phrases, on the
   skripsi chapters and the Sinta article.
3. `tools/gen_kamus.py --check` — the dictionary/structure lines must stay in
   sync.
4. `tools/validate.py` — the validator suite, including:
   - **papers** — every `[@key]` in `content/**/*.md` exists in `assets/refs.bib`
     *and* every bib entry is cited somewhere (no orphan entries);
   - **sources / research / journals / corpora / workflow** — schema and
     consistency checks for `sources/`, `research/`, and the corpus manifests.
   - **web_corpus** — enforces WG1–WG8 / manifest consistency for
     `docs/web-corpus/manifest.tsv`: nine columns
     (`slug,url,accessed,mode,status,http,bytes,sha256,text_chars`), unique valid
     slugs, dated `accessed`, `mode` ∈ {`curl`, `headless-puppeteer`,
     `headless-chrome`}, 64-hex `sha256`, and a `MANIFEST.md` `FAILED=<n>` that
     matches the non-`ok` rows (curl-first acquisition, headless escalation, and
     provenance are never fabricated).
   - **bab1_framework** — menegakkan aturan BAB I (lima subbagian, tag formula,
     pita Latar Belakang, lima Batasan, Manfaat teoretis+praktis);
   - **article_framework** — kini mencakup `artikel-kyt.md` (fail) **dan**
     `artikel-sinta.md` (warn), serta varian HI/IR `content/artikel/artikel-hi.md`
     (fail) dan `content/artikel-en/artikel-hi-en.md` (fail).
   - **citation_framework** — enforces CT1–CT7 over
     `content/{artikel,skripsi,drafts}` + `assets/refs.bib`; **CT7** menegakkan
     tautan daftar pustaka (hanya berita/siaran pers/web menampilkan URL; karya
     akademik menampilkan DOI, tidak pernah URL).
   - **evidence_recency** — menegakkan kebaruan bukti: sumber bukti
     (Berita/Siaran pers/Artikel/Web) wajib ≤ 5 tahun dan di dalam `periode`
     dokumen (`assets/bahasa/kamus-id.yaml` §`recency`; bawaan `2020–2025`).
   - **layout_typography**: enforces the Sinta article layout (LT2, LT6) via
     `tools/pandoc_filters/sinta_layout.lua`: centered front matter/abstract,
     ALL-CAPS headings, justified body, italic foreign terms; it also enforces
     LT7 via `tools/pandoc_filters/bilingual.lua` (second-language `::: {lang=en}`
     blocks, e.g. `ABSTRACT`, are italicized when `bahasa.utama` differs), LT8
     (no em dash `—` or spaced hyphen ` - ` in prose, en dash `–` only for
     numeric ranges, and automatic hyphenation suppressed via
     `\hyphenpenalty`/`\exhyphenpenalty` in `templates/*-preamble.tex`), and LT9
     (each `istilah_teknis` term carries an English gloss in parentheses at its
     first prose occurrence). The
     `.table` generator (`tools/table.py`, filter `tools/pandoc_filters/table.lua`)
     emits **native** tables; `.table` columns wrap by default, and `make tables`
     renders them. `make diagrams` renders the diagram tree.

A successful run prints `SEMUA PEMERIKSAAN LULUS.`, `KAMUS: SELARAS.`,
`RAGAM BAHASA: LULUS.`, and `VALIDASI: LULUS.`.

## Research corpora are not tracked

`docs/sinta-corpus/`, `docs/ir-corpus/`, and `docs/libgen-corpus/` hold
**third-party copyrighted material** (journal articles and LibGen books). To
respect copyright and keep the repository small, only each corpus's
`MANIFEST.md` and `manifest.tsv` are committed — the PDFs are git-ignored and
must be re-fetched locally:

```bash
make corpus        # Sinta journal study corpus
make corpus-hi     # Hubungan Internasional corpus
make corpus-libgen # LibGen reference corpus
```

The corpus validators expect the PDFs to be present on disk, so a fresh clone
should run the relevant `make corpus*` target before `make check`.

## Convention: ALL-CAPS BAB headings

Write BAB headings in the Markdown source in **ALL CAPS**, e.g.:

```markdown
# PENDAHULUAN
```

## Convention: bilingual blocks and generated tables

Mark a second-language block with `::: {lang=en} … :::` (the article's
`ABSTRACT` carries `lang=en`); when `bahasa.utama` in `assets/bahasa/kamus-id.yaml`
differs, `tools/pandoc_filters/bilingual.lua` italicizes the block (LT7).
Write generated tables as a `{.table #tbl-<slug>}` fence containing YAML; run
`make tables` to render them via `tools/table.py` into **native** tables.

## Workspace skill

`.claude/skills/nykripsi/` is a Claude Code **workspace skill** for this repo:

- **Google Scholar reference gathering** — collects sources into
  `assets/refs.bib` (falling back to Crossref/OpenAlex).
- **Multi-source gathering** — `.claude/skills/nykripsi/scripts/search.py` also
  gathers general web results, forum/Q&A discussion, and video sources
  (alongside news, articles, books, datasets, public data, company filings, and
  open-access PDFs) into `sources/registry.json`. Each gathered source is
  classified as **primary** (*kebenaran subjek* — a direct interview of the
  company/main actor) or **secondary** (*kebenaran pendukung* — the subject's
  press release plus news, articles, and other mediated material).
- **Scaffolding/authoring the skripsi** from the Sinta-derived templates —
  generates and fills `content/skripsi/` chapters (see
  `scripts/scaffold.py` and `references/skripsi-structure.md`).
- **Judul-availability + research-gap framework** — checks whether a thesis
  title is still available (blocking `duplicate`/`too-similar` verdicts),
  records browser cross-check findings, and scaffolds the gap report
  (`research/judul.json`, `scripts/research_gap.py`, `docs/research-gap.md`).
- **Full-text rule** — obtain and verify the full text before concluding: follow
  the acquisition ladder, and record `access_level`/`fulltext_*` in
  `sources/registry.json`.
- **Subject sweep** — declare a research subject and sweep every secondary
  channel (press release, news, article, official, web) until saturation,
  tagging each source with `subject`/`channel` in `sources/registry.json` and
  tracking per-subject coverage in `subjects/registry.json`
  (`scripts/search.py`, `tools/scrape.py`, `docs/subject-framework.md`).

Claude Code auto-discovers the skill from the project directory, so it is
available in any session opened in this workspace. `make check` enforces the
resulting structure, register, and citations.

## Documentation

- [docs/workflow.md](docs/workflow.md) — the numbered end-to-end walkthrough.
- [docs/skripsi-pedoman.md](docs/skripsi-pedoman.md) — the STMIK Triguna Dharma pedoman checklist.
- [docs/conversion-skripsi-to-article.md](docs/conversion-skripsi-to-article.md) — skripsi → article conversion.
- [docs/sinta-reference.md](docs/sinta-reference.md) — Sinta target-journal reference + pre-submit checklist.
- [docs/bahasa-artikel.md](docs/bahasa-artikel.md) — the Indonesian academic register rules.
- [docs/kamus-bahasa-artikel.md](docs/kamus-bahasa-artikel.md) — the register dictionary.
- [docs/kamus-riset-korpus.md](docs/kamus-riset-korpus.md) / [docs/kamus-riset-korpus-hi.md](docs/kamus-riset-korpus-hi.md) — corpus research dictionaries.
- [docs/source-classification.md](docs/source-classification.md) — primary/secondary source framework.
- [docs/research-gap.md](docs/research-gap.md) — title-availability + research-gap method.
- [docs/fulltext-framework.md](docs/fulltext-framework.md) — full-text acquisition + verification framework.
- [docs/subject-framework.md](docs/subject-framework.md) — subject-sweep (secondary-source) framework.
- [docs/webgrab-framework.md](docs/webgrab-framework.md) — web-grab (curl → headless escalation) framework (WG1–WG8).
- [docs/argument-framework.md](docs/argument-framework.md) — kerangka alur argumen & kohesi paragraf (drafting jurnal/riset/paper).
- [docs/diagram-framework.md](docs/diagram-framework.md) — kerangka diagram, tabel & fungsi keluaran (caption, penomoran, D1–D7; termasuk generator tabel `.table` yang membungkus kolom secara bawaan, dan `make diagrams` yang merender pohon).
- [docs/sintesa-diagram-framework.md](docs/sintesa-diagram-framework.md) — kerangka diagram sintesa teori / lensa terpadu (TS1–TS6; skema empat lapis `teori_utama`/`teori_pendukung`/`cabang_bukti`/`lingkup`/`lensa`).
- [docs/bagan-diagram-framework.md](docs/bagan-diagram-framework.md) — kerangka bagan simpul-sisi/pohon (BG1–BG5).
- [docs/layout-framework.md](docs/layout-framework.md): kerangka tata letak & tipografi (LT1–LT9; kata miring, singkatan/kepanjangan, tata letak Sinta terpusat, bahasa kedua miring, larangan em dash/hyphen berspasi, padanan Inggris istilah teknis).
- [docs/judul-framework.md](docs/judul-framework.md) — mutu judul ditegakkan oleh validator `judul` (JD1–JD6) via `tools/validators/judul.py`.
- [docs/citation-framework.md](docs/citation-framework.md) — kerangka sitasi & catatan kaki (CT1–CT6; `[@key]`, `[@a; @b]`, footnote penjelas, kutipan langsung).
- [docs/bab1-framework.md](docs/bab1-framework.md) — kerangka BAB I / Pendahuluan (A1–A8/B1–B3; gerak CARS, pita panjang).
- [docs/bab1-corpus-stats.md](docs/bab1-corpus-stats.md) — statistik korpus BAB I (85 paper).
- [docs/article-framework.md](docs/article-framework.md) — kerangka artikel jurnal (AR1–AR8; IMRaD, abstrak dwibahasa, konversi skripsi).
- [docs/ir-article-framework.md](docs/ir-article-framework.md) — kerangka artikel HI/IR dwibahasa (IA1–IA8).
- [CONTRIBUTING.md](CONTRIBUTING.md) — development workflow and conventions.

## License & status

This is a **private** repository containing unpublished academic work and
third-party research material; no open-source license is granted. Do not
redistribute the content or the research corpora.
