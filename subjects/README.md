# Registry Subjek

Direktori ini menyimpan subjek penelitian (perusahaan, aktor, negara, lembaga)
beserta keadaan sapuan materi sekunder tentangnya untuk Nykripsi v2.

- `registry.json` — registry (array JSON) berisi catatan subjek. Ini sumber
  kebenaran.
- `index.md` — indeks Markdown yang **dibuat ulang** oleh `tools/scrape.py
  render`. Jangan sunting berkas ini; sunting `registry.json`.

Alat utamanya adalah `tools/scrape.py` (stdlib saja). Rincian kerangka ada di
[docs/subject-framework.md](../docs/subject-framework.md).

## Skema Catatan Subjek

Setiap catatan di `registry.json` selalu memuat kunci berikut:

| Kunci | Tipe | Keterangan |
| --- | --- | --- |
| `id` | str | `subject-<accessed>-<slug(name)>`; bentrokan diberi akhiran `-1`, `-2`, … |
| `name` | str | Nama subjek apa adanya seperti dideklarasikan. |
| `aliases` | list | Daftar alias/nama lain subjek (dipakai memperluas kueri). |
| `accessed` | str | Tanggal `YYYY-MM-DD` saat subjek dideklarasikan. |
| `channels` | dict | Lima kanal wajib; tiap nilai `{"required": true, "count": 0}`. |
| `queries` | list | Kueri yang sudah dijalankan untuk subjek ini. |
| `saturation` | dict | `{"k": 3, "barren_rounds": 0, "saturated": false}`. |
| `status` | str | `incomplete` \| `complete`. |
| `notes` | str | Catatan bebas. |

Struktur `channels` selalu memuat kelima kanal dengan hitungan awal nol:

```json
{
  "id": "subject-<accessed>-<slug(name)>",
  "name": "<nama subjek>",
  "aliases": [],
  "accessed": "YYYY-MM-DD",
  "channels": {
    "press":    {"required": true, "count": 0},
    "news":     {"required": true, "count": 0},
    "article":  {"required": true, "count": 0},
    "official": {"required": true, "count": 0},
    "web":      {"required": true, "count": 0}
  },
  "queries": [],
  "saturation": {"k": 3, "barren_rounds": 0, "saturated": false},
  "status": "incomplete",
  "notes": ""
}
```

## Kanal Sapuan

Kelima kanal berikut wajib disapu berurutan. Setiap kanal memakai subperintah
`search.py` dan kueri berikut:

| Kanal | Subperintah `search.py` | Kueri |
| --- | --- | --- |
| `press` | `web` | `<name> press release` |
| `news` | `news` | `<name>` |
| `article` | `article` | `<name>` |
| `official` | `company` | `<name>` |
| `web` | `web` | `<name>` |

Kanal `video` dan `forum` tidak termasuk. Setiap sumber yang dikumpulkan
ditandai `subject` dan `channel` pada `sources/registry.json`.

## Aturan Kelengkapan

Sebuah subjek berstatus `complete` **hanya bila** kedua syarat berikut
terpenuhi:

1. **Daftar periksa kanal** — setiap kanal wajib (`required == true`) memiliki
   `count >= 1` sumber terverifikasi.
2. **Saturasi** — `saturation.saturated == true`, yaitu `K` putaran berurutan
   tanpa sumber baru (bawaan K=3).

`sweep` menghitung sumber baru dari keluaran `search.py` (regex `TAMBAH: <n>
baru`), menaikkan `barren_rounds` bila satu putaran menghasilkan nol sumber
baru, dan menyetel `status` menjadi `complete` hanya bila kedua syarat di atas
terpenuhi. Selama belum, status tetap `incomplete`. Validator `subjects` akan
gagal bila sebuah subjek `complete` tetapi kanal wajibnya kosong atau saturasi
belum tercapai.

## Aturan Provenance

**Jangan pernah mengarang hitungan, URL, atau status.** Setiap hitungan kanal
berasal dari sapuan nyata `tools/scrape.py sweep` yang memanggil `search.py`.
Jumlah hitungan seluruh kanal harus sama dengan jumlah record di
`sources/registry.json` yang bertanda `subject` senama; bila berbeda, validator
gagal dan perbaikannya menjalankan ulang sapuan atau memperbaiki catatan.

## Subperintah `scrape.py`

- `add NAME [--aliases "a,b"] [--k N] [--registry PATH]`
  — deklarasikan subjek baru dengan skema di atas. Keluar `1` bila `NAME` sudah
  ada.
- `sweep NAME [--channel CH] [--rounds N] [--registry PATH] [--sources PATH]
  [--limit N] [--email ADDR]`
  — jalankan sapuan kanal sekunder, perbarui hitungan, saturasi, dan status.
  Keluar `1` bila subjek belum ada.
- `render [--registry PATH] [--index PATH]`
  — tulis ulang `subjects/index.md` dari registry.

Target Make yang tersedia:

- `make subjects` — regenerasi `subjects/index.md`.
- `make scrape S=<nama>` — sapu kanal sekunder untuk subjek `<nama>`.
