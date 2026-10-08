# Contributing & Development Guide

This repository is a **private** academic workspace. This guide documents how to
work in it safely and how to keep `make check` green.

## Prerequisites

Run the one-shot setup once:

```bash
make setup
```

See [README.md](README.md) for the full toolchain list and the Pandoc fallback.

## The golden rule: `make check`

`make check` is the gate. It builds the skripsi PDF and the Sinta article, then
runs every linter and validator. **Do not commit if it fails.** A passing run
ends with:

```
SEMUA PEMERIKSAAN LULUS.
KAMUS: SELARAS.
RAGAM BAHASA: LULUS.
VALIDASI: LULUS.
```

Fast iteration without rebuilding PDFs:

```bash
bash tools/check-bahasa.sh content/skripsi/11-bab-02-tinjauan-pustaka.md
python3 tools/validate.py papers
python3 tools/gen_kamus.py --check
```

## Editing content

1. Write chapters in `content/skripsi/*.md` (concatenated in filename order) or
   the article in `content/artikel/artikel-sinta.md`.
2. Keep BAB headings in **ALL CAPS** (e.g. `# PENDAHULUAN`).
3. Follow the Indonesian register in
   [docs/bahasa-artikel.md](docs/bahasa-artikel.md) and the dictionary in
   `assets/bahasa/kamus-id.yaml`. If the dictionary changes, run `make kamus`.
4. Cite only keys that exist in `assets/refs.bib`, and never leave a bib entry
   uncited — the `papers` validator fails in both directions.

### Work-in-progress chapters

Put unfinished chapters in `content/drafts/`. That folder is **excluded** from
`make check`. Lint drafts separately with `make check-drafts`, then promote a
finished draft:

```bash
make promote DRAFT=content/drafts/11-bab-02-tinjauan-pustaka.md
```

Draft filenames **must** match the target chapter filename.

## The Indonesian register linter

`tools/check-bahasa.sh` enforces `ragam bahasa ilmiah`. In tracked prose it
rejects:

- first/second-person pronouns: `saya`, `aku`, `kami`, `kita`, `anda`, `kamu`,
  `kalian`;
- non-standard vocabulary (EYD Edisi V), e.g. `analisa`, `praktek`, `dimana`,
  `dikarenakan`, `mempengaruhi`, `kerjasama`;
- generic AI filler phrases (see `tools/gen_kamus.py --pattern frasa_ai_generik`).

If the linter rejects a word, replace it — the linter is the source of truth.

## Dictionary-driven structure

Structural lines in the chapters carry anchors such as
`<!-- kamus:f id=… -->`. `tools/gen_kamus.py --check` requires these lines to
stay byte-for-byte identical, and `make kamus` regenerates the derived documents
from `assets/bahasa/kamus-id.yaml`. Do not hand-edit generated documents.

## Research corpora

The corpus PDFs under `docs/*-corpus/` are third-party copyrighted and are
**git-ignored**. Only `MANIFEST.md` and `manifest.tsv` are tracked. Re-fetch
locally before validating:

```bash
make corpus        # Sinta journal study corpus
make corpus-hi     # Hubungan Internasional corpus
make corpus-libgen # LibGen reference corpus
```

## Commit conventions

- Keep commits focused: one logical change per commit.
- Use an imperative subject line; add a short body when the *why* is not obvious.
- Never commit build output (`out/`), `__pycache__/`, `.promote-backups/`, or
  corpus PDFs — all are git-ignored.
- Do not commit secrets, personal data, or third-party copyrighted material.

## Adding a validator

Validators live in `tools/validators/`. Register one with the decorator:

```python
@register("my_check", "path/glob/*")
def run(ctx: Context) -> list[Finding]:
    ...
```

Then ensure `tools/validate.py` discovers it. `make validate` runs the suite;
`make validate-agent` adds the optional LLM re-read pass.

## Repository hygiene

This repo is private and contains unpublished academic work. Do not publish,
mirror, or redistribute its contents or the research corpora.
