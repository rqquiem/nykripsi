# Kerangka Diagram Sintesa Teori — Menggabungkan Beberapa Teori menjadi Satu Lensa Terpadu (Sinta, HI/IR, Skripsi, Proposal)

Kerangka ini menetapkan cara menyusun **diagram sintesa teori** — penggabungan
beberapa teori menjadi **satu lensa terpadu** plus kerangka yang dipertahankan
sebagai **tingkat analisis lintas tahap** — dari **sumber Markdown**. Setiap
klaim dalam dokumen ini bersumber pada **berkas repositori ini** (URL/berkas
repo) atau **literatur/dokumen eksternal** yang terekam sesi ini — tidak ada
aturan tanpa sumber.

Kerangka ini **melengkapi** kerangka yang sudah ada dan tidak menggantikannya.
`docs/diagram-framework.md` menetapkan aturan diagram/tabel dan fungsi keluaran
(D1–D6); `docs/skripsi-pedoman.md` menetapkan tata letak skripsi (§Kajian Teori,
§Kerangka Pemikiran); `docs/conversion-skripsi-to-article.md` mengatur konversi
skripsi menjadi artikel (BAB II dilipat ke Pendahuluan + Pembahasan); dan
`docs/research-gap.md` memakai dimensi `teori`. Kerangka sintesa **tidak
menggantikan** salah satu dari keempatnya: ia hanya menetapkan **bagaimana**
penggabungan beberapa teori menjadi satu lensa terpadu disusun dan diperiksa
mesin dari sumber Markdown.

---

## 1. Definisi dan Fungsi

**Definisi.** *Sintesa teori* adalah penggabungan **dua teori atau lebih**
menjadi **satu lensa terpadu** yang menjawab **satu pertanyaan**. *Lensa
terpadu* adalah **nama gabungan** yang menyatukan teori-teori tersebut, mis.
"lensa diplomasi publik–soft power terpadu". *Teori* adalah kerangka konseptual
yang dicatat dengan `nama` + `peran`. *Tingkat analisis lintas tahap* adalah
kerangka yang **tidak** digabung ke dalam lensa tetapi **menelusuri setiap
tahap** analisis. *Diagram sintesa* adalah **blok kode berpagar (*fenced code
block*) Markdown** berkelas `sintesa` yang badannya berupa **YAML**.

**Fungsi kerangka.** Pertama, **menjadikan sintesa dapat direproduksi dari
teks**: penggabungan teori dibangun ulang dari blok Markdown, bukan disisipkan
sebagai prosa yang tak dapat diperiksa. Kedua, **menegakkan bahwa setiap teori
punya peran** dan bahwa **lensa terpadu menamai ≥ 2 teori gabungan**. Ketiga,
**menautkan nama lensa ke prosa** sehingga diagram tertaut ke narasi. Sumber:
`docs/skripsi-pedoman.md`; `docs/conversion-skripsi-to-article.md`;
`docs/diagram-framework.md`; Pandoc Lua filters
<https://pandoc.org/lua-filters.html>.

---

## 2. Lanskap Sintesa dan Keluaran

Sintesa teori dalam repositori ini tersusun dari beberapa unsur. Tabel 2.1
memetakan anatomi sintesa beserta kunci YAML, kewajiban, dan keterangannya;
Tabel 2.2 merangkum **contoh terattestasi** yang sudah ada di naskah.

### Tabel 2.1 — Anatomi sintesa

|Unsur|Kunci YAML|Wajib|Keterangan|
|---|---|---|---|
|Teori|`teori[].nama`, `teori[].peran`|ya|≥ 2 teori, tiap teori bernama dan berperan|
|Lensa terpadu|`lensa.nama`, `lensa.gabungan`|ya|nama lensa + ≥ 2 teori yang digabung|
|Tingkat lintas tahap|`lintas_tahap[].nama`, `lintas_tahap[].peran`|tidak|kerangka yang tetap terpisah dari lensa|
|Tahap analisis|`tahap[]`|ya|≥ 2 tahap berurutan|

### Tabel 2.2 — Contoh terattestasi

|Unsur|Nilai|Sumber|
|---|---|---|
|Teori|Diplomasi Publik; Soft Power dan Nation Branding; Analisis Kebijakan Luar Negeri (FPA)|`11-bab-02` §Kajian Teori|
|Lensa terpadu|"lensa diplomasi publik–soft power terpadu"|`11-bab-02` L78|
|Gabungan|Diplomasi Publik + Soft Power dan Nation Branding|`11-bab-02` L78|
|Tingkat lintas tahap|Analisis Kebijakan Luar Negeri (FPA)|`11-bab-02` L78|
|Tahap|Instrumen → Paparan → Persepsi → Implikasi|`11-bab-02` Tabel 2.1|

Sumber: `content/skripsi/11-bab-02-tinjauan-pustaka.md` §Kerangka Pemikiran.

> **Bentuk fence lengkap (contoh):** fence dibuka dengan tiga *backtick* lalu
> ``{.sintesa #fig-slug}`` pada baris yang sama, diikuti badan YAML, lalu
> ditutup tiga *backtick*. Pola yang sama berlaku untuk setiap blok sintesa
> ber-id `#fig-<slug>`.

---

## 3. Aturan Absolut (TS1–TS6)

Keenam aturan berikut bersifat **absolut**: naskah yang melanggarnya belum layak
disebut memiliki sintesa teori yang reprodusibel. Setiap butir menyebut
definisi, penegak, dan sumbernya. Penegak: `tools/validators/sintesa_diagram.py`.

1. **TS1 — Blok sintesa ber-YAML sah.** Badan setiap blok `sintesa` **wajib**
   dapat diurai sebagai *mapping* YAML dengan kunci `teori`, `lensa`, `tahap`
   (`lintas_tahap` opsional). YAML tak sah atau bukan mapping → gagal.
2. **TS2 — Setiap teori bernama dan berperan.** `teori` **wajib** *list* dengan
   **≥ 2** entri; setiap entri **wajib** memuat `nama` dan `peran` tak kosong.
3. **TS3 — Lensa terpadu menamai ≥ 2 teori gabungan.** `lensa.nama` **wajib**
   tak kosong; `lensa.gabungan` **wajib** *list* **≥ 2** entri dan setiap entri
   **wajib** menunjuk `nama` teori yang ada di `teori`.
4. **TS4 — Tingkat lintas tahap terpisah.** Bila `lintas_tahap` ada, setiap
   entri **wajib** memuat `nama` + `peran` tak kosong dan `nama`-nya **tidak
   boleh** muncul di `lensa.gabungan` (satu kerangka digabung **atau** lintas
   tahap, tidak keduanya).
5. **TS5 — Tahap analisis berurutan dan unik.** `tahap` **wajib** *list* dengan
   **≥ 2** entri unik.
6. **TS6 — Nama lensa disebut di prosa.** `lensa.nama` **wajib** muncul sebagai
   substring di prosa berkas yang sama (**di luar** seluruh blok `sintesa`),
   sehingga diagram tertaut ke narasi.

---

## 4. Frame (Alur Drafting Sintesa)

Menulis diagram sintesa teori yang reprodusibel mengikuti prosedur tujuh
langkah:

1. **Daftarkan teori** (`nama` + `peran`).
2. **Pilih ≥ 2 teori yang digabung**, tetapkan `lensa.nama` +
   `lensa.gabungan`.
3. Bila ada kerangka yang tetap terpisah, **tulis `lintas_tahap`**.
4. **Daftar `tahap`** analisis (≥ 2, berurutan).
5. **Tulis blok** `` ```{.sintesa #fig-<slug>} `` + caption
   `Gambar <bab>.<n> <Judul>` **di bawah** blok.
6. **Sebut nama lensa di prosa**.
7. **Jalankan `make diagrams`** lalu `make check-figures` lalu
   `make skripsi`/`make artikel`.

Sumber: `docs/skripsi-pedoman.md`; `docs/diagram-framework.md` §4.

---

## 5. Model Komponen (Anatomi Blok Sintesa)

Sebuah sintesa teori yang sehat tersusun dari delapan komponen fungsional:

- **Blok sumber** — kode berkelas `{.sintesa #fig-<slug>}` dengan badan YAML.
- **Teori** — daftar `teori[]` dengan `nama` + `peran`.
- **Lensa terpadu** — `lensa` dengan `nama` + `gabungan`.
- **Tingkat lintas tahap** — `lintas_tahap` (bila ada) dengan `nama` + `peran`.
- **Tahap** — daftar `tahap[]` berurutan.
- **Perender** — `tools/diagrams.py` `_render_sintesa` (matplotlib).
- **Filter** — `tools/pandoc_filters/figure_table.lua` yang mengubah caption dan
  menggantikan blok sintesa dengan gambar.
- **Penegak** — `tools/validators/sintesa_diagram.py` (TS1–TS6) +
  `tools/validators/figures_tables.py` (D1–D6).

Sumber: `docs/skripsi-pedoman.md`; `docs/diagram-framework.md` §5; Matplotlib
<https://matplotlib.org/stable/>.

---

## 6. Pita dan Ambang

### (a) Ambang yang diperiksa mesin

|Parameter|Nilai|Tingkat|
|---|---|---|
|Jumlah teori|**≥ 2**|fail (TS2)|
|Jumlah gabungan|**≥ 2**|fail (TS3)|
|Jumlah tahap unik|**≥ 2**|fail (TS5)|
|`lintas_tahap[].nama` ∉ `lensa.gabungan`|**benar**|fail (TS4)|
|Nama lensa ada di prosa|**ada**|fail (TS6)|

Ambang pada (a) dikalibrasi pada **8 berkas** repositori ini (**0 blok sintesa**
saat ini) dan **lulus** (validator mengembalikan `ok` bila tak ada blok);
sebaliknya, blok cacat buatan **gagal**. Bila kelak muncul berkas sah yang
melampaui ambang, konstanta di `tools/validators/sintesa_diagram.py` **dan**
tabel (a) di dokumen ini harus diubah **bersamaan** agar tetap selaras.

---

## 7. Matriks Kepatuhan per-Tingkat

|Aturan|Sinta 1–2|Sinta 3–6|Scopus|Skripsi HI|Proposal|
|---|---|---|---|---|---|
|TS1 — Blok sintesa ber-YAML sah|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS2 — Setiap teori bernama dan berperan|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS3 — Lensa terpadu menamai ≥ 2 teori gabungan|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS4 — Tingkat lintas tahap terpisah|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS5 — Tahap analisis berurutan dan unik|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS6 — Nama lensa disebut di prosa|wajib|wajib|unverified — confirm first|wajib|wajib|

TS1–TS6 **wajib** untuk semua kolom: sintesa teori yang reprodusibel adalah
syarat kelayakan dasar, bukan pilihan gaya. Kolom **Scopus** ditandai
**`unverified — confirm first`**: status indeksasi venue internasional tidak
dapat diverifikasi dari korpus lokal, konsisten dengan sikap
`docs/subject-framework.md` §8 yang menandai klaim tak terverifikasi secara
eksplisit.

---

## 8. Daftar Periksa Do/Don't

|Lakukan (Do)|Hindari (Don't)|
|---|---|
|Gabung ≥ 2 teori jadi satu lensa bernama|Menumpuk teori tanpa menyebut lensa|
|Beri peran tiap teori|Mendaftar teori tanpa peran|
|Pisahkan kerangka lintas tahap dari lensa|Memasukkan kerangka lintas tahap ke dalam lensa|
|Sebut nama lensa di prosa|Menaruh diagram tanpa menyebut lensa di teks|

---

## 9. Rubrik Penilaian

Nilai **0–2** untuk setiap komponen TS1–TS6; skor maksimum **12**.

|Komponen|0|1|2|
|---|---|---|---|
|TS1 — Blok sintesa ber-YAML sah|YAML tak sah / bukan mapping|Mapping tanpa kunci wajib lengkap|Mapping dengan kunci wajib lengkap|
|TS2 — Setiap teori bernama dan berperan|< 2 teori / tanpa nama|Sebagian teori tanpa peran|≥ 2 teori, semua bernama + berperan|
|TS3 — Lensa terpadu menamai ≥ 2 teori gabungan|Tanpa `lensa.nama` / < 2 gabungan|Gabungan menunjuk teori tak ada|`lensa.nama` + ≥ 2 gabungan sah|
|TS4 — Tingkat lintas tahap terpisah|Lintas tahap tumpang-tindih gabungan|Entri lintas tahap tanpa peran|Lintas tahap bernama + berperan, terpisah|
|TS5 — Tahap analisis berurutan dan unik|< 2 tahap|Tahap duplikat|≥ 2 tahap unik berurutan|
|TS6 — Nama lensa disebut di prosa|Nama lensa tak ada di prosa|—|Nama lensa muncul di prosa|

**Tafsiran:** **12** = patuh penuh; **9–11** = revisi ringan; **5–8** = perlu
perbaikan; **≤ 4** = belum layak.

---

## 10. Sumber

### 10.1 Berkas repositori

- `docs/diagram-framework.md` — kerangka diagram/tabel D1–D6 (dilengkapi).
- `docs/skripsi-pedoman.md` — tata letak skripsi (§Kajian Teori, §Kerangka
  Pemikiran).
- `docs/conversion-skripsi-to-article.md` — konversi skripsi menjadi artikel.
- `docs/research-gap.md` — dimensi `teori`.
- `content/skripsi/11-bab-02-tinjauan-pustaka.md` — contoh sintesa terattestasi.
- `README.md` — ringkasan sintesa lensa terpadu + FPA.
- `tools/validators/sintesa_diagram.py` — penegak TS1–TS6.
- `tools/validators/figures_tables.py` — penegak D1–D6 untuk blok sintesa.
- `tools/diagrams.py` — perender `_render_sintesa`.
- `tools/pandoc_filters/figure_table.lua` — filter caption/gambar.

### 10.2 Literatur/dokumen eksternal

- Pandoc Lua filters <https://pandoc.org/lua-filters.html>
- Matplotlib <https://matplotlib.org/stable/>
- Jabareen, Y. (2009) *Building a Conceptual Framework: Philosophy,
  Definitions, and Procedure*, International Journal of Qualitative Methods —
  `unverified — confirm first`
- Baumeister, R. F., & Leary, M. R. (1997) *Writing Narrative Literature
  Reviews*, Review of General Psychology — `unverified — confirm first`

### 10.3 Venue

Venue HI Indonesia dan Sinta — lihat `docs/argument-framework.md` Tabel 2.1.
