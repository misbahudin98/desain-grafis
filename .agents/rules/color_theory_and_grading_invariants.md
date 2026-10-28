# Invarian Teori Warna & Penataan Warna Sinematik (color_theory_and_grading_invariants.md)
> **Engine:** Desain-Grafis Color Core v1.0.0  
> **Standar Dunia:** Johannes Itten (*The Art of Color* - Bauhaus), Josef Albers (*Interaction of Color*), DaVinci Resolve Academy Grading Standards, Kodak/Fujifilm Cine Stocks, WCAG 2.2 AAA.  
> **Aplikasi:** Visual Prompting, Color Palettes, Brand Guidelines, Video LUTs, UI/UX Color Tokens.

---

## 1. MANDAT TEORI WARNA INTERNASIONAL

Warna adalah bahasa emosional pertama yang diproses oleh otak manusia sebelum bentuk atau kata-kata. Desain kelas dunia tidak menggunakan warna secara serampangan atau berlebihan. Repositori ini mewajibkan disiplin warna berbasis harmoni matematis dan psikologi persepsi.

```
┌────────────────────────────────────────────────────────────────────────┐
│ 7 ATURAN BAKU PENATAAN WARNA (COLOR DISCIPLINE INVARIANTS)             │
├────────────────────────────────────────────────────────────────────────┤
│ 1. [COL-01] THE_60_30_10_RULE (Distribusi Keseimbangan Visual)        │
│ 2. [COL-02] ITTEN_7_COLOR_CONTRASTS (Kontras Warna Murni Bauhaus)      │
│ 3. [COL-03] COLOR_PSYCHOLOGY_MAPPING (Kesesuaian Emosi & Bounded Context│
│ 4. [COL-04] CINE_FILM_STOCK_EMULATION (Kodak Vision3, Portra, Fuji)    │
│ 5. [COL-05] COMPLEMENTARY_SPLIT_GRADING (Teal & Orange Separation)     │
│ 6. [COL-06] NO_AGGRESSIVE_FLUORESCENCE (Larangan Neon Toksik AI)       │
│ 7. [COL-07] WCAG_2_2_AAA_COLOR_CONTRAST (Rasio ≥ 7:1 untuk Teks)      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. ATURAN EMAS DISTRIBUSI WARNA (THE 60-30-10 RULE)

Setiap komposisi grafis, slide presentasi, atau adegan visual wajib menerapkan proporsi pembagian bidang warna:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ [60%] WARNA DOMINAN (Latar Belakang / Kanvas / Dinding Lingkungan)      │
│  - Warna netral yang menenangkan (Slate 50, Off-White, Charcoal, Deep) │
├───────────────────────────────────────────────────┬─────────────────────┤
│ [30%] WARNA STRUKTURAL (Kartu, Pembagi, Teks Utama)│ [10%] WARNA AKSEN   │
│  - Memberikan kontras bentuk, hierarki, dan tubuh │  - Tombol CTA, rim  │
│  - Slate 900, Graphite, Warm Walnut, Muted Navy   │    light, fokus mata│
└───────────────────────────────────────────────────┴─────────────────────┘
```

- **60% Latar Belakang (Dominant):** Membangun suasana keseluruhan (*ambiance*) dan memberikan ruang bernapas mata.
- **30% Struktur (Secondary):** Membentuk batas elemen, kartu, kolom teks, atau pakaian subjek.
- **10% Aksen (Focal Accent):** Titik fokus visual yang menarik perhatian (*call to action*, perhiasan emas, lampu neon latar, atau tatapan mata).

---

## 3. 7 KONTRAS WARNA JOHANNES ITTEN (BAUHAUS)

Gunakan satu atau kombinasi dari 7 teknik kontras Itten untuk membangun ketertarikan visual tanpa menghasilkan kekacauan:

1. **Kontras Warna Murni (*Contrast of Hue*):** Mempertemukan warna-warna primer murni (Merah, Kuning, Biru) dengan intensitas setara.
2. **Kontras Terang-Gelap (*Light-Dark Contrast*):** Dasar dari teknik *Chiaroscuro* lukisan Rembrandt dan film Noir. Memisahkan subjek melalui gradasi luminansi.
3. **Kontras Hangat-Dingin (*Cold-Warm Contrast*):** Biru/Cyan (dingin, jauh, tenang) vs Merah/Oranye/Emas (hangat, dekat, gairah). Menciptakan ilusi kedalaman 3 dimensi pada bidang datar.
4. **Kontras Komplementer (*Complementary Contrast*):** Dua warna yang berseberangan tepat $180^\circ$ pada roda warna (contoh: Teal & Orange, Amber & Navy Blue).
5. **Kontras Simultan (*Simultaneous Contrast*):** Efek optik di mana mata manusia secara otomatis memproyeksikan warna komplementer pada warna abu-abu netral di sebelahnya.
6. **Kontras Kejenuhan (*Contrast of Saturation*):** Memadukan warna yang sangat pekat/jenuh (*vivid*) dengan warna pastel atau monokrom teredam (*muted*).
7. **Kontras Perluasan Luas (*Contrast of Extension / Proportion*):** Menyeimbangkan kekuatan luminansi warna dengan luas area (contoh: kuning memiliki daya pantul 3x lebih kuat dari ungu, sehingga area kuning hanya butuh $\frac{1}{4}$ dari luas area ungu untuk seimbang).

---

## 4. EMULASI FILM STOCK & PALET SINEMATOGRAFI DUNIA

Prompt gambar dan video di repositori ini wajib menggunakan penataan warna (*color grading*) yang didasarkan pada film stock kimia legendaris:

### A. Kodak Vision3 500T (5219):
- **Ciri Khas:** Diformulasikan untuk pencahayaan tungsten. Memberikan bayangan (*shadows*) biru malam yang sejuk, highlight emas lilin hangat, dan transisi warna kulit (*skin tones*) yang sangat halus dan organik.
- **Penerapan Prompt:** `Kodak Vision3 500T 5219 film stock, subtle halation around light sources, gentle organic grain, rich dynamic range`.

### B. Kodak Portra 400:
- **Ciri Khas:** Standar emas fotografi potret dan komersial mewah. Warna kulit tampak bercahaya alami (*healthy golden undertone*), warna pastel lembut, dan kontras medium yang tidak keras.
- **Penerapan Prompt:** `Shot on Kodak Portra 400, luminous warm skin tones, soft pastel highlights, creamy bokeh, natural daylight exposure`.

### C. Hollywood Teal & Orange (Bleach Bypass):
- **Ciri Khas:** Pemisahan warna komplementer paling populer dalam sinema aksi Hollywood (*blockbuster*). Bayangan ditanam ke warna *Cyan/Teal* gelap, sementara warna kulit subjek dipisahkan ke warna *Amber/Orange* hangat.
- **Penerapan Prompt:** `Cinematic teal and orange color grade, deep cyan shadows, warm amber highlights on skin, anamorphic flare, high dynamic range`.

### D. Fujifilm Eterna 500:
- **Ciri Khas:** Kontras lembut, saturasi warna hijau dan merah teredam, memberikan nuansa melankolis, puitis, dan autentik seperti film drama Eropa.
- **Penerapan Prompt:** `Fujifilm Eterna 500 cinema stock, desaturated muted tones, soft natural highlights, poetic moody atmosphere`.

---

## 5. REKOMENDASI PALET WARNA BERKARAKTER TINGGI (PRE-CALIBRATED)

```
[PALET 1: QUIET LUXURY / HERITAGE OBSIDIAN]
- Obsidian Black:    #0B0F19 (Background Dark)
- Deep Forest Green: #064E3B (Primary / Structural)
- Luminous Emerald:  #10B981 (Accent CTA / Focus)
- Warm Alabaster:    #F8FAFC (Text / Contrast)
- Muted Gold:        #D97706 (Special Accent)

[PALET 2: NORDIC MINIMALIST / CLEAN ARCHITECTURE]
- Snow Mist:         #F8FAFC (Background Light)
- Slate Graphite:    #1E293B (Primary Text & Structure)
- Nordic Ice Blue:   #0284C7 (Accent Functional)
- Soft Stone:        #E2E8F0 (Borders 1px hairline)
- Charcoal Midnight: #0F172A (Deep Contrast)

[PALET 3: CYBERNETIC NOIR / HIGH-TECH CINEMA]
- Void Deep Black:   #030712 (Background 60%)
- Tungsten Indigo:   #312E81 (Structural 30%)
- Bioluminescent Cyan: #06B6D4 (Accent 10%)
- Silver Titanium:   #94A3B8 (Metadata & Typo)
- Hazard Amber:      #F59E0B (Critical Warning)
```

---

## 6. LARANGAN WARNA TOKSIK AI (ANTI-SLOP COLOR RULE)

1. **Dilarang Neon Magenta-Cyan AI:** Dilarang menggunakan kombinasi warna ungu neon murahan `#FF00FF` dan cyan `#00FFFF` berdampingan tanpa alasan fungsional.
2. **Dilarang Warna 100% Saturated Se-Canvas:** Dilarang membuat visual di mana seluruh latar belakang, pakaian, dan langit sama-sama memiliki saturasi $100\%$, yang merusak mata dan terlihat seperti mainan plastik anak-anak.
3. **Wajib Mempertahankan Warna Kulit Alami:** Warna kulit manusia (*Melanin Vector*) wajib berada pada kurva hangat alami (*the skin tone indicator line* di vectorscope), tidak boleh terpengaruh menjadi hijau pucat atau ungu kecuali karakter alien fiksi ilmiah.
