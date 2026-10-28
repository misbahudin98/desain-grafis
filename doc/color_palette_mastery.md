# Panduan Penguasaan Palet Warna & Penataan Sinematik (color_palette_mastery.md)
> **Engine:** Desaiin-Grafis Color Harmony System v1.0.0  
> **Fondasi:** Johannes Itten (*Bauhaus*), Josef Albers (*Yale*), DaVinci Resolve Academy, Kodak & Fujifilm Motion Picture Laboratories.  
> **Status:** Single Source of Truth (SSoT) untuk Desain Brand, Tipografi, Gradasi Digital, dan Prompting AI.

---

## 1. STRUKTUR DISTRIBUSI WARNA 60-30-10

Dalam setiap kanvas grafis, antarmuka aplikasi, maupun frame sinematik, warna didistribusikan secara hierarkis:

```
┌────────────────────────────────────────────────────────────────────────┐
│ [60%] WARNA DOMINAN NETRAL                                             │
│ - Membangun suasana (mood) dan ruang bernapas mata (visual calm).       │
│ - Nilai saturasi rendah (< 15%), luminansi terkontrol.                │
├───────────────────────────────────────────────────┬────────────────────┤
│ [30%] WARNA STRUKTURAL                            │ [10%] WARNA AKSEN  │
│ - Membentuk kontur, teks utama, batas kartu,      │ - Titik fokus mata │
│   atau kostum karakter. Kontras tinggi thd dominan│   CTA, rim light   │
└───────────────────────────────────────────────────┴────────────────────┘
```

---

## 2. 7 KONTRAK WARNA JOHANNES ITTEN (BAUHAUS)

Johannes Itten membedah bahwa mata manusia merespons kontras visual melalui 7 gerbang persepsi:
1. **Hue Contrast:** Mempertemukan warna murni (Merah, Kuning, Biru) yang memiliki saturasi tinggi. Menghasilkan energi visual primitif dan kuat.
2. **Light-Dark Contrast:** Membedakan elemen berdasarkan luminansi. Fondasi dari hierarki keterbacaan tipografi dan teknik pencahayaan *Chiaroscuro*.
3. **Cold-Warm Contrast:** Hubungan dinamis antara warna dingin (Cyan, Indigo, Emerald) dan warna hangat (Amber, Terracotta, Gold). Warna hangat tampak maju mendekati mata penonton; warna dingin tampak mundur ke kejauhan.
4. **Complementary Contrast:** Dua warna berseberangan $180^\circ$ pada roda warna (contoh: Navy & Gold, Teal & Terracotta). Mengunci mata penonton dalam kesetimbangan optik.
5. **Simultaneous Contrast:** Fenomena biologis mata yang secara otomatis memunculkan bayangan warna komplementer pada area netral di sekitar warna jenuh.
6. **Saturation Contrast:** Memadukan warna murni berkilau dengan warna kelabu atau teredam (*muted/dusty tones*).
7. **Extension Contrast:** Menyeimbangkan bobot cahaya warna dengan rasio luas bidang. Contoh: Kuning memiliki daya pantul cahaya $3\times$ lebih terang dari Ungu, sehingga bidang Kuning harus berukuran $\frac{1}{3}$ dari bidang Ungu agar seimbang.

---

## 3. MASTER COLOR PALETTES PRE-CALIBRATED

Berikut adalah 5 palet warna master berkarakter tinggi yang telah terkalibrasi secara matematis untuk kepatuhan WCAG 2.2 AAA ($\text{rasio kontras} \ge 7:1$):

### PALET 1: HERITAGE OBSIDIAN & EMERALD (LUXURY, LAW, & FINANCE)
*Cocok untuk: Brand hukum, notaris, investasi perbankan swasta, arsitektur premium.*
- **Dominant Base (60%):** `#0B0F19` (Obsidian Midnight, sRGB: 11, 15, 25)
- **Secondary Structure (30%):** `#F8FAFC` (Alabaster Snow, sRGB: 248, 250, 252)
- **Accent Focal (10%):** `#10B981` (Luminous Emerald, sRGB: 16, 185, 129)
- **Subtle Border Hairline:** `#1E293B` (Dark Slate Border, sRGB: 30, 41, 59)
- **Auxiliary Gold:** `#D97706` (Muted Amber Gold, sRGB: 217, 119, 6)
- **Rasio Kontras Teks:** `#F8FAFC` di atas `#0B0F19` = **$17.8:1$ (Lulus AAA)**.

### PALET 2: NORDIC EDITORIAL MINIMALISM (STUDIO, ART, ARCHITECTURE)
*Cocok untuk: Majalah seni, pameran galeri, brand fashion berkelanjutan.*
- **Dominant Base (60%):** `#F1F5F9` (Nordic Mist, sRGB: 241, 245, 249)
- **Secondary Structure (30%):** `#0F172A` (Charcoal Ink, sRGB: 15, 23, 42)
- **Accent Focal (10%):** `#0284C7` (Cobalt Ice, sRGB: 2, 132, 199)
- **Subtle Border Hairline:** `#CBD5E1` (Soft Stone, sRGB: 203, 213, 225)
- **Rasio Kontras Teks:** `#0F172A` di atas `#F1F5F9` = **$16.2:1$ (Lulus AAA)**.

### PALET 3: CYBERNETIC NOIR & VOLUMETRIC CYAN (HIGH-TECH & SCI-FI)
*Cocok untuk: Video game, sistem AI canggih, sinematografi fiksi ilmiah.*
- **Dominant Base (60%):** `#030712` (Void Black, sRGB: 3, 7, 18)
- **Secondary Structure (30%):** `#1E293B` (Tungsten Slate, sRGB: 30, 41, 59)
- **Accent Focal (10%):** `#06B6D4` (Bioluminescent Cyan, sRGB: 6, 182, 212)
- **Warning Indicator:** `#F59E0B` (Hazard Amber, sRGB: 245, 158, 11)
- **Text Primary:** `#F8FAFC` (Pure Starlight, sRGB: 248, 250, 252)

### PALET 4: MEDITERRANEAN TERRACOTTA & WARM SAGE (LIFESTYLE & GASTRONOMY)
*Cocok untuk: Restoran kelas atas, produk kerajinan tangan, resort tepi laut.*
- **Dominant Base (60%):** `#FDFBF7` (Warm Ecru Canvas, sRGB: 253, 251, 247)
- **Secondary Structure (30%):** `#292524` (Warm Espresso, sRGB: 41, 37, 36)
- **Accent Focal (10%):** `#C2410C` (Baked Terracotta, sRGB: 194, 65, 12)
- **Harmonic Tone:** `#047857` (Deep Sage, sRGB: 4, 120, 87)

---

## 4. FORMULA PERHITUNGAN KONTRAS WCAG 2.2 AAA

Kontras warna antara teks dan latar belakang dihitung berdasarkan Luminansi Relatif ($L$):
$$L = 0.2126 R + 0.7152 G + 0.0722 B$$
di mana masing-masing komponen $R, G, B$ dinormalisasi ke skala linear $0$ hingga $1$.

Rasio Kontras ($CR$) didefinisikan sebagai:
$$CR = \frac{L_1 + 0.05}{L_2 + 0.05}$$
(di mana $L_1$ adalah luminansi yang lebih terang, dan $L_2$ adalah luminansi yang lebih gelap).
- **Target Standar AAA (Teks Normal):** $CR \ge 7.0:1$
- **Target Standar AAA (Teks Besar $\ge 24\text{px}$):** $CR \ge 4.5:1$

---

## 5. EMULASI FILM STOCK & LUT KANONIKAL DALAM PROMPT AI

Untuk memberikan bobot organik pada visual AI, gunakan deskripsi emulasi kimia film berikut:
- **Kodak Vision3 500T (5219):** `Kodak Vision3 500T tungsten motion picture film stock, rich organic grain, soft halation around practical lights, balanced warm highlights and deep neutral shadows`.
- **Kodak Portra 400:** `Shot on 35mm Kodak Portra 400, luminous natural warm skin tones, soft pastel highlights, fine grain structure, daytime editorial look`.
- **Fujifilm Superia Reala:** `Fujifilm Superia color grade, subtle cyan-green undertones in deep shadows, vivid natural greens, lifelike daylight rendering`.
- **CineStill 800T:** `CineStill 800T tungsten color profile, distinctive red halation rings blooming around neon lights, moody night street atmosphere`.
