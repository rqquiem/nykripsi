# Kerangka Diagram Sintesa Teori — Menggabungkan Beberapa Teori menjadi Satu Lensa Terpadu (Sinta, HI/IR, Skripsi, Proposal)

Kerangka ini menetapkan cara menyusun **diagram sintesa teori** — penggabungan
beberapa teori menjadi **satu lensa terpadu** yang disusun sebagai **kerangka
berlapis empat** (*Teori Utama -> Teori Pendukung -> Cabang Bukti -> Lingkup*)
— dari **sumber Markdown**. Setiap
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
menjadi **satu lensa terpadu** yang menjawab **satu pertanyaan**, disusun
sebagai **kerangka berlapis empat** yang menghubungkan teori ke bukti:
**Teori Utama -> Teori Pendukung -> Cabang Bukti -> Lingkup**. *Teori utama*
adalah kerangka pokok yang dicatat dengan `nama` + `peran`. *Teori pendukung*
adalah kerangka pelengkap (≥ 1) yang dicatat dengan `nama` + `peran`. *Cabang
bukti* adalah poros bukti empiris (≥ 1) yang dicatat dengan `nama` + `peran`.
*Lingkup* adalah batas kajian (≥ 1 string) yang menandai ruang dan waktu
penelaahan. *Lensa terpadu* adalah **nama gabungan** yang menyatukan
teori-teori tersebut, mis. "lensa diplomasi publik–soft power terpadu".
*Diagram sintesa* adalah **blok kode berpagar (*fenced code block*) Markdown**
berkelas `sintesa` yang badannya berupa **YAML** dan digambar sebagai **pohon
terhubung**: setiap kotak teori utama disambung ke kotak teori pendukung, ke
kotak cabang bukti, lalu ke kotak lingkup.

**Fungsi kerangka.** Pertama, **menjadikan sintesa dapat direproduksi dari
teks**: penggabungan teori dibangun ulang dari blok Markdown, bukan disisipkan
sebagai prosa yang tak dapat diperiksa. Kedua, **menegakkan bahwa setiap teori
punya peran** dan bahwa **lensa terpadu menamai ≥ 2 teori gabungan**. Ketiga,
**menautkan nama lensa ke prosa** sehingga diagram tertaut ke narasi. Keempat,
**menghubungkan teori ke bukti** melalui lapis cabang bukti dan lingkup yang
tergambar sebagai pohon tersambung. Sumber: `docs/skripsi-pedoman.md`;
`docs/conversion-skripsi-to-article.md`; `docs/diagram-framework.md`; Pandoc
Lua filters <https://pandoc.org/lua-filters.html>.

---

## 2. Lanskap Sintesa dan Keluaran

Sintesa teori dalam repositori ini tersusun dari beberapa unsur. Tabel 2.1
memetakan anatomi sintesa beserta kunci YAML, kewajiban, dan keterangannya;
Tabel 2.2 merangkum **contoh terattestasi** yang sudah ada di naskah.

### Tabel 2.1 — Anatomi sintesa

|Unsur|Kunci YAML|Wajib|Keterangan|
|---|---|---|---|
|Teori utama|`teori_utama.nama`, `teori_utama.peran`|ya|satu kerangka pokok bernama dan berperan|
|Teori pendukung|`teori_pendukung[].nama`, `teori_pendukung[].peran`|ya|≥ 1 kerangka pelengkap, tiap entri bernama dan berperan|
|Cabang bukti|`cabang_bukti[].nama`, `cabang_bukti[].peran`|ya|≥ 1 poros bukti empiris, tiap entri bernama dan berperan|
|Lingkup|`lingkup[]`|ya|≥ 1 string tak kosong dan unik (ruang dan waktu)|
|Lensa terpadu|`lensa.nama`, `lensa.gabungan`|ya|nama lensa + ≥ 2 teori utama/pendukung yang digabung|

### Tabel 2.2 — Contoh terattestasi

|Unsur|Nilai|Sumber|
|---|---|---|
|Teori utama|Ekuitas Merek|`artikel-arai` blok `#fig-sintesa-arai`|
|Teori pendukung|Negara Asal; Daya Saing Porter|`artikel-arai` blok `#fig-sintesa-arai`|
|Cabang bukti|Kesadaran Merek; Persepsi Asal; Posisi Bersaing|`artikel-arai` blok `#fig-sintesa-arai`|
|Lingkup|Saluran impor dan distribusi di Indonesia; Pasar helm Indonesia; Periode 2015–2025|`artikel-arai` blok `#fig-sintesa-arai`|
|Lensa terpadu|"lensa ekuitas merek–negara asal–daya saing terpadu"|`artikel-arai` L25|

Sumber: `content/artikel/artikel-arai.md` blok `#fig-sintesa-arai`.

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
   dapat diurai sebagai *mapping* YAML dengan kunci `teori_utama`,
   `teori_pendukung`, `cabang_bukti`, `lingkup`, `lensa`. YAML tak sah, bukan
   mapping, atau kunci wajib hilang → gagal.
2. **TS2 — Teori utama dan teori pendukung bernama dan berperan.**
   `teori_utama` **wajib** *mapping* dengan `nama` dan `peran` tak kosong;
   `teori_pendukung` **wajib** *list* dengan **≥ 1** entri, setiap entri
   **wajib** memuat `nama` dan `peran` tak kosong.
3. **TS3 — Cabang bukti bernama dan berperan.** `cabang_bukti` **wajib** *list*
   dengan **≥ 1** entri; setiap entri **wajib** memuat `nama` dan `peran` tak
   kosong.
4. **TS4 — Lingkup unik dan tak kosong.** `lingkup` **wajib** *list* dengan
   **≥ 1** string tak kosong dan unik (menandai ruang dan waktu kajian).
5. **TS5 — Lensa terpadu menamai ≥ 2 teori gabungan.** `lensa.nama` **wajib**
   tak kosong; `lensa.gabungan` **wajib** *list* **≥ 2** entri dan setiap entri
   **wajib** menunjuk `nama` pada `teori_utama` atau `teori_pendukung`.
6. **TS6 — Nama lensa disebut di prosa.** `lensa.nama` **wajib** muncul sebagai
   substring di prosa berkas yang sama (**di luar** seluruh blok `sintesa`),
   sehingga diagram tertaut ke narasi.

---

## 4. Frame (Alur Drafting Sintesa)

Menulis diagram sintesa teori yang reprodusibel mengikuti prosedur tujuh
langkah:

1. **Daftarkan teori utama** (`nama` + `peran`) dan **teori pendukung**
   (`nama` + `peran`).
2. **Daftar cabang bukti** (`nama` + `peran`) sebagai poros bukti empiris.
3. **Daftar lingkup** (≥ 1 string) sebagai batas ruang dan waktu kajian.
4. **Pilih ≥ 2 teori yang digabung**, tetapkan `lensa.nama` +
   `lensa.gabungan` yang menunjuk teori utama/pendukung.
5. **Tulis blok** `` ```{.sintesa #fig-<slug>} `` + caption
   `Gambar <bab>.<n> <Judul>` **di bawah** blok.
6. **Sebut nama lensa di prosa**.
7. **Jalankan `make diagrams`** lalu `make check-figures` lalu
   `make skripsi`/`make artikel`.

Sumber: `docs/skripsi-pedoman.md`; `docs/diagram-framework.md` §4.

---

## 5. Model Komponen (Anatomi Blok Sintesa)

Sebuah sintesa teori yang sehat tersusun dari sembilan komponen fungsional:

- **Blok sumber** — kode berkelas `{.sintesa #fig-<slug>}` dengan badan YAML.
- **Teori utama** — `teori_utama` dengan `nama` + `peran`.
- **Teori pendukung** — daftar `teori_pendukung[]` dengan `nama` + `peran`.
- **Cabang bukti** — daftar `cabang_bukti[]` dengan `nama` + `peran`.
- **Lingkup** — daftar `lingkup[]` string ruang dan waktu.
- **Lensa terpadu** — `lensa` dengan `nama` + `gabungan`.
- **Perender** — `tools/diagrams.py` `_render_sintesa` (matplotlib), yang
  menggambar lima lapis (judul, teori utama, teori pendukung, cabang bukti,
  lingkup) sebagai **pohon tersambung** dengan panah antarlapis.
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
|Teori utama bernama + berperan|**benar**|fail (TS2)|
|Jumlah teori pendukung|**≥ 1**|fail (TS2)|
|Jumlah cabang bukti|**≥ 1**|fail (TS3)|
|Jumlah lingkup unik|**≥ 1**|fail (TS4)|
|Jumlah gabungan|**≥ 2**|fail (TS5)|
|Nama lensa ada di prosa|**ada**|fail (TS6)|

Ambang pada (a) dikalibrasi pada **12 berkas** repositori ini (**4 blok sintesa**
saat ini) dan **lulus** (validator mengembalikan `ok` bila semua blok patuh);
sebaliknya, blok cacat buatan **gagal**. Bila kelak muncul berkas sah yang
melampaui ambang, konstanta di `tools/validators/sintesa_diagram.py` **dan**
tabel (a) di dokumen ini harus diubah **bersamaan** agar tetap selaras.

---

## 7. Matriks Kepatuhan per-Tingkat

|Aturan|Sinta 1–2|Sinta 3–6|Scopus|Skripsi HI|Proposal|
|---|---|---|---|---|---|
|TS1 — Blok sintesa ber-YAML sah|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS2 — Teori utama + teori pendukung bernama dan berperan|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS3 — Cabang bukti bernama dan berperan|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS4 — Lingkup unik dan tak kosong|wajib|wajib|unverified — confirm first|wajib|wajib|
|TS5 — Lensa terpadu menamai ≥ 2 teori gabungan|wajib|wajib|unverified — confirm first|wajib|wajib|
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
|Beri peran tiap teori utama/pendukung|Mendaftar teori tanpa peran|
|Susun cabang bukti dan lingkup di bawah teori|Menaruh bukti tanpa cabang yang bernama|
|Sebut nama lensa di prosa|Menaruh diagram tanpa menyebut lensa di teks|

---

## 9. Rubrik Penilaian

Nilai **0–2** untuk setiap komponen TS1–TS6; skor maksimum **12**.

|Komponen|0|1|2|
|---|---|---|---|
|TS1 — Blok sintesa ber-YAML sah|YAML tak sah / bukan mapping|Mapping tanpa kunci wajib lengkap|Mapping dengan kunci wajib lengkap|
|TS2 — Teori utama + teori pendukung bernama dan berperan|Tanpa `teori_utama` / tanpa nama|Sebagian entri tanpa peran|Teori utama + ≥ 1 pendukung, semua bernama + berperan|
|TS3 — Cabang bukti bernama dan berperan|Tanpa `cabang_bukti` / < 1|Entri cabang bukti tanpa peran|≥ 1 cabang bukti bernama + berperan|
|TS4 — Lingkup unik dan tak kosong|Tanpa `lingkup` / string kosong|Lingkup memuat duplikat|≥ 1 lingkup unik tak kosong|
|TS5 — Lensa terpadu menamai ≥ 2 teori gabungan|Tanpa `lensa.nama` / < 2 gabungan|Gabungan menunjuk teori tak ada|`lensa.nama` + ≥ 2 gabungan sah|
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
