# Workflow

Numbered walkthrough for building the skripsi PDF and the Sinta article draft.

1. Run `make setup` **once** to prepare the toolchain.
2. Write chapters in `content/skripsi/*.md`.
3. Follow [docs/bahasa-artikel.md](bahasa-artikel.md) for the Indonesian
   register; `make check` enforces it. Struktur dan diksi mengikuti `assets/bahasa/kamus-id.yaml` → `docs/kamus-bahasa-artikel.md`; jalankan `make kamus` bila kamus berubah.
4. Run `make skripsi` → produces `out/skripsi.pdf`.
5. Run `make artikel` → produces the Sinta article draft.
6. Download the target journal's **official template** from its OJS **Author Guidelines**
   and paste the article text into it before submission.
7. Run `tools/check.sh`.
8. Follow the pre-submit checklist (see [sinta-reference.md](sinta-reference.md)).
9. Run `python3 tools/validate.py` (atau `make validate`) — verifikator alur kerja + validator korpus jurnal, sitasi artikel, catatan riset, DOI, dan sumber; `make check` menegakkannya.
10. Draft material lives in `content/drafts/`; run `make check-drafts` to lint the register, then promote a finished draft with `make promote` (`DRAFT=<file>`).
11. Gather sources with `.claude/skills/nykripsi/scripts/search.py` (news, article, book, interview, dataset, publicdata, company, pdf, web, forum, video) and refresh the generated index with `make sources`.
12. Classify every gathered source as **primary** (kebenaran subjek / subject truth — a direct interview of the company / main actor / main subject) or **secondary** (kebenaran pendukung / supporting truth — the subject's press release, plus news, articles, and other mediated material). Kelas bawaan ditentukan oleh `type` (`interview` -> `primary`, selain itu `secondary`), dapat ditimpa per record dengan `--class {primary,secondary}`, dan dihitung ulang dengan `python3 .claude/skills/nykripsi/scripts/search.py classify`. Rincian kerangka ada di `docs/source-classification.md`.
13. Periksa ketersediaan judul dengan `make research` + `python3 .claude/skills/nykripsi/scripts/research_gap.py check`, lengkapi lintas-periksa peramban atas Google Scholar dan pencarian web biasa (hasilnya dimasukkan dengan `python3 .claude/skills/nykripsi/scripts/research_gap.py browser-record`), lalu tulis laporan celah dengan `python3 .claude/skills/nykripsi/scripts/research_gap.py gap`. Rincian kerangka ada di `docs/research-gap.md`.
14. Unduh korpus jurnal Hubungan Internasional dengan `make corpus-hi` (skrip `tools/fetch_corpus_ir.sh`, hasil di `docs/ir-corpus/`). Setelah korpus diperbarui, jalankan riset korpus HI dan bangkitkan ulang kamus dengan `make kamus`; rincian kamus riset ada di `docs/kamus-riset-korpus-hi.md`.

> **Important:** the generated `.docx` is a **content-and-style draft**. The target
> journal's **own template always wins**.
