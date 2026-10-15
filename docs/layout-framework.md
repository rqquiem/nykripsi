# Kerangka Tata Letak & Tipografi — Artikel Jurnal, Skripsi, dan Paper Akademik (Sinta, HI/IR, Skripsi, Proposal)

Kerangka ini menetapkan **tata letak** dan **tipografi** naskah ilmiah agar setiap
berkas Markdown dapat dirender menjadi PDF/DOCX yang patuh tanpa penyuntingan
manual. Prinsipnya: **tata letak harus dapat direproduksi dari teks** (margin,
spasi, indent, font, dan penomoran halaman/bab diturunkan dari preamble, bukan
ditempel sebagai berkas mati) dan **tipografi harus dapat diperiksa mesin**
(kata miring istilah asing dan penjabaran singkatan ditolak otomatis bila
melanggar). Setiap klaim dalam dokumen ini bersumber pada **berkas repositori
ini** (URL/berkas repo) atau **literatur/dokumen eksternal** yang terekam sesi
ini — tidak ada aturan tanpa sumber.

Kerangka ini **melengkapi** kerangka yang sudah ada dan tidak menggantikannya.
`docs/diagram-framework.md` mengatur gambar, tabel, dan fungsi keluaran
(*caption*, penomoran, `DAFTAR GAMBAR`/`DAFTAR TABEL`); `docs/skripsi-pedoman.md`
menetapkan pedoman skripsi STMIK Triguna Dharma (TGD) — margin **2,5 cm**,
spasi **1,5**, penomoran bab Romawi `I.` tanpa kata "BAB"; `docs/sinta-reference.md`
menetapkan anatomi dan spesifikasi teknis artikel Sinta (margin ~2,5–3 cm, font
Times New Roman/Arial/Cambria 10–12 pt, spasi 1,0 atau 1,15); `docs/bahasa-artikel.md`
menetapkan ragam bahasa ilmiah Indonesia (EYD Edisi V, linter
`tools/check-bahasa.sh`); dan `docs/argument-framework.md` mengatur alur argumen
serta kohesi paragraf. Kerangka tata letak **tidak menggantikan** kelimanya: ia
hanya menetapkan **bagaimana** margin, spasi, indent, font, penomoran, kata
miring istilah asing, dan penjabaran singkatan ditegakkan secara reprodusibel dan
dapat diperiksa mesin.

---

## 1. Definisi dan Fungsi

**Definisi.** *Tata letak* adalah seperangkat parameter halaman yang menentukan
tampilan fisik naskah: **margin** (batas tepi kertas), **spasi** (jarak
antarbaris, mis. 1,5), **indent** (lekuk baris pertama), **font** (keluarga dan
ukuran huruf), serta **penomoran halaman dan bab** (angka Romawi/Arab, posisi
nomor, penomoran bab). *Tipografi* adalah seperangkat konvensi penulisan teks
yang menentukan penampilan kata: **kata miring istilah asing** (menuliskan
ungkapan bahasa asing dengan huruf miring) dan **singkatan & kepanjangan**
(menjabarkan singkatan pada penyebutan pertama dan mendaftarkannya). Tata letak
diturunkan dari preamble LaTeX dan *reference-docx*; tipografi ditegakkan dari
registri bahasa.

**Tiga profil.** Repositori ini mengelola **tiga profil** tata letak:

1. **Skripsi** (TGD) — profil paling ketat: margin **2,5 cm** keempat sisi,
   spasi **1,5**, indent **0,5 cm**, font serif (**Liberation Serif** ≈ Times New
   Roman), penomoran bab **Romawi** `I.` tanpa kata "BAB". Sumber:
   `docs/skripsi-pedoman.md`; `templates/skripsi-preamble.tex`.
2. **Artikel jurnal** (Sinta) — profil submisi: margin **2,5 cm**, spasi **1,15**,
   indent **0**, font **Times New Roman**, tanpa penomoran bab. Sumber:
   `docs/sinta-reference.md`; `templates/artikel-preamble.tex`;
   `templates/journal-reference.docx`.
3. **Paper akademik** — **profil terdokumentasi saja (*documented profile
   only*)**: parameter mengikuti *author guidelines* tiap venue (margin
   ~2,5–3 cm, spasi **1,0–1,5**, font Times/Arial/Cambria **10–12 pt**), **tanpa
   build/template** khusus di repositori ini. Sumber: `docs/sinta-reference.md`
   (Tabel *Technical spec table*).

**Fungsi kerangka.** Pertama, **menjadikan tata letak dapat direproduksi dari
teks**: margin, spasi, indent, font, dan penomoran dihasilkan ulang dari
Markdown + preamble, bukan disunting tangan per berkas. Kedua, **menjadikan
tipografi dapat diperiksa mesin**: setiap istilah asing pada registri wajib
miring dan setiap singkatan wajib dijabarkan serta terdaftar, sehingga validator
dapat menolak naskah yang melanggar.

**Dasar normatif.** EYD Edisi V menetapkan bahwa **ungkapan bahasa asing
ditulis dengan huruf miring**, kecuali nama diri dan nama merek yang tidak
dimiringkan (butir **G.3**, catatan a) — lihat
<https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-huruf/huruf-miring/>. EYD
Edisi V juga menetapkan aturan **singkatan dan akronim** (butir **F.3**): sebuah
singkatan yang belum lazim **dijabarkan** lebih dulu sebelum dipakai — lihat
<https://ejaan.kemendikdasmen.go.id/eyd/penulisan-kata/singkatan-dan-akronim/>.
Registri istilah dan singkatan repositori ini menurunkan kedua kaidah itu ke
daftar konkret di `assets/bahasa/kamus-id.yaml`.

---

## 2. Lanskap Profil Tata Letak dan Anatomi Tipografi

Tata letak tidak berdiri di ruang hampa: ia dibentuk oleh **profil** tempat
naskah dirender. Tabel 2.1 memetakan parameter tata letak ketiga profil; Tabel
2.2 merangkum aturan tipografi istilah asing dan singkatan.

### Tabel 2.1 — Profil tata letak

|Unsur|Skripsi|Artikel Jurnal|Paper Akademik|Sumber|
|---|---|---|---|---|
|Margin|2,5 cm keempat sisi|2,5 cm|per *author guidelines*|`docs/skripsi-pedoman.md`; `templates/skripsi-preamble.tex`; `templates/artikel-preamble.tex`|
|Spasi|1,5|1,15|1,0–1,5|`docs/skripsi-pedoman.md`; `templates/skripsi-preamble.tex`; `docs/sinta-reference.md`|
|Indent|0,5 cm|0|—|`docs/skripsi-pedoman.md`; `templates/skripsi-preamble.tex`|
|Font|Liberation Serif ≈ Times New Roman|Times New Roman|Times/Arial/Cambria 10–12 pt|`templates/skripsi-preamble.tex`; `templates/journal-reference.docx`; `docs/sinta-reference.md`|
|Penomoran bab|Romawi `I.`, tanpa "BAB"|tanpa bab|tanpa bab|`docs/skripsi-pedoman.md`; `templates/skripsi-preamble.tex`|

### Tabel 2.2 — Anatomi tipografi

|Unsur|Aturan|Contoh|
|---|---|---|
|Istilah asing|Ditulis miring `*istilah*` pada prosa/heading (EYD Edisi V G.3)|`*soft power*`|
|Singkatan|Ditulis `SINGKATAN (Kepanjangan)` pada penyebutan pertama + didaftarkan di `DAFTAR SINGKATAN` (EYD Edisi V F.3)|`PLTU (Pembangkit Listrik Tenaga Uap)`|

Anatomi di atas menentukan **bagaimana** teks ditampilkan; aturan LT1–LT9 di
Bagian 3 menentukan **apa** yang wajib ada agar tata letak dan tipografi itu
reprodusibel dan dapat diperiksa mesin.

### Tata Letak Sinta 1–6 (artikel)

Artikel Sinta 1–6 dirender satu kolom mengikuti contoh korpus
`docs/sinta-corpus/s6-jutik.pdf`. Tata letaknya:

- **Front matter terpusat** — masthead jurnal, judul, penulis, afiliasi, email,
  dan penulis korespondensi semuanya di tengah.
- **`ABSTRAK`/`ABSTRACT` terpusat** — judul abstrak dicetak di tengah, badan
  abstrak **rata kanan-kiri (justified)**.
- **Enam kepala bagian kanonik** dirender **terpusat, tebal (bold), dan HURUF
  BESAR (ALL-CAPS), tanpa nomor** sesuai urutan sumber (`PENDAHULUAN` …
  `DAFTAR PUSTAKA`).
- **Sub-heading `##`** rata kiri, tebal, **tanpa nomor**.
- **Badan artikel** rata kanan-kiri (justified).
- **Font ber-metrik Times** (Times New Roman; PDF memakai Liberation Serif yang
  setara metrik).
- **Label caption `Gambar`/`Tabel`** (bukan `Figure`/`Table`).
- **Istilah asing** dari registri `istilah_asing` ditulis **miring**.

Transformasi tata letak ini dijalankan oleh filter Pandoc
`tools/pandoc_filters/sinta_layout.lua`; contoh acuan ada di
`docs/sinta-corpus/s6-jutik.pdf`.

---

## 3. Aturan Absolut (LT1–LT9)

Kesembilan aturan berikut bersifat **absolut**: naskah yang melanggarnya belum layak
disebut memiliki tata letak dan tipografi yang reprodusibel. Setiap butir
menyebut definisi, penegak, dan sumbernya.

1. **LT1 — Tata letak skripsi.** `templates/skripsi-preamble.tex` **wajib**
   memuat anchor: margin `2.5cm` keempat sisi, `\onehalfspacing`, indent
   `0.5cm`, font serif (`Liberation Serif`), dan penomoran bab Romawi
   (`\thechapter` → `\Roman`). Definisi: skripsi TGD dirender dari preamble ini
   sehingga parameter halaman tidak diatur per berkas. Penegak:
   `tools/validators/layout_typography.py`. Sumber: `docs/skripsi-pedoman.md`;
   `templates/skripsi-preamble.tex`.
2. **LT2 — Tata letak artikel/jurnal.** `templates/artikel-preamble.tex`
   **wajib** memuat `margin=2.5cm` + `\setstretch{1.15}`; dan
   `templates/journal-reference.docx` **wajib** ada serta bergaya **Times New
   Roman**. Definisi: artikel Sinta dirender dari preamble LaTeX (PDF) dan
   *reference-docx* (DOCX) sehingga gaya kedua keluaran selaras. Penegak:
   `tools/validators/layout_typography.py`. Sumber:
   `templates/artikel-preamble.tex`; `templates/journal-reference.docx`;
   `docs/sinta-reference.md`.
3. **LT3 — Kata miring istilah asing.** Setiap istilah pada registri
   `istilah_asing` **wajib** ditulis `*istilah*` di prosa/heading (di luar
   *fence*, komentar, blok abstrak, tabel, *caption*, dan label kata kunci).
   Definisi: EYD Edisi V G.3 catatan a mewajibkan huruf miring untuk ungkapan
   asing; nama diri/merek dikecualikan sehingga tidak didaftarkan. Penegak:
   `tools/validators/layout_typography.py`. Sumber:
   <https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-huruf/huruf-miring/>;
   `assets/bahasa/kamus-id.yaml` (`istilah_asing`); APA Style.
4. **LT4 — Penjabaran singkatan.** Penyebutan **prosa pertama** tiap singkatan
   registri **wajib** berpola `SINGKATAN (Kepanjangan)`. Definisi: EYD Edisi V
   F.3 menuntut singkatan yang belum lazim dijabarkan lebih dulu; pola ini
   menempatkan kepanjangan tepat pada kemunculan pertama di prosa. Penegak:
   `tools/validators/layout_typography.py`. Sumber:
   <https://ejaan.kemendikdasmen.go.id/eyd/penulisan-kata/singkatan-dan-akronim/>;
   `assets/bahasa/kamus-id.yaml` (`singkatan`).
5. **LT5 — DAFTAR SINGKATAN.** Setiap singkatan yang terpakai
   (prosa/heading/tabel) **wajib** terdaftar di `DAFTAR SINGKATAN` — untuk
   skripsi di `content/skripsi/07-daftar-singkatan.md`; untuk artikel di blok
   `## Daftar Singkatan` di berkas artikel. Definisi: daftar menjamin pembaca
   dapat memecahkan setiap singkatan tanpa menelusuri prosa. Penegak:
   `tools/validators/layout_typography.py`. Sumber: `docs/skripsi-pedoman.md`;
   `content/skripsi/07-daftar-singkatan.md`; `content/artikel/artikel-sinta.md`.
6. **LT6 — Tata letak Sinta terpusat.** Artikel Sinta 1–6 **wajib** dirender
   dengan tata letak terpusat: filter `tools/pandoc_filters/sinta_layout.lua`
   **wajib** ada dan dipakai; `templates/artikel-preamble.tex` **wajib** memuat
   anchor `\centering`, `\titleformat{\section}`,
   `\renewcommand{\figurename}{Gambar}`, dan
   `\renewcommand{\tablename}{Tabel}`; dan setiap target artikel pada `Makefile`
   **wajib** menyisipkan filter itu. Definisi: front matter, judul
   `ABSTRAK`/`ABSTRACT`, dan enam kepala bagian kanonik dirender terpusat,
   HURUF BESAR, dengan badan rata kanan-kiri — sesuai contoh
   `docs/sinta-corpus/s6-jutik.pdf`. Penegak:
   `tools/validators/layout_typography.py`. Sumber:
   `templates/artikel-preamble.tex`; `tools/pandoc_filters/sinta_layout.lua`;
   `Makefile`.
7. **LT7 — Bahasa kedua (EN) miring.** Setiap blok berbahasa kedua — blok
   `::: {lang=en} … :::`, termasuk `ABSTRACT` — **wajib** dimiringkan otomatis
   bila `bahasa.utama` pada kamus **berbeda** dari bahasa blok itu. Definisi:
   naskah dwibahasa (Indonesia + Inggris) menandai blok bahasa kedua dengan
   atribut `lang=en` sehingga filter merendernya miring, menandai bahwa teks itu
   bukan bahasa utama. Penegak: `tools/validators/layout_typography.py`. Sumber:
   `assets/bahasa/kamus-id.yaml` §`bahasa` (kunci `bahasa.utama`);
   `tools/pandoc_filters/bilingual.lua`.
8. **LT8 — Tanda pisah (dash ban).** Pada prosa akademik, EM DASH `—` (U+2014)
   dan HYPHEN ASCII BERSPASI ` - ` **dilarang**; gantikan dengan koma, titik dua,
   atau titik. EN DASH `–` (U+2013) **hanya** diizinkan untuk rentang angka
   (mis. `2020–2022`). Selain itu, pemenggalan kata otomatis LaTeX ditekan
   sehingga tidak ada hyphen pada kata yang terpotong di ujung baris: baik
   `templates/skripsi-preamble.tex` maupun `templates/artikel-preamble.tex`
   **wajib** memuat `\hyphenpenalty=10000` dan `\exhyphenpenalty=10000`.
   Definisi: tanda pisah mengganggu keterbacaan dan gaya korpus lebih memilih
   koma/titik dua/titik; en dash dikhususkan untuk rentang angka, sedangkan
   hyphenasi otomatis disembunyikan agar tidak ada tanda pisah buatan pada
   pemenggalan baris. Penegak: `tools/validators/layout_typography.py`. Sumber:
   `assets/bahasa/kamus-id.yaml` §`tanda_pisah`;
   `templates/skripsi-preamble.tex`; `templates/artikel-preamble.tex`.
9. **LT9 — Istilah teknis dwibahasa.** Setiap istilah teknis Indonesia tingkat
   lanjut yang terdaftar di `assets/bahasa/kamus-id.yaml` §`istilah_teknis`
   **wajib** diikuti padanan bahasa Inggrisnya dalam tanda kurung pada
   **kemunculan prosa pertama**: `istilah (english gloss)`, atau
   `istilah (*english gloss*)` bila padanan itu sendiri istilah `istilah_asing`
   yang terdaftar (huruf miring EYD G.3). Definisi: pembaca Indonesia tetap
   memahami istilah teknis lanjut melalui padanan Inggrisnya, dan istilah asing
   yang menjadi padanan tetap dimiringkan sesuai EYD Edisi V G.3. Dikecualikan:
   blok abstrak, tabel, *caption*, label kata kunci, *fence* kode, dan komentar.
   Penegak: `tools/validators/layout_typography.py`. Sumber:
   `assets/bahasa/kamus-id.yaml` §`istilah_teknis`; `docs/layout-framework.md`
   LT3.

LT1–LT2 menuntut sifat **statis** (keberadaan anchor di preamble dan
*reference-docx*) sehingga dapat diperiksa dengan pencocokan pola berkas; LT3–LT5
menuntut sifat **permukaan** pada prosa (penanda miring, pola penjabaran,
keberadaan di daftar) sehingga dapat ditegakkan otomatis. Karena itu LT3–LT5
berlaku lintas profil: apa pun venunya, istilah asing tetap miring dan singkatan
tetap dijabarkan. LT8 menuntut sifat **permukaan** (tidak ada em dash atau
hyphen berspasi pada prosa, en dash hanya untuk rentang angka) sekaligus sifat
**statis** (anchor `\hyphenpenalty`/`\exhyphenpenalty` di preamble), sedangkan
LT9 menuntut sifat **permukaan** (pola `istilah (padanan Inggris)` pada
kemunculan prosa pertama); keduanya pun berlaku lintas profil.

---

## 4. Frame (Alur Drafting)

Menulis dengan tata letak dan tipografi yang terjaga mengikuti prosedur enam
langkah:

1. **Tulis istilah asing miring.** Setiap ungkapan pada registri `istilah_asing`
   ditulis `*istilah*` sejak draf pertama, bukan saat revisi
   (`assets/bahasa/kamus-id.yaml`).
2. **Jabarkan singkatan pada penyebutan pertama.** Tulis `SINGKATAN
   (Kepanjangan)` pada kemunculan prosa pertama (EYD Edisi V F.3).
3. **Daftarkan di `DAFTAR SINGKATAN`.** Tambahkan singkatan yang terpakai ke
   `content/skripsi/07-daftar-singkatan.md` (skripsi) atau blok `## Daftar
   Singkatan` (artikel).
4. **Jaga margin/spasi/font per profil.** Periksa Tabel 2.1: skripsi (2,5 cm /
   1,5 / indent 0,5 cm / serif / bab Romawi) atau artikel (2,5 cm / 1,15 /
   indent 0 / Times New Roman).
5. **Jalankan `make check-layout`.** Menjalankan
   `tools/validators/layout_typography.py` untuk memastikan LT1–LT9 terpenuhi
   secara mesin.
6. **Build.** Render naskah lewat `make skripsi` (PDF) atau `make artikel`
   (DOCX + PDF) dari `Makefile`.

Urutan kerja ini menempatkan kepatuhan tipografi di **hulu** (langkah 1–3) dan
verifikasi tata letak di **hilir** (langkah 4–5), sehingga revisi tidak menumpuk
pada tahap akhir.

---

## 5. Model Komponen (Anatomi Berkas Tata Letak)

Tata letak dan tipografi yang reprodusibel tersusun dari enam komponen
fungsional:

- **Berkas sumber (Markdown)** — `content/skripsi/*.md` dan
  `content/artikel/artikel-sinta.md`; tempat istilah asing ditulis miring dan
  singkatan dijabarkan.
- **Preamble LaTeX**: `templates/skripsi-preamble.tex` (margin, `\onehalfspacing`,
  indent, font serif, `\thechapter` → `\Roman`) dan
  `templates/artikel-preamble.tex` (`margin=2.5cm`, `\setstretch{1.15}`,
  anchor terpusat LT6); keduanya juga memuat `\hyphenpenalty=10000` dan
  `\exhyphenpenalty=10000` yang menekan hyphenasi otomatis (LT8); sumber
  parameter tata letak untuk keluaran PDF.
- ***Reference-docx***: `templates/journal-reference.docx`; sumber gaya
  Times New Roman untuk keluaran DOCX artikel.
- **Registri**: `assets/bahasa/kamus-id.yaml` pada kunci `istilah_asing`
  (kata miring), `singkatan` (kepanjangan + varian), `istilah_teknis` (istilah
  teknis lanjut yang wajib berglos Inggris, LT9), dan `tanda_pisah` (kaidah
  em dash/en dash/hyphen berspasi, LT8); sumber daftar yang diperiksa
  LT3–LT4, LT8, dan LT9.
- **Filter Pandoc** — `tools/pandoc_filters/sinta_layout.lua`; menata front
  matter, `ABSTRAK`/`ABSTRACT`, dan kepala bagian kanonik terpusat untuk
  artikel Sinta (LT6). `tools/pandoc_filters/bilingual.lua`; memiringkan blok
  bahasa kedua (`lang=en`) bila `bahasa.utama` berbeda (LT7).
- **Penegak** — `tools/validators/layout_typography.py` yang menegakkan
  LT1–LT9, dan **linter register** `tools/check-bahasa.sh` yang menjaga ragam
  bahasa ilmiah (EYD Edisi V) sebagai lapis pelengkap.

Sumber: `docs/skripsi-pedoman.md`; `docs/sinta-reference.md`;
`templates/skripsi-preamble.tex`; `templates/artikel-preamble.tex`;
`templates/journal-reference.docx`; `assets/bahasa/kamus-id.yaml`;
`tools/validators/layout_typography.py`; `tools/check-bahasa.sh`.

---

## 6. Pita dan Ambang

### (a) Ambang yang diperiksa mesin

|Parameter|Nilai|Tingkat|
|---|---|---|
|Margin (keempat sisi)|**2,5 cm**|fail (LT1/LT2)|
|Spasi baris|**1,5**|fail (LT1/LT2)|
|Indent baris pertama|**0,5 cm**|fail (LT1)|
|Anchor tata letak skripsi (LT1)|**8**|fail (LT1)|
|Anchor tata letak artikel (LT2)|**2**|fail (LT2)|
|Istilah asing terdaftar|**14**|fail (LT3)|
|Singkatan terdaftar|**4**|fail (LT4/LT5)|
|Filter Sinta (LT6)|**ada**|fail (LT6)|
|Anchor tata letak Sinta (LT6)|**4**|fail (LT6)|
|Target artikel Makefile berfilter (LT6)|**3**|fail (LT6)|
|Filter bilingual (LT7)|**ada**|fail (LT7)|
|Anchor bahasa utama (LT7)|**2**|fail (LT7)|
|Tanda pisah terlarang (LT8)|**0**|fail (LT8)|
|Anchor hipenasi (LT8)|**2**|fail (LT8)|
|Istilah teknis berglos (LT9)|**22**|fail (LT9)|

**Anchor LT1 = 8** dihitung dari `templates/skripsi-preamble.tex`: empat sisi
margin (`top=2.5cm`, `bottom=2.5cm`, `left=2.5cm`, `right=2.5cm`),
`\onehalfspacing`, `\setlength{\parindent}{0.5cm}`, `\setmainfont{Liberation
Serif}`, dan `\renewcommand{\thechapter}{\Roman{chapter}}`. **Anchor LT2 = 2**
dihitung dari `templates/artikel-preamble.tex`: `margin=2.5cm` dan
`\setstretch{1.15}`. **Anchor LT6 = 4** dihitung dari
`templates/artikel-preamble.tex`: `\centering`, `\titleformat{\section}`,
`\renewcommand{\figurename}{Gambar}`, dan `\renewcommand{\tablename}{Tabel}`;
**filter LT6 = ada** (`tools/pandoc_filters/sinta_layout.lua`) dan **target
artikel berfilter = 3** (`artikel`, `artikel-kyt`, `artikel-arai` pada
`Makefile`). **Istilah registri = 14** (`soft power`, `nation branding`,
`public diplomacy`, `vaccine diplomacy`, `health diplomacy`, `brand equity`,
`country of origin`, `country-of-origin`, `perceived quality`, `target market`,
`marketing mix`, `entry mode`, `full face`, `business matching`) dan **singkatan
registri = 4** (`ASEAN`, `FPA`, `ECE`, `SWOT`) dihitung dari
`assets/bahasa/kamus-id.yaml`. **Filter LT7 = ada**
(`tools/pandoc_filters/bilingual.lua`, disisipkan pada target artikel di
`Makefile`) dan **anchor bahasa utama LT7 = 2**: (1) filter bilingual hadir
dipakai pada `Makefile`, dan (2) kunci `bahasa.utama` ada di
`assets/bahasa/kamus-id.yaml` §`bahasa`. **Tanda pisah terlarang LT8 = 0**
(tidak ada em dash `—` atau hyphen ASCII berspasi ` - ` pada prosa; en dash `–`
hanya untuk rentang angka) dan **anchor hipenasi LT8 = 2**: `\hyphenpenalty=10000`
dan `\exhyphenpenalty=10000` pada kedua preamble
(`templates/skripsi-preamble.tex`, `templates/artikel-preamble.tex`).
**Istilah teknis berglos LT9 = 22** dihitung dari jumlah entri
`assets/bahasa/kamus-id.yaml` §`istilah_teknis` yang wajib diikuti padanan
Inggris pada kemunculan prosa pertama.

Ambang pada (a) dikalibrasi pada **8 berkas final** repositori ini
(`content/artikel/artikel-sinta.md`, `content/artikel/artikel-kyt.md`, dan enam
bab `content/skripsi/1[0-5]-*.md`) **beserta draf** di `content/drafts/` dan
**lulus**. Bila kelak muncul berkas sah yang melampaui ambang, konstanta di
`tools/validators/layout_typography.py` **dan** tabel (a) di dokumen ini harus
diubah **bersamaan** agar tetap selaras.

---

## 7. Matriks Kepatuhan per-Tingkat

|Aturan|Sinta 1–2|Sinta 3–6|Scopus|Skripsi HI|Proposal|
|---|---|---|---|---|---|
|LT1 — Tata letak skripsi|—|—|—|wajib|—|
|LT2 — Tata letak artikel/jurnal|wajib|wajib|unverified — confirm first|—|—|
|LT3 — Kata miring istilah asing|wajib|wajib|unverified — confirm first|wajib|wajib|
|LT4 — Penjabaran singkatan|wajib|wajib|unverified — confirm first|wajib|wajib|
|LT5 — DAFTAR SINGKATAN|wajib|wajib|unverified — confirm first|wajib|wajib|
|LT6 — Tata letak Sinta terpusat|wajib|wajib|unverified — confirm first|—|—|
|LT7 — Bahasa kedua (EN) miring|wajib|wajib|unverified — confirm first|wajib|wajib|
|LT8 — Tanda pisah (dash ban)|wajib|wajib|unverified — confirm first|wajib|wajib|
|LT9 — Istilah teknis dwibahasa|wajib|wajib|unverified — confirm first|wajib|wajib|

**LT1** hanya relevan untuk kolom **Skripsi HI** (profil skripsi TGD); pada
kolom lain ditandai `—` karena tidak ada penomoran bab dan tidak ada preamble
skripsi. **LT2** wajib untuk semua kolom jurnal/artikel (**Sinta 1–2**,
**Sinta 3–6**, **Scopus**); pada kolom **Skripsi HI** dan **Proposal** ditandai
`—` karena keduanya dirender dengan profil skripsi atau mengikuti panduan
proposal. **LT3–LT5** wajib untuk **semua** kolom: istilah asing yang miring dan
singkatan yang terjabar serta terdaftar adalah syarat kelayakan dasar, bukan
pilihan gaya. **LT6** wajib untuk kolom artikel Sinta (**Sinta 1–2**,
**Sinta 3–6**); pada **Skripsi HI** dan **Proposal** ditandai `—` karena tidak
dirender sebagai artikel Sinta. **LT7** wajib untuk **semua** kolom: setiap
blok bahasa kedua (`lang=en`) dimiringkan otomatis bila `bahasa.utama`
berbeda, sehingga naskah dwibahasa tetap terbaca sebagai dwibahasa di profil
mana pun. **LT8** dan **LT9** juga wajib untuk **semua** kolom: larangan em
dash/hyphen berspasi (en dash hanya untuk rentang angka) serta padanan Inggris
pada istilah teknis lanjut adalah syarat keterbacaan dasar, bukan pilihan gaya.
Kolom **Scopus** ditandai **`unverified — confirm first`**: status
indeksasi venue internasional tidak dapat diverifikasi dari korpus lokal,
konsisten dengan sikap `docs/subject-framework.md` §8 yang menandai klaim tak
terverifikasi secara eksplisit.

---

## 8. Daftar Periksa Do/Don't

|Lakukan (Do)|Hindari (Don't)|
|---|---|
|Pakai `*soft power*` (miring)|Tulis `soft power` polos di prosa|
|Jabarkan `ASEAN (Association of Southeast Asian Nations)` pada penyebutan pertama|Pakai singkatan telanjang tanpa kepanjangan|
|Daftarkan setiap singkatan di `DAFTAR SINGKATAN`|Pakai singkatan tanpa daftar|
|Jaga margin 2,5 cm keempat sisi|Margin tak seragam antarhalaman|
|Jaga spasi 1,5 dan indent 0,5 cm (skripsi)|Spasi/indent berubah antarbab|
|Pakai font serif per profil|Campur font antarbagian|

Istilah asing pada kolom "Lakukan" harus berasal dari registri `istilah_asing`,
dan singkatan dari registri `singkatan`, di `assets/bahasa/kamus-id.yaml` —
ungkapan di luar registri tidak diperiksa mesin dan berisiko tidak konsisten.

---

## 9. Rubrik Penilaian

Nilai **0–2** untuk setiap komponen LT1–LT9; skor maksimum **18**.

|Komponen|0|1|2|
|---|---|---|---|
|LT1 — Tata letak skripsi|Preamble tanpa anchor margin/spasi/indent/font/bab|Sebagian anchor hilang|Semua 8 anchor ada (margin, spasi, indent, font, bab Romawi)|
|LT2 — Tata letak artikel/jurnal|Preamble tanpa margin/spasi atau *reference-docx* hilang|Salah satu anchor hilang|`margin=2.5cm` + `\setstretch{1.15}` + *reference-docx* Times New Roman|
|LT3 — Kata miring istilah asing|Istilah registri ditulis polos|Sebagian istilah tidak miring|Semua istilah registri miring di prosa/heading|
|LT4 — Penjabaran singkatan|Singkatan telanjang pada penyebutan pertama|Sebagian singkatan tanpa kepanjangan|Semua singkatan berpola `SINGKATAN (Kepanjangan)`|
|LT5 — DAFTAR SINGKATAN|Tanpa daftar|Daftar tidak lengkap|Semua singkatan terpakai terdaftar|
|LT6 — Tata letak Sinta terpusat|Filter/anchor/preamble terpusat tidak ada|Sebagian anchor terpusat atau sebagian target artikel tak berfilter|Filter ada, 4 anchor terpusat ada, dan 3 target artikel berfilter|
|LT7 — Bahasa kedua (EN) miring|Blok `lang=en` tidak ada penanda/`bahasa.utama` tak dideklarasikan|Sebagian blok `lang=en` tanpa miring|Filter bilingual ada, `bahasa.utama` dideklarasikan, semua blok `lang=en` miring|
|LT8 — Tanda pisah (dash ban)|Em dash/hyphen berspasi dipakai di prosa atau anchor hipenasi hilang|Sebagian em dash/hyphen berspasi tersisa atau salah satu anchor hipenasi hilang|0 tanda pisah terlarang, en dash hanya untuk rentang, dan 2 anchor hipenasi ada|
|LT9 — Istilah teknis dwibahasa|Istilah teknis registri tanpa padanan Inggris pada kemunculan pertama|Sebagian istilah teknis tanpa padanan atau padanan asing tidak miring|Semua istilah `istilah_teknis` berglos `istilah (padanan)`; padanan asing miring|

**Tafsiran:** **18** = patuh penuh; **13–17** = revisi ringan; **8–12** = perlu
memperbaiki preamble/registri; **≤ 7** = tata letak dan tipografi belum layak.

---

## 10. Sumber

### 10.1 Berkas repositori

- `docs/skripsi-pedoman.md` — pedoman skripsi TGD (margin 2,5 cm, spasi 1,5, bab Romawi; DAFTAR SINGKATAN).
- `docs/sinta-reference.md` — anatomi artikel Sinta + *Technical spec table*.
- `docs/bahasa-artikel.md` — ragam bahasa ilmiah Indonesia (EYD Edisi V).
- `docs/diagram-framework.md` — gambar, tabel, caption, penomoran.
- `templates/skripsi-preamble.tex`: preamble skripsi (anchor LT1, `\hyphenpenalty`/`\exhyphenpenalty` LT8).
- `templates/artikel-preamble.tex`: preamble artikel (anchor LT2, `\hyphenpenalty`/`\exhyphenpenalty` LT8).
- `templates/journal-reference.docx` — *reference-docx* artikel (Times New Roman).
- `assets/bahasa/kamus-id.yaml`: registri `istilah_asing`, `singkatan`, `istilah_teknis` (LT9), dan `tanda_pisah` (LT8).
- `tools/validators/layout_typography.py`: penegak LT1–LT9.
- `tools/pandoc_filters/sinta_layout.lua` — filter tata letak Sinta terpusat (LT6).
- `tools/pandoc_filters/bilingual.lua` — filter blok bahasa kedua `lang=en` (LT7).
- `docs/sinta-corpus/s6-jutik.pdf` — contoh acuan tata letak artikel Sinta 1–6.
- `tools/gen_kamus.py` — pembangkit/pemeriksa registri kamus.
- `content/skripsi/07-daftar-singkatan.md` — `DAFTAR SINGKATAN` skripsi (LT5).

### 10.2 Literatur eksternal

- EYD Edisi V, *Huruf Miring* (butir G.3, catatan a).
  <https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-huruf/huruf-miring/>
- EYD Edisi V, *Singkatan dan Akronim* (butir F.3).
  <https://ejaan.kemendikdasmen.go.id/eyd/penulisan-kata/singkatan-dan-akronim/>
- APA Style. *Italics and Quotations — Italics*.
  <https://apastyle.apa.org/style-grammar-guidelines/italics-quotations/italics>
- Pandoc Lua filters. <https://pandoc.org/lua-filters.html>

### 10.3 Venue

Venue HI Indonesia dan Sinta — lihat `docs/argument-framework.md` Tabel 2.1.
