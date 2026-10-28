# Invarian Desain Marketing, Media Sosial, & Percetakan (social_and_marketing_design_invariants.md)
> **Engine:** Desain-Grafis Marketing Invariant Core v1.0.0  
> **Standar Dunia:** ISO 216 (Paper Sizing), ISO 12647-2 (FOGRA39 CMYK Print Control), IAB Tech Lab (LEAN Display Banner Standards), Meta Platform Ad Guidelines (Instagram, Facebook, WhatsApp Safe Zones), LinkedIn Carousel Standards.  
> **Target Media:** Flayer (Print/Digital Flyer), Web Banner (IAB/Display), Carousel (Multi-Slide 4:5), Image Status/Stories (9:16 WhatsApp, IG, FB).

---

## 1. INVARIAN FLAYER (PRINT & DIGITAL FLYER)

### 1.1 Standar Dimensi Fisik (ISO 216 Paper Sizes)
- **DIN A4 ($210 \times 297\text{ mm}$):** Flayer korporat, brosur teknis, dan surat promosi terlipat.
- **DIN A5 ($148 \times 210\text{ mm}$):** Ukuran paling populer dan efisien untuk hand-out promosi langsung, peluncuran produk, dan kuliner.
- **DIN A6 ($105 \times 148\text{ mm}$):** Kartu pos promosi mini, tiket voucher, dan *event flyer*.
- **DL ($99 \times 210\text{ mm}$):** Brosur vertikal sepertiga A4 untuk amplop kantor dan dudukan meja akrilik.

### 1.2 Ketentuan Cetak Presisi (Pre-Press Invariants - ISO 12647)
1. **Bleed Margin (+3mm / 0.125"):** Wajib menambahkan area lebihan pemotongan sebesar $3\text{mm}$ di keempat sisi luar dokumen. Gambar latar belakang dan blok warna wajib ditarik memenuhi garis bleed agar tidak terjadi tepi putih (*white hairline error*) saat pisau industri bergeser.
2. **Inner Safe Zone (Margin Aman $\ge 4\text{mm} - 5\text{mm}$):** Seluruh elemen tipografi kritis, logo, nomor kontak, dan teks penawaran wajib berada minimal $4\text{mm}$ di dalam garis potong (*trim line*).
3. **Resolusi Raster 300 DPI:** Seluruh citra fotografi wajib memiliki kerapatan minimal $300\text{ DPI}$ pada ukuran cetak 100%. Dilarang menggunakan citra 72 DPI layar web.
4. **Ruang Warna CMYK FOGRA39:** Seluruh palet wajib dikonversi ke CMYK dengan profil warna ICC *PSO Coated v2 (FOGRA39)* atau *GRACoL 2006*. Nilai *Total Area Coverage* (TAC) tinta tidak boleh melampaui $300\%$.
5. **Batas Ketebalan Garis Minimum (Hairline $\ge 0.25\text{pt}$ / $0.088\text{mm}$):** Garis vektor yang lebih tipis dari 0.25pt berisiko hilang saat proses separasi pelat cetak offset.

### 1.3 Komposisi Gravitasi Optik (Optical Center & Gutenberg Rule)
- **Titik Pusat Optik (Optical Center):** Mata manusia secara psikologis menganggap titik seimbang berada $55\% - 60\%$ dari dasar kertas (sedikit di atas titik tengah matematis $50\%$). Headline utama dan visual *hero* wajib berlabuh pada area sepertiga atas (*upper-third optical sweet spot*).
- **Aliran Bacaan Gravitasi (Reading Gravity):**
  - **Sudut Kiri Atas (Primary Optical Area):** Tempat menaruh nama merek, kategori pengumuman, atau logo.
  - **Sumbu Tengah-Atas (Strong Focus Area):** Tempat visual hero produk dan headline penawaran utama.
  - **Sudut Kanan Bawah (Terminal Area):** Tempat Call-to-Action (CTA), nomor WhatsApp, QR Code, dan alamat lokasi.

---

## 2. INVARIAN BANNER IAB & DISPLAY ADVERTISING

### 2.1 4 Ukuran Kanonikal IAB Display Ads
| Format Banner | Dimensi Piksel | Rasio | Penempatan Kunci |
| :--- | :--- | :--- | :--- |
| **Medium Rectangle (MPU)** | $300 \times 250\text{px}$ | 6:5 | Di dalam badan artikel editorial web, sidebar desktop & mobile |
| **Leaderboard** | $728 \times 90\text{px}$ | 8.09:1 | Header utama halaman web, tepat di bawah bilah navigasi menu |
| **Half Page / Large Skyscraper** | $300 \times 600\text{px}$ | 1:2 | Sidebar vertikal luas untuk visual storytelling produk premium |
| **Billboard** | $970 \times 250\text{px}$ | 3.88:1 | Puncak halaman web (*top hero expander*) dengan impresi visual tinggi |
| **OpenGraph / Social Card** | $1200 \times 630\text{px}$ | 1.91:1 | Thumbnail preview pratinjau tautan di X, LinkedIn, FB, WhatsApp |

### 2.2 Prinsip LEAN IAB Tech Lab
1. **Lightweight File Weight:**
   - Ukuran awal (*Initial Load*): Maksimal $\le 150\text{KB} - 250\text{KB}$.
   - Ukuran lanjutan (*Subload*): Maksimal $\le 500\text{KB}$ setelah halaman host tuntas termuat.
2. **Batas Durasi Animasi:** Durasi animasi HTML5/GIF maksimum **15 detik** dengan batas perulangan (*loop limit*) 3 kali.
3. **Bingkai Pembatas Kontras (1px Border):** Banner yang menggunakan latar putih atau transparan wajib memiliki garis batas keliling solid $1\text{px}$ (`#E2E8F0` atau `#94A3B8`) agar terpisah jelas dari konten redaksi portal web.
4. **Non-Intrusive Audio:** Audio dilarang berputar otomatis (*must be muted by default*). Kontrol suara "Sound On/Off" wajib disediakan secara eksplisit jika banner memuat audio.

---

## 3. INVARIAN CAROSEL (MULTI-SLIDE SOCIAL CAROUSEL)

### 3.1 Dimensi Kanonikal & Screen Real Estate
- **Rasio Emas 4:5 Vertikal ($1080 \times 1350\text{px}$):** Standar superior untuk Instagram Carousel dan LinkedIn Document PDF. Memaksimalkan area tampilan layar vertikal smartphone dan meningkatkan *scroll-stopping power* dibanding format bujur sangkar.
- **Rasio Alternatif 1:1 Bujur Sangkar ($1080 \times 1080\text{px}$):** Format standar untuk feed desktop dan kompatibilitas multi-platform.

### 3.2 Struktur Busur Narasi 7–10 Slide (Hook-to-Conversion Arc)
```
[SLIDE 1: THE HOOK] ➔ [SLIDE 2: THE AGITATION] ➔ [SLIDES 3-7: CORE VALUE] ➔ [SLIDE 8: CLIMAX] ➔ [SLIDE 9-10: CTA]
```
1. **Slide 1 — The Hook Slide (Penentu 80% Performa):**
   - Batas Teks: 5–8 kata kunci hasil/janji spesifik (*Outcome-driven headline*), bukan label kategori basi.
   - Ukuran Tipografi: Huruf display besar ($\ge 54\text{px} - 72\text{px}$).
   - Aksen Kontras: Latar belakang kontras tinggi yang menonjol di feed media sosial.
   - Petunjuk Geser (*Swipe Cue*): Tanda panah halus ($\rightarrow$) atau potongan grafis yang melintasi tepi kanan slide.
2. **Slide 2 — The Agitation / Context:** Membedah masalah mendasar atau rasa sakit pengguna mengapa hal ini sangat penting.
3. **Slide 3 s/d 7 — The Core Framework (Satu Ide Per Slide):**
   - Batas Kepadatan Kata: Maksimal 40–60 kata per slide. Dilarang menumpuk paragraf panjang.
   - Penomoran Progres: Indikator halaman eksplisit di sudut atas/bawah (misal: `03 / 08`).
   - Elemen Lintas-Batas (*Seamless Carousel*): Garis atau grafis yang tersambung mulus antar-slide untuk memancing gestur geser.
4. **Slide Terakhir — The Conversion CTA:**
   - Instruksi aksi tunggal yang jelas: *"Simpan postingan ini untuk rujukan nanti"*, *"Komentar 'PANDUAN' untuk menerima dokumen PDF lengkap"*, atau *"Klik tautan di profil"*.

### 3.3 Margin Aman Carousel
- Padding batas tepi minimal **80px hingga 100px** di keempat sisi agar teks tidak terpotong oleh antarmuka pagination bullet atau tombol simpan media sosial.

---

## 4. INVARIAN IMAGE STATUS & STORIES (WHATSAPP, IG, FB)

### 4.1 Dimensi Layar Penuh 9:16
- **Resolusi Standar:** $1080 \times 1920\text{px}$ (Aspek Rasio 9:16 vertikal murni).
- **Resolusi Ultra Retina:** $1440 \times 2560\text{px}$ (Proporsi matematis identik).

### 4.2 Peta Zona Bahaya UI Antarmuka (Overlay UI Danger Zones)
Pada antarmuka WhatsApp Status, Instagram Stories, dan Facebook Stories, layar ponsel tertutup oleh elemen sistemik aplikasi. Pelanggaran terhadap zona ini akan mengakibatkan teks penting tertutup:

```
┌────────────────────────────────────────────────────────┐ Y = 0px
│ [ZONA BAHAYA ATAS: 250px - 270px (14%)]                │
│ Progress Bar, Foto Profil Akun, Username, Tombol X     │
├────────────────────────────────────────────────────────┤ Y = 270px
│                                                        │
│                    ZONA AMAN UTAMA                     │
│               (SAFE CONTENT CANVAS AREA)               │
│                                                        │
│        Lebar Aman Horizontal: 950px                    │
│        Margin Kiri: 65px | Margin Kanan: 65px          │
│        Tinggi Aman: 1400px (Organic) / 980px (Ads)     │
│                                                        │
├────────────────────────────────────────────────────────┤ Y = 1650px (Organic)
│ [ZONA BAHAYA BAWAH: 250px - 270px (Organic)]           │
│ Kotak Pesan Balasan (Reply Box), Tombol Reaksi Emoji   │
├────────────────────────────────────────────────────────┤ Y = 1250px (Paid Ads)
│ [ZONA BAHAYA BAWAH IKLAN: 670px (35%)]                 │
│ Tombol Geser / Swipe-up CTA, Label "Bersponsor",       │
│ Tombol Interaksi Sudut Kanan Bawah (227x768px)         │
└────────────────────────────────────────────────────────┘ Y = 1920px
```

1. **Zona Bahaya Atas ($Y = 0\text{px}$ s/d $270\text{px}$):**
   - Area ini tertutup bilah durasi cerita (*progress bars*), avatar profil, nama akun, durasi waktu, dan tombol tutup.
   - **Larangan:** Dilarang meletakkan logo merek, headline judul, atau wajah subjek utama di atas $Y = 270\text{px}$.
2. **Zona Bahaya Bawah ($Y = 1650\text{px}$ s/d $1920\text{px}$ untuk Organik):**
   - Area ini tertutup bilah balasan pesan WhatsApp (*Reply text input*) dan tombol suka/reaksi cepat.
   - **Larangan:** Dilarang meletakkan teks instruksi, nomor kontak, atau alamat di bawah $Y = 1650\text{px}$.
3. **Zona Bahaya Bawah Iklan Berbayar ($Y = 1250\text{px}$ s/d $1920\text{px}$):**
   - Pada iklan berbayar (Meta Ads), tombol CTA (*Shop Now, Learn More, Send WhatsApp Message*) menempati area masif di bagian bawah.
   - **Larangan:** Seluruh teks krusial wajib berhenti di atas $Y = 1250\text{px}$.
4. **Margin Kiri & Kanan ($65\text{px}$ per sisi):**
   - Jarak aman minimal dari batas fisik kaca layar sentuh ponsel untuk menghindari terpotongnya teks pada layar berponi (*curved/rounded edge display*).
