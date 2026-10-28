# Invarian Tipografi & Tata Letak Modular Grid Internasional (typography_and_layout_invariants.md)
> **Engine:** Desaiin-Grafis Typography Core v1.0.0  
> **Standar Dunia:** Josef Müller-Brockmann (*Grid Systems in Graphic Design*), Robert Bringhurst (*The Elements of Typographic Style*), Jan Tschichold (*Die neue Typographie*), Wim Crouwel, Massimo Vignelli (*The Vignelli Canon*), Ellen Lupton (*Thinking with Type*), WCAG 2.2 AAA.  
> **Aplikasi:** Editorial Layout, Brand Guidelines, UI/UX Posters, Pitch Decks, Social Media Typography.

---

## 1. MANDAT TATA LETAK & TIPOGRAFI TINGKAT DUNIA

Tipografi bukan sekadar memilih jenis huruf yang terlihat indah. Tipografi adalah arsitektur informasi visual yang mengatur ritme pembacaan, kejelasan kognitif, dan kepatuhan hierarki matematis.

```
┌────────────────────────────────────────────────────────────────────────┐
│ 7 PILAR MATEMATIKA TIPOGRAFI & SISTEM GRID MODULAR                     │
├────────────────────────────────────────────────────────────────────────┤
│ 1. [TYPO-01] SWISS_MODULAR_GRID_SYSTEM (Kolom, Gutters, Baseline)     │
│ 2. [TYPO-02] BRINGHURST_OPTIMAL_MEASURE (45–75 Karakter per Baris)     │
│ 3. [TYPO-03] MODULAR_TYPE_SCALE (Skala Musik Matematis 1.25 / 1.618)  │
│ 4. [TYPO-04] VERTICAL_RHYTHM_AND_LEADING (Rasio Line-Height Progresif) │
│ 5. [TYPO-05] FONT_PAIRING_DISCIPLINE (Harmoni Kontras, No Conflicting) │
│ 6. [TYPO-06] OPTICAL_KERNING_AND_TRACKING (Koreksi Spasi Huruf Mata)  │
│ 7. [TYPO-07] UNIVERSAL_LEGIBILITY_AND_CONTRAST (WCAG 2.2 AAA ≥ 7:1)   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. SISTEM GRID MODULAR SWISS (JOSEF MÜLLER-BROCKMANN)

Setiap karya grafis statis maupun dinamis WAJIB dibangun di atas fondasi grid struktural:

### A. Anatomi Grid:
1. **Marginal Bands (Margin):** Ruang bernapas luar yang membingkai kanvas. DILARANG teks menyentuh atau berjarak kurang dari 5% dari tepi kanvas.
2. **Columns (Kolom):**
   - Media Sosial & Poster Sederhana: 4 s/d 6 Kolom.
   - Majalah / Publikasi Editorial & Web: 12 Kolom.
   - Perangkat Mobile: 4 Kolom.
3. **Gutters (Jarak Antar Kolom):** Ruang kosong penahan antar-kolom (standar: 16px, 20px, atau 24px) untuk mencegah percampuran teks secara visual.
4. **Hanglines & Flowlines:** Garis horizontal konsisten tempat elemen judul atau gambar mulai digantungkan di setiap halaman.
5. **Baseline Grid (8-Point Grid System):** Seluruh ukuran font, jarak margin, dan *line-height* wajib merupakan kelipatan matematis dari $4\text{px}$ atau $8\text{px}$ ($8, 16, 24, 32, 40, 48, 64, 80\text{px}$).

---

## 3. SKALA MODULAR TIPOGRAFI MATEMATIS (MODULAR SCALE)

DILARANG menentukan ukuran huruf secara acak. Terapkan rasio modular geometris yang mencerminkan harmoni tangga nada musik:

| Tingkat Hierarki | Rasio Major Third ($1.250$) | Rasio Golden Ratio ($1.618$) | Fungsi Penerapan |
| :--- | :--- | :--- | :--- |
| **Micro Caption / Legal** | $10\text{px}$ | $9\text{px}$ | Metadata, hak cipta, label mikro, disclaimer |
| **Small / Body Fine** | $12\text{px}$ | $11\text{px}$ | Keterangan gambar, sub-teks, penanda waktu |
| **Base Body Text** | **$16\text{px}$** | **$16\text{px}$** | Standar teks baca utama (Body paragraph) |
| **Lead Paragraph / H5** | $20\text{px}$ | $21\text{px}$ | Paragraf pembuka, subjudul artikel |
| **Subheading / H4** | $25\text{px}$ | $26\text{px}$ | Judul seksi bagian dalam dokumen |
| **Major Header / H3** | $31.25\text{px} \approx 32\text{px}$ | $42\text{px}$ | Judul bab atau judul kartu utama |
| **Section Header / H2** | $39\text{px} \approx 40\text{px}$ | $68\text{px}$ | Judul seksi utama (*Section Title*) |
| **Hero Display / H1** | $48.8\text{px} \approx 48\text{px}$ | $110\text{px}$ | Headline halaman, judul poster utama |
| **Massive Poster Title** | $61\text{px}$ s/d $76\text{px}$ | $178\text{px}$ | Tipografi pajangan monumental (*Display Art*) |

---

## 4. ATURAN HIERARKI & KENYAMANAN BACA (ROBERT BRINGHURST)

1. **Batas Ukuran Baris Ideal (*Optimal Measure*):**
   - Panjang baris teks baca wajib berkisar antara **45 hingga 75 karakter per baris (CPL)** termasuk spasi. Panjang terbaik untuk kenyamanan mata adalah **66 karakter**.
   - DILARANG membiarkan teks satu kalimat membentang horizontal tanpa batas melintasi layar atau poster lebar.
2. **Proporsi *Leading* (Line Height):**
   - Teks bodi (*body copy*): Rasio leading berkisar antara $140\%$ hingga $160\%$ dari ukuran font (misal font $16\text{px}$ menggunakan leading $24\text{px}$).
   - Headline / Judul Besar: Gunakan leading yang lebih rapat ($105\%$ hingga $115\%$) agar judul tetap terbaca sebagai satu kesatuan visual yang solid (*tight tracking*).
3. **Koreksi *Kerning* & *Tracking*:**
   - **Teks Kapital Semua (ALL CAPS):** WAJIB diberi *letter-spacing* positif ($+5\%$ s/d $+12\%$) untuk menghindari tabrakan optik.
   - **Judul Besar (*Display Headlines*):** WAJIB menggunakan tracking agak negatif ($-1\%$ s/d $-3\%$) dengan kerning optik (*optical kerning*) agar spasi antar-huruf terlihat seimbang dan kokoh.
   - **Teks Bodi Biasa:** Gunakan *normal tracking* ($0\%$) tanpa manipulasi paksa.

---

## 5. MATRIKS PERPADUAN FONT BERSTANDAR INTERNASIONAL (FONT PAIRING MATRIX)

Hukum emas: **Kombinasikan Font Melalui Kontras Tajam, Bukan Kemiripan yang Menyerupai.** Dilarang memasangkan dua font Serif berbeda yang mirip satu sama lain atau dua Sans-Serif geometris yang hampir serupa.

| Gaya Desain | Font Judul (Display / Primary) | Font Bodi (Reading / Secondary) | Font Teknis / Monospace | Karakter & Suasana Visual |
| :--- | :--- | :--- | :--- | :--- |
| **Swiss Modernist** | Helvetica Neue / Neue Haas Grotesk | Inter / Univers | Space Mono | Rasional, objektif, netral, kejelasan absolut |
| **Quiet Luxury / Editorial** | Playfair Display / Cormorant Garamond | Plus Jakarta Sans / Literata | JetBrains Mono | Anggun, terpelajar, warisan agung (*heritage*), bernilai tinggi |
| **Bauhaus Geometric** | Futura Bold / Montserrat | Satoshi / Work Sans | IBM Plex Mono | Geometris murni, fungsional, industrial, berkarakter tegas |
| **Silicon Valley Tech** | General Sans / Geist | Inter / Roboto | Fira Code / Geist Mono | Modern, presisi, cepat, ramah pengembang |
| **Nordic Minimalist** | Syne / Outfit | DM Sans | Fragment Mono | Bersih, sejuk, kontemporer, berkarakter avant-garde |
| **Brutalist / Editorial High-End** | PP Editorial New / Fraunces | Neue Montreal | DM Mono | Dinamis, artistik, provokatif, berani |

---

## 6. AKSESIBILITAS & RASIO KONTRAS WCAG 2.2 AAA

1. **Rasio Kontras Teks Normal:** Minimal **$7:1$** terhadap latar belakang (Standar AAA) untuk teks bodi ($\le 18\text{px}$).
2. **Rasio Kontras Teks Besar:** Minimal **$4.5:1$** untuk teks judul besar ($\ge 18\text{px}$ bold atau $\ge 24\text{px}$ regular).
3. **Warna Teks:** DILARANG menggunakan hitam pekat murni `#000000` di atas putih murni `#FFFFFF` untuk teks panjang karena menyebabkan ketegangan mata optik (*halation effect*). Gunakan warna Slate gelap seperti `#0F172A` atau `#1E293B` di atas latar abu-abu sejuk atau putih gading lembut.
