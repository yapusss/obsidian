---
type: catatan
created: 2026-09-07
source: hermes
---

# Akses Dashboard Web Hermes (via Tailscale)

## Ringkasan
Dashboard web Hermes berjalan sebagai systemd service dan hanya dapat diakses
melalui jaringan Tailscale pribadi (bukan internet publik).

## Akses
- URL: http://100.88.221.38:9119 (IP tailscale node yvserver)
  Buka dari perangkat yang join tailnet (browser apa saja).
- Login (username/password basic auth):
  - Username: `yvadmin`
  - Password: JANGAN tampilkan di catatan ini (secreto). Simpan di
    `/root/.hermes/dashboard_pass.txt` di server (chmod 600) dan/atau di
    password manager pemilik. Buka server lalu `cat /root/.hermes/dashboard_pass.txt`.
- Dashboard bind ke IP tailscale (100.88.221.38:9119), bukan loopback.

## Service
- Unit: `hermes-dashboard.service` (systemd), enabled, auto-start:
  - `systemctl status hermes-dashboard` / `restart` / `stop`
- Web dist sudah di-build (hermes_cli/web_dist); dijalankan `--skip-build`.
- Config: host = IP tailscale, port 9119.

## Keamanan
- Hanya tailnet (perangkat yang join) yang bisa akses; tidak ada domain/publik.
- Auth wajib (username/password) karena bind non-loopback.
- Config basic_auth via `hermes config set dashboard.basic_auth.*`.
- Password tersimpan terpisah dari vault ini (bukan disinkron ke GitHub).

## Catatan setup
- Sebelumnya pakai tailscale serve (domain tapi dimatikan) karena dshost check
  dashboard menolak host non-loopback.
- Solusi: bind langsung ke IP tailscale + set basic auth.

## Hubungan
- [[Setup Sinkronisasi Vault Obsidian]] — server & sinkron
- [[Basis Pengetahuan Hermes]] — knowledge base