---
type: catatan
created: 2026-09-07
source: hermes
---

# Setup Sinkronisasi Vault Obsidian

## Ringkasan
Vault Obsidian di /root/Obsidian (server yvserver, headless) disinkronkan ke
GitHub lewat repo privat yapusss/obsidian. Server auto-push harian via cron.

## Isi
- Repo lokal: `/root/Obsidian` (branch `master`).
- Remote: `https://github.com/yapusss/obsidian.git` (private, akun yapusss).
- Kredensial: PAT di `~/.git-credentials` (chmod 600).
- Auto-sync: cron `0 1 * * *` → `/root/scripts/obsidian-sync.sh`, log di
  `/var/log/obsidian-sync.log`. Commit+push jika ada perubahan; diam jika tidak.
- Identitas git: `yapusss` <haarisnursalim@gmail.com>.
- Folder `_knowledge/` = basis pengetahuan jangka panjang Hermes (otomatis ikut sync).

## Hubungan
- [[Basis Pengetahuan Hermes]] — tempat knowledge base disimpan
- [[Obsidian - Catatan]] — dokumentasi vault dan template catatan
- [[Setup Sinkronisasi Vault Obsidian]] — catatan ini sendiri (topik setup)

## Status
- ✅ Push pertama berhasil (commit 6ad29c7) dan terverifikasi di GitHub.
- ✅ Auto-sync cron terpasang.
- ⏳ Opsional: sinkron 2 arah (server tarik juga perubahan dari perangkat lain)
  belum diaktifkan, menunggu konfirmasi.