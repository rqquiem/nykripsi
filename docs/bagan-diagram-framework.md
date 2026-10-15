# Kerangka Diagram Bagan Simpul-Sisi — Menyambung Simpul seperti Pohon (Sinta, HI/IR, Skripsi, Proposal)

Kerangka ini menetapkan cara menyusun **diagram bagan simpul-sisi** — diagram
bertingkat yang menghubungkan **simpul** menjadi **pohon** (akar → anak → cucu)
melengkapi **sisi** sebagai relasi tambahan — dari **sumber Markdown**. Setiap
klaim dalam dokumen ini bersumber pada **berkas repositori ini** (URL/berkas
repo) atau **literatur/dokumen eksternal** yang terekam sesi ini — tidak ada
aturan tanpa sumber.

Kerangka ini **melengkapi** kerangka yang sudah ada dan tidak menggantikannya.
`docs/diagram-framework.md` menetapkan aturan diagram/tabel dan fungsi keluaran
(D1–D6); `docs/skripsi-pedoman.md` menetapkan tata letak skripsi (caption di
bawah gambar, penomoran `Gambar <bab>.<n>`); dan
`docs/sintesa-diagram-framework.md` menetapkan diagram sintesa teori (TS1–TS6).
Kerangka bagan **tidak menggantikan** salah satu dari ketiganya: ia hanya
menetapkan **bagaimana** diagram simpul-sisi bertingkat disusun dan diperiksa
mesin dari sumber Markdown.

---

## 1. Definisi dan Fungsi

**Definisi.** *Bagan* adalah **blok kode berpagar (*fenced code block*)**
Markdown berkelas `bagan` yang badannya berupa **YAML**. *Simpul* adalah entri
`simpul[]` dengan `id` + `teks` (dan `induk` opsional). *Sisi* adalah relasi
tambahan `sisi[]` yang menghubungkan `dari` → `ke`. *Akar* adalah simpul **tanpa
`induk`**. *Diagram bagan* adalah pohon yang dibentuk dari relasi `induk`
(akar → anak → cucu) yang dapat **direproduksi dari teks** dan **dirender
luring** (`matplotlib`, tanpa Node/LaTeX).

**Fungsi kerangka.** Pertama, **menjadikan bagan dapat direproduksi dari teks**:
diagram dibangun ulang dari blok Markdown, bukan disisipkan sebagai berkas
biner tanpa sumber. Kedua, **menegakkan struktur pohon yang sah**: tiap simpul
bernama, relasi `induk` asiklik, dan **≥ 1 akar**. Ketiga, **menautkan bagan ke
narasi** lewat caption `Gambar <bab>.<n>`. Sumber:
`docs/diagram-framework.md`; `docs/skripsi-pedoman.md`; Matplotlib
<https://matplotlib.org/stable/>.

---

## 2. Lanskap Bagan dan Keluaran

Bagan dalam repositori ini tersusun dari beberapa unsur. Tabel 2.1 memetakan
anatomi bagan beserta kunci YAML, kewajiban, dan keterangannya.

### Tabel 2.1 — Anatomi bagan

|Unsur|Kunci YAML|Wajib|Keterangan|
|---|---|---|---|
|Simpul|`simpul[].id`, `simpul[].teks`, `simpul[].induk`|ya|≥ 2 simpul, tiap simpul ber-`id` unik + `teks` tak kosong; `induk` opsional|
|Sisi|`sisi[].dari`, `sisi[].ke`|tidak|relasi tambahan yang menunjuk `id` yang ada|
|Judul|`judul`|tidak|judul bagan (opsional)|

Sumber: `docs/diagram-framework.md`; `tools/validators/bagan_diagram.py`.

> **Bentuk fence lengkap (contoh):** fence dibuka dengan tiga *backtick* lalu
> ``{.bagan #fig-slug}`` pada baris yang sama, diikuti badan YAML, lalu ditutup
> tiga *backtick*. Pola yang sama berlaku untuk setiap blok bagan ber-id
> `#fig-<slug>`.

---

## 3. Aturan Absolut (BG1–BG5)

Kelima aturan berikut bersifat **absolut**: naskah yang melanggarnya belum layak
disebut memiliki bagan yang reprodusibel. Setiap butir menyebut definisi,
penegak, dan sumbernya. Penegak: `tools/validators/bagan_diagram.py`.

1. **BG1 — Blok bagan ber-YAML sah.** Badan setiap blok `bagan` **wajib** dapat
   diurai sebagai *mapping* YAML dengan kunci `simpul`. YAML tak sah atau bukan
   mapping → gagal.
2. **BG2 — Simpul bernama dan unik.** `simpul` **wajib** *list* dengan **≥ 2**
   entri; setiap entri **wajib** *dict* dengan `id` + `teks` tak kosong; `id`
   **wajib** unik.
3. **BG3 — Relasi induk sah dan asiklik.** Setiap `induk` tak kosong **wajib**
   menunjuk `id` yang ada; graf relasi `induk` **wajib** asiklik; **≥ 1 akar**
   (simpul tanpa `induk` tak kosong).
4. **BG4 — Sisi menunjuk simpul yang ada.** Bila `sisi` ada, ia **wajib**
   *list*; tiap entri **wajib** *dict* dengan `dari` + `ke` yang menunjuk `id`
   yang ada.
5. **BG5 — Bagan terhubung.** Setiap simpul **wajib** dapat dicapai dari sebuah
   akar melalui sisi `induk` **atau** `sisi` (BFS dari semua akar); simpul
   yatim (tidak terjangkau) → gagal.

---

## 4. Frame (Alur Drafting Bagan)

Menulis bagan simpul-sisi yang reprodusibel mengikuti prosedur enam langkah:

1. **Tulis blok** `` ```{.bagan #fig-<slug>} `` berisi YAML.
2. **Tulis caption** `Gambar <bab>.<n> <Judul>` **di bawah** blok.
3. **Jalankan `make diagrams`** untuk merender aset.
4. **Rujuk lewat teks** `pada Gambar <n>`.
5. **Jalankan `make check-figures`**.
6. **Build** (`make skripsi`/`make artikel`).

Sumber: `docs/diagram-framework.md` §4; `docs/skripsi-pedoman.md`.

---

## 5. Model Komponen (Anatomi Blok Bagan)

Sebuah bagan yang sehat tersusun dari komponen fungsional:

- **Blok sumber** — kode berkelas `{.bagan #fig-<slug>}` dengan badan YAML.
- **Aset gambar** — berkas hasil render di `assets/figures/`.
- **Caption** — paragraf `Gambar <n> <Judul>` di bawah blok.
- **Filter** — `tools/pandoc_filters/figure_table.lua` yang mengubah caption dan
  menggantikan blok bagan dengan gambar.
- **Renderer** — `tools/diagrams.py` `_render_bagan` (`matplotlib`).
- **Penegak** — `tools/validators/bagan_diagram.py` (BG1–BG5) +
  `tools/validators/figures_tables.py` (D1–D6).

Sumber: `docs/diagram-framework.md` §5; Matplotlib
<https://matplotlib.org/stable/>.

---

## 6. Pita dan Ambang

### (a) Ambang yang diperiksa mesin

|Parameter|Nilai|Tingkat|
|---|---|---|
|Jumlah simpul|**≥ 2**|fail (BG2)|
|`id` unik|**benar**|fail (BG2)|
|`induk` menunjuk id ada|**benar**|fail (BG3)|
|Graf `induk` asiklik|**benar**|fail (BG3)|
|Jumlah akar|**≥ 1**|fail (BG3)|
|Bagan terhubung|**benar**|fail (BG5)|

Ambang pada (a) dikalibrasi pada **8 berkas final** repositori ini **plus
draf** dan **lulus** (validator mengembalikan `ok` bila tak ada blok); sebaliknya,
blok cacat buatan **gagal**. Bila kelak muncul berkas sah yang melampaui ambang,
konstanta di `tools/validators/bagan_diagram.py` **dan** tabel (a) di dokumen ini
harus diubah **bersamaan** agar tetap selaras.

---

## 7. Matriks Kepatuhan per-Tingkat

|Aturan|Sinta 1–2|Sinta 3–6|Scopus|Skripsi HI|Proposal|
|---|---|---|---|---|---|
|BG1 — Blok bagan ber-YAML sah|wajib|wajib|unverified — confirm first|wajib|wajib|
|BG2 — Simpul bernama dan unik|wajib|wajib|unverified — confirm first|wajib|wajib|
|BG3 — Relasi induk sah dan asiklik|wajib|wajib|unverified — confirm first|wajib|wajib|
|BG4 — Sisi menunjuk simpul yang ada|wajib|wajib|unverified — confirm first|wajib|wajib|
|BG5 — Bagan terhubung|wajib|wajib|unverified — confirm first|wajib|wajib|

BG1–BG5 **wajib** untuk semua kolom: bagan yang reprodusibel adalah syarat
kelayakan dasar, bukan pilihan gaya. Kolom **Scopus** ditandai
**`unverified — confirm first`**: status indeksasi venue internasional tidak
dapat diverifikasi dari korpus lokal, konsisten dengan sikap
`docs/subject-framework.md` §8 yang menandai klaim tak terverifikasi secara
eksplisit.

---

## 8. Daftar Periksa Do/Don't

|Lakukan (Do)|Hindari (Don't)|
|---|---|
|Beri tiap simpul `id` + `teks`|Membuat simpul yatim (tanpa `id`/`teks`)|
|Jaga relasi `induk` tetap asiklik|Membuat siklus `induk`|
|Sediakan ≥ 1 akar dan bagan terhubung|Membiarkan simpul tak terjangkau dari akar|
|Render lewat `make diagrams`|Menempel PNG mentah tanpa sumber Markdown|

---

## 9. Rubrik Penilaian

Nilai **0–2** untuk setiap komponen BG1–BG5; skor maksimum **10**.

|Komponen|0|1|2|
|---|---|---|---|
|BG1 — Blok bagan ber-YAML sah|YAML tak sah / bukan mapping|Mapping tanpa kunci `simpul`|Mapping dengan kunci `simpul`|
|BG2 — Simpul bernama dan unik|< 2 simpul / tanpa `id`|Sebagian simpul tanpa `teks`|≥ 2 simpul, semua ber-`id` unik + `teks`|
|BG3 — Relasi induk sah dan asiklik|`induk` menggantung / siklus|Tanpa akar|`induk` sah, asiklik, ≥ 1 akar|
|BG4 — Sisi menunjuk simpul yang ada|`sisi` bukan list / menggantung|Sebagian sisi menggantung|Semua sisi menunjuk id ada|
|BG5 — Bagan terhubung|Ada simpul yatim|—|Semua simpul terjangkau dari akar|

**Tafsiran:** **10** = patuh penuh; **7–9** = revisi ringan; **4–6** = perlu
perbaikan; **≤ 3** = belum layak.

---

## 10. Sumber

### 10.1 Berkas repositori

- `docs/diagram-framework.md` — kerangka diagram/tabel D1–D6 (dilengkapi).
- `docs/skripsi-pedoman.md` — tata letak skripsi (caption di bawah gambar).
- `tools/diagrams.py` — perender `_render_bagan`.
- `tools/validators/bagan_diagram.py` — penegak BG1–BG5.
- `tools/validators/figures_tables.py` — penegak D1–D6 untuk blok bagan.
- `tools/pandoc_filters/figure_table.lua` — filter caption/gambar.
- `assets/figures/` — direktori aset gambar.

### 10.2 Literatur/dokumen eksternal

- Pandoc Lua filters <https://pandoc.org/lua-filters.html>
- Matplotlib <https://matplotlib.org/stable/>

### 10.3 Venue

Venue HI Indonesia dan Sinta — lihat `docs/argument-framework.md` Tabel 2.1.
