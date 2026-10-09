# Kerangka Diagram, Tabel & Fungsi Keluaran — Drafting Jurnal, Riset, dan Paper (Sinta, HI/IR, Skripsi, Proposal)

Kerangka ini menetapkan cara menghasilkan **gambar (diagram)**, **tabel**, dan
**fungsi keluaran** — *caption*, penomoran, `DAFTAR GAMBAR`/`DAFTAR TABEL`, serta
*cross-reference* — dari **sumber Markdown**. Prinsipnya: setiap gambar dan tabel
harus **dapat direproduksi dari teks**, bukan ditempel sebagai berkas mati.
Setiap klaim dalam dokumen ini bersumber pada **berkas repositori ini**
(URL/berkas repo) atau **literatur/dokumen eksternal** yang terekam sesi ini —
tidak ada aturan tanpa sumber.

Kerangka ini **melengkapi** kerangka yang sudah ada dan tidak menggantikannya.
`docs/skripsi-pedoman.md` menetapkan tata letak skripsi (caption di bawah gambar,
di atas tabel; penomoran `Gambar <bab>.<n>` / `Tabel <bab>.<n>`);
`docs/sinta-reference.md` menetapkan anatomi artikel Sinta (nomor dan judul
semua gambar/tabel); `docs/conversion-skripsi-to-article.md` mengatur konversi
skripsi menjadi artikel; dan `docs/argument-framework.md` mengatur alur argumen
serta kohesi paragraf. Kerangka diagram **tidak menggantikan** salah satu dari
keempatnya: ia hanya menetapkan **bagaimana** gambar, tabel, dan fungsi
keluarannya diproduksi dan diperiksa mesin dari sumber Markdown.

---

## 1. Definisi dan Fungsi

**Definisi.** *Sumber diagram* adalah **blok kode berpagar (*fenced code block*)
Markdown** yang diberi kelas `mermaid`, `chart`, atau `tikz` dan dirender menjadi
**berkas gambar**. *Aset gambar* adalah berkas hasil render yang disimpan di
`assets/figures/<slug>.png`. *Caption* adalah **judul bernomor** yang diletakkan
**di atas tabel** dan **di bawah gambar**. *Cross-reference* adalah **rujukan
dalam teks** berbentuk `pada Tabel <n>` atau `pada Gambar <n>` yang menunjuk ke
caption tersebut.

**Fungsi kerangka.** Pertama, **menjadikan diagram/tabel dapat direproduksi dari
teks**: gambar dibangun ulang dari blok Markdown, bukan disisipkan sebagai berkas
biner tanpa sumber. Kedua, **menegakkan penomoran** `Gambar <bab>.<n>` dan
`Tabel <bab>.<n>` secara berurutan. Ketiga, **mengisi `DAFTAR GAMBAR`/`DAFTAR
TABEL`** dari caption yang benar-benar ada. Sumber: `docs/skripsi-pedoman.md`
(§Figures, tables, equations & code — caption di bawah gambar, di atas tabel;
penomoran `Gambar <bab>.<n>` / `Tabel <bab>.<n>`); Pandoc Lua filters
<https://pandoc.org/lua-filters.html>.

---

## 2. Lanskap Sumber Diagram dan Keluaran

Diagram dan tabel dalam repositori ini berasal dari beberapa jenis sumber. Tabel
2.1 memetakan jenis sumber beserta sintaks, perender, keluaran, dan
ketergantungannya; Tabel 2.2 merangkum fungsi keluaran (*caption*, penomoran,
daftar, rujukan).

### Tabel 2.1 — Jenis sumber diagram

|Jenis|Sintaks Markdown|Perender|Keluaran|Ketergantungan|
|---|---|---|---|---|
|Diagram alir/graf|fence `mermaid` ber-id `#fig-slug`|`npx -y @mermaid-js/mermaid-cli`|`assets/figures/fig-slug.png`|Node + unduhan sekali (daring)|
|Grafik data|fence `chart` ber-id `#fig-slug`|`tools/diagrams.py` (matplotlib)|`assets/figures/fig-slug.png`|`matplotlib` (luring)|
|Gambar vektor|fence `tikz` ber-id `#fig-slug`|`tools/diagrams.py` (XeLaTeX `standalone`)|`assets/figures/fig-slug.png`|`xelatex` + `pdftoppm` (luring)|
| Diagram sintesa teori | fence `sintesa` ber-id `#fig-slug` | `tools/diagrams.py` (matplotlib) | `assets/figures/fig-slug.png` | `matplotlib` (luring) |
|Tabel|pipe table Markdown|Pandoc|caption + `\listoftables`|—|

> **Bentuk fence lengkap (contoh):** fence dibuka dengan tiga *backtick* lalu
> ``{.mermaid #fig-slug}`` pada baris yang sama, diikuti badan diagram, lalu
> ditutup tiga *backtick*. Pola yang sama berlaku untuk ``{.chart #fig-slug}``
> dan ``{.tikz #fig-slug}``.

### Tabel 2.2 — Keluaran dan daftar

|Fungsi keluaran|Aturan|Sumber|
|---|---|---|
|Caption tabel|Di **atas** tabel|`docs/skripsi-pedoman.md`|
|Caption gambar|Di **bawah** gambar|`docs/skripsi-pedoman.md`|
|Penomoran|`<bab>.<n>` (skripsi) / `<n>` (artikel)|`docs/skripsi-pedoman.md`|
|`DAFTAR GAMBAR` + `DAFTAR TABEL`|Diisi dari caption nyata (`\listoffigures`, `\listoftables`)|`content/skripsi/06-daftar-isi.md`|
|Cross-reference|Rujukan eksplisit `pada Gambar <n>` / `pada Tabel <n>`|`docs/skripsi-pedoman.md`|

Sumber: `docs/skripsi-pedoman.md`; `content/skripsi/06-daftar-isi.md`.

---

## 3. Aturan Absolut (D1–D6)

Keenam aturan berikut bersifat **absolut**: naskah yang melanggarnya belum layak
disebut memiliki diagram dan tabel yang reprodusibel. Setiap butir menyebut
definisi, penegak, dan sumbernya.

1. **D1 — Caption wajib.** Setiap tabel **wajib** didahului paragraf caption
   `Tabel <n> <Judul>`; setiap sumber diagram **wajib** diikuti paragraf caption
   `Gambar <n> <Judul>`. Penegak: `tools/validators/figures_tables.py`.
2. **D2 — Penomoran berurutan.** Pada berkas `1X-bab-0Y-*.md`, tabel/gambar
   bernomor `Tabel <bab>.<n>` / `Gambar <bab>.<n>` dengan `bab = X-9` dan `n`
   berurutan dari **1** per berkas **tanpa lompatan/duplikat**. Pada
   `content/artikel/*.md` bernomor `Tabel <n>` / `Gambar <n>`. Penegak: idem.
3. **D3 — Caption ringkas.** Judul caption **tanpa titik akhir** dan **≤ 15 kata**
   (peringatan bila lebih). Penegak: idem.
4. **D4 — Blok diagram berlabel.** Setiap blok `mermaid`/`chart`/`tikz`
   **wajib** memiliki `#fig-<slug>` unik; aset `assets/figures/fig-<slug>.png`
   diharapkan ada setelah `make diagrams` (peringatan bila belum dirender).
   Penegak: idem.
5. **D5 — Cross-reference sah.** Setiap rujukan dalam teks `Tabel <n>` /
   `Gambar <n>` di prosa **wajib** menunjuk ke nomor caption yang ada di berkas
   yang sama. Penegak: idem.
6. **D6 — Tabel berheader.** Setiap pipe table **wajib** memiliki baris header
   dan **≥ 2 baris data**. Penegak: idem.

---

## 4. Frame (Alur Drafting Diagram/Tabel)

Menulis diagram dan tabel yang reprodusibel mengikuti prosedur enam langkah:

1. **Tulis blok sumber diagram** dengan id `#fig-<slug>`.
2. **Tulis caption** `Gambar <n> <Judul>` **di bawah** blok.
3. Untuk tabel, **tulis caption** `Tabel <n> <Judul>` **di atas** tabel.
4. **Jalankan `make diagrams`** untuk merender aset.
5. **Rujuk lewat teks** `pada Gambar <n>` / `pada Tabel <n>`.
6. **Jalankan `make check-figures`** lalu `make skripsi`/`make artikel`.

Sumber: `docs/skripsi-pedoman.md`.

---

## 5. Model Komponen (Anatomi Caption & Aset)

Sebuah gambar/tabel yang sehat tersusun dari lima komponen fungsional:

- **Blok sumber** — kode berkelas (`mermaid`/`chart`/`tikz`) dengan id
  `#fig-<slug>`.
- **Aset gambar** — berkas hasil render di `assets/figures/`.
- **Caption** — paragraf `Gambar <n> <Judul>` atau `Tabel <n> <Judul>`.
- **Filter** — `tools/pandoc_filters/figure_table.lua` yang mengubah caption
  menjadi caption Pandoc sungguhan dan menggantikan blok diagram dengan gambar.
- **Renderer** — `tools/diagrams.py` yang merender blok menjadi aset PNG.

Sumber: `docs/skripsi-pedoman.md`; Pandoc Lua filters
<https://pandoc.org/lua-filters.html>.

---

## 6. Pita dan Ambang

### (a) Ambang yang diperiksa mesin

|Parameter|Nilai|Tingkat|
|---|---|---|
|Caption tanpa titik akhir|**0** titik|fail (D3)|
|Panjang caption|**≤ 15** kata|warn (D3)|
|Nomor `n` berurutan dari|**1**|fail (D2)|
|Baris data minimum tabel|**≥ 2**|fail (D6)|
|Cross-reference harus resolve|**ada**|fail (D5)|

Ambang pada (a) dikalibrasi pada **8 berkas** repositori ini (**2 tabel, 0
gambar**) dan **lulus**. Bila kelak muncul berkas sah yang melampaui ambang,
konstanta di `tools/validators/figures_tables.py` **dan** tabel (a) di dokumen
ini harus diubah **bersamaan** agar tetap selaras.

---

## 7. Matriks Kepatuhan per-Tingkat

|Aturan|Sinta 1–2|Sinta 3–6|Scopus|Skripsi HI|Proposal|
|---|---|---|---|---|---|
|D1 — Caption wajib|wajib|wajib|unverified — confirm first|wajib|wajib|
|D2 — Penomoran berurutan|wajib|wajib|unverified — confirm first|wajib|wajib|
|D3 — Caption ringkas|wajib|wajib|unverified — confirm first|wajib|wajib|
|D4 — Blok diagram berlabel|wajib|wajib|unverified — confirm first|wajib|wajib|
|D5 — Cross-reference sah|wajib|wajib|unverified — confirm first|wajib|wajib|
|D6 — Tabel berheader|wajib|wajib|unverified — confirm first|wajib|wajib|

D1–D6 **wajib** untuk semua kolom: diagram dan tabel yang reprodusibel adalah
syarat kelayakan dasar, bukan pilihan gaya. Kolom **Scopus** ditandai
**`unverified — confirm first`**: status indeksasi venue internasional tidak
dapat diverifikasi dari korpus lokal, konsisten dengan sikap
`docs/subject-framework.md` §8 yang menandai klaim tak terverifikasi secara
eksplisit.

---

## 8. Daftar Periksa Do/Don't

|Lakukan (Do)|Hindari (Don't)|
|---|---|
|Caption di atas tabel, di bawah gambar|Caption menyatu dengan paragraf prosa|
|Rujuk lewat teks "pada Tabel 2.1"|Menyebut nomor tanpa caption|
|Blok diagram ber-#fig-slug|Menyisipkan gambar lewat LaTeX mentah|
|Jalankan make diagrams|Menaruh PNG tanpa sumber Markdown|

---

## 9. Rubrik Penilaian

Nilai **0–2** untuk setiap komponen D1–D6; skor maksimum **12**.

|Komponen|0|1|2|
|---|---|---|---|
|D1 — Caption wajib|Tanpa caption|Sebagian tanpa caption|Setiap tabel/gambar bercaption|
|D2 — Penomoran berurutan|Lompatan/duplikat|Sebagian tidak berurutan|Berurutan dari 1|
|D3 — Caption ringkas|Titik akhir / > 15 kata|Titik akhir atau > 15 kata|Tanpa titik akhir, ≤ 15 kata|
|D4 — Blok diagram berlabel|Tanpa `#fig-<slug>`|Sebagian berlabel|Semua blok berlabel unik|
|D5 — Cross-reference sah|Rujukan menggantung|Sebagian menggantung|Semua rujukan resolve|
|D6 — Tabel berheader|Tanpa header|Header < 2 baris data|Header + ≥ 2 baris data|

**Tafsiran:** **12** = patuh penuh; **9–11** = revisi ringan; **5–8** = perlu
perbaikan; **≤ 4** = belum layak.

---

## 10. Sumber

### 10.1 Berkas repositori

- `docs/skripsi-pedoman.md` — caption di bawah gambar, di atas tabel; penomoran.
- `docs/sinta-reference.md` — anatomi artikel Sinta (nomor dan judul gambar/tabel).
- `docs/conversion-skripsi-to-article.md` — konversi skripsi menjadi artikel.
- `docs/argument-framework.md` — alur argumen & kohesi paragraf.
- `content/skripsi/06-daftar-isi.md` — `DAFTAR GAMBAR`/`DAFTAR TABEL`.
- `templates/skripsi-preamble.tex` — preamble skripsi.
- `templates/artikel-preamble.tex` — preamble artikel.
- `assets/figures/` — direktori aset gambar.
- `tools/validators/figures_tables.py` — penegak D1–D6.
- `tools/diagrams.py` — perender diagram.
- `tools/pandoc_filters/figure_table.lua` — filter caption/gambar.
- `docs/sintesa-diagram-framework.md` — kerangka diagram sintesa teori (TS1–TS6).

### 10.2 Literatur/dokumen eksternal

- Pandoc Lua filters <https://pandoc.org/lua-filters.html>
- Pandoc Manual <https://pandoc.org/MANUAL.html>
- Mermaid <https://mermaid.js.org/intro/>
- mermaid-cli <https://github.com/mermaid-js/mermaid-cli>
- Matplotlib <https://matplotlib.org/stable/>
- LaTeX `caption` <https://ctan.org/pkg/caption>

### 10.3 Venue

Venue HI Indonesia dan Sinta — lihat `docs/argument-framework.md` Tabel 2.1.
