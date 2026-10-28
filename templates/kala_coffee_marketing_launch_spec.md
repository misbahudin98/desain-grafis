# Marketing Collateral Specification: Peluncuran KALA COFFEE Artisanal
> **Brand:** KALA COFFEE ROASTERS  
> **Campaign:** "The Slow Extraction" — Artisanal Amber Cold Brew Launch  
> **Target Media:** Flayer Cetak DIN A5 (ISO 216 / ISO 12647-2) & Carousel Feed 8 Slide (4:5 / 1080x1350px)  
> **Arsitek Desain:** Marketing Collateral Architect v1.0.0

---

## 1. SISTEM TOKEN DESAIN & IDENTITAS VISUAL

### 1.1 Palet Warna Kanonikal (Aturan 60-30-10 & Kontras WCAG AAA)
| Token Nama | Hex Code | sRGB (Digital) | CMYK (FOGRA39 Offset) | Pantone (PMS) | Proporsi & Fungsi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `color-base-obsidian` | `#0B0F19` | `11, 15, 25` | `75, 68, 60, 85` | Pantone Black 6 C | **60%** Kanvas latar gelap, teks pada media terang |
| `color-structure-amber` | `#D97706` | `217, 119, 6` | `16, 61, 100, 3` | Pantone 7564 C | **30%** Warna botol kaca amber, kartu struktural |
| `color-accent-emerald` | `#10B981` | `16, 185, 129` | `76, 0, 68, 0` | Pantone 339 C | **10%** Badge penawaran, tombol CTA, aksen titik fokus |
| `color-text-pure` | `#F8FAFC` | `248, 250, 252` | `2, 1, 0, 0` | Pantone 7541 C | Tipografi utama di atas kanvas gelap (Kontras 18.3:1) |
| `color-text-muted` | `#94A3B8` | `148, 163, 184` | `43, 31, 28, 0` | Pantone Cool Gray 6 C | Subtitle, detail teknis, CPL terukur (Kontras 7.8:1) |

### 1.2 Sistem Tipografi (Bringhurst Scale)
- **Display Headline:** *Neue Haas Grotesk* / *Inter Display* (Bobot: Bold 800, Tracking: `-0.02em`)
- **Subheadline & Navigation:** *Inter* (Bobot: SemiBold 600, Tracking: `-0.01em`)
- **Body Text:** *Inter* (Bobot: Regular 400, Line-height: `1.5`, CPL limit: 45–65 karakter per baris)
- **Monospace Metadata:** *JetBrains Mono* (Bobot: Medium 500, Tracking: `+0.05em`, Caps)

---

## 2. SPESIFIKASI FLAYER CETAK DIN A5 (ISO 216 / ISO 12647-2)

### 2.1 Parameter Geometris & Pre-Press Mutlak
- **Ukuran Potong Bersih (*Trim Size*):** $148 \times 210\text{ mm}$ (Rasio $\sqrt{2} \approx 1:1.414$)
- **Ukuran dengan Bleed (*Bleed Size*):** $154 \times 216\text{ mm}$ ($+3\text{mm}$ di keempat sisi luar)
- **Batas Margin Teks Aman (*Safe Margin*):** Minimal $5\text{mm}$ di dalam garis potong
- **Kerapatan Resolusi Raster:** $300\text{ DPI}$ murni
- **Mode Warna & Profil ICC:** CMYK dengan profil *PSO Coated v2 (FOGRA39)*
- **Total Area Coverage (TAC):** $\le 285\%$ (Aman dari bahaya *ink smudging/offsetting*)
- **Ketebalan Garis Minimum:** Garis pemisah hairline $\ge 0.25\text{pt}$ ($0.088\text{mm}$)

### 2.2 Tata Letak Zonal Flayer A5 (Optical Center & Gutenberg Gravity)
```
0mm ───────────────────────────────────────────────────────── (Puncak Kertas Trim)
     [ZONA 1: BRAND HEADER // Y: 5mm s/d 25mm]
     - Logomark: "KALA COFFEE ROASTERS" (Kiri atas, Inter SemiBold 12pt, tracking +0.05em)
     - Tag Kampanye: "EDISI TERBATAS BATCH 01 // 2026" (Kanan atas, JetBrains Mono 8pt)
     - Garis hairline 0.25pt Obsidian memisahkan header
25mm ────────────────────────────────────────────────────────
     
     [ZONA 2: OPTICAL CENTER HEADLINE // Y: 30mm s/d 75mm]
     - Titik Pusat Optik Mata (55% - 60% Ketinggian Kertas)
     - Kicker Teks: "SEDUHAN LAMBAT 24 JAM" (JetBrains Mono 9pt, Amber `#D97706`)
     - Headline Utama (3 Baris Display):
       "KETENANGAN RASA
        DALAM KACA AMBER
        MURNI."
       (Inter Display Bold, 28pt, Leading 32pt, Obsidian `#0B0F19`)
     - Subheadline: "Diekstraksi dingin dari mata air alpin dengan 100% Arabica Single Origin Gayo."
75mm ────────────────────────────────────────────────────────
     
     [ZONA 3: HERO PHOTOGRAPHY // Y: 75mm s/d 145mm]
     - Visual: Botol kaca amber tebal 250ml berembun dengan tutup ulir aluminium hitam.
       Label kertas katun bertekstur bertuliskan "KALA COLD BREW".
       Berdiri kokoh di atas batu basalt basah dengan percikan air mikro fotorealistik.
       (Pencahayaan studio kontras tinggi, bukaan f/5.6, 300 DPI CMYK).
145mm ───────────────────────────────────────────────────────
     
     [ZONA 4: 3 FITUR PILAR KUALITAS // Y: 145mm s/d 175mm]
     - Modul 3 Kolom Grid Swiss:
       * Kolom A: "4°C COLD EXTRACTION" — Ekstraksi lambat tanpa rasa asam berlebih.
       * Kolom B: "AMBER UV PROTECTION" — Menjaga aroma floral & dark chocolate utuh.
       * Kolom C: "ZERO PRESERVATIVES" — Murni tanpa gula tambahan atau pengawet.
175mm ───────────────────────────────────────────────────────
     
     [ZONA 5: CALL TO ACTION & KONTAK TERMINAL // Y: 175mm s/d 205mm]
     - Kotak Penawaran (Kiri): 
       "KLAIM DISKON 25% BATCH PERTAMA"
       Kode Voucher: KALA25 | Berlaku hingga 50 botol pertama.
     - QR Code Scanner (Kanan):
       Ukuran fisik $22 \times 22\text{mm}$, menghubungkan ke WhatsApp Direct Chat Admin.
     - Footer Teks: "Jl. Senopati No. 45, Kebayoran Baru, Jakarta Selatan // @kalacoffee.id"
210mm ─────────────────────────────────────────────────────── (Dasar Kertas Trim)
```

---

## 3. SPESIFIKASI CAROUSEL FEED INSTAGRAM & LINKEDIN (8 SLIDE // 4:5)

### 3.1 Parameter Teknis
- **Dimensi Kanonikal:** $1080 \times 1350\text{px}$ (Aspek Rasio 4:5 Vertikal)
- **Margin Padding Aman:** $100\text{px}$ Atas & Bawah, $80\text{px}$ Kiri & Kanan
- **Format Ekspor:**
  - Instagram: 8 berkas gambar PNG/JPEG terpisah ($1080\times 1350\text{px}$).
  - LinkedIn: 1 berkas dokumen PDF gabungan 8 halaman dengan resolusi seragam.

---

### 3.2 Cetak Biru Busur Cerita 8 Slide (Hook-to-Conversion Arc)

#### SLIDE 01: THE SCROLL-STOPPING HOOK
- **Tujuan:** Menghentikan scroll pengguna dalam 1.5 detik pertama.
- **Latar Belakang:** Hitam Obsidian pekat (`#0B0F19`) dengan tekstur partikel halus.
- **Top Bar:** Logo kecil `KALA COFFEE` di kiri, Slide tracker `01 / 08` di kanan.
- **Badge Kategori:** Kotak hijau emerald (`#064E3B`, teks `#10B981`): `CRAFT BEVERAGE REVOLUTION`.
- **Headline Janji Hasil (Display 56px, Leading 64px, Putih `#F8FAFC`):**  
  **"Kenapa Cold Brew Terbaik Tidak Pernah Memakai Botol Bening?"**
- **Sub-headline (Inter Regular 22px, `#94A3B8`):**  
  *Rahasia di balik perlindungan foton cahaya dan ekstraksi suhu 4°C.*
- **Visual Cue:** Potongan siluet tepi botol kaca amber di sisi kanan luar kanvas + Panah geser (`Geser untuk mengungkap rahasianya →`).

---

#### SLIDE 02: THE AGITATION / THE PROBLEM
- **Tujuan:** Membedah masalah umum yang sering dirasakan penikmat kopi.
- **Top Bar:** Slide tracker `02 / 08`.
- **Kicker:** `PERMASALAHAN UMUM` (Amber `#D97706`).
- **Headline (Inter Display 40px):**  
  **"Pernahkah Anda Meminum Cold Brew yang Terasa Datar dan Pahit Menusuk?"**
- **Body Copy (42 Kata, Inter 20px, `#CBD5E1`):**  
  "Sinar ultraviolet dan oksigen adalah musuh nomor satu senyawa aromatik kopi. Ketika kopi botolan terpapar cahaya rak toko hanya dalam 3 jam, minyak esensial mengalami fotooksidasi—menghilangkan kompleksitas rasa alami dan menyisakan rasa asam pahit yang hambar."
- **Infografis Kartu:** Ikon matahari bersilang ➔ Penurunan cita rasa hingga $60\%$.

---

#### SLIDE 03: THE SINGLE-ORIGIN HARVEST
- **Tujuan:** Memperkenalkan kualitas bahan baku murni.
- **Top Bar:** Slide tracker `03 / 08`.
- **Kicker:** `BAHAN BAKU PILIHAN`.
- **Headline (Inter Display 40px):**  
  **"Dimulai dari Ketinggian 1.600 MDPL Dataran Tinggi Gayo."**
- **Body Copy (45 Kata, Inter 20px):**  
  "Kami hanya memetik ceri kopi merah sempurna (*100% ripe red cherries*) varietas Typica dan Bourbon. Diproses secara natural dengan fermentasi anaerobik terkontrol untuk mengunci rasa manis buah berry dan body tebal seperti sutra."
- **Data Callout Box (JetBrains Mono):**  
  - Elevation: `1600 MASL`  
  - Variety: `Arabica Typica & Bourbon`  
  - Process: `Controlled Anaerobic Natural`

---

#### SLIDE 04: THE 24-HOUR CRYOGENIC EXTRACTION
- **Tujuan:** Menunjukkan keunggulan proses produksi yang sabar dan presisi.
- **Top Bar:** Slide tracker `04 / 08`.
- **Kicker:** `METODOLOGI KALA`.
- **Headline (Inter Display 40px):**  
  **"24 Jam Perendaman Lambat pada Suhu Presisi 4° Celsius."**
- **Body Copy (48 Kata, Inter 20px):**  
  "Kami tidak pernah memanaskan kopi. Menggunakan air yang telah difiltrasi mineral secara mikronis, kami mengekstraksi bubuk kopi selama 24 jam penuh di dalam ruangan pendingin steril. Hasilnya: tingkat keasaman lambung turun hingga $67\%$ dibanding seduhan kopi panas konvensional."
- **Visual Diagram Grid:** 
  `Air Alpin Terfilter + Suhu Dingin 4°C + Waktu 24 Jam = Ekstraksi Rendah Asam Lambung`.

---

#### SLIDE 05: THE AMBER GLASS SHIELD
- **Tujuan:** Memvalidasi jawaban dari pertanyaan hook di Slide 01.
- **Top Bar:** Slide tracker `05 / 08`.
- **Kicker:** `REKAYASA KEMASAN`.
- **Headline (Inter Display 40px):**  
  **"Botol Kaca Amber: Tameng Mutlak Terhadap Penuaan Rasa."**
- **Body Copy (46 Kata, Inter 20px):**  
  "Kaca amber tebal grade farmasi memblokir $99\%$ spektrum sinar UV berbahaya dan cahaya biru. Ini menjamin setiap tetes KALA Cold Brew yang menyentuh lidah Anda memiliki kesegaran dan profil aroma yang sama persis seperti saat pertama kali diekstraksi."
- **Highlight Tag:** `100% UV Protection // Kedap Udara // Dapat Didaur Ulang Selamanya`.

---

#### SLIDE 06: THE SENSORY PROFILE & TASTING NOTES
- **Tujuan:** Membangkitkan sensasi sensorik audiens (*mouth-watering effect*).
- **Top Bar:** Slide tracker `06 / 08`.
- **Kicker:** `PROFIL RASA RESMI`.
- **Headline (Inter Display 40px):**  
  **"Tiga Lapisan Rasa dalam Satu Tegukan Elegan."**
- **Tabel Rasa (3 Kartu Modular Swiss Grid):**
  1. **Top Note:** *Candied Citrus & Bergamot Blossom* (Segar dan memikat saat pertama menyentuh bibir).
  2. **Heart Note:** *Swiss Dark Chocolate & Toasted Hazelnut* (Sensasi cokelat hitam pekat di lidah).
  3. **Finish:** *Sweet Cedarwood & Honeycomb Lingering* (Rasa manis alami yang bertahan lama di tenggorokan).

---

#### SLIDE 07: THE EXECUTIVE CHEAT-SHEET (HIGH SAVE VALUE)
- **Tujuan:** Slide perbandingan ringkas bernilai rujukan tinggi yang memicu tombol simpan (*Saved Post*).
- **Top Bar:** Slide tracker `07 / 08`.
- **Kicker:** `PERBANDINGAN KUALITAS`.
- **Headline (Inter Display 36px):**  
  **"KALA Artisanal Cold Brew vs Kopi Botolan Biasa"**
- **Tabel Komparasi:**
  | Parameter | Kopi Botolan Biasa | KALA Cold Brew Artisanal |
  | :--- | :--- | :--- |
  | **Kemasan** | Plastik PET Bening (Tembus UV) | Kaca Amber Farmasi 250ml (Anti-UV) |
  | **Waktu Ekstraksi** | 2-4 Jam Kimiawi | 24 Jam Alami Suhu 4°C |
  | **Karakter Asam** | Asam Pahit Tajam di Lambung | Halus, Lembut, Nyaman di Lambung |
  | **Bahan Aditif** | Perisa & Pengawet Sintetis | 100% Biji Kopi Murni & Air Alpin |
- **Watermark:** `Simpan kartu ini untuk panduan memilih kopi harian Anda ↗`

---

#### SLIDE 08: THE CONVERSION CALL TO ACTION (CTA)
- **Tujuan:** Mengonversi perhatian audiens menjadi pemesanan langsung.
- **Top Bar:** Slide tracker `08 / 08`.
- **Badge Eksklusif:** `BATCH 01 // HANYA TERSEDIA 50 BOTOL PERTAMA`.
- **Headline Utama (Inter Display 44px, Emerald `#10B981`):**  
  **"Rasakan Ekstraksi Murni Hari Ini."**
- **Penawaran Terbatas:**  
  "Dapatkan potongan eksklusif $25\%$ untuk pemesanan botol pertama Anda dengan nomor seri kurasi."
- **Tombol Aksi Interaktif:**
  - *Di Instagram:* "Ketik **'COLDBREW'** di kolom komentar, dan link pemesanan langsung masuk ke DM Anda."
  - *Di LinkedIn / WhatsApp:* "Klik link di bio profil atau hubungi WhatsApp Concierge kami di **+62 811-2345-6789**."
- **Brand Signature:** Logomark KALA COFFEE + "Crafted with reverence in Jakarta."
