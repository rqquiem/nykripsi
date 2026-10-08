# Draf Bab (Bahan Kerja)

Folder ini menampung bahan tulisan yang belum selesai. Draf adalah materi
kerja-sementara, bukan bab final, sehingga boleh belum lengkap atau belum rapi.

## Pengecualian dari `make check`

Isi `content/drafts/` **dikecualikan** dari `make check`, mencakup:

- build Pandoc (PDF/DOCX),
- linter ragam bahasa Indonesia, dan
- validator sitasi.

Karena itu, draf yang belum selesai tidak akan mematikan pemeriksaan repositori.
Lint khusus draf dijalankan terpisah lewat `make check-drafts`.

## Aturan nama berkas

Nama berkas draf **WAJIB** sama dengan nama berkas bab tujuan. Sebagai contoh:

- `content/drafts/10-bab-01-pendahuluan.md` -> `content/skripsi/10-bab-01-pendahuluan.md`

Kesamaan nama inilah yang dipakai oleh `make promote` untuk menentukan bab
tujuan.

## Alur kerja

1. Salin bab yang sudah ada sebagai draf awal:

       cp content/skripsi/10-bab-01-pendahuluan.md content/drafts/

2. Sunting draf tersebut sampai dirasa cukup.

3. Lint draf dengan linter ragam bahasa yang sama:

       make check-drafts

4. Promosikan draf menimpa bab tujuan:

       make promote DRAFT=content/drafts/10-bab-01-pendahuluan.md

Langkah promosi hanya berjalan bila berkas tujuan sudah ada di
`content/skripsi/`. Bab yang benar-benar baru tidak dapat dipromosikan sebelum
bab tujuan dibuat lebih dahulu, sehingga salah ketik nama tidak menciptakan bab
baru secara tak sengaja. Sebelum ditimpa, berkas tujuan dicadangkan ke folder
`.promote-backups/`.
