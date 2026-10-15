# Kerangka Sitasi & Catatan Kaki — Artikel Jurnal, Skripsi, dan Paper Akademik (Sinta, HI/IR, Skripsi, Proposal)

Kerangka ini menetapkan aturan **sitasi**, **daftar pustaka**, **catatan kaki**,
dan **kutipan langsung** agar setiap klaim dalam naskah dapat ditelusuri ke
sumbernya dan setiap naskah dapat dirender secara reprodusibel. Prinsipnya:
**sitasi harus dapat direproduksi dari markup** (setiap klaim ditandai `[@key]`
dan dirender mesin lewat `--citeproc`, bukan ditulis tangan sebagai
`(Author, year)` atau `[1]`) dan **ketertutupan sitasi ↔ daftar pustaka harus
dapat diperiksa mesin** (setiap kunci tersitasi wajib ada di bib, dan setiap
entri bib wajib tersitasi). Setiap klaim dalam dokumen ini bersumber pada
**berkas repositori ini** atau **literatur eksternal** yang terekam sesi ini —
tidak ada aturan tanpa sumber.

Kerangka ini **melengkapi** kerangka yang sudah ada dan tidak menggantikannya.
`docs/argument-framework.md` mengatur alur argumen dan kohesi paragraf;
`docs/layout-framework.md` mengatur tata letak dan tipografi; `docs/bahasa-artikel.md`
mengatur ragam bahasa ilmiah Indonesia (EYD Edisi V); `docs/fulltext-framework.md`
mengatur tangga akuisisi teks penuh; dan `docs/source-classification.md`
mengatur klasifikasi sumber primer/sekunder. Kelima kerangka itu menetapkan
**apa** yang harus ada dan **bagaimana** ia ditata; kerangka sitasi menetapkan
**bagaimana** klaim diikatkan ke sumber lewat markup `[@key]`, blok
`::: {#refs} :::`, catatan kaki penjelas, dan kutipan langsung bertanda petik
melengkung — sehingga sitasi itu reprodusibel dan dapat diperiksa mesin.

---

## 1. Definisi dan Fungsi

**Definisi.**

- **Sitasi** adalah penanda yang **menghubungkan sebuah klaim dengan sumbernya**.
  Di repositori ini sitasi ditulis sebagai markup pandoc `[@key]`, dengan `key`
  adalah kunci entri pada `assets/refs.bib`; build merender markup itu menjadi
  gaya APA *author-date* lewat `assets/csl/apa.csl`. APA Style menegaskan bahwa
  sitasi dalam teks menautkan pembaca ke entri daftar pustaka yang sesuai
  (<https://apastyle.apa.org/style-grammar-guidelines/citations>).
- **Catatan kaki** (*footnote*) adalah **keterangan penjelas** yang diletakkan di
  kaki halaman, ditulis `[^label]` pada prosa dengan definisi `[^label]: …`.
  Sesuai keputusan kerangka ini, catatan kaki di repositori ini **hanya untuk
  keterangan penjelas** — bukan sebagai gaya sitasi. (Gaya **catatan kaki sebagai
  sitasi**, *Chicago notes*, didokumentasikan sebagai varian korpus non-default,
  bukan gaya build.)
- **Daftar pustaka** adalah **daftar lengkap entri yang tersitasi**, dirender
  oleh blok `::: {#refs} :::` dari `assets/refs.bib`. Tautannya mengikuti CT7:
  URL hanya untuk berita/siaran pers/web, sedangkan karya akademik menampilkan
  DOI (bukan URL).
- **Kutipan langsung** adalah **petikan verbatim** dari sumber; ia diapit tanda
  petik melengkung `“…”` dan sitasinya **sebaiknya** menyertakan lokator
  (`[@key, hlm. N]`).

**Fungsi kerangka.** Pertama, **ketertutupan sitasi ↔ daftar pustaka dapat
diperiksa mesin**: tidak boleh ada kunci tersitasi yang tak punya entri bib,
dan tidak boleh ada entri bib yang tak pernah disitasi. Kedua, **sitasi
reprodusibel dari markup `[@key]`**: gaya keluaran ditentukan CSL, bukan
disunting tangan per kalimat, sehingga mengubah gaya cukup mengubah satu berkas
CSL. Ketiga, **kutipan langsung dan catatan kaki terikat pada kaidah EYD**:
petikan langsung memakai tanda petik melengkung (EYD Edisi V, butir tanda petik
J — <https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-tanda-baca/tanda-petik/>),
dan catatan kaki dibatasi pada keterangan penjelas.

---

## 2. Lanskap Gaya Sitasi dan Anatomi Markup

Sitasi tidak berdiri di ruang hampa: ia dibentuk oleh **venue** dan **korpus**
tempat naskah dikirim. Tabel 2.1 memetakan gaya sitasi dan catatan kaki (default
build repo vs varian korpus); Tabel 2.2 merangkum anatomi markup sitasi.

### Tabel 2.1 — Gaya sitasi & catatan kaki

|Aspek|Default build repo|Varian korpus|Sumber|
|---|---|---|---|
|Gaya dalam teks|APA *name-year* via `[@key]`|numerik kurung `[1]` (Sinta 23/29; IR 6/43)|`docs/kamus-riset-korpus.md` §8; `docs/kamus-riset-korpus-hi.md` §4|
|Daftar pustaka|APA alfabetis via `::: {#refs} :::`|daftar bernomor|`docs/kamus-riset-korpus.md` §8; `docs/kamus-riset-korpus-hi.md` §4|
|Catatan kaki|penjelas saja (`[^label]:`) |catatan akhir bernomor (`hi-ivran-mask-diplomacy`)|scout sesi ini; `docs/kamus-riset-korpus-hi.md` §4|
|Kutipan langsung|`“…”` + lokator `[@key, hlm. N]`|—|EYD Edisi V tanda petik J; APA in-text|

Korpus Sinta memuat gaya **numerik kurung** pada 23/29 berkas dan **APA
*name-year*** pada 6/29 berkas; korpus HI/IR memuat **APA *name-year*** pada
34/43 berkas, **numerik kurung** pada 6/43 berkas, dan 3 berkas tanpa sitasi.
Build artikel/skripsi repo ini memakai **APA *name-year*** — **gaya numerik
adalah varian korpus, bukan gaya build**. Satu berkas HI
(`hi-ivran-mask-diplomacy`) memakai catatan akhir bernomor; catatan kaki sebagai
**gaya sitasi** tidak tercatat di korpus mana pun dan karena itu didokumentasikan
sebagai varian non-default.

### Tabel 2.2 — Anatomi markup sitasi

|Markup|Arti|Contoh|
|---|---|---|
|`[@key]`|sitasi tunggal|`[@hall2013struggle]`|
|`[@a; @b]`|beberapa sumber dalam satu kurung|`[@ratnawati2020analisis; @wicaksono2017strategi]`|
|`[@key, hlm. 12]`|sitasi dengan lokator (kutipan langsung)|`[@hall2013struggle, hlm. 12]`|
|`[^1]` + `[^1]: …`|catatan kaki penjelas (rujukan + definisi)|`[^1]` … `[^1]: Lihat Bab II untuk uraian lengkap.`|
|`::: {#refs} :::`|blok daftar pustaka yang dirender|`::: {#refs}` … `:::`|

Anatomi di atas menentukan **bagaimana** klaim diikat ke sumber; aturan CT1–CT7
di Bagian 3 menentukan **apa** yang wajib dipatuhi agar ikatan itu reprodusibel
dan dapat diperiksa mesin.

---

## 3. Aturan Absolut (CT1–CT7)

Ketujuh aturan berikut bersifat **absolut**: naskah yang melanggarnya belum layak
disebut memiliki sitasi yang reprodusibel. Setiap butir menyebut definisi,
penegak, dan sumbernya.

1. **CT1 — Gaya sitasi dalam teks.** Setiap sitasi memakai markup pandoc
   `[@key]`; build merender APA *author-date* via `assets/csl/apa.csl`. Sitasi
   parentetik `(Author, year)` atau numerik `[1]` yang **ditulis tangan** di
   prosa **dilarang** karena melewati citeproc. Penegak:
   `tools/validators/citation_framework.py`. Sumber:
   <https://apastyle.apa.org/style-grammar-guidelines/citations>;
   <https://pandoc.org/MANUAL.html#citations>.
2. **CT2 — Ketertutupan sitasi ↔ daftar pustaka.** Setiap kunci dalam setiap
   `[@…]` (termasuk kurung **multi-kunci** `[@a; @b]`) **wajib** ada di
   `assets/refs.bib`, dan setiap entri bib **wajib** disitasi. Penegak:
   `tools/validators/citation_framework.py` (validator ini **sadar multi-kunci**;
   `tools/validators/papers.py` tetap berjalan sebagai lapis pertama). Sumber:
   `docs/bab1-framework.md` C4.
3. **CT3 — Blok daftar pustaka dirender.** Daftar pustaka dirender oleh blok
   `::: {#refs} :::` — `content/skripsi/90-daftar-pustaka.md` untuk skripsi;
   di dalam berkas untuk tiap `content/artikel/*.md`. Penegak:
   `tools/validators/citation_framework.py`. Sumber:
   `content/skripsi/90-daftar-pustaka.md`; `content/artikel/artikel-sinta.md`;
   `content/artikel/artikel-kyt.md`.
4. **CT4 — Catatan kaki penjelas.** Catatan kaki `[^label]`/`[^label]:` hanya
   untuk keterangan penjelas; **wajib** punya definisi; **tidak boleh** memuat
   sitasi `[@key]` (itu catatan-kaki-sitasi, varian non-default). Penegak:
   `tools/validators/citation_framework.py`. Sumber: `docs/bahasa-artikel.md`;
   <https://pandoc.org/MANUAL.html#footnotes>.
5. **CT5 — Abstrak bersih.** Blok abstrak (`::: {custom-style="Abstract"} … :::`)
   **tidak** memuat sitasi **maupun** catatan kaki. Penegak:
   `tools/validators/citation_framework.py` (memperluas larangan sitasi di
   `tools/validators/papers.py`). Sumber: `docs/abstrak-framework.md` §6.3.
6. **CT6 — Kutipan langsung & lokator.** Petikan langsung memakai tanda petik
   melengkung `“…”` (EYD tanda petik J) dan sitasi kutipan langsung
   **sebaiknya** menyertakan lokator (`[@key, hlm. N]`). Tanda petik lurus `"…"`
   di prosa **dilarang**. Penegak: `tools/validators/citation_framework.py`
   (lokator = `warn`). Sumber: EYD tanda petik J; APA in-text;
   <https://pandoc.org/MANUAL.html#citations>.
7. **CT7 — Tautan daftar pustaka.** URL hanya untuk **berita/siaran pers/web**;
   **karya akademik menampilkan DOI, bukan URL**. Secara mekanis: (a) sebuah
   entri **tidak boleh** memuat `doi` **dan** `url` sekaligus; (b) entri
   **bukti** (entri yang `note`-nya memuat kanal `Berita`/`Siaran pers`/
   `Artikel`/`Web`) **wajib** memuat `url`. Penegak:
   `tools/validators/citation_framework.py`. Perilaku keluaran diatur makro CSL
   `source-DOI-URL` pada `assets/csl/apa.csl`: bila `DOI` ada, cetak
   `https://doi.org/<DOI>`; bila tidak, cetak `URL` **hanya** untuk tipe web
   (`webpage`/`post-weblog`/`post`) sehingga entri akademik non-web tidak
   mencetak URL. Sumber: APA Style 9.34–9.36; `assets/csl/apa.csl`.

CT1, CT2, dan CT6 menuntut sifat **permukaan** pada prosa (markup sitasi, kunci
yang tertutup, tanda petik) sehingga dapat ditegakkan otomatis; CT3–CT5 dan CT7
menuntut sifat **statis/struktural** (keberadaan blok `{#refs}`, kebijakan
catatan kaki, kebersihan abstrak, higiene bidang `doi`/`url`/`note`) sehingga
dapat diperiksa dengan pencocokan pola berkas.
Karena itu ketujuh aturan berlaku lintas venue: apa pun venunya, sitasi tetap
bermarkup `[@key]`, tertutup ke daftar pustaka, dan kutipan langsung tetap
bertanda petik melengkung.

---

## 4. Frame (Alur Drafting)

Menulis dengan sitasi yang terjaga mengikuti prosedur enam langkah:

1. **Tandai klaim dengan `[@key]`.** Setiap klaim yang bersumber ditandai markup
   pandoc `[@key]` sejak draf pertama — bukan parentetik `(Author, year)` atau
   numerik `[1]` manual.
2. **Kutipan langsung: `“…”` + lokator.** Untuk petikan verbatim, apit dengan
   tanda petik melengkung `“…”` (EYD tanda petik J) dan sertakan lokator
   `[@key, hlm. N]`.
3. **Tambahkan catatan kaki penjelas bila perlu.** Tulis `[^label]` +
   `[^label]: …` **tanpa** sitasi `[@key]` di dalamnya (catatan kaki penjelas,
   bukan catatan-kaki-sitasi).
4. **Pastikan entri bib ada & tersitasi.** Setiap kunci yang dipakai wajib ada di
   `assets/refs.bib`, dan setiap entri bib wajib tersitasi (CT2).
5. **Pastikan blok `::: {#refs} :::` ada.** Daftar pustaka dirender lewat blok
   ini — di `content/skripsi/90-daftar-pustaka.md` untuk skripsi, di dalam
   berkas untuk tiap `content/artikel/*.md`.
6. **Jalankan `make check-citations`.** Perintah ini menjalankan
   `tools/validators/citation_framework.py` untuk memastikan CT1–CT7 terpenuhi
   secara mesin. Untuk tautan, ingat CT7: berita/siaran pers/web memakai `url`;
   karya akademik memakai `doi` (tanpa `url`).

Urutan kerja ini menempatkan kepatuhan sitasi di **hulu** (langkah 1–3) dan
verifikasi ketertutupan di **hilir** (langkah 4–6), sehingga revisi tidak
menumpuk pada tahap akhir.

---

## 5. Model Komponen (Anatomi Pipa Sitasi)

Pipa sitasi yang reprodusibel tersusun dari tujuh komponen fungsional:

- **Sumber markup** — `content/artikel/*.md` dan `content/skripsi/*.md`; tempat
  klaim ditandai `[@key]`, catatan kaki ditulis `[^label]`, dan kutipan langsung
  diapit `“…”`.
- **Basis data** — `assets/refs.bib`; himpunan entri yang boleh disitasi.
- **Gaya CSL** — `assets/csl/apa.csl`; menentukan gaya keluaran APA
  *author-date*. Makro `source-DOI-URL` mencetak `https://doi.org/<DOI>` bila
  `DOI` ada, dan mencetak `URL` **hanya** untuk tipe web
  (`webpage`/`post-weblog`/`post`) — inilah penegak CT7 pada sisi keluaran.
- **Blok keluaran** — `::: {#refs} :::`; tempat daftar pustaka dirender.
- **Registri** — `assets/bahasa/kamus-id.yaml` pada kunci `kutipan`,
  `daftar_pustaka`, `catatan_kaki`, dan `kutipan_langsung`; sumber kebijakan
  sitasi yang terdokumentasi.
- **Penegak** — `tools/validators/citation_framework.py` (CT1–CT7),
  `tools/validators/papers.py` (ketertutupan lapis pertama), dan
  `tools/validators/doi.py` (tautan/DOI).
- **Pipa build** — `Makefile` dengan `--citeproc` (target `skripsi`, `artikel`,
  `artikel-kyt`) yang merender sitasi dan blok `{#refs}`.

Sumber: `assets/refs.bib`; `assets/csl/apa.csl`; `assets/bahasa/kamus-id.yaml`;
`tools/validators/citation_framework.py`; `tools/validators/papers.py`;
`tools/validators/doi.py`; `Makefile`.

---

## 6. Pita dan Ambang

### (a) Ambang yang diperiksa mesin

|Parameter|Nilai|Tingkat|
|---|---|---|
|Markup sitasi|`[@key]`|fail (CT1)|
|Sitasi parentetik/numerik ditulis tangan|**0**|fail (CT1)|
|Kunci pertama kurung multi-kunci tertangkap|**wajib**|fail (CT2)|
|Selisih sitasi ↔ entri bib|**0**|fail (CT2)|
|Blok `::: {#refs} :::`|**ada**|fail (CT3)|
|Catatan kaki memuat sitasi|**0**|fail (CT4)|
|Catatan kaki tanpa definisi|**0**|fail (CT4)|
|Sitasi di abstrak|**0**|fail (CT5)|
|Catatan kaki di abstrak|**0**|fail (CT5)|
|Tanda petik lurus di prosa|**0**|fail (CT6)|
|Lokator pada kutipan langsung|disarankan|warn (CT6)|
|Entri memuat `doi` **dan** `url` sekaligus|**0**|fail (CT7)|
|Entri bukti (note berkanal) tanpa `url`|**0**|fail (CT7)|
|URL pada entri akademik non-web|**0**|fail (CT7; makro `source-DOI-URL`)|

### (b) Pita dari korpus

|Aspek|Pita|Sumber|
|---|---|---|
|Jumlah entri daftar pustaka (Sinta)|12–78|`docs/kamus-riset-korpus.md` §8|
|Jumlah entri daftar pustaka (HI/IR)|5–76|`docs/kamus-riset-korpus-hi.md` §4|

Ambang pada (a) dikalibrasi pada **8 berkas final** repositori ini
(`content/artikel/artikel-sinta.md`, `content/artikel/artikel-kyt.md`, dan enam
bab `content/skripsi/`) **beserta draf** di `content/drafts/`, dan **lulus**.
Bila kelak muncul aturan sitasi baru, tambahkan kunci ke
`assets/bahasa/kamus-id.yaml` **dan** perbarui tabel (a) di dokumen ini
**bersamaan** agar tetap selaras.

---

## 7. Matriks Kepatuhan per-Tingkat

|Aturan|Sinta 1–2|Sinta 3–6|Scopus|Skripsi HI|Proposal|
|---|---|---|---|---|---|
|CT1 — Gaya sitasi dalam teks|wajib|wajib|unverified — confirm first|wajib|wajib|
|CT2 — Ketertutupan sitasi ↔ daftar pustaka|wajib|wajib|unverified — confirm first|wajib|wajib|
|CT3 — Blok daftar pustaka dirender|wajib|wajib|unverified — confirm first|wajib|wajib|
|CT4 — Catatan kaki penjelas|wajib|wajib|unverified — confirm first|wajib|wajib|
|CT5 — Abstrak bersih|wajib|wajib|unverified — confirm first|wajib|wajib|
|CT6 — Kutipan langsung & lokator|wajib|wajib|unverified — confirm first|wajib|wajib|
|CT7 — Tautan daftar pustaka (DOI/URL)|wajib|wajib|unverified — confirm first|wajib|wajib|

CT1–CT7 **wajib** untuk semua kolom: sitasi yang reprodusibel dan tertutup
adalah syarat kelayakan dasar, bukan pilihan gaya. Kolom **Scopus** ditandai
**`unverified — confirm first`**: status indeksasi venue internasional tidak
dapat diverifikasi dari korpus lokal, konsisten dengan sikap
`docs/subject-framework.md` §8 yang menandai klaim tak terverifikasi secara
eksplisit.

---

## 8. Daftar Periksa Do/Don't

|Lakukan (Do)|Hindari (Don't)|
|---|---|
|Tandai klaim dengan `[@key]`|Tulis `(Author, year)` manual di prosa|
|Pakai `[@a; @b]` untuk beberapa sumber|Tulis kunci yang tak punya entri di `assets/refs.bib`|
|Pakai catatan kaki penjelas `[^label]: …` tanpa sitasi|Isi catatan kaki dengan `[@key]` (catatan-kaki-sitasi)|
|Pakai `“…”` + lokator untuk kutipan langsung|Pakai tanda petik lurus `"…"` di prosa|
|Rendel daftar pustaka via `::: {#refs} :::`|Menempel daftar pustaka sebagai teks mati|

Kunci pada kolom "Lakukan" harus berasal dari `assets/refs.bib`, dan markup
harus konsisten dengan `assets/csl/apa.csl` di `Makefile` — kunci di luar bib
tidak dapat dirender dan berisiko gagal CT2.

---

## 9. Rubrik Penilaian

Nilai **0–2** untuk setiap komponen CT1–CT7; skor maksimum **14**.

|Komponen|0|1|2|
|---|---|---|---|
|CT1 — Gaya sitasi dalam teks|Banyak sitasi parentetik/numerik manual|Sebagian sitasi tidak bermarkup `[@key]`|Semua sitasi memakai `[@key]`|
|CT2 — Ketertutupan sitasi ↔ daftar pustaka|Ada kunci tanpa entri bib atau entri bib tanpa sitasi|Sebagian tidak tertutup|Nol selisih sitasi ↔ entri bib|
|CT3 — Blok daftar pustaka dirender|Tanpa blok `::: {#refs} :::`|Sebagian berkas tanpa blok|Setiap berkas relevan punya blok `{#refs}`|
|CT4 — Catatan kaki penjelas|Ada catatan kaki tanpa definisi atau memuat sitasi|Sebagian catatan kaki menyimpang|Semua catatan kaki penjelas, terdefinisi, tanpa sitasi|
|CT5 — Abstrak bersih|Abstrak memuat sitasi atau catatan kaki|—|Abstrak tanpa sitasi dan tanpa catatan kaki|
|CT6 — Kutipan langsung & lokator|Ada tanda petik lurus di prosa|Tanda petik melengkung tanpa lokator|Semua kutipan langsung `“…”` + lokator|
|CT7 — Tautan daftar pustaka|Entri `doi`+`url` sekaligus, bukti tanpa `url`, atau URL pada akademik|Sebagian entri menyimpang|DOI untuk akademik, URL hanya untuk berita/web|

**Tafsiran:** **14** = patuh penuh; **11–13** = revisi ringan; **6–10** = perlu
memperbaiki markup/kebijakan sitasi; **≤ 5** = sitasi belum layak.

---

## 10. Sumber

### 10.1 Berkas repositori

- `docs/argument-framework.md` — alur argumen & kohesi paragraf (K1–K5; Tabel 2.1 venue).
- `docs/layout-framework.md` — tata letak & tipografi (LT1–LT5).
- `docs/bahasa-artikel.md` — ragam bahasa ilmiah Indonesia (EYD Edisi V).
- `docs/abstrak-framework.md` — anatomi abstrak (§6.3 larangan).
- `docs/bab1-framework.md` — gerak Pendahuluan (C4 ketertutupan sitasi).
- `docs/kamus-riset-korpus.md` — gaya sitasi korpus Sinta (§8).
- `docs/kamus-riset-korpus-hi.md` — gaya sitasi korpus HI/IR (§4).
- `assets/refs.bib` — basis data entri sitasi.
- `assets/csl/apa.csl` — gaya CSL keluaran APA; makro `source-DOI-URL`
  (DOI-first, URL hanya untuk tipe web) menegakkan CT7 pada sisi keluaran.
- `tools/validators/citation_framework.py` — penegak CT1–CT7.
- `tools/validators/papers.py` — penegak ketertutupan sitasi lapis pertama.
- `tools/validators/doi.py` — penegak tautan/DOI.
- `assets/bahasa/kamus-id.yaml` — registri `kutipan`, `daftar_pustaka`, `catatan_kaki`, `kutipan_langsung`.
- `content/skripsi/90-daftar-pustaka.md` — blok `::: {#refs} :::` skripsi.

### 10.2 Literatur eksternal

- APA Style. *In-Text Citations*.
  <https://apastyle.apa.org/style-grammar-guidelines/citations>
- EYD Edisi V, *Tanda Petik* (butir J).
  <https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-tanda-baca/tanda-petik/>
- Pandoc. *Citations* dan *Footnotes*.
  <https://pandoc.org/MANUAL.html#citations>

### 10.3 Venue

Venue HI Indonesia dan Sinta — lihat `docs/argument-framework.md` Tabel 2.1.
