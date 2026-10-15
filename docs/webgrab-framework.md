# Kerangka Pengambilan Web (Web Grab) — Akuisisi Bertahap dan Provenans Berbasis Bukti

Kerangka ini menetapkan aturan operasional untuk **memperoleh isi sebuah
halaman web** (HTML, JSON, atau PDF) secara **dapat direproduksi** dan
**tercatat provenansnya**, sebelum isi itu dipakai sebagai bahan riset,
triangulasi, atau kutipan. Kerangka diturunkan dari sumber yang dapat diaudit:
**berkas repositori ini** (skrip `tools/webgrab.py`, target `make`, validator
`web_corpus`, dan korpus web) serta **praktik pengambilan web yang lazim**
(curl untuk HTTP mentah, peramban tanpa kepala untuk halaman yang dirender
JavaScript). Tidak ada klaim tanpa sumber.

Kerangka ini **melengkapi** kerangka yang sudah ada dan tidak menggantikannya.
`docs/fulltext-framework.md` memaksa **teks utuh** tiap karya akademik yang
dipakai sebagai dasar simpulan (aturan F1–F8); `docs/subject-framework.md`
memaksa **keluasan** sapuan materi sekunder tentang sebuah subjek (aturan
S1–S8). Pengambilan web menangani **mekanisme akuisisi** atas halaman web yang
menjadi sumber kedua kerangka tersebut: sapuan subjek menemukan kandidat URL,
teks utuh menuntut berkas yang benar-benar diperoleh, dan kerangka ini
menetapkan **bagaimana** halaman itu diambil, diekstrak, dan dicatat.

Landasan operasionalnya sederhana dan dapat diperiksa. **Pertama**, sebagian
besar halaman dapat diambil dengan **HTTP mentah** (`curl`) tanpa peramban;
memulai dengan peramban tanpa kepala membuang waktu, memori, dan kredibilitas
provenans. **Kedua**, sebagian halaman adalah **aplikasi satu-halaman**
(*single-page application*, SPA) yang bodinya kosong sampai JavaScript
dijalankan; halaman seperti itu baru bermakna setelah **eskalasi** ke peramban
tanpa kepala. Karena itu aturan WG1–WG8 di bawah bersifat mengikat: mulailah
dari `curl`, deteksi kekacauan, eskalasi **berurutan**, dan catat provenans
setiap pengambilan tanpa mengarang.

---

## 1. Definisi dan Fungsi

**Definisi.** *Pengambilan web (web grab)* adalah proses **memperoleh isi sebuah
URL** secara terprogram, menyimpannya sebagai **badan mentah** (*raw body*) dan
**teks bersih** (*clean text*), serta mencatat **provenansnya**. Badan mentah
adalah respons apa adanya (HTML/JSON/PDF); teks bersih adalah representasi
prosais yang diekstrak darinya. Pengambilan berbeda secara kategoris dari
**penemuan** (*discovery*), yaitu pencarian kandidat URL lewat mesin pencari
yang tidak dengan sendirinya menghasilkan isi halaman.

**Perbedaan `curl` dan peramban tanpa kepala.**

| Aspek | Rung `curl` | Rung peramban tanpa kepala |
|-------|-------------|----------------------------|
| Mesin | HTTP mentah (permintaan + respons) | Peramban penuh (puppeteer/chrome) dijalankan tanpa tampilan |
| Isi yang terlihat | HTML **sebagaimana dikirim server** | DOM **setelah JavaScript dijalankan** |
| Biaya | Ringan, cepat, hemat memori | Berat, lambat, butuh peramban terpasang |
| Halaman SPA | Bodinya kosong/kacau | Bodinya terisi |
| Posisi dalam tangga | Rung **pertama** (wajib) | Rung **eskalasi** (bila kacau) |
| Provenans `mode` | `curl` | `headless-puppeteer` / `headless-chrome` |

**Mengapa `curl` lebih dulu.** Memulai setiap pengambilan dengan `curl` bersifat
mengikat (WG1) karena tiga alasan. **Pertama**, mayoritas halaman yang
dibutuhkan untuk riset adalah dokumen HTML biasa yang sudah lengkap pada respons
pertama; menyalakan peramban untuk halaman seperti itu hanya menambah biaya.
**Kedua**, badan mentah dari `curl` adalah **bukti yang paling jujur** tentang
apa yang benar-benar dikirim server, termasuk kode status 4xx/5xx yang justru
perlu dipertahankan (WG1). **Ketiga**, peramban tanpa kepala memerlukan
perangkat lunak tambahan yang tidak selalu tersedia; menjadikannya pilihan
pertama membuat pipeline rapuh, padahal kerangka ini menuntut hasil yang dapat
direproduksi.

**Fungsi kerangka.** Kerangka ini menjadikan kebiasaan di atas sebagai aturan
yang dapat **diperiksa mesin**: setiap pengambilan menempuh tangga §3 secara
berurutan, halaman kacau dideteksi dengan kriteria eksplisit §4, dan setiap
pengambilan mencatat satu baris provenans pada `docs/web-corpus/manifest.tsv`
(§6) yang konsistensinya ditegakkan validator `web_corpus`.

---

## 2. Aturan Absolut (WG1–WG8)

1. **WG1 — curl dulu.** Setiap pengambilan dimulai dengan rung `curl` (HTTP
   mentah, badan dipertahankan pada 4xx/5xx); headless **bukan** pilihan
   pertama kecuali `--force-headless`.
2. **WG2 — deteksi kacau.** Halaman HTML dinyatakan **kacau** bila salah satu:
   (a) penanda SPA (`id="root"`, `__NEXT_DATA__`, `__NUXT__`, `data-reactroot`,
   `ng-version`, …); (b) teks "enable JavaScript"; (c) ≥ 3 `<script>` dan
   < 200 karakter terlihat; (d) < 50 karakter terlihat dan > 2000 byte mentah.
3. **WG3 — tangga eskalasi.** `curl` → `headless-puppeteer` →
   `headless-chrome`; berhenti pada rung pertama yang menghasilkan badan
   tidak-kacau. Bila headless tak tersedia, catat `chaotic-unresolved` (jangan
   mengarang).
4. **WG4 — ekstraksi.** HTML → teks polos via `pandoc -f html -t plain`;
   non-HTML (pdf/json) diarsipkan apa adanya (pdf → `pdftotext` bila ada).
5. **WG5 — provenans.** Setiap pengambilan mencatat
   `slug,url,accessed,mode,status,http,bytes,sha256,text_chars` di
   `manifest.tsv`; dilarang mengarang.
6. **WG6 — persistensi.** Badan mentah + teks di `docs/web-corpus/` yang
   di-*git-ignore*; hanya `manifest.tsv`/`MANIFEST.md` yang terlacak.
7. **WG7 — penemuan (discovery).** Kandidat URL berasal dari
   `search.py … --json --no-save` (pengambilan nyata), bukan diketik tangan;
   de-duplikasi berdasarkan URL.
8. **WG8 — integrasi.** `webgrab.py discover --fetch` merangkai penemuan →
   pengambilan; setiap URL dicatat **sekali** (de-dup tak peka huruf
   besar/kecil).

**Perintah persis.**

```
python3 tools/webgrab.py fetch <url>
python3 tools/webgrab.py discover "<q>" --fetch
make webgrab URL=<url>
make webdiscover Q="<q>"
python3 tools/validate.py web_corpus
```

---

## 3. Tangga Pengambilan (curl → headless-puppeteer → headless-chrome)

Tangga ditelusuri **berurutan**; pengambilan berhenti pada **rung pertama yang
menghasilkan badan tidak-kacau** (§4). Rung 1 selalu dijalankan lebih dulu
(WG1); rung 2 dan 3 hanya dijalankan bila badan dari rung sebelumnya dinyatakan
kacau (WG3).

| Rung | Mode | Alat | Kondisi berhenti | Kondisi lanjut |
|------|------|------|------------------|----------------|
| 1 | `curl` | HTTP mentah (permintaan + respons); badan dipertahankan pada 4xx/5xx | Badan **tidak-kacau** (§4) | Badan kacau → rung 2 |
| 2 | `headless-puppeteer` | peramban tanpa kepala lewat puppeteer | Badan **tidak-kacau** (§4) | Puppeteer tak tersedia atau badan tetap kacau → rung 3 |
| 3 | `headless-chrome` | peramban tanpa kepala lewat chrome langsung | Badan **tidak-kacau** (§4) | Chrome tak tersedia → status `chaotic-unresolved` |

**Catatan operasional.**

- **Badan dipertahankan pada 4xx/5xx.** Rung `curl` **tidak** membuang badan
  respons hanya karena kode status galat; kode status dicatat apa adanya pada
  kolom `http`, dan badan disimpan. Ini menjaga bukti tentang apa yang benar-benar
  dikirim server (WG1).
- **Berhenti pada rung pertama yang bersih.** Begitu sebuah rung menghasilkan
  badan tidak-kacau, rung berikutnya **tidak** dijalankan; kolom `mode`
  merekam rung yang menang, sehingga provenans mencerminkan cara isi diperoleh.
- **Headless tak tersedia bukan alasan mengarang.** Bila peramban tanpa kepala
  tidak terpasang dan badan tetap kacau, pengambilan dicatat dengan status
  `chaotic-unresolved`; isi halaman **tidak** boleh ditebak atau dikarang (WG3).
- **`--force-headless`.** Opsi ini melompati rung 1 dan langsung memulai dari
  rung 2; dipakai hanya bila diketahui lebih dahulu bahwa halaman bersangkutan
  memerlukan JavaScript, dan **bukan** pilihan bawaan (WG1).

---

## 4. Deteksi Halaman Kacau (chaotic)

Sebuah halaman HTML dinyatakan **kacau** bila **salah satu** sinyal berikut
terpenuhi (WG2). Deteksi ini dijalankan atas badan rung saat itu; keputusan
kacau/tidak-kacau menentukan apakah pengambilan berhenti atau naik ke rung
berikutnya (§3).

| Sinyal | Kriteria | Makna |
|--------|----------|-------|
| (a) Penanda SPA | `id="root"`, `__NEXT_DATA__`, `__NUXT__`, `data-reactroot`, `ng-version`, … | Kerangka JavaScript menandakan bodi diisi setelah render |
| (b) Pesan JavaScript | memuat teks "enable JavaScript" | Halaman meminta JavaScript sebelum menampilkan isi |
| (c) Skrip tanpa isi | ≥ 3 `<script>` **dan** < 200 karakter terlihat | Banyak skrip, sedikit teks tampak → isi dirender klien |
| (d) Bodi besar tanpa isi | < 50 karakter terlihat **dan** > 2000 byte mentah | Badan besar namun nyaris tanpa teks tampak |

**Cara membaca sinyal.** Sinyal (a) dan (b) bersifat **penanda eksplisit**: satu
kemunculan saja sudah cukup untuk menyatakan kacau. Sinyal (c) dan (d) bersifat
**ambang**: keduanya memerlukan pemenuhan **dua** syarat sekaligus (jumlah skrip
**dan** sedikit teks; bodi besar **dan** nyaris tanpa teks), sehingga halaman
sederhana yang panjangnya wajar tidak salah ditandai. Karakter terlihat adalah
teks yang tersisa setelah tag dan skrip dibuang, yaitu teks yang benar-benar
dapat dibaca.

**Ambang yang dipakai.** `< 200` karakter terlihat bersama `≥ 3` `<script>`
(sinyal c); `< 50` karakter terlihat bersama `> 2000` byte mentah (sinyal d).
Bila **tidak satu pun** sinyal terpenuhi, badan dinyatakan **tidak-kacau** dan
pengambilan berhenti pada rung itu (§3).

---

## 5. Scope

**Cakupan (berlaku).**

- Halaman **HTML** biasa (dokumen, artikel, siaran pers, halaman lembaga).
- Halaman **aplikasi satu-halaman** yang memerlukan eskalasi ke peramban tanpa
  kepala.
- Berkas **non-HTML** yang dapat diambil lewat URL: JSON (API) dan PDF.

**Di luar cakupan (tidak berlaku).**

- Halaman yang menuntut **otentikasi**, captcha, atau interaksi manusia:
  kerangka ini tidak melewati dinding seperti itu dan tidak mengarang isi.
- Rekaman **non-prosais** murni: data tabular, basis data terstruktur, atau
  himpunan data numerik yang tidak memiliki narasi.
- Penemuan kandidat URL (itu ranah **penemuan**, WG7) — kerangka ini menangani
  **pengambilan** isi, bukan pencariannya.

**Kapan aturan berlaku.**

- Aturan berlaku ketika isi sebuah halaman web dipakai untuk **riset atau
  penulisan** (menyusun argumen, menetapkan konteks, atau mengutip).
- Aturan **tidak** berlaku ketika tindakan hanya sebatas **menyimpan tautan**
  atau menandai kandidat untuk ditelaah kemudian; penyimpanan tautan belum
  merupakan klaim tentang isi halaman dan tidak boleh berubah menjadi klaim
  tanpa pengambilan yang benar-benar tercatat.

---

## 6. Model Komponen

**Kolom manifest (`docs/web-corpus/manifest.tsv`).** Setiap pengambilan
menghasilkan **tepat satu baris** berisi sembilan kolom berikut (WG5); urutan
kolom bersifat tetap dan dibaca validator `web_corpus`.

| Kolom | Makna |
|-------|-------|
| `slug` | Pengenal ringkas halaman (huruf kecil, angka, tanda hubung) |
| `url` | URL yang benar-benar diambil |
| `accessed` | Tanggal akses (`YYYY-MM-DD`) |
| `mode` | Rung yang menang: `curl`, `headless-puppeteer`, atau `headless-chrome` |
| `status` | Hasil pengambilan: `ok` atau penanda galat (mis. `chaotic-unresolved`) |
| `http` | Kode status HTTP apa adanya (badan dipertahankan pada 4xx/5xx) |
| `bytes` | Ukuran badan mentah dalam byte |
| `sha256` | Sidik jari SHA-256 badan mentah (64 digit heksadesimal) |
| `text_chars` | Jumlah karakter teks bersih hasil ekstraksi |

**Nilai `mode` dan `status`.** Kolom `mode` merekam rung tangga §3 yang
menghasilkan badan tidak-kacau; kolom `status` merekam hasilnya. Varian yang
dipakai kerangka ini:

| Medan | Nilai | Makna |
|-------|-------|-------|
| `mode` | `curl` | Diperoleh pada rung 1 (HTTP mentah) |
| `mode` | `headless-puppeteer` | Diperoleh setelah eskalasi ke puppeteer |
| `mode` | `headless-chrome` | Diperoleh setelah eskalasi ke chrome |
| `status` | `ok` | Badan tidak-kacau dan tersimpan |
| `status` | `chaotic-unresolved` | Badan tetap kacau dan headless tak tersedia (WG3) |

**Berkas pendamping.** Badan mentah (`.html`, `.json`, `.pdf`) dan teks bersih
(`.txt`) disimpan di `docs/web-corpus/` yang di-*git-ignore* (WG6); hanya
`manifest.tsv` dan `MANIFEST.md` yang terlacak. `MANIFEST.md` adalah ringkasan
yang dapat dibaca manusia dan **wajib** menyatakan jumlah pengambilan yang
gagal (`FAILED=<n>`), konsisten dengan baris berstatus bukan `ok` pada
`manifest.tsv`.

---

## 7. Daftar Periksa Do / Don't

| ✔ Lakukan | ✘ Hindari |
|-----------|-----------|
| Mulai setiap pengambilan dengan rung `curl` (WG1) | Menjadikan peramban tanpa kepala sebagai pilihan pertama |
| Pertahankan badan respons pada 4xx/5xx dan catat kode `http` apa adanya | Membuang badan atau mengarang isi saat server mengembalikan galat |
| Deteksi kekacauan dengan kriteria §4 sebelum mengeskalasi | Mengeskalasi ke headless untuk halaman HTML biasa |
| Eskalasi berurutan `curl` → `headless-puppeteer` → `headless-chrome` (WG3) | Melompat langsung ke rung terakhir atau mengulang rung |
| Berhenti pada rung pertama yang menghasilkan badan tidak-kacau | Terus mengeskalasi setelah badan sudah bersih |
| Catat `chaotic-unresolved` bila headless tak tersedia (WG3) | Mengarang isi halaman yang tidak berhasil diambil |
| Ekstrak teks HTML via `pandoc -f html -t plain` (WG4) | Menyalin teks dari sumber lain lalu mengakuinya sebagai hasil ekstraksi |
| Catat sembilan kolom provenans pada `manifest.tsv` (WG5) | Membiarkan provenans kosong atau tidak konsisten |
| Simpan badan + teks di `docs/web-corpus/` yang di-*git-ignore* (WG6) | Menyimpan badan mentah di lokasi terlacak |
| Ambil kandidat dari `search.py … --json --no-save` (WG7) | Mengetik URL kandidat dengan tangan |
| De-duplikasi kandidat berdasarkan URL | Menghitung satu URL dua kali |
| Catat setiap URL **sekali** lewat `discover --fetch` (WG8) | Membiarkan URL tercatat ganda dengan beda huruf besar/kecil |

---

## 8. Rubrik

Skor **0–2 per komponen** untuk lima komponen; skor maksimum **10** (5 × 2).

| Komponen | 0 | 1 | 2 |
|----------|---|---|---|
| **Kepatuhan tangga** | Mulai dari headless atau melompati rung | Sebagian tangga ditelusuri | Mulai dari `curl`, eskalasi berurutan, berhenti pada rung pertama yang bersih |
| **Deteksi kekacauan** | Tanpa deteksi; kacau/tidak ditebak | Deteksi sebagian (satu sinyal) | Empat sinyal §4 diperiksa dan keputusan eksplisit |
| **Ekstraksi** | Teks tidak diekstrak | Ekstraksi tidak konsisten | HTML → `pandoc -f html -t plain`; non-HTML diarsipkan apa adanya |
| **Provenans** | Tidak dicatat | Sebagian kolom dicatat | Sembilan kolom `manifest.tsv` lengkap dan konsisten |
| **Persistensi & dedup** | Badan terlacak atau URL ganda | Sebagian benar | Badan di-*git-ignore*, hanya manifest terlacak; setiap URL dicatat sekali |

**Tafsiran.** **10** = kepatuhan penuh; **7–9** = revisi ringan (lengkapi
provenans atau deteksi); **4–6** = perlu pengambilan ulang dengan tangga yang
benar; **≤ 3** = hasil belum layak dipakai dan wajib diulang dari rung `curl`.

---

## 9. Sumber

**Berkas repositori (bukti utama).**

- `tools/webgrab.py` — implementasi tangga pengambilan (`fetch`), penemuan
  (`discover --fetch`), deteksi kekacauan §4, ekstraksi §4 (WG4), dan
  penulisan provenans `manifest.tsv` (WG5).
- `docs/web-corpus/manifest.tsv` — manifest provenans terlacak dengan skema
  sembilan kolom `slug,url,accessed,mode,status,http,bytes,sha256,text_chars`.
- `docs/web-corpus/MANIFEST.md` — ringkasan terbaca-manusia yang menyatakan
  `FAILED=<n>`.
- `docs/fulltext-framework.md` — kerangka teks utuh (F1–F8) yang melengkapi
  kerangka ini: pengambilan web memasok berkas, teks utuh menuntut verifikasi.
- `docs/subject-framework.md` — kerangka sapuan subjek (S1–S8) yang memasok
  kandidat URL untuk pengambilan.
- `tools/validators/web_corpus.py` — validator `web_corpus` yang menegakkan
  konsistensi manifest: sembilan kolom, `slug` unik dan sah, `url` sah,
  `accessed` bertanggal, `mode` dalam {`curl`, `headless-puppeteer`,
  `headless-chrome`}, `sha256` 64 digit heksadesimal, dan `FAILED=<n>` pada
  `MANIFEST.md` yang konsisten dengan baris bukan-`ok`.
- `.claude/skills/nykripsi/scripts/search.py` — sumber kandidat penemuan
  (WG7) lewat `… --json --no-save`; pengambilan nyata, bukan diketik tangan.

**Target `make` dan perintah.**

| Perintah | Fungsi |
|----------|--------|
| `python3 tools/webgrab.py fetch <url>` | Ambil satu URL menempuh tangga §3 |
| `python3 tools/webgrab.py discover "<q>" --fetch` | Temukan kandidat lalu ambil (WG7, WG8) |
| `make webgrab URL=<url>` | Padanan target untuk `fetch` |
| `make webdiscover Q="<q>"` | Padanan target untuk `discover --fetch` |
| `python3 tools/validate.py web_corpus` | Tegakkan konsistensi manifest (validator `web_corpus`) |

> **Catatan integritas sumber.** Kerangka ini **tidak** mengarang URL, hash,
> jumlah byte, atau karakter teks: seluruh nilai pada `manifest.tsv` berasal
> dari pengambilan yang benar-benar dijalankan `tools/webgrab.py`. Bila sebuah
> halaman tetap kacau setelah tangga §3 ditempuh, statusnya dicatat
> `chaotic-unresolved`, bukan diisi dengan tebakan.
