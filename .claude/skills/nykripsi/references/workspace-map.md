# Workspace Map — Nykripsi v2

Orientation for the `nykripsi` skill. Where the chapters, citations, templates,
and dictionaries live, how the build and validators work, and the rules that
apply to every edit. This is a map, not a copy — follow the linked documents for
the authoritative detail.

## Layout

| Path | What it holds |
| --- | --- |
| `content/skripsi/*.md` | Skripsi sources. Front matter (00–06), body chapters (10–15), bibliography (90). Pandoc concatenates them in **filename order**. |
| `content/artikel/` | Article sources: `artikel-sinta.md` (default), `artikel-kyt.md`, `artikel-arai.md`, `artikel-datacenter.md`, and the HI/IR variant `artikel-hi.md` (per-journal variants; its English counterpart is `content/artikel-en/artikel-hi-en.md`). |
| `assets/refs.bib` | The BibTeX database. Every `[@key]` in `content/**/*.md` must resolve to an entry here, and every entry must be cited. |
| `assets/bahasa/kamus-id.yaml` | Machine dictionary. Top-level keys: `kepala_bagian`, `kepala_tambahan`, `formula`, `kosakata_baku`, `istilah_asing`, `singkatan`, `istilah_teknis`, `tanda_pisah`, `frasa_ai_generik`, `leksikon_verba`, `konektor`, `kutipan`, `rangkai_argumen`, `judul` (plus corpus/structure keys such as `varian_kepala`, `bab1`, `artikel`, `abstrak`). |
| `assets/csl/apa.csl` | CSL style for `--citeproc` (repo default APA 7). |
| `assets/figures/` | Figures referenced from chapters (`assets/figures/contoh.png`). |
| `templates/` | Build inputs: `skripsi-preamble.tex`, `artikel-preamble.tex` (PDF preambles); `artikel-meta.yaml`, `artikel-kyt-meta.yaml`, `artikel-arai-meta.yaml` (metadata); `journal-reference.docx` (reference `.docx`). |
| `tools/pandoc_filters/sinta_layout.lua` | Pandoc filter that centers Sinta front matter/abstract and renders ALL-CAPS headings (LT6). |
| `tools/pandoc_filters/bilingual.lua` | Pandoc filter that italicizes second-language `lang=en` blocks when `bahasa.utama` differs (LT7). |
| `tools/validators/layout_typography.py` | Layout/typography enforcer (LT1–LT9): preamble anchors, italic foreign terms, abbreviation expansion, Sinta centered layout, bilingual blocks, dash ban (LT8), bilingual technical-term glosses (LT9). |
| `tools/pandoc_filters/figure_table.lua` | Pandoc filter for figure/table caption & numbering (see `docs/diagram-framework.md`). |
| `tools/table.py` + `tools/pandoc_filters/table.lua` | `.table` generator: renders `{.table}` YAML fences into **native** tables (LaTeX/OOXML), not images (`make tables`). |
| `tools/webgrab.py` | Web grab: `fetch <url>` (curl-first; escalate to headless puppeteer/chrome when the HTML is chaotic), `discover "<q>" --fetch`; archives raw+text in git-ignored `docs/web-corpus/` with provenance in `docs/web-corpus/manifest.tsv` (`make webgrab`, `make webdiscover`). |
| `tools/validators/judul.py` | Title-quality validator (JD1–JD6) over `research/judul.json` + article meta + `00-halaman-judul.md`. |
| `research/` | Research artifacts: `judul.json` (title bank), `gap-<slug>.md` (per-topic gap notes), `index.md`. |
| `sources/` | Source registry (`registry.json`, `index.md`) rendered by `make sources`. |
| `subjects/` | Subject registry (`registry.json`, `index.md`) rendered by `make subjects`. |
| `out/` | Build artifacts: `skripsi.pdf`; `artikel-sinta.docx/.pdf`; `artikel-kyt.docx/.pdf`; `artikel-arai.docx/.pdf`; `out/artikel-datacenter.docx/.pdf`. Git-ignored. |

## Documentation (read these, don't duplicate them)

- [`docs/workflow.md`](../../../../docs/workflow.md) — numbered build walkthrough.
- [`docs/skripsi-pedoman.md`](../../../../docs/skripsi-pedoman.md) — STMIK Triguna Dharma
  pedoman: layout, typography, ≥ 20 references, BAB I–VI sub-sections.
- [`docs/conversion-skripsi-to-article.md`](../../../../docs/conversion-skripsi-to-article.md)
  — skripsi → Sinta article mapping and rewrite rules.
- [`docs/bahasa-artikel.md`](../../../../docs/bahasa-artikel.md) — sourced Indonesian
  academic register rules.
- [`docs/kamus-bahasa-artikel.md`](../../../../docs/kamus-bahasa-artikel.md) — generated
  human-readable dictionary (from `make kamus`).
- [`docs/kamus-riset-korpus.md`](../../../../docs/kamus-riset-korpus.md) — corpus research
  notes over the 29 Sinta PDFs.
- [`docs/sinta-reference.md`](../../../../docs/sinta-reference.md) — Sinta ranking,
  ARJUNA indicators, journal requirements.
- [`docs/judul-framework.md`](../../../../docs/judul-framework.md) — title-quality
  framework (JD1–JD6; enforcer `tools/validators/judul.py`).
- [`docs/layout-framework.md`](../../../../docs/layout-framework.md): layout &
  typography rules (LT1–LT9; enforcer `tools/validators/layout_typography.py`).
- [`docs/citation-framework.md`](../../../../docs/citation-framework.md) — citation
  rules (CT1–CT7; CT7 tautan daftar pustaka; enforcer `tools/validators/citation_framework.py`).
- [`docs/bab1-framework.md`](../../../../docs/bab1-framework.md) — BAB I
  introduction framework (A1–A8/B1–B3; enforcer `tools/validators/bab1_framework.py`).
- [`docs/article-framework.md`](../../../../docs/article-framework.md) — article
  structure framework (AR1–AR9; enforcer `tools/validators/article_framework.py`).
- [`docs/ir-article-framework.md`](../../../../docs/ir-article-framework.md) — HI/IR
  bilingual article framework (IA1–IA8; two files/two targets, secondary data only).
- [`docs/argument-framework.md`](../../../../docs/argument-framework.md) — argument
  flow framework (K1–K5; enforcer `tools/validators/argument_flow.py`).
- [`docs/diagram-framework.md`](../../../../docs/diagram-framework.md) — figure/table
  diagram framework (D1–D6; enforcer `tools/validators/figures_tables.py`); includes
  the `.table` generator (`tools/table.py`, `make tables`).
- [`docs/sintesa-diagram-framework.md`](../../../../docs/sintesa-diagram-framework.md)
  — theory-synthesis diagram framework (TS1–TS6; skema empat lapis
  `teori_utama`/`teori_pendukung`/`cabang_bukti`/`lingkup`/`lensa`; enforcer
  `tools/validators/sintesa_diagram.py`).
- [`docs/bagan-diagram-framework.md`](../../../../docs/bagan-diagram-framework.md) —
  node-edge diagram framework (BG1–BG5; enforcer `tools/validators/bagan_diagram.py`).
- [`docs/abstrak-framework.md`](../../../../docs/abstrak-framework.md) — abstract
  framework.
- [`docs/research-gap.md`](../../../../docs/research-gap.md) — research-gap workflow.
- [`docs/fulltext-framework.md`](../../../../docs/fulltext-framework.md) — full-text
  retrieval framework.
- [`docs/subject-framework.md`](../../../../docs/subject-framework.md) — subject
  registry framework.
- [`docs/webgrab-framework.md`](../../../../docs/webgrab-framework.md) — web-grab
  framework (WG1–WG8; curl-first acquisition, headless escalation when chaotic,
  provenance in `docs/web-corpus/manifest.tsv`; enforcer `tools/validators/web_corpus.py`).
- [`docs/source-classification.md`](../../../../docs/source-classification.md) —
  source classification rules.
- [`docs/bab1-corpus-stats.md`](../../../../docs/bab1-corpus-stats.md) — BAB I
  corpus statistics.
- [`docs/sinta-corpus/MANIFEST.md`](../../../../docs/sinta-corpus/MANIFEST.md) — the
  verified journal corpus manifest.
- [`references/skripsi-structure.md`](skripsi-structure.md) — **chapter skeleton
  spec**: the 14-file layout, BAB I–VI sub-sections, and `kamus:f id=` formula
  ids emitted by `scripts/scaffold.py`.

## Make targets

| Target | Purpose |
| --- | --- |
| `make setup` | Prepare the toolchain (pandoc, `python-docx`, `pyyaml`, reference `.docx`). |
| `make skripsi` | Build `out/skripsi.pdf` (pandoc + `figure_table.lua` + xelatex). |
| `make artikel` | Build the Sinta article (`out/artikel-sinta.docx` + `.pdf`). |
| `make artikel-kyt` | Build `artikel-kyt.md` → `out/artikel-kyt.docx` + `.pdf`. |
| `make artikel-arai` | Build `artikel-arai.md` → `out/artikel-arai.docx` + `.pdf`. |
| `make artikel-datacenter` | Build `artikel-datacenter.md` → `out/artikel-datacenter.docx` + `.pdf`. |
| `make artikel-hi` | Build the Indonesian HI/IR article (`content/artikel/artikel-hi.md`) → `out/artikel-hi.docx` + `.pdf`. |
| `make artikel-hi-en` | Build the English HI/IR article (`content/artikel-en/artikel-hi-en.md`) → `out/artikel-hi-en.docx` + `.pdf`. |
| `make check` | `all` + `tools/check.sh` + `tools/check-bahasa.sh` + `gen_kamus.py --check` + `tools/validate.py`. |
| `make check-kyt` | `validate.py article_framework`. |
| `make check-bab1` | `validate.py bab1_framework`. |
| `make check-alur` | `validate.py argument_flow`. |
| `make check-figures` | `validate.py figures_tables sintesa_diagram bagan_diagram`. |
| `make check-layout` | `validate.py layout_typography`. |
| `make check-citations` | `validate.py citation_framework`. |
| `make kamus` | Regenerate dictionary-derived structure and docs from `assets/bahasa/kamus-id.yaml` (`gen_kamus.py --emit --doc`). |
| `make diagrams` | Render diagrams (`tools/diagrams.py render`). |
| `make tables` | Render `.table` YAML fences into native tables (`tools/table.py`). |
| `make corpus` | Download the Sinta journal study corpus (`tools/fetch_corpus.sh`). |
| `make corpus-hi` | Download the IR corpus (`tools/fetch_corpus_ir.sh`). |
| `make corpus-libgen` | Fetch the LibGen corpus (`tools/libgen.py fetch`). |
| `make fulltext` | Verify full text for a source (`tools/fulltext.py verify $(F)`). |
| `make check-drafts` | Language-check `content/drafts/*.md` (`check-bahasa.sh`). |
| `make promote` | Promote a draft into the build (`tools/promote.py --draft $(DRAFT)`). |
| `make sources` | Render the source registry (`search.py render`). |
| `make subjects` | Render the subject registry (`tools/scrape.py render`). |
| `make scrape` | Sweep a site for sources (`tools/scrape.py sweep $(S)`). |
| `make research` | Render research-gap notes (`research_gap.py render`). |
| `make validate` | Run `python3 tools/validate.py` (all validators). |
| `make validate-agent` | Validators + an LLM re-read pass (`validate.py --agent`, needs the `claude` CLI). |
| `make validate-offline` | Validators with network checks skipped (`validate.py --offline`). |
| `make clean` | Remove `out/`. |

## Validator suite

`python3 tools/validate.py [names…] [--offline] [--agent] [--list] [--json]`.
Validators are registered in `tools/validators/` and run in registration order:

| Name | Subject |
| --- | --- |
| `workflow` | `docs/workflow.md` vs `Makefile` (target/path references, step continuity). |
| `journals` | `docs/sinta-corpus/{manifest.tsv,MANIFEST.md,*.pdf}` consistency. |
| `papers` | `content/**/*.md` citations vs `assets/refs.bib`; required fields + brace balance; abstract must not contain citations. |
| `article_framework` | `content/artikel/*.md` (abstrak + kepala bagian). |
| `bab1_framework` | `content/skripsi/10-bab-01-pendahuluan.md` (A1–A8/B1–B3). |
| `argument_flow` | `content/artikel/*.md` + `content/skripsi/1[0-5]-*.md` (K1–K5). |
| `figures_tables` | `content/{artikel,skripsi}/**` + `content/drafts` (caption & penomoran). |
| `sintesa_diagram` | `content/{artikel,skripsi}/**` + `content/drafts` (diagram sintesa teori). |
| `bagan_diagram` | `content/{artikel,skripsi}/**` + `content/drafts` (bagan simpul-sisi). |
| `layout_typography` | `templates/*` + `content/{artikel,skripsi,drafts}` (LT1–LT9). |
| `citation_framework` | `content/{artikel,skripsi,drafts}` + `assets/refs.bib` (CT1–CT7; CT7 tautan daftar pustaka). |
| `evidence_recency` | kebaruan bukti ≤ 5 tahun di dalam `periode` dokumen (`assets/bahasa/kamus-id.yaml` §`recency`). |
| `research_notes` | `docs/kamus-riset-korpus.md` vs the corpus on disk (`docs/sinta-corpus/*`). |
| `ir_journals` | `docs/ir-corpus/{manifest.tsv,MANIFEST.md,*.pdf}` consistency. |
| `ir_research_notes` | `docs/kamus-riset-korpus-hi.md` + `docs/ir-corpus/*`. |
| `libgen_corpus` | `docs/libgen-corpus/{manifest.tsv,MANIFEST.md,*.pdf}` consistency. |
| `doi` | `assets/refs.bib` DOI structure + optional online resolution. |
| `sources` | `sources/registry.json` + `sources/index.md`. |
| `subjects` | `subjects/registry.json` + `subjects/index.md`. |
| `research` | `research/judul.json` + `research/index.md`. |
| `judul` | `research/judul.json` + `templates/artikel-*-meta.yaml` + `content/skripsi/00-halaman-judul.md` (JD1–JD6). |

`tools/validators/papers.py` requires, per entry type: `article` →
`author,title,journal,year`; `book` → `author,title,publisher,year`;
`inproceedings` → `author,title,booktitle,year`; otherwise `author,title,year`.

## Register rules (summary)

Enforced by `tools/check-bahasa.sh` (via `make check`) over body chapters and the
article — see [`docs/bahasa-artikel.md`](../../../../docs/bahasa-artikel.md) for sources.

- **No first/second-person pronouns** in body text (`saya`, `aku`, `kami`,
  `kita`, `anda`, `kamu`, `kalian`). Prefer passive (`dilakukan`, `digunakan`,
  `dikumpulkan`, `dianalisis`); `penulis`/`peneliti` are allowed as impersonal
  self-reference.
- **Baku diction (EYD Edisi V):** `analisa→analisis`, `praktek→praktik`,
  `merubah→mengubah`, `aktifitas→aktivitas`, `hipotesa→hipotesis`,
  `sistim→sistem`, `standard→standar`, `jadual→jadwal`, `obyek→objek`,
  `metoda→metode`.
- **No generic AI filler phrases** (see `frasa_ai_generik` in the dictionary).
- **Exemption:** `content/skripsi/03-surat-pernyataan.md` is a personal legal
  declaration and legitimately uses first person.

## Citations

- Cite in Markdown with **`[@key]`**, where `key` is a BibTeX key in
  `assets/refs.bib`.
- The article's reference list is rendered by the `::: {#refs} :::` block at the
  end of `content/artikel/artikel-sinta.md`.
- Add references with [`scripts/scholar.py`](../scripts/scholar.py) (Google
  Scholar → Crossref → OpenAlex), which appends de-duplicated BibTeX.
- **Never fabricate a citation or DOI.** Verify with `python3 tools/validate.py
  papers doi`.

## Conventions

- **Judul** — a title must be directive, scope-bounded, and state a problem or
  contribution; language must be consistently ID or EN (enforced by
  `tools/validators/judul.py`, JD1–JD6).
- **Sinta layout** — the article build centers the front matter/abstract and
  renders ALL-CAPS headings for the six canonical sections, with a justified body
  and italic foreign terms, via `tools/pandoc_filters/sinta_layout.lua`
  ([`docs/layout-framework.md`](../../../../docs/layout-framework.md) LT2, LT6).
- **Bilingual blocks** — mark a second-language block as `::: {lang=en} … :::`
  (the article `ABSTRACT` carries `lang=en`); when `bahasa.utama` in
  `assets/bahasa/kamus-id.yaml` differs, `tools/pandoc_filters/bilingual.lua`
  italicizes it (LT7).
- **Dash ban**: in prose never use the em dash `—` or spaced hyphen ` - `; the
  en dash `–` is only for numeric ranges, and automatic hyphenation is
  suppressed via `\hyphenpenalty`/`\exhyphenpenalty` in `templates/*-preamble.tex`
  (LT8; `assets/bahasa/kamus-id.yaml` §`tanda_pisah`).
- **Bilingual technical terms**: gloss each `istilah_teknis` term with its
  English equivalent in parentheses at first prose occurrence
  (`istilah (english gloss)`; italic gloss when the gloss is a registered
  `istilah_asing` term) (LT9; `assets/bahasa/kamus-id.yaml` §`istilah_teknis`).
- **Generated tables** — write a `.table` YAML fence and run `make tables`
  (`tools/table.py` + `tools/pandoc_filters/table.lua`); output is a **native**
  table, not an image (`docs/diagram-framework.md`, D6: `kolom` ≥ 1, `baris` ≥ 2).
- **ALL-CAPS BAB headings** in Markdown, e.g. `# PENDAHULUAN`.
- Chapter front matter uses raw-LaTeX ` ```{=latex} ` blocks; body chapters
  (10–15) are plain Markdown.
- Formula-bearing sections carry two comments on the opening line:
  `<!-- TODO: … -->` (fill-in) and `<!-- kamus:f id=<formula-id> -->` (binds to
  `formula:` in `assets/bahasa/kamus-id.yaml`).
