---
type: catatan
created: 2026-09-07
source: hermes
---

# Peta Fitur Advance Hermes (Goals, Agents, Lainnya)

## Ringkasan
Dokumentasi praktis fitur-fitur canggih Hermes Agent: Persistent Goals (/goal),
Agents (delegasi, Bot Mode, spawning), Kanban, Cron, Curator, execute_code,
dua arah vault. Disediakan untuk dipakai cepat saat perlu.

## Isi

### 1. Persistent Goals ("/goal")
- Fungsi: tujuan jangka panjang yang tetap hidup lintas giliran. Setelah tiap
  giliran, judge model ringan mengecek pencapaian; jika belum, Hermes otomatis
  injeksi perintah lanjutan dan terus bekerja sampai selesai / di-pause / clear /
  budget turn habis. Versi "Ralph loop" ala Codex CLI.
- Kapan dipakai: tugas yang butuh iterasi sendiri (bukan satu giliran).
  Contoh: "Fix semua lint error dan pastikan `ruff check` lolos";
  "Port fitur X + tests, lalu CI hijau".
- Batas tegas: /goal = SATU sesi. Tidak membuat kartu kanban, tidak menyerah ke
  profile lain, tidak fan-out. Untuk banyak tugas mandiri pakai Kanban.

### 2. Agents
Arti tergantung konteks:
- a) Subagent paralel (delegate_task): child agent berkonteks terisolasi +
  terminal sendiri. Default 3 paralel (delegation.max_concurrent_children).
  Leaf (tidak bisa menurunkan) vs orchestrator (bisa punya anak).
  Tidak durable: jika proses parent mati, anak hilang.
- b) Bot Mode: profile Hermes jadi "roster" Bot bernama, masing-masing punya
  role/model/memory/skills/avatar, bisa jalankan rutinitas, berunding di grup,
  saling kirim pesan. Bot = profile Hermes (~/.hermes/profiles/<name>/).
- c) Spawning proses Hermes penuh: `hermes chat -q` (one-shot) atau `hermes`
  (interaktif, pakai tmux). Proses mandiri, bertahan lama, akses tool penuh.
- d) Profiles: instansi independen ber-sesi/skills/memory terisolasi.

### 3. Fitur canggih lain
- Kanban: papan kerja multi-agent (SQLite). Banyak kartu tugas, tiap kartu
  dispatch ke worker process + sesi sendiri (toolset kanban_*). Ada dependensi,
  assignee, handoff. `hermes kanban create`. Kartu `--goal` meminjam mesin
  Ralph /goal dalam satu sesi worker.
- Cron: penjadwal durable, natural language / 5-field / durasi. Delivery ke
  platform mana pun, dukung chain job (context_from) + pre-run script
  (no_agent). Terlihat di `hermes cron list`.
- Curator: perawatan otomatis skill — lacak pemakaian, tandai stale, arsipkan,
  backup tar.gz sebelum tindakan. Hanya sentuh skill buatan agent,
  TIDAK pernah hapus (maks. archive), pinned dikecualikan.
- execute_code: tulis Python yang memanggil tool Hermes programatik, satukan
  pipeline multi-langkah jadi satu inference call.
- Batch Processing: jalankan Hermes di ratusan/ribuan prompt paralel (data
  ShareGPT) untuk training/evaluasi.
- Memory + Skills: memory = fakta singkat lintas sesi; skills = prosedur dari
  pengalaman, dimuat on-demand (hemat token).
- Context Files: otomatis baca AGENTS.md / .hermes.md / SOUL.md / CLAUDE.md /
  .cursorrules proyek untuk membentuk perilaku.
- @ references: ketik @ + referensi untuk inject file/folder/git-diff/URL.
- Checkpoints / /rollback: snapshot folder kerja sebelum ubah file, bisa rollback.
- MCP: konek ke MCP server untuk tool tambahan.
- Voice Mode: interaksi suara real-time di CLI/Telegram/Discord.

### 4. Relevansi khusus server yvserver (headless + Telegram)
- /goal: "rapikan vault, perbaiki wikilink mati, push ke GitHub" — jalan terus
  sampai selesai.
- Cron: auto-sync vault (sekarang via cron sistem; Hermes cron lebih kaya:
  delivery Telegram + attachment skill).
- Bot Mode: bot penulis catatan Obsidian lewat Telegram, bot monitoring server,
  bot briefing pagi.

## Hubungan
- [[Setup Sinkronisasi Vault Obsidian]] — tempat vault dan auto-sync
- [[Basis Pengetahuan Hermes]] — panduan knowledge base ini
- [[Obsidian - Catatan]] — dokumentasi vault