# Kerangka Kelas Sumber (Primer vs Sekunder)

Setiap catatan (record) pada `sources/registry.json` diberi **kelas sumber**
(`source_class`): `primary` atau `secondary`. Kerangka ini membedakan sumber
yang menyuarakan subjek secara langsung dari sumber yang menyokong atau
memberitakan subjek.

## Definisi

**Sumber primer (kebenaran subjek / subject truth).** Suatu *wawancara langsung*
terhadap perusahaan / aktor utama / subjek utama. Subjek utama yang berbicara
secara langsung merupakan kebenaran dari subjek itu sendiri.

**Sumber sekunder (kebenaran pendukung / supporting truth).** Materi yang
menyokong atau memberitakan subjek, tetapi bukan wawancara langsung — secara
khusus **siaran pers** (press release) perusahaan / aktor utama / subjek utama,
ditambah **berita** (news), **artikel**, dan seluruh materi termediasi / pihak
ketiga lainnya.

## Kelas bawaan menurut `type`

Kelas bawaan ditentukan oleh medan `type` pada setiap record:

| `type` record | Kelas bawaan (`source_class`) |
| --- | --- |
| `interview` | `primary` |
| `news` | `secondary` |
| `article` | `secondary` |
| `book` | `secondary` |
| `dataset` | `secondary` |
| `publicdata` | `secondary` |
| `company` | `secondary` |
| `pdf` | `secondary` |
| `web` | `secondary` |
| `forum` | `secondary` |
| `video` | `secondary` |

Dengan kata lain: hanya `interview` yang berkelas `primary`; seluruh tipe lain
berkelas `secondary`.

## Penimpaan kelas (`--class`)

Kelas bawaan dapat ditimpa per record melalui bendera `--class {primary,secondary}`
pada setiap subperintah pencarian `search.py`. Penimpaan menandai record dengan
`class_origin` bernilai `manual`.

```bash
python3 .claude/skills/nykripsi/scripts/search.py interview "UMKM digital" --class primary
python3 .claude/skills/nykripsi/scripts/search.py news "nation branding" --class secondary
```

## Penghitungan ulang (`search.py classify`)

Subperintah `search.py classify` menghitung ulang kelas setiap record
non-manual dari `type`-nya. Varian `classify --class X` memaksa setiap record
menjadi `X` dan menandainya `manual`.

```bash
python3 .claude/skills/nykripsi/scripts/search.py classify
python3 .claude/skills/nykripsi/scripts/search.py classify --class secondary
```

## Medan skema baru

Dua medan baru disisipkan setelah medan `backend` pada setiap record:

| Medan | Nilai | Keterangan |
| --- | --- | --- |
| `source_class` | `primary` \| `secondary` | Kelas sumber record. |
| `class_origin` | `auto` \| `manual` | Apakah kelas ditetapkan otomatis dari `type` atau ditimpa manual. |

`sources/index.md` memperoleh kolom `kelas` (tepat setelah kolom `id`) yang
menampilkan `source_class` setiap record. `tools/validators/sources.py`
mewajibkan medan `source_class` dan melaporkan pembagian jumlah sumber primer
dan sekunder.

## Contoh

| Sumber | `type` | `source_class` | Alasan |
| --- | --- | --- | --- |
| Transkrip wawancara CEO perusahaan | `interview` | `primary` | Wawancara langsung; subjek utama berbicara sendiri. |
| Siaran pers perusahaan | `news` (atau record termediasi) | `secondary` | Materi pendukung yang dirilis perusahaan, bukan wawancara langsung. |
| Artikel berita tentang perusahaan | `news` | `secondary` | Pemberitaan pihak ketiga tentang subjek. |

## Catatan tentang petunjuk (lead) pada subperintah `interview`

Subperintah `interview` mengambil petunjuk dari umpan berita (news feed) GDELT
dan Google News RSS. Petunjuk tersebut sering kali **bukan** wawancara langsung,
sehingga harus ditandai ulang sebagai `secondary` dengan
`--class secondary` apabila memang bukan wawancara langsung. Hanya transkrip
wawancara langsung yang layak berkelas `primary`.
