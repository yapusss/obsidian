# Template Catatan — dipakai Hermes dari Telegram

Ini template WAJIB yang selalu dipakai saat mencatat ke vault. Isi setiap bagian.

```markdown
---
type: note
created: YYYY-MM-DD
source: telegram
---

# [Judul Catatan]

## Ringkasan
[Satu sampai tiga kalimat — apa inti catatan ini]

## Isi
[Detail utama / isi catatan]

## Hubungan
[Sebutkan koneksi ke catatan lain dengan wikilink `[[Nama Catatan]]`.
Jika belum ada catatan target, tetap tulis wikilink-nya: agent akan membuatkan file itu.
Pola yang umum:
- `[[Topik Induk]]` — ini bagian dari topik yang lebih besar
- `[[Catatan Terkait]]` — saling terkait / membandingkan
- `[[Kebiasaan/Proyek]]` — bagian dari rutinitas atau proyek]
```

## Aturan pemakaian
1. Selalu isi seluruh bagian (frontmatter, Ringkasan, Isi, Hubungan).
2. File diletakkan di `Inbox/` kecuali ada permintaan folder lain.
3. Setiap `[[Nama Catatan]]` di bagian Hubungan wajib benar-benar ditulis sebagai link (bukan sekadar menyebut nama).
4. `created` memakai tanggal hari ini, format YYYY-MM-DD.
5. `source` tetap `telegram` untuk semua catatan yang masuk lewat Telegram.