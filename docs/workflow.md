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
15. Wajibkan teks penuh: tempuh tangga akuisisi pada `docs/fulltext-framework.md` sebelum menandai sebuah karya tidak dapat diakses; jalankan `python3 tools/fulltext.py resolve|fetch|verify` (dan `make fulltext F=<file.pdf>` untuk memverifikasi berkas) lalu catat `access_level`/`fulltext_*` di `sources/registry.json`.
16. Sapu seluruh materi sekunder tentang subjek: deklarasikan subjek dengan `python3 tools/scrape.py add "<nama>"`, jalankan sapuan kanal dengan `python3 tools/scrape.py sweep "<nama>"` (atau `make scrape S="<nama>"`), lalu regenerasi indeks dengan `make subjects`; rincian kerangka ada di `docs/subject-framework.md`.
17. Hasilkan diagram/tabel: tulis blok ` ```{.mermaid #fig-<slug>} `, ` ```{.chart #fig-<slug>} `, atau ` ```{.tikz #fig-<slug>} ` lalu caption `Gambar <bab>.<n> <Judul>` di bawahnya (tabel: caption `Tabel <bab>.<n> <Judul>` di atas tabel), jalankan `make diagrams`, lalu `make check-figures`; rincian kerangka ada di `docs/diagram-framework.md`.
18. Susun diagram sintesa teori: tulis blok ` ```{.sintesa #fig-<slug>} ` berisi YAML (`teori` ≥ 2 dengan `nama`/`peran`, `lensa.nama` + `lensa.gabungan` ≥ 2, `tahap` ≥ 2, `lintas_tahap` opsional), tulis caption `Gambar <bab>.<n> <Judul>` di bawahnya, sebut nama lensa di prosa, lalu jalankan `make diagrams` dan `make check-figures`; rincian kerangka ada di `docs/sintesa-diagram-framework.md`.

> **Important:** the generated `.docx` is a **content-and-style draft**. The target
> journal's **own template always wins**.
