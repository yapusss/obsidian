# Aturan Mencatat ke Vault Ini

Ini file panduan bagi Hermes (dan siapa pun yang menulis ke vault ini).

## Lokasi file
- Catatan baru masuk ke `Inbox/` kecuali diminta folder lain.
- Template disimpan di `_templates/Catatan Telegram.md` — BACA file itu sebelum membuat catatan apa pun.

## Wajib dilakukan saat mencatat dari Telegram
1. Baca `_templates/Catatan Telegram.md` dan ikuti formatnya.
2. Isi frontmatter: `type`, `created` (YYYY-MM-DD), `source: telegram`.
3. Dukung hubungan dengan `[[Nama Catatan]]` di bagian "Hubungan".
4. Kalau catatan target di `[[..]]` belum ada, buatkan ringkas — kecuali target jelas kategori luas (mis. `[[Daftar X]]`) yang lebih masuk akal dibuat manual.

## Hubungan antarcatatan
- Selalu pakai wikilink `[[Nama]]`, bukan sebutan teks biasa.
- Tujuannya: catatan bisa saling "backlink" di Obsidian.