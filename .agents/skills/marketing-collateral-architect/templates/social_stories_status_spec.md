# Template Spesifikasi Image Status & Stories Layar Penuh (social_stories_status_spec.md)
> **Engine Target:** Marketing Collateral Architect v1.0.0  
> **Platform:** WhatsApp Status, Instagram Stories, Facebook Stories  
> **Dimensi Kanonikal:** 1080 x 1920 px (Aspek Rasio 9:16 Vertikal Penuh)

---

## 1. STRUKTUR GRID & PEMBAGIAN ZONAL 9:16

```markdown
# SPESIFIKASI IMAGE STATUS / STORIES: [JUDUL PESAN]
- **Dimensi Kanonikal:** 1080 x 1920 px (9:16)
- **Tipe Kampanye:** [Status Organik / Iklan Stories Berbayar (Meta Ads)]
- **Margin Batas Samping:** 65 px (Kiri & Kanan)

---

### TABEL ZONAL VERTIKAL (SAFE ZONE COORDINATES)

| Zona Vertikal | Rentang Sumbu Y | Status Keamanan | Isi Komponen yang Diizinkan |
| :--- | :--- | :--- | :--- |
| **Zona Header UI** | $0\text{px} - 270\text{px}$ | ❌ **DANGER ZONE** | Hanya latar belakang pemandangan/kanvas kosong. DILARANG menaruh logo, teks judul, atau wajah orang di sini. |
| **Zona Pesan Utama** | $270\text{px} - 1250\text{px}$ | ✅ **ULTIMATE SAFE ZONE** | Headline utama, visual hero produk, sub-penjelasan, harga diskon, dan elemen nilai penting. |
| **Zona Khusus Organik** | $1250\text{px} - 1650\text{px}$ | ⚠️ **SAFE FOR ORGANIC ONLY** | Boleh diisi teks penutup pada status organik non-iklan. |
| **Zona Footer UI** | $1650\text{px} - 1920\text{px}$ | ❌ **DANGER ZONE** | Area reply box WhatsApp, bilah komentar DM Instagram, dan tombol reaksi stiker. |
| **Pengecualian Iklan** | $1250\text{px} - 1920\text{px}$ | ❌ **ADS DANGER ZONE** | Area tombol geser CTA ("Kunjungi Toko", "Kirim WhatsApp"), label Bersponsor, dan tombol interaksi samping. |
```

---

## 2. TEMPLATE KONTRAK STATUS WHATSAPP / IG STORY SIAP PAKAI

```markdown
### RANCANGAN STATUS 9:16: [KAMPANYE FLASH SALE 24 JAM]

[0px s/d 270px: UI SAFE PADDING]
- Latar gradien gelap `#0B0F19` ke `#1E293B` tanpa teks.

[270px s/d 450px: BRAND & HOOK]
- Tagline: "PENAWARAN HARI INI // HANYA 24 JAM" (JetBrains Mono, 16px, Emerald `#10B981`)
- Headline Utama: "HEMAT 40% UNTUK 50 PEMBELI PERTAMA." (Inter Display Bold, 48px, Putih `#F8FAFC`)

[450px s/d 1150px: HERO PRODUCT SHOWCASE]
- Visual: Foto botol parfum kaca amber di atas batu basalt basah (diisolasi tajam).
- Badge Diskon: Lingkaran geometris $120\times 120\text{px}$ di sudut produk bertuliskan "-40%".

[1150px s/d 1350px: SYARAT & KETENTUAN SINGKAT]
- 1 Baris Teks: "Gunakan kode kupon: FLASH40 saat checkout di website kami."

[1350px s/d 1600px: ARROW CALL TO ACTION]
- Simbol Panah Berkedip / Petunjuk Balas Chat:
  "Balas status ini untuk klaim voucher langsung dari admin kami ↓"

[1650px s/d 1920px: RESERVED UNTUK WHATSAPP REPLY BAR]
- Kanvas kosong bersih untuk ruang mengetik balasan pengguna.
```
