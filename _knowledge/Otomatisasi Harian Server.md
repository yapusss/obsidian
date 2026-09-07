---
type: catatan
created: 2026-09-07
source: hermes
---

# Otomatisasi Harian Server (Briefing, Monitoring, Todo)

## Ringkasan
Server yvserver punya rutinitas harian yang dikirim ke Telegram: briefing pagi,
monitoring resource, plus command /homesrv dan /todo. Semua berbasis Hermes cron,
script shell, dan skill command.

## Isi

### Cron (Hermes cron, zona: server UTC = WIB-7)
- Briefing Pagi: `30 23 * * *` (UTC) = 06.30 WIB, tiap hari. LLM job, baca vault
  Obsidian + /root/scripts/todo.sh, susun ringkasan komitmen/todo/catatan baru.
  Skill: obsidian, todo. Job id: 4073203b1cb1.
- Monitoring Resource Server: `0 0 * * *` (UTC) = 07.00 WIB, tiap hari.
  no_agent job, script homesrv.sh, stdout dikirim verbatim ke Telegram.
  Job id: 490315507611.
- Delivery: `all` = semua home channel yang terhubung, resolve saat fire.

### Command Telegram (/homesrv dan /todo)
- Skill dengan `metadata.hermes.commands[].slash` mendaftarkan command Telegram.
- `/homesrv` → skill `devops/homesrv` → jalankan /root/scripts/homesrv.sh:
  snapshot CPU, RAM, disk, uptime, load, suhu.
- `/todo` → skill `productivity/todo` → jalankan /root/scripts/todo.sh:
  baca item unchecked di /root/Obsidian/_todo/*.md, tampilkan yang belum selesai.

### Script
- /root/scripts/homesrv.sh dan /root/scripts/todo.sh (salinan cron di
  /root/.hermes/scripts/homesrv.sh — cron butuh path relatif ke ~/.hermes/scripts/).
- PENTING: script harus exit 0; exit non-zero membuat cron mengirim alert error.
  (kasus temp n/a yang bikin exit 1 sudah diperbaiki).

## Hubungan
- [[Peta Fitur Advance Hermes]] — konsep cron, Bot Mode, skill command
- [[Setup Sinkronisasi Vault Obsidian]] — vault tempat todo & auto-push
- [[Basis Pengetahuan Hermes]] — knowledge base tempat catatan ini