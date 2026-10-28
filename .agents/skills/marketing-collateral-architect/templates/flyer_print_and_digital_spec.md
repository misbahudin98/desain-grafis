# Template Spesifikasi Desain Flayer Cetak & Digital (flyer_print_and_digital_spec.md)
> **Engine Target:** Marketing Collateral Architect v1.0.0  
> **Standar:** ISO 216 Paper Sizes, ISO 12647-2 FOGRA39 CMYK, Optical Center & Gutenberg Hierarchy.

---

## 1. FORMULA STRUKTUR FLAYER KANONIKAL

```markdown
# SPESIFIKASI FLAYER: [NAMA KAMPANYE / PRODUK]
- **Tipe Format:** [DIN A4 / DIN A5 / DIN A6 / DL]
- **Dimensi Bersih (Trim):** [Contoh: 148 x 210 mm untuk A5]
- **Dimensi Total dengan Bleed (+3mm):** [Contoh: 154 x 216 mm]
- **Margin Aman Teks:** Minimum 5 mm dari garis potong
- **Ruang Warna:** CMYK (Profil: PSO Coated v2 / FOGRA39)
- **Kerapatan Resolusi:** 300 DPI mutlak

---

### STRUKTUR TATA LETAK ZONAL (GUTENBERG & OPTICAL CENTER)

#### ZONA 1: HEADER & IDENTITAS MEREK (Sudut Kiri Atas // Y: 5mm - 30mm)
- **Komponen:** Logomark Merek + Tag Kategori Promosi
- **Tipografi:** Sans-serif tegas (Inter SemiBold / 12pt)
- **Fungsi:** Menetapkan kredibilitas dan identitas pengirim pesan secara instan.

#### ZONA 2: TITIK PUSAT OPTIK & HEADLINE UTAMA (Optical Sweet Spot // Y: 35mm - 85mm)
- **Headline Utama:** [Janji Nilai / Diskon / Peluncuran Eksklusif]
- **Tipografi:** Display Bold (Neue Haas Grotesk / Inter Display, 28pt - 36pt)
- **Subheadline:** [Kalimat penjelas konteks dalam 1 baris, 14pt]
- **Fungsi:** Menangkap 80% perhatian pandangan mata pertama pengguna.

#### ZONA 3: HERO VISUAL & DEMONSTRASI PRODUK (Area Tengah // Y: 90mm - 145mm)
- **Visual Utama:** [Foto Produk Komersial Mewah / Visual Render 3D / Ilustrasi Fotorealistik]
- **Pencahayaan & Kontras:** Kontras tinggi terisolasi rapi dengan bayangan alami di atas kanvas.

#### ZONA 4: 3 FITUR UNGGULAN & NILAI MANFAAT (Area Bawah // Y: 150mm - 175mm)
- **Poin 1:** [Manfaat Konkret 1] (Ikon + Deskripsi 2 baris)
- **Poin 2:** [Manfaat Konkret 2] (Ikon + Deskripsi 2 baris)
- **Poin 3:** [Manfaat Konkret 3] (Ikon + Deskripsi 2 baris)

#### ZONA 5: CALL TO ACTION & TERMINAL KONTAK (Sudut Kanan Bawah // Y: 180mm - 205mm)
- **Tombol / Box CTA:** "Kunjungi Sekarang" / "Pesan Meja Anda" (Warna Aksen 10% Kontras Tinggi)
- **QR Code Cepat:** Dimensi minimal 20 x 20 mm dengan margin putih 2mm
- **Informasi Kontak:** Nomor WhatsApp resmi, URL Website, & Alamat Fisik
```

---

## 2. CONTOH IMPLEMENTASI SIAP PAKAI: FLAYER A5 PROMOSI COLD BREW ARTISANAL

```markdown
# SPESIFIKASI FLAYER: ARTISAN COLD BREW LAUNCH (DIN A5)
- Dimensi Trim: 148 x 210 mm | Bleed: 154 x 216 mm (+3mm) | Safe Margin: 5 mm
- Warna: CMYK FOGRA39 | Resolusi: 300 DPI | TAC: 280%

[ZONA 1: BRAND LOGO]
- Logo: "KALA COFFEE ROASTERS" (Kiri atas, tinggi 12mm, warna Obsidian `#0B0F19`)

[ZONA 2: OPTICAL CENTER HEADLINE]
- Headline: "SEDUHAN DINGIN DARI MATA AIR ALPIN."
- Subhead: "Diekstraksi lambat selama 24 jam dengan biji kopi Gayo terkurasi."

[ZONA 3: HERO PHOTOGRAPHY]
- Foto: Botol kaca amber dingin dengan tetesan embun alami di atas lempengan batu basalt.

[ZONA 4: 3 FITUR PILAR]
- 100% Arabica Single Origin
- Ekstraksi Suhu Rendah 4°C Rendah Asam Lambung
- Tanpa Bahan Pengawet Sintetis

[ZONA 5: CTA & TERMINAL KONTAK]
- CTA Box: "DAPATKAN DISKON 25% BATCH PERTAMA"
- QR Code: Tautan instan ke WhatsApp Chat Pemesanan
- Footer: Jl. Senopati No. 45, Jakarta Selatan // www.kalacoffee.id
```
