# Kerangka Sapuan Subjek (Subject Sweep) — Mengumpulkan Seluruh Materi Sekunder tentang Subjek

Kerangka ini menetapkan aturan operasional untuk **menyapu seluruh materi
sekunder** tentang sebuah **subjek penelitian** — siaran pers (*press release*),
berita, artikel, dokumen resmi/perusahaan, dan hasil web umum — sehingga
pemahaman atas subjek bersifat **menyeluruh (*exhaustive*)**, bukan
sepotong-sepotong. Kerangka diturunkan dari dua sumber yang dapat diaudit:
**berkas repositori ini** (skrip, target `make`, registry, dan validator) serta
**literatur akademik internasional** yang benar-benar terekam lewat `scholar.py`
pada sesi ini. Tidak ada klaim tanpa sumber.

Kerangka ini **melengkapi** dua kerangka yang sudah ada dan tidak
menggantikannya. `docs/source-classification.md` menetapkan bahwa **hanya
wawancara langsung oleh penulis** yang berkelas `primary`, sedangkan seluruh
materi lain berkelas `secondary`. `docs/fulltext-framework.md` memaksa **teks
utuh** tiap karya yang dipakai sebagai dasar simpulan (aturan F1–F8). Sapuan
subjek menangani **keluasan** cakupan; teks utuh menangani **kedalaman**
pembacaan. Keduanya saling melengkapi: keluasan tanpa kedalaman menghasilkan
klaim yang tidak terverifikasi, sedangkan kedalaman tanpa keluasan menghasilkan
simpulan yang tidak menyeluruh.

---

## 1. Definisi dan Fungsi

**Definisi.** *Subjek* adalah **entitas yang diteliti** — perusahaan, aktor,
negara, atau lembaga — yang menjadi fokus sebuah karya. *Sapuan sekunder
(*subject sweep*)* adalah penelusuran sistematis atas **seluruh materi
sekunder** tentang subjek tersebut di internet, mencakup lima kanal wajib:
siaran pers, berita, artikel, dokumen resmi/perusahaan, dan web umum.

**Mengapa materi sekunder, bukan primer.** Berdasarkan
`docs/source-classification.md`, hanya `type == "interview"` — yaitu wawancara
langsung oleh penulis terhadap subjek — yang berkelas `primary`
(`CLASS_BY_TYPE = {"interview": "primary"}`). Seluruh tipe lain (berita,
artikel, buku, dokumen perusahaan, dataset, web) berkelas `secondary`. Konsekuensi
metodologisnya penting: siaran pers diterbitkan oleh **pihak berkepentingan**
(*first-party*), berita dan artikel melewati penyuntingan pihak ketiga, dan
dokumen resmi mewakili posisi institusi — semuanya **bukan** pernyataan penulis
yang dapat diperlakukan sebagai kebenaran subjek. Karena itu materi sekunder
berfungsi sebagai **bahan triangulasi dan konteks**, bukan sebagai data primer.

**Mengapa keluasan perlu dipaksakan.** Materi sekunder tentang sebuah subjek
tersebar di banyak kanal dan terbit dalam jendela waktu yang panjang; sapuan
yang berhenti pada satu kanal (mis. hanya berita) menghasilkan gambaran yang
berat sebelah. Dua temuan empiris mendasari aturan keluasan ini. Pertama,
Sumner dkk. (2014) menemukan bahwa **teks siaran pers** merupakan sumber utama
**melebih-lebihkan (*exaggeration*)** yang kemudian menyusup ke pemberitaan,
sehingga siaran pers tidak dapat diabaikan maupun dipercaya begitu saja. Kedua,
sapuan yang berhenti sebelum **saturasi** berisiko melewatkan materi yang belum
muncul pada putaran awal; kerangka saturasi (Saunders dkk., 2018) menetapkan
bahwa penambahan pencarian hanya berhenti setelah tidak ada lagi informasi baru.

**Fungsi kerangka.** Kerangka ini menjadikan kebiasaan di atas sebagai aturan
yang dapat **diperiksa mesin**: setiap sumber wajib ditandai subjek dan
kanalnya, setiap subjek memiliki catatan cakupan, dan validator menolak status
`complete` yang belum memenuhi daftar periksa kanal maupun saturasi.

---

## 2. Aturan Absolut (Wajib)

1. **S1.** Setiap sumber yang dikumpulkan **wajib** ditandai **subjek**
   (`subject`) dan **kanal** (`channel`) asalnya pada `sources/registry.json`.
   Sumber tanpa penandaan subjek/kanal tidak dapat dihitung sebagai cakupan
   subjek.
2. **S2.** Sebelum sebuah subjek dinyatakan lengkap, **seluruh kanal wajib**
   (§3) harus terisi sekurang-kurangnya **satu** sumber terverifikasi
   (`count ≥ 1`).
3. **S3.** Sapuan **wajib** dilanjutkan sampai **saturasi**: **K putaran
   berurutan tanpa sumber baru** (bawaan K=3); berhenti sebelum saturasi
   dilarang.
4. **S4.** Data **primer** hanya wawancara langsung oleh penulis terhadap
   subjek; seluruh materi lain adalah **sekunder** dan **tidak boleh**
   diperlakukan sebagai kebenaran subjek.
5. **S5.** Provenans wajib: setiap catatan subjek memuat **hitungan per kanal**,
   **jumlah putaran**, dan **status saturasi**; dilarang mengarang hitungan,
   URL, atau status.
6. **S6.** Subjek **tidak boleh** ditandai `complete` bila **daftar periksa
   kanal** atau **saturasi** belum terpenuhi.
7. **S7.** De-duplikasi: satu URL/DOI **tidak** dihitung dua kali.
8. **S8.** Sumber sekunder tetap tunduk pada kerangka teks utuh
   (`docs/fulltext-framework.md`, F1–F8) sebelum dipakai sebagai dasar
   simpulan.

---

## 3. Kanal Sapuan (Wajib Berurutan)

Kelima kanal berikut disapu **berurutan**. Urutan wajib: `press` → `news` →
`article` → `official` → `web`. Setiap kanal memakai subperintah `search.py`
yang berbeda dan kueri yang berbeda. Kondisi berhenti adalah keadaan ketika
kanal dinyatakan cukup; kondisi lanjut adalah keadaan ketika sapuan pada kanal
tersebut harus diulang.

| Kanal | Subperintah `search.py` | Kueri | Kondisi berhenti | Kondisi lanjut |
|-------|-------------------------|-------|------------------|----------------|
| `press` | `web` | `"<name>" press release` | Ditemukan ≥ 1 siaran pers terverifikasi tentang subjek | Tidak ditemukan siaran pers → perluas dengan alias subjek, lalu ulangi |
| `news` | `news` | `"<name>"` | Ditemukan ≥ 1 berita terverifikasi tentang subjek | Tidak ditemukan berita → perluas dengan alias subjek, lalu ulangi |
| `article` | `article` | `"<name>"` | Ditemukan ≥ 1 artikel akademik terverifikasi tentang subjek | Tidak ditemukan artikel → perluas dengan nama lengkap/afiliasi, lalu ulangi |
| `official` | `company` | `"<name>"` | Ditemukan ≥ 1 dokumen resmi/perusahaan terverifikasi | Tidak ditemukan dokumen resmi → perluas dengan nama badan hukum, lalu ulangi |
| `web` | `web` | `"<name>"` | Ditemukan ≥ 1 sumber web umum terverifikasi | Tidak ditemukan sumber web → perluas dengan alias subjek, lalu ulangi |

**Perintah persis.** Sapuan satu kanal dijalankan dengan:

```
python3 tools/scrape.py sweep "<name>" --channel <ch>
```

Sapuan seluruh kanal sekaligus (satu putaran penuh) dijalankan dengan:

```
make scrape S="<name>"
```

**Satu putaran = satu kali melewati seluruh kanal** (`press`, `news`, `article`,
`official`, `web`). Sapuan diulang putaran demi putaran sampai saturasi (§4).
Kanal `video` dan `forum` **tidak** termasuk kanal wajib.

---

## 4. Kriteria Kelengkapan (Daftar Periksa + Saturasi)

Sebuah subjek berstatus `complete` **hanya bila** kedua syarat berikut
terpenuhi secara bersamaan:

1. **(a) Daftar periksa kanal** — setiap kanal wajib (`required == true`)
   memiliki `count ≥ 1` sumber terverifikasi. Kelima kanal wajib harus terisi.
2. **(b) Saturasi** — `saturation.saturated == true`, yaitu **K putaran
   berurutan tanpa sumber baru** (bawaan K=3).

Bila salah satu syarat belum terpenuhi, status tetap `incomplete`. Status
`complete` **dilarang** diberikan hanya karena kanal terisi tanpa saturasi,
atau karena saturasi tercapai tanpa kelima kanal terisi.

**Cara `tools/scrape.py sweep` menghitung.** Pada setiap kanal, `sweep`
menjalankan `search.py` sebagai subproses dan membaca keluarannya. Baris
ringkasan `search.py` berbentuk `TAMBAH: <n> baru, <m> duplikat dilewati`
(lihat fungsi `_run_search` pada
`.claude/skills/nykripsi/scripts/search.py`). Nilai `<n>` diekstrak dengan
regex `TAMBAH: <n> baru` (`TAMBAH_RE = re.compile(r"TAMBAH:\s+(\d+)\s+baru")`)
dan ditambahkan ke `channels[<ch>]["count"]`. Setelah **satu putaran penuh**:

- bila total sumber baru pada putaran itu **nol** (`round_new == 0`), maka
  `barren_rounds` **dinaikkan** satu (`barren_rounds += 1`);
- bila ada sumber baru, maka `barren_rounds` **direset** menjadi nol.

Setelah seluruh putaran selesai, `saturated = barren_rounds >= k`. Selanjutnya
`status` disetel menjadi `complete` **hanya bila** kelima kanal wajib memiliki
`count ≥ 1` **dan** `saturated == true`; selain itu `status` tetap
`incomplete`. Validator `subjects` menolak berkas yang melanggar aturan ini.

---

## 5. Provenans dan Penandaan Sumber

**Medan pada `sources/registry.json`.** Setiap record sumber memuat dua medan
provenans sapuan:

| Medan | Tipe | Keterangan |
|-------|------|------------|
| `subject` | str \| null | Nama subjek yang sumber ini wakili; `null` bila belum ditandai. |
| `channel` | str \| null | Kanal sapuan asal sumber: `press`, `news`, `article`, `official`, atau `web`. |

Kedua medan diisi oleh `search.py` melalui argumen `--subject` dan `--channel`,
yang dipanggil oleh `tools/scrape.py sweep`. Penandaan ini memenuhi **S1**.

**Medan catatan subjek (`subjects/registry.json`).**

| Medan | Tipe | Keterangan |
|-------|------|------------|
| `channels` | dict | Lima kanal wajib; tiap nilai `{"required": true, "count": <int ≥ 0>}`. |
| `queries` | list | Kueri yang sudah dijalankan untuk subjek ini. |
| `saturation` | dict | `{"k": <int ≥ 1>, "barren_rounds": <int ≥ 0>, "saturated": <bool>}`. |
| `status` | str | `incomplete` atau `complete`. |

Skema lengkap dan aturan penyuntingannya didokumentasikan pada
[`subjects/README.md`](../subjects/README.md). Berkas `subjects/index.md`
dihasilkan oleh `tools/scrape.py render` dan **tidak** disunting tangan.

**Aturan konsistensi.** Jumlah seluruh hitungan kanal sebuah subjek
(`sum(ch["count"] for ch in channels.values())`) **wajib sama** dengan jumlah
record di `sources/registry.json` yang bertanda `subject` senama. Bila berbeda,
berarti ada sumber bertanda subjek yang ditambahkan di luar sapuan (atau
hitungan tidak sinkron), dan validator `subjects` **gagal**. Perbaikannya
adalah menjalankan ulang sapuan atau memperbaiki catatan — bukan melonggarkan
validator. Aturan ini memenuhi **S5**.

---

## 6. Scope

**Cakupan (berlaku).**

- **Subjek riset**: perusahaan, aktor (individu/tokoh), negara, atau lembaga
  yang menjadi fokus karya.
- **Materi prosais**: siaran pers, berita, artikel akademik, dokumen
  resmi/perusahaan, dan sumber web umum yang memiliki struktur teks berjalan.

**Di luar cakupan (tidak berlaku).**

- Rekaman **non-prosais**: data tabular, basis data terstruktur, atau himpunan
  data numerik murni yang tidak memiliki narasi.
- Kanal `video` dan `forum` — keduanya **bukan** kanal wajib sapuan.

**Kapan aturan berlaku.**

- Aturan berlaku ketika materi sekunder dipakai untuk **riset atau penulisan**
  (menyusun argumen, menetapkan konteks, atau menilai subjek).
- Aturan **tidak** berlaku ketika tindakan hanya sebatas **menyimpan tautan**
  atau menandai kandidat untuk ditelaah kemudian; penyimpanan tautan belum
  merupakan klaim tentang subjek.

---

## 7. Model Komponen dan Varian

**Komponen sapuan yang wajib dipahami.** Setiap catatan subjek dibaca melalui
komponen berikut; kehadirannya dipakai pada rubrik §10.

| Komponen | Fungsi | Padanan medan |
|----------|--------|---------------|
| `channels` | Kanal yang disapu beserta hitungannya | `channels[<ch>] = {"required", "count"}` |
| `queries` | Kueri yang benar-benar dijalankan | `queries` (list) |
| `saturation` | Keadaan saturasi sapuan | `saturation = {"k", "barren_rounds", "saturated"}` |
| `status` | Kesimpulan kelengkapan | `status` (`incomplete` \| `complete`) |

**Varian kelas sumber.** Kelas sumber mengikuti
`docs/source-classification.md`:

| Kelas | Definisi | Contoh kanal |
|-------|----------|--------------|
| `primary` | Wawancara **langsung oleh penulis** terhadap subjek | `interview` (satu-satunya) |
| `secondary` | Seluruh materi lain tentang subjek | `press`, `news`, `article`, `official`, `web` |

Kanal sapuan subjek seluruhnya berkelas `secondary`. Materi sekunder yang
dipakai sebagai dasar simpulan tetap tunduk pada kerangka teks utuh
(`docs/fulltext-framework.md`), sesuai **S8**.

---

## 8. Matriks Kepatuhan per-Tingkat

Matriks menetapkan tingkat keberlakuan setiap aturan per jenis keluaran.
`wajib` = mengikat; `disarankan` = dianjurkan, bukan syarat mutlak;
`tidak berlaku` = di luar scope (§6).

| Aturan | Sinta 1–2 | Sinta 3–6 | Scopus | Skripsi HI | Sumber berita/web |
|--------|-----------|-----------|--------|------------|-------------------|
| S1 | wajib | wajib | wajib (unverified — confirm first) | wajib | disarankan |
| S2 | wajib | wajib | wajib (unverified — confirm first) | wajib | tidak berlaku |
| S3 | wajib | wajib | wajib (unverified — confirm first) | disarankan | tidak berlaku |
| S4 | wajib | wajib | wajib (unverified — confirm first) | wajib | wajib |
| S5 | wajib | wajib | wajib (unverified — confirm first) | wajib | disarankan |
| S6 | wajib | wajib | wajib (unverified — confirm first) | wajib | tidak berlaku |
| S7 | wajib | wajib | wajib (unverified — confirm first) | wajib | disarankan |
| S8 | wajib | wajib | wajib (unverified — confirm first) | wajib | tidak berlaku |

**Catatan verifikasi kolom Scopus.** Kolom **Scopus** ditandai
`unverified — confirm first` karena **status indeksasi Scopus tidak dapat
diverifikasi dari korpus lokal**. Korpus repositori hanya memuat korpus Sinta
(`docs/sinta-corpus/`, Sinta 1–6) dan korpus Hubungan Internasional
(`docs/ir-corpus/`, nasional/internasional); tidak ada metadata indeksasi
Scopus di dalamnya. Karena itu status indeksasi Scopus **tidak boleh
diasumsikan** dan wajib dikonfirmasi lebih dahulu pada sumber resmi sebelum
dipakai sebagai dasar klaim.

---

## 9. Daftar Periksa Do / Don't

| ✔ Lakukan | ✘ Hindari |
|-----------|-----------|
| Tandai setiap sumber dengan `subject` dan `channel` pada `sources/registry.json` | Mengumpulkan sumber tanpa provenans subjek/kanal |
| Sapu kelima kanal berurutan (`press` → `news` → `article` → `official` → `web`) | Berhenti pada satu kanal saja (mis. hanya berita) |
| Lanjutkan sapuan sampai saturasi K putaran tanpa sumber baru | Menandai `complete` sebelum kelima kanal terisi |
| Catat hitungan per kanal, jumlah putaran, dan status saturasi | Mengarang hitungan, URL, atau status |
| Perlakukan seluruh kanal sapuan sebagai sumber sekunder | Memperlakukan siaran pers/berita sebagai kebenaran subjek |
| Bedakan data primer (wawancara penulis) dari materi sekunder | Menyamakan siaran pers pihak berkepentingan dengan data primer |
| Verifikasi teks utuh sumber sekunder (F1–F8) sebelum menyimpulkan | Menyimpulkan isi sumber hanya dari judul atau *snippet* |
| De-duplikasi berdasarkan URL/DOI | Menghitung satu URL/DOI dua kali |
| Jaga konsistensi jumlah hitungan kanal dengan jumlah sumber bertanda subjek | Membiarkan catatan subjek tidak sinkron dengan registry sumber |

---

## 10. Rubrik Penilaian

Skor **0–2 per komponen** untuk lima komponen; skor maksimum **10** (5 × 2).

| Komponen | 0 | 1 | 2 |
|----------|---|---|---|
| **Cakupan kanal** | Tidak ada kanal tersapu | Sebagian kanal tersapu | Kelima kanal terisi (`count ≥ 1`) |
| **Kedalaman putaran/saturasi** | Satu putaran tanpa rencana lanjut | Beberapa putaran, belum saturasi | Saturasi tercapai (K putaran berurutan tanpa sumber baru) |
| **Ketepatan kelas sumber** | Kelas sumber salah (sekunder dianggap primer) | Sebagian kelas tepat | Seluruh kanal diklasifikasi `secondary`; wawancara penulis `primary` |
| **Provenans** | Tidak dicatat | Sebagian medan dicatat | `subject`/`channel` pada sumber dan `channels`/`queries`/`saturation`/`status` pada subjek lengkap |
| **Kepatuhan dedup** | Duplikat dihitung ganda | Duplikat sebagian tersaring | Setiap URL/DOI dihitung satu kali |

**Tafsiran.** **10** = kepatuhan penuh; **7–9** = revisi ringan (lengkapi
sapuan kanal atau provenans); **4–6** = perlu sapuan ulang pada kanal yang
kosong atau belum saturasi; **≤ 3** = cakupan subjek belum layak dan wajib
diulang dari daftar periksa kanal.

---

## 11. Sumber

**Berkas repositori (bukti utama).**

- [`docs/source-classification.md`](source-classification.md) — `CLASS_BY_TYPE
  = {"interview": "primary"}`; hanya wawancara langsung oleh penulis yang
  berkelas `primary`, seluruh tipe lain `secondary` (dasar §1 dan §7).
- [`docs/fulltext-framework.md`](fulltext-framework.md) — aturan F1–F8 dan
  tangga akuisisi teks utuh (dasar **S8**).
- [`tools/scrape.py`](../tools/scrape.py) — alat sapuan: subperintah `add`,
  `sweep`, `render`; `CHANNEL_SEARCH`, `DEFAULT_K = 3`, dan regex
  `TAMBAH_RE = re.compile(r"TAMBAH:\s+(\d+)\s+baru")` (dasar §3 dan §4).
- [`subjects/registry.json`](../subjects/registry.json) — registry catatan
  subjek (sumber kebenaran).
- [`subjects/README.md`](../subjects/README.md) — skema catatan subjek,
  tabel kanal, aturan kelengkapan, dan aturan provenans.
- [`subjects/index.md`](../subjects/index.md) — indeks yang dihasilkan
  `tools/scrape.py render`.
- [`sources/registry.json`](../sources/registry.json) — 33 catatan sumber
  dengan medan `subject` dan `channel` (provenans §5).
- [`sources/README.md`](../sources/README.md) — bagian "Subject and channel".
- [`.claude/skills/nykripsi/scripts/search.py`](../.claude/skills/nykripsi/scripts/search.py)
  — `_run_search` mencetak `TAMBAH: <n> baru, <m> duplikat dilewati`;
  argumen `--subject`/`--channel`; subperintah `news`, `article`, `company`,
  `web`.
- [`Makefile`](../Makefile) — target `subjects` (`python3 tools/scrape.py
  render`) dan `scrape` (`python3 tools/scrape.py sweep "$(S)"`).

**Literatur eksternal (rekaman nyata `scholar.py`).**

- Bowen, G. A. (2009). *Document Analysis as a Qualitative Research Method*.
  Qualitative Research Journal. <https://doi.org/10.3316/qrj0902027>
- Fusch, P. I., & Ness, L. R. (2015). *Are we there yet? Data saturation in
  qualitative research*. The Qualitative Report.
  <https://scholarworks.waldenu.edu/facpubs/455/>
- Guest, G., Bunce, A., & Johnson, L. (2006). *How many interviews are enough?
  An experiment with data saturation and variability*. Field Methods.
  <https://journals.sagepub.com/doi/abs/10.1177/1525822x05279903>
- Guest, G., Namey, E., & Chen, M. (2020). *A simple method to assess and
  report thematic saturation in qualitative research*. PLOS ONE.
  <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0232076>
- Heale, R., & Forbes, D. (2013). *Understanding triangulation in research*.
  Evidence-Based Nursing. <https://ebn.bmj.com/content/16/4/98.short>
- Hennink, M. M., Kaiser, B. N., & Marconi, V. C. (2017). *Code Saturation
  Versus Meaning Saturation*. Qualitative Health Research.
  <https://doi.org/10.1177/1049732316665344>
- Hsieh, H.-F., & Shannon, S. E. (2005). *Three Approaches to Qualitative
  Content Analysis*. Qualitative Health Research.
  <https://doi.org/10.1177/1049732305276687>
- Johnston, M. P. (2014). *Secondary data analysis: A method of which the time
  has come*. Qualitative and Quantitative Methods in Libraries.
  <http://www.qqml-journal.net/index.php/qqml/article/view/169>
- Saunders, B., Sim, J., Kingstone, T., Baker, S., Waterfield, J., Bartlam,
  B., Burroughs, H., & Jinks, C. (2018). *Saturation in qualitative research:
  exploring its conceptualization and operationalization*. Quality & Quantity.
  <https://link.springer.com/article/10.1007/s11135-017-0574-8>
- Sumner, P., Vivian-Griffiths, S., Boivin, J., Williams, A., Venetis, C. A.,
  Davies, A., Ogden, J., Whelan, L., Hughes, B., Wilson, B., Boy, F.,
  Chambers, C. D., & Bott, L. (2014). *The association between exaggeration in
  health related science news and academic press releases: retrospective
  observational study*. BMJ.
  <https://www.bmj.com/content/349/bmj.G7015.abstract>
- Tripathy, J. P. (2013). *Secondary data analysis: Ethical issues and
  challenges*. Journal of Pharmacology and Pharmacotherapeutics. **unverified
  — confirm first** (tidak terverifikasi lewat `scholar.py` pada sesi ini;
  DOI/URL tidak dicantumkan agar tidak mengarang).

> **Catatan integritas sumber.** Seluruh entri di atas, kecuali yang ditandai
> **unverified — confirm first**, berasal dari keluaran nyata perintah
> `python3 .claude/skills/nykripsi/scripts/scholar.py search "<judul>"
> --limit 3`; URL yang dicantumkan adalah URL yang benar-benar dikembalikan
> pencarian. Tidak ada DOI atau URL yang dikarang. Entri yang tidak dapat
> diverifikasi ditandai eksplisit dan **tidak** diberi DOI/URL.
