# Conversion: Skripsi → Sinta Article

How to convert a completed skripsi into a journal article targeting a Sinta-indexed journal.

## Mapping table

| Skripsi section | Article section | Action |
|-----------------|-----------------|--------|
| BAB I | Pendahuluan | Condense into the article introduction |
| BAB II | folded into Pendahuluan + Pembahasan | Merge theory into intro/discussion; drop textbook padding |
| BAB III | Metode | Compress to the actual method used |
| BAB IV + V | Hasil dan Pembahasan | Merge design + results into one results-and-discussion section |
| BAB VI | Simpulan dan Saran | Rewrite as a conclusion answering the objective |
| Lampiran | dropped | Omit from the article |
| Daftar Pustaka | filtered to only what the article cites | Remove uncited references |

## Rewrite rules

- Compress the **title** (drop school/class/year).
- Write the **abstract last**.
- Choose **3–5 specific keywords**.
- **Introduction** in 4 beats: context → prior work → gap → objective.
- **Methods** stripped of textbook definitions — describe only what you did.
- **Results** limited to what answers the objective.
- **Discussion** that interprets: meaning / why / comparison vs prior work / implications.
- **Conclusion** answering the objective.
- **Filtered reference list** — keep only cited works.

## Ragam Bahasa Indonesia

The article must use the authentic Indonesian academic register. Full sourced
rules: [docs/bahasa-artikel.md](bahasa-artikel.md).

**Heading set** (article sections, in order):

> `Pendahuluan` / `Metode Penelitian` / `Hasil dan Pembahasan` /
> `Simpulan dan Saran` / `Ucapan Terima Kasih` / `Daftar Pustaka`

**Three core formulas** (verbatim):

- `Penelitian ini bertujuan untuk …`
- `Hasil penelitian menunjukkan bahwa …`
- `Berdasarkan hasil penelitian dan pembahasan, dapat disimpulkan bahwa …`

**No-pronoun rule.** Write impersonally: no `saya`, `aku`, `kami`, `kita`,
`anda`, `kamu`, `kalian`; prefer passive (`dilakukan`, `digunakan`,
`dikumpulkan`, `dianalisis`); `penulis`/`peneliti` are allowed as impersonal
self-reference.

**Baku-pair table** (EYD Edisi V): `analisa→analisis`, `praktek→praktik`,
`merubah→mengubah`, `aktifitas→aktivitas`, `hipotesa→hipotesis`,
`sistim→sistem`, `standard→standar`, `jadual→jadwal`, `obyek→objek`,
`metoda→metode`.

## Struktur dan Kamus

Struktur, rangkai argumen, dan leksikon artikel diturunkan dari kamus:
[docs/kamus-bahasa-artikel.md](kamus-bahasa-artikel.md).

**Kepala bagian** (urutan wajib, id → judul):

1. `pendahuluan` — Pendahuluan
2. `metode` — Metode Penelitian
3. `hasil` — Hasil dan Pembahasan
4. `simpulan` — Simpulan dan Saran
5. `ucapan` — Ucapan Terima Kasih
6. `pustaka` — Daftar Pustaka

`make kamus` meregenerasi kerangka artikel dari kamus
(`assets/bahasa/kamus-id.yaml`).

## Recommended work order

1. Target journal
2. One-sentence main finding
3. Select supporting tables
4. Results
5. Methods
6. Discussion
7. Introduction
8. Conclusion
9. Abstract
