# Kerangka Ketersediaan Judul & Celah Penelitian (Research Gap)

Kerangka ini memeriksa apakah sebuah **judul** penelitian masih tersedia atau
sudah terpakai, lalu membantu merumuskan **celah penelitian** (*research gap*)
beserta **kebaruan**-nya. Seluruh pemeriksaan dijalankan oleh skrip
`.claude/skills/nykripsi/scripts/research_gap.py` (hanya pustaka standar Python 3,
tanpa kunci API).

## Tujuan

Kerangka ini bertujuan untuk:

1. mencegah pengajuan **judul yang sudah ada atau terlalu mirip** dengan
   penelitian terdahulu;
2. mendokumentasikan bukti pemeriksaan judul secara **terlacak** pada
   `research/judul.json`;
3. menyediakan **papan kerja celah penelitian** (`research/gap-<slug>.md`) yang
   memandu perumusan kebaruan;
4. menyediakan indeks terpadu `research/index.md` yang diregenerasi dengan
   `make research`.

## Aturan ketersediaan judul

Setiap judul memperoleh satu **verdict**:

| Kondisi | Verdict |
| --- | --- |
| Kecocokan judul **persis** (setelah normalisasi) dengan penelitian terdahulu | `duplicate` |
| Kemiripan **token-Jaccard ≥ 0,80** | `too-similar` |
| Selain kedua kondisi di atas | `available` |

Judul yang **dipilih** (selected) dan berverdict `duplicate` atau `too-similar`
**DIBLOKIR** oleh validator `research` yang tertanam pada `make check`. Ambang
kemiripan dapat diubah dengan bendera `--threshold F` (misalnya `--threshold 0.85`).

Selain ketersediaan (duplikat/terlalu mirip), **mutu** judul ditegakkan oleh
`tools/validators/judul.py` (JD1–JD6); lihat `docs/judul-framework.md`.

## Dua jalur pemeriksaan

Pemeriksaan judul menempuh **dua jalur** yang saling melengkapi:

1. **Jalur skrip tanpa kunci (keyless).** Subperintah `check` menelusuri
   **Crossref + OpenAlex + Google Scholar (via `scholar.py`) + registry lokal**
   dan menghitung verdict secara otomatis.
2. **Jalur peramban (browser) yang WAJIB.** Setelah pemeriksaan skrip, dilakukan
   lintas-periksa manual melalui **Google Scholar** dan **pencarian web biasa**
   (mesin pencari umum). Temuan dari jalur ini dimasukkan dengan subperintah
   `browser-record` agar verdict dihitung ulang.

Jalur peramban bersifat **wajib** secara prosedural, tetapi **tidak** digerbangi
oleh build (`make check`); temuan peramban diserap melalui `browser-record`.

> **Aturan provenans:** jangan pernah mengarang kecocokan. Setiap kecocokan harus
> berasal dari **penelusuran langsung** (skrip `check`) atau dari **hasil peramban
> agen** yang dimasukkan via `browser-record`. Bila tidak ada temuan, nyatakan
> demikian — jangan mengisi celah secara manual.

## Metode menemukan celah

Perumusan celah penelitian menempuh empat langkah:

**(a) Kumpulkan penelitian terdahulu.** Telusuri dan catat karya-karya yang
relevan (judul, URL/DOI, tahun) ke dalam registry.

**(b) Analisis kelemahan (weakness).** Untuk setiap karya terdahulu, telaah
kelemahannya pada **dimensi tetap** berikut:

- `ruang lingkup`
- `metode`
- `data`
- `populasi/konteks`
- `rentang waktu`
- `variabel`
- `teori`
- `tingkat analisis`

**(c) Tentukan sudut pandang berbeda (angle).** Pilih **sekurang-kurangnya dua
dimensi** yang sengaja **dibedakan** oleh penelitian baru dari penelitian
terdahulu.

**(d) Rumuskan celah + kebaruan.** Nyatakan celah penelitian (*gap*) dan
kebaruan (*novelty*) yang menjadi kontribusi penelitian baru.

## Prosedur

```bash
R=.claude/skills/nykripsi/scripts/research_gap.py

# 1. Periksa ketersediaan judul (Crossref + OpenAlex + Scholar + registry lokal).
python3 $R check "Judul Penelitian" --limit 10 --threshold 0.80
python3 $R check "Judul Penelitian" --json --no-save

# 2. Lintas-periksa peramban (WAJIB): Google Scholar + pencarian web biasa,
#    lalu masukkan temuannya.
python3 $R browser-record "Judul Penelitian" \
  --title "Karya yang ditemukan" --url "https://..." \
  --doi "10.xxxx/yyyy" --year 2024 --backend scholar

# 3. Tulis kerangka laporan celah (research/gap-<slug>.md).
python3 $R gap "Judul Penelitian" \
  --prior "Judul Terdahulu|https://...|kelemahan|angle"

# 4. Regenerasi indeks research/index.md.
python3 $R render          # atau: make research
```

Bendera umum: `--registry PATH` (lokasi `research/judul.json`), `--threshold F`
(ambang kemiripan), `--json`, `--no-save` (jangan simpan record), `--email ADDR`
(pool sopan Crossref/OpenAlex). `gap` juga menerima `--out PATH` untuk lokasi
berkas laporan, dan `render` menerima `--index PATH` untuk lokasi indeks.

## Rujukan

- `research/README.md` — penjelasan direktori riset, skema record, dan alur
  validasi.
