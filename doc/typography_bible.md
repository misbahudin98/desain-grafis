# Kitab Suci Tipografi & Ritme Spasial (typography_bible.md)
> **Engine:** Desain-Grafis Typography Master Guide v1.0.0  
> **Fondasi Teoretis:** Robert Bringhurst (*The Elements of Typographic Style*), Jan Tschichold (*The Form of the Book*), Josef Müller-Brockmann, Massimo Vignelli.  
> **Status:** Single Source of Truth (SSoT) untuk Seluruh Pengarah Tipografi, Desainer Editorial, dan Agen AI.

---

## 1. HUKUM KELAYAKAN BACA ROBERT BRINGHURST

Robert Bringhurst menyatakan bahwa tipografi yang hebat adalah **arsitektur hening yang menghormati teks dan pembaca**:
1. Tipografi ada untuk menghormati isi teks, bukan untuk pamer ketangkasan desainer semata.
2. Huruf yang baik memikat pembaca ke dalam dunia pemikiran, bukan memaksanya mengagumi bentuk huruf itu sendiri.
3. Desain yang baik menyingkapkan makna dan struktur tanpa memaksakan ornamen asing.

---

## 2. ATURAN PANJANG BARIS IDEAL (OPTIMAL MEASURE: 45-75 CPL)

- **Rentang Optimal:** Panjang baris teks baca yang nyaman berkisar antara **45 hingga 75 karakter per baris (CPL)** termasuk spasi.
- **Titik Paling Sempurna:** **66 karakter per baris**.
- **Bahaya Baris Terlalu Panjang (> 85 CPL):** Otot mata manusia kelelahan saat berpindah dari ujung kanan baris ke awal baris berikutnya (*eye-tracking fatigue*), menyebabkan pembaca sering salah melompati baris.
- **Bahaya Baris Terlalu Pendek (< 35 CPL):** Ritme membaca terpotong-potong secara gelisah dan memicu terlalu banyak tanda hubung pemisah kata (*hyphenation bloat*).

---

## 3. SKALA MODULAR TIPOGRAFI MATEMATIS (MODULAR TYPE SCALES)

Dilarang keras memilih ukuran font berdasarkan "perasaan kira-kira". Gunakan rasio geometri terukur:

```
                      [TITIK KELAHIRAN: 16px BASE]
                                  │
       ┌──────────────────────────┴──────────────────────────┐
       ▼                                                     ▼
[SKALA MAJOR THIRD: 1.250]                       [GOLDEN RATIO: 1.618]
- 10.24px (Micro Caption)                        - 9.88px  (Fine Legal)
- 12.80px (Fine Body / Time)                     - 16.00px (Base Body Text)
- 16.00px (Base Body Text)                       - 25.88px (H4 Subtitle)
- 20.00px (H5 Lead / Card Title)                 - 41.88px (H3 Section)
- 25.00px (H4 Subheading)                        - 67.77px (H2 Header)
- 31.25px (H3 Section Header)                    - 109.66px(H1 Monumental)
- 39.06px (H2 Page Header)
- 48.83px (H1 Display Headline)
- 61.04px (Monumental Poster Title)
```

---

## 4. SISTEM GRID GARIS DASAR 8-POINT (8-PT BASELINE GRID)

1. Semua ukuran margin luar, padding kartu, tinggi baris (*line-height*), dan jarak antar elemen grafis wajib merupakan kelipatan dari $8\text{px}$ (atau unit sub-grid $4\text{px}$):
   $$\text{Ukuran} \in \{4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128\}\text{px}$$
2. Teks bodi $16\text{px}$ dipasangkan dengan *line-height* tepat $24\text{px}$ ($1.5\times$ rasio, kelipatan 8).
3. Judul $32\text{px}$ dipasangkan dengan *line-height* tepat $40\text{px}$ ($1.25\times$ rasio, kelipatan 8).
4. Hasil: Setiap paragraf dan judul di halaman yang berbeda akan selalu mengunci secara harmonis pada garis horizontal yang sama (*cross-column alignment*).

---

## 5. MIKRO-TIPOGRAFI: KERNING, TRACKING, DAN TANDA BACA GANTUNG

### A. Kerning & Tracking:
- **ALL CAPS (Huruf Kapital Semua):** Wajib diberi tracking renggang ($+0.05\text{em}$ hingga $+0.12\text{em}$). Huruf kapital dirancang untuk awal kalimat; jika dijejerkan bersamaan tanpa spasi tambahan, bentuknya saling bertabrakan secara visual.
- **Display Headlines ($\ge 32\text{px}$):** Wajib diberi tracking agak rapat ($-0.01\text{em}$ hingga $-0.03\text{em}$) dengan kerning optik agar kata tampak solid sebagai satu kesatuan grafis.
- **Teks Bodi Biasa:** Gunakan tracking normal ($0\text{em}$).

### B. Tanda Baca Gantung (Hanging Punctuation):
- Saat paragraf dibuka dengan tanda kutip pembuka (`"`), tanda kutip tersebut harus digantung di luar garis tepi kiri teks (*hung outside the left margin*), sehingga seluruh huruf pertama di setiap baris membentuk garis lurus vertikal yang tidak terganggu.

### C. Eliminasi Cacat Tipografi (Typographic Errors):
- **Dilarang *Widow* (Janda):** Baris terakhir paragraf yang hanya berisi satu kata pendek yang berdiri sendirian di bawah.
- **Dilarang *Orphan* (Yatim):** Baris pertama suatu bab atau paragraf yang tertinggal sendirian di bagian paling bawah halaman sebelum berpindah ke halaman baru.
- **Dilarang *Fake Italic* (Slanted):** Memiringkan font tegak secara paksa melalui software. Selalu gunakan berkas font True Italic yang digambar tangan oleh perancang huruf aslinya.
- **Dilarang *Fake Bold* (Stroked):** Menebalkan garis luar font regular secara paksa. Selalu gunakan bobot font SemiBold/Bold resmi.

---

## 6. MATRIKS PERPADUAN FONT MASTER (WORLD-CLASS PAIRINGS)

```
┌────────────────────────────────────────────────────────────────────────┐
│ MATRIKS PERPADUAN FONT INTERNASIONAL                                   │
├────────────────────────────────────────────────────────────────────────┤
│ [1. THE EDITORIAL HERITAGE (Sastra, Seni, Firma Hukum Mewah)]          │
│     Display:   Playfair Display / Fraunces (Serif Berwibawa)           │
│     Body Text: Inter / Plus Jakarta Sans (Sans-Serif Sangat Terbaca)   │
│     Monospace: JetBrains Mono                                          │
├────────────────────────────────────────────────────────────────────────┤
│ [2. THE SWISS RATIONALIST (Desain Produk, Korporasi Global, UI/UX)]     │
│     Display:   Neue Haas Grotesk / Inter Display                       │
│     Body Text: Inter (Regular / Medium)                                │
│     Monospace: Space Mono / IBM Plex Mono                              │
├────────────────────────────────────────────────────────────────────────┤
│ [3. THE BAUHAUS INDUSTRIAL (Teknik, Arsitektur, Otomotif, Manufaktur)] │
│     Display:   Futura / Satoshi Bold                                   │
│     Body Text: Work Sans / General Sans                                │
│     Monospace: Fragment Mono                                           │
└────────────────────────────────────────────────────────────────────────┘
```
