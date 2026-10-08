# Workspace Map — Nykripsi v2

Orientation for the `nykripsi` skill. Where the chapters, citations, templates,
and dictionaries live, how the build and validators work, and the rules that
apply to every edit. This is a map, not a copy — follow the linked documents for
the authoritative detail.

## Layout

| Path | What it holds |
| --- | --- |
| `content/skripsi/*.md` | Skripsi sources. Front matter (00–06), body chapters (10–15), bibliography (90). Pandoc concatenates them in **filename order**. |
| `content/artikel/artikel-sinta.md` | The Sinta journal article source. |
| `assets/refs.bib` | The BibTeX database. Every `[@key]` in `content/**/*.md` must resolve to an entry here, and every entry must be cited. |
| `assets/bahasa/kamus-id.yaml` | Machine dictionary: `kepala_bagian`, `formula`, `rangkai_argumen`, `kosakata_baku`, `frasa_ai_generik`, `leksikon_verba`, `konektor`, `kutipan`. |
| `assets/csl/apa.csl` | CSL style for `--citeproc` (repo default APA 7). |
| `assets/figures/` | Figures referenced from chapters (`assets/figures/contoh.png`). |
| `templates/skripsi-preamble.tex` | LaTeX preamble for the skripsi PDF build. |
| `templates/artikel-preamble.tex`, `templates/artikel-meta.yaml`, `templates/journal-reference.docx` | Article build inputs (PDF preamble, metadata, reference `.docx`). |
| `out/` | Build artifacts (`skripsi.pdf`, `artikel-sinta.docx`, `artikel-sinta.pdf`). Git-ignored. |

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
- [`docs/sinta-corpus/MANIFEST.md`](../../../../docs/sinta-corpus/MANIFEST.md) — the
  verified journal corpus manifest.
- [`references/skripsi-structure.md`](skripsi-structure.md) — **chapter skeleton
  spec**: the 14-file layout, BAB I–VI sub-sections, and `kamus:f id=` formula
  ids emitted by `scripts/scaffold.py`.

## Make targets

| Target | Purpose |
| --- | --- |
| `make setup` | Prepare the toolchain (run once). |
| `make skripsi` | Build `out/skripsi.pdf`. |
| `make artikel` | Build the Sinta article (`.docx` + `.pdf`). |
| `make check` | Build + `tools/check.sh` + `tools/check-bahasa.sh` + `gen_kamus.py --check` + `tools/validate.py`. |
| `make kamus` | Regenerate dictionary-derived structure and docs from `assets/bahasa/kamus-id.yaml`. |
| `make corpus` | Download the Sinta journal study corpus. |
| `make validate` | Run `python3 tools/validate.py` (all validators). |
| `make validate-agent` | Validators + an LLM re-read pass (needs the `claude` CLI). |
| `make validate-offline` | Validators with network checks skipped. |
| `make clean` | Remove `out/`. |

## Validator suite

`python3 tools/validate.py [names…] [--offline] [--agent] [--list] [--json]`.
Validators are registered in `tools/validators/` and run in registration order:

| Name | Subject |
| --- | --- |
| `workflow` | `docs/workflow.md` vs `Makefile` (target/path references, step continuity). |
| `journals` | `docs/sinta-corpus/{manifest.tsv,MANIFEST.md,*.pdf}` consistency. |
| `papers` | `content/**/*.md` citations vs `assets/refs.bib`; required fields + brace balance; abstract must not contain citations. |
| `research_notes` | `docs/kamus-riset-korpus.md` vs the corpus on disk. |
| `doi` | `assets/refs.bib` DOI structure + optional online resolution. |

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

- **ALL-CAPS BAB headings** in Markdown, e.g. `# PENDAHULUAN`.
- Chapter front matter uses raw-LaTeX ` ```{=latex} ` blocks; body chapters
  (10–15) are plain Markdown.
- Formula-bearing sections carry two comments on the opening line:
  `<!-- TODO: … -->` (fill-in) and `<!-- kamus:f id=<formula-id> -->` (binds to
  `formula:` in `assets/bahasa/kamus-id.yaml`).
