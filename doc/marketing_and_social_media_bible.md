# Kitab Standar Desain Pemasaran, Flayer, Banner, Carousel, & Stories (marketing_and_social_media_bible.md)
> **Engine:** Desain-Grafis Marketing SSoT Core v1.0.0  
> **Otoritas Acuan:** ISO 216, ISO 12647-2 (FOGRA39), IAB Tech Lab (LEAN Guidelines), Meta Platform Standards, LinkedIn Publishing Guidelines, Josef Müller-Brockmann, Robert Bringhurst.  
> **Status:** Single Source of Truth (SSoT) untuk Produksi Flayer, Banner IAB, Carousel Multi-Slide, dan Status/Stories Layar Penuh.

---

## 1. LANDASAN TEORITIS & OTORITAS DUNIA

Desain materi pemasaran (*marketing collateral*) bukanlah sekadar menaruh teks di atas foto acak, melainkan rekayasa komunikasi visual terstruktur yang menjembatani psikologi perhatian manusia (*cognitive attention span*) dengan batasan fisik medium:

1. **ISO 216 & ISO 12647-2 (Percetakan Presisi Dunia):** Mengatur standarisasi ukuran kertas berbasis rasio $\sqrt{2}$ (A-series) serta kendali proses cetak separasi warna CMYK, densitas tinta, dan profil ICC FOGRA39/GRACoL.
2. **IAB Tech Lab (Interactive Advertising Bureau):** Menetapkan arsitektur ukuran display iklan digital global dan prinsip LEAN (*Lightweight, Encrypted, AdChoices, Non-invasive*) untuk kecepatan muat halaman web tanpa latensi.
3. **Meta & WhatsApp Platform UI Standards:** Memetakan zona bahaya antarmuka (*interface danger zones*) ponsel pintar 9:16 agar elemen navigasi sistem tidak menutupi pesan penjualan utama.
4. **LinkedIn Document Ads & Instagram Swipe Dynamics:** Menetapkan format vertikal 4:5 ($1080\times 1350\text{px}$) sebagai rasio optimal untuk memaksimalkan *dwell time* dan retensi gestur geser.
5. **Gutenberg Reading Gravity & Optical Center Theory:** Menempatkan pesan terpenting pada titik keseimbangan optik mata manusia (55–60% dari batas bawah kanvas) mengikuti pola gravitasi diagonal kiri-atas ke kanan-bawah.

---

## 2. PANDUAN LENGKAP PRODUKSI FLAYER (PRINT & DIGITAL FLYER)

### 2.1 Peta Ukuran Fisik & Rekomendasi Penggunaan
| Ukuran Kertas | Dimensi Bersih (*Trim Size*) | Dimensi dengan Bleed (+3mm) | Target Penggunaan Ideal |
| :--- | :--- | :--- | :--- |
| **DIN A4** | $210 \times 297\text{ mm}$ | $216 \times 303\text{ mm}$ | Flayer korporat, katalog produk B2B, proposal penawaran, lembar spesifikasi |
| **DIN A5** | $148 \times 210\text{ mm}$ | $154 \times 216\text{ mm}$ | Hand-out promosi retail, kuliner, event seminar, pembagian langsung di jalan |
| **DIN A6** | $105 \times 148\text{ mm}$ | $111 \times 154\text{ mm}$ | Kartu pos diskon, voucher hadiah, undangan eksklusif meja kasir |
| **DIN DL** | $99 \times 210\text{ mm}$ | $105 \times 216\text{ mm}$ | Flayer vertikal menu restoran, brosur masuk amplop standar kantoran |

### 2.2 Aturan Baku Pra-Cetak (Pre-Press Checklist)
1. **Bleed Area ($+3\text{mm}$ Keliling):** Seluruh elemen visual latar belakang wajib ditarik menembus garis potong hingga ke garis bleed untuk mencegah munculnya celah putih saat pisau potong hidrolik bergeser $\pm 1.5\text{mm}$.
2. **Margin Aman Teks ($\ge 4\text{mm} - 5\text{mm}$):** Teks, logo, dan nomor kontak tidak boleh berada lebih dekat dari 5mm dari garis potong.
3. **Resolusi 300 DPI Mutlak:** Gambar wajib berkepadatan $\ge 300\text{ DPI}$ pada skala $100\%$. Dilarang memperbesar gambar 72 DPI dari internet.
4. **Ruang Warna CMYK FOGRA39:** Warna wajib CMYK dengan batas cakupan tinta maksimum (*Total Area Coverage / TAC*) $\le 300\%$ untuk mencegah kertas basah dan tinta luntur (*set-off*).
5. **Konversi Font ke Kurva (Create Outlines):** Seluruh tipografi pada berkas akhir PDF/X-1a wajib di-outline untuk mencegah font hilang di mesin cetak.

### 2.3 Formula Tata Letak Flayer Berbasis Titik Pusat Optik
```
┌────────────────────────────────────────────────────────┐ Y = 0 (Top Trim)
│ [HEADER KATEGORI / LOGO PERUSAHAAN]                    │ ➔ Sudut Kiri Atas
├────────────────────────────────────────────────────────┤
│                                                        │
│             TITIK PUSAT OPTIK (OPTICAL CENTER)         │ ➔ Area 55% - 60% Ketinggian
│          [HEADLINE UTAMA: PENAWARAN MENARIK]           │   (Upper-Third Eye Magnet)
│                                                        │
├────────────────────────────────────────────────────────┤
│                                                        │
│          [HERO IMAGE PRODUK / FOTO UTAMA]              │
│                                                        │
├────────────────────────────────────────────────────────┤
│                                                        │
│          [3 POIN KEUNGGULAN / FITUR KUNCI]             │
│                                                        │
├────────────────────────────────────────────────────────┤
│ [DETAIL KONTAK / LOKASI]           [CALL TO ACTION /]  │ ➔ Area Terminal Bawah
│                                    [QR CODE SCANNER ]  │   (Sudut Kanan Bawah)
└────────────────────────────────────────────────────────┘ Y = Tinggi Kertas
```

---

## 3. PANDUAN LENGKAP WEB DISPLAY & BANNER IAB

### 3.1 Dimensi Standar & Karakter Penempatan
| Nama Format | Dimensi Piksel | Karakter & Fungsi |
| :--- | :--- | :--- |
| **Medium Rectangle (MPU)** | $300 \times 250\text{px}$ | Unit paling laris di dunia. Melekat di sela paragraf artikel berita dan blog portal. |
| **Leaderboard** | $728 \times 90\text{px}$ | Bilah horizontal penanda identitas kampanye di puncak halaman website. |
| **Half Page / Large Tower** | $300 \times 600\text{px}$ | Kanvas vertikal megah yang memberikan ruang branding leluasa di bilah samping. |
| **Billboard** | $970 \times 250\text{px}$ | Unit premium lebar penuh di atas lipatan layar (*above the fold*) berdaya pikat tinggi. |
| **Social OpenGraph Banner** | $1200 \times 630\text{px}$ | Format pratinjau kartu saat tautan dibagikan di Twitter/X, WhatsApp, LinkedIn, dan Meta. |

### 3.2 Kepatuhan Arsitektur IAB LEAN
1. **Lightweight Asset (< 200 KB):** Bobot berkas awal aset banner statis/animasi wajib ringan agar tidak memperlambat waktu muat website pengguna.
2. **Batas Loop Animasi (Max 15 Detik):** Jika banner bergerak, durasi gerakan berhenti pada detik ke-15 pada frame penutup yang memuat tombol CTA jelas.
3. **Bingkai Kontras 1 Piksel:** Banner dengan latar putih wajib memiliki batas garis 1px solid abu-abu netral (`#CBD5E1`) di sekelilingnya.

---

## 4. PANDUAN LENGKAP CAROSEL MULTI-SLIDE (INSTAGRAM & LINKEDIN)

### 4.1 Mengapa Format 4:5 ($1080 \times 1350\text{px}$) Mendominasi?
Format 4:5 memakan $80\%$ tinggi layar ponsel pada aplikasi Instagram dan LinkedIn feed, memberikan luas visual $25\%$ lebih besar dibandingkan rasio 1:1 ($1080\times 1080\text{px}$). Luas ekstra ini meningkatkan waktu henti scrolling (*stop-rate*) dan angka keterbacaan tipografi.

### 4.2 Cetak Biru Busur Cerita 10 Slide (The 10-Slide Engagement Blueprint)
```
SLIDE 01: THE SCROLL-STOPPING HOOK
  - Janji hasil nyata (Outcome-Driven Headline) dalam 5-8 kata.
  - Tipografi Display Bold (Ukuran >= 60px).
  - Tanda visual ajakan geser (Swipe cue arrow).
      │
      ▼
SLIDE 02: THE PROBLEM / EMPATHY BRIDGE
  - Membedah tantangan nyata atau mitos umum yang dihadapi audiens.
  - Nada bicara relatable dan membangkitkan rasa ingin tahu (*curiosity gap*).
      │
      ▼
SLIDE 03 - 07: THE STEP-BY-STEP SOLUTION (THE MEAT)
  - Satu prinsip kunci per slide (Maksimal 40-60 kata per slide).
  - Skema tipografi: Subheadline Medium (24px) + Body Copy (18px) + Visual Diagram.
  - Elemen visual tersambung (*seamless graphic bleed*) di tepi kanan untuk memicu geser.
      │
      ▼
SLIDE 08: THE BIG REVELATION / CLIMAX
  - Rangkuman nilai paling berbobot atau 'aha-moment' yang memuaskan pembaca.
      │
      ▼
SLIDE 09: THE CHEAT SHEET / EXECUTIVE SUMMARY
  - Rangkuman satu slide ringkas yang sangat berharga untuk disimpan (*High Saveability*).
      │
      ▼
SLIDE 10: ACTION-ORIENTED CALL TO ACTION (CTA)
  - Aksi tunggal terfokus: "Ketik 'PANDUAN' di kolom komentar untuk mendapatkan dokumen lengkap".
```

### 4.3 Margin Aman Komponen Carousel
- Batas atas & bawah: Minimal **100px** untuk menghindari tabrakan dengan indikator slide counter (misal: `1/10`) dan bilah caption nama akun Instagram.
- Batas kiri & kanan: Minimal **80px** untuk ruang bernapas tipografi.

---

## 5. PANDUAN LENGKAP IMAGE STATUS & STORIES (WHATSAPP, IG, FB)

### 5.1 Spesifikasi Layar Penuh 9:16 ($1080 \times 1920\text{px}$)
Stories dan WhatsApp Status dirancang untuk pengalaman vertikal imersif satu tangan (*single-handed mobile experience*).

### 5.2 Pemetaan Koordinat Zona Bahaya UI (Danger Zones)
```
0px ───────────────────────────────────────────────────────── (Puncak Layar)
     ZONA BAHAYA ATAS (Tinggi: 270px / Y: 0 s/d 270px)
     - Progress Bar waktu cerita WhatsApp/IG
     - Avatar profil akun, nama pengirim, dan stempel jam
     - Tombol silang tutup (X)
270px ────────────────────────────────────────────────────────
     
     ZONA KONTEN AMAN UTAMA (SAFE ZONE CANVAS)
     - Koordinat X: 65px s/d 1015px (Lebar Bersih: 950px)
     - Koordinat Y (Organik): 270px s/d 1650px (Tinggi Bersih: 1380px)
     - Koordinat Y (Iklan Ads): 270px s/d 1250px (Tinggi Bersih: 980px)
     
1250px ─────────────────────────────────────────────────────── (Batas Bawah Iklan Berbayar)
     ZONA BAHAYA CTA IKLAN (Tinggi: 670px / Y: 1250 s/d 1920px)
     - Tombol "Swipe Up", "Install Now", "Kirim Pesan WhatsApp"
     - Stempel "Bersponsor / Sponsored"
1650px ─────────────────────────────────────────────────────── (Batas Bawah Status Organik)
     ZONA BAHAYA STATUS ORGANIK (Tinggi: 270px / Y: 1650 s/d 1920px)
     - Kolom teks ketik balasan (Reply Bar) WhatsApp / IG DM
     - Deretan tombol emoji reaksi cepat
1920px ─────────────────────────────────────────────────────── (Dasar Layar Ponsel)
```

### 5.3 Golden Rules untuk Status WhatsApp & Instagram Stories
1. **Aturan 3 Detik Pertama:** Headline atau visual hook harus dapat dicerna dalam 3 detik sebelum pengguna mengetuk (*tap*) layar untuk melompati cerita.
2. **Maksimal 1 Subjek Fokus:** Jangan mengisi satu layar status dengan 5 produk sekaligus; gunakan satu fokus visual tunggal dengan teks penjelas singkat.
3. **Kontras Ekstrem pada Latar:** Pastikan teks utama menggunakan latar penopang atau bayangan tipis terkalibrasi (*soft shadow*) agar tetap terbaca jelas di berbagai layar AMOLED maupun IPS berlayar redup.

---

## 6. LEMBAR AUDIT 20 POIN KUALITAS MATERI MARKETING SEBELUM PUBLIKASI

Sebelum mencetak flayer atau mengunggah banner/carousel/stories, periksa 20 kriteria ini:

### A. Dimensi & Aspek Rasio (Poin 1–4):
1. [ ] Flayer mematuhi standar ISO 216 (A4/A5/A6) dengan bleed $+3\text{mm}$.
2. [ ] Banner web mematuhi resolusi IAB resmi ($300\times 250$, $728\times 90$, $300\times 600$, $970\times 250$).
3. [ ] Carousel menggunakan rasio vertikal optimal 4:5 ($1080\times 1350\text{px}$) atau 1:1 ($1080\times 1080\text{px}$).
4. [ ] Status/Stories menggunakan rasio 9:16 ($1080\times 1920\text{px}$).

### B. Zona Aman & Antarmuka UI (Poin 5–8):
5. [ ] Flayer menjaga teks penting $\ge 5\text{mm}$ dari garis potong (*trim line*).
6. [ ] Status/Stories menjaga teks penting bebas dari zona bahaya atas ($Y < 270\text{px}$).
7. [ ] Status/Stories menjaga teks bebas dari bilah balasan bawah ($Y > 1650\text{px}$ untuk organik, $Y > 1250\text{px}$ untuk iklan).
8. [ ] Carousel menyisakan ruang margin minimal $80\text{px}$ di setiap sisi.

### C. Teknis Cetak & File Web (Poin 9–12):
9. [ ] Gambar flayer berkepadatan $300\text{ DPI}$ dalam ruang warna CMYK FOGRA39.
10. [ ] Total Area Coverage (TAC) tinta pada berkas flayer $\le 300\%$.
11. [ ] Aset banner web berbobot ringan ($\le 200\text{KB}$) sesuai pedoman LEAN IAB.
12. [ ] Banner berlatar putih memiliki garis batas keliling $1\text{px}$.

### D. Psikologi Perhatian & Tipografi (Poin 13–16):
13. [ ] Headline flayer berlabuh di titik pusat optik ($55\% - 60\%$ dari bawah).
14. [ ] Slide pertama carousel memiliki headline janji hasil dalam 5–8 kata kunci.
15. [ ] Setiap slide carousel hanya memuat 1 ide pokok dengan batas 40–60 kata.
16. [ ] Tipografi mematuhi skala modular dan kontras WCAG 2.2 AAA ($\ge 7:1$).

### E. Penawaran & Call To Action (Poin 17–20):
17. [ ] Terdapat Call to Action (CTA) tunggal yang jelas dan tidak membingungkan.
18. [ ] QR Code pada flayer memiliki ukuran fisik minimal $20\times 20\text{mm}$ dan kontras tinggi.
19. [ ] Nomor kontak WhatsApp disajikan dengan format internasional tanpa spasi rumit.
20. [ ] Seluruh klaim penawaran, harga, dan tanggal batas waktu (*deadline*) telah terverifikasi akurat.
