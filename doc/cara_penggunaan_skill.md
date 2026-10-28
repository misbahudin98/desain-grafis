# Buku Panduan Lengkap Cara Penggunaan Seluruh Skill (cara_penggunaan_skill.md)
> **Engine:** Desaiin-Grafis User Playbook v1.0.0  
> **Target:** Desainer, Art Director, Content Creator, dan Agen AI Otonom.  
> **Status:** Panduan Praktis Interaktif Langkah-demi-Langkah Penggunaan Seluruh Skill di Repositori `desaiin-grafis`.

---

## 1. PETA 5 SKILL KREATIF & TAG PEMICU KANONIKAL

Repositori `desaiin-grafis` dilengkapi dengan **5 Skill Spesialis Otonom** yang dapat dipanggil menggunakan tag pemicu khusus:

```
┌────────────────────────────────────────────────────────────────────────┐
│ PETA 5 SKILL DESAIN MULTIMEDIA KANONIKAL                               │
├────────────────────────────────────────────────────────────────────────┤
│ 1. international-prompt-standards   ➔ Tag: @prompt                     │
│ 2. visual-prompt-architect          ➔ Tag: @image / @visual            │
│ 3. cinema-video-director            ➔ Tag: @video / @cinema            │
│ 4. brand-identity-crafter           ➔ Tag: @brand / @identity          │
│ 5. programmatic-graphics-engine     ➔ Tag: @programmatic / @svg        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. PANDUAN PENGGUNAAN SKILL-BY-SKILL

---

### SKILL 1: `international-prompt-standards` (Tag: `@prompt`)

#### A. Kapan Menggunakannya?
- Saat Anda memiliki ide prompt mentah dan ingin mengubahnya menjadi format berstandar internasional (IEEE P3394, ISO/IEC TS 42119-8, dan Jonas Oppenlaender 6-Modifier).
- Saat ingin mengaudit apakah sebuah prompt bebas dari kata-kata basi AI (*buzzwords*) dan layak diproduksi.

#### B. Cara Memanggilnya:
Ketik permintaan Anda dengan tag `@prompt`. Contoh:
> `@prompt tolong audit dan sempurnakan ide saya ini menjadi prompt internasional: "foto wanita karir elegan minum kopi di kafe mewah, sangat realistis 8k"`

#### C. Output yang Dihasilkan:
Agen akan:
1. Memindai dan membuang kata-kata basi (`sangat realistis 8k`).
2. Menginjeksi formula 7 segmen (kamera Leica M11, lensa 50mm f/1.4, pencahayaan Rembrandt jendela, palet Kodak Portra 400).
3. Memberikan laporan skor audit kualitas (0–100) dan kode prompt siap pakai untuk Midjourney v6.1 dan FLUX.1.

---

### SKILL 2: `visual-prompt-architect` (Tag: `@image` atau `@visual`)

#### A. Kapan Menggunakannya?
- Saat Anda ingin merancang foto produk iklan komersial (jam tangan, parfum, kosmetik, mobil).
- Saat ingin membuat potret manusia fotorealistik dengan pori-pori kulit asli (*subsurface scattering*).
- Saat ingin membuat visual arsitektur interior atau lanskap megah.

#### B. Cara Memanggilnya:
Ketik permintaan Anda dengan tag `@image`. Contoh:
> `@image buatkan prompt foto komersial botol parfum mewah kaca amber di atas batu basalt basah dengan asap dupa kayu cendana tipis untuk Midjourney v6.1`

#### C. Output yang Dihasilkan:
Prompt 7 segmen siap copy-paste lengkap dengan parameter flag:
```text
Commercial luxury product photography of an amber glass perfume bottle with an obsidian magnetic cap and brushed gold label reading "ÉCLAT". The bottle rests on a dark wet basalt stone slab surrounded by delicate water droplets and thin curling tendrils of aromatic sandalwood incense smoke. Lighting: A single high-contrast key softbox overhead with gentle silver reflector fill on the label and subtle golden rim lighting tracing the contour of the amber glass. Shot on Hasselblad H6D-100c, 100mm macro lens at f/5.6. Hyper-detailed glass refraction, micro-droplets of water, deep shadows, premium editorial campaign aesthetic --ar 4:5 --style raw --v 6.1
```

---

### SKILL 3: `cinema-video-director` (Tag: `@video` atau `@cinema`)

#### A. Kapan Menggunakannya?
- Saat Anda ingin membuat video komersial multi-adegan (30 detik / 60 detik) untuk Runway Gen-3 Alpha, Kling 1.5, OpenAI Sora, atau Luma Dream Machine.
- Saat Anda butuh *Shot List*, naskah *Storyboard*, atau penataan sudut gerak kamera fisik (Dolly, Pan, Tilt, Crane) tanpa *drifting* atau *morphing*.

#### B. Cara Memanggilnya:
Ketik permintaan Anda dengan tag `@video`. Contoh:
> `@video buatkan storyboard dan shot list 3 adegan berurutan untuk iklan kopi cold brew artisanal, durasi 15 detik, gaya sinematik sinema film 24fps`

#### C. Output yang Dihasilkan:
Spesifikasi adegan terstruktur (Shot 01 ELS ➔ Shot 02 MCU ➔ Shot 03 ECU Macro) dengan prompt siap copy untuk Runway Gen-3 dan Kling 1.5:
```text
[Camera]: Smooth low-angle dolly-in forward at 0.5m/s tracking the glass bottle.
[Scene Description]: Fresh water droplet condensing and sliding slowly down the chilled amber glass bottle, splash of cold water in background with realistic fluid dynamics.
[Optics & Lighting]: Arri Alexa Mini LF, 85mm prime lens at T2.0, natural golden hour backlight, Kodak Vision3 500T 5219 grain, 24fps cinema pace, zero morphing.
```

---

### SKILL 4: `brand-identity-crafter` (Tag: `@brand` atau `@identity`)

#### A. Kapan Menggunakannya?
- Saat Anda ingin merancang identitas merek korporat, logo monogram/wordmark, pedoman tata letak, dan palet warna resmi.
- Saat butuh token warna yang telah lolos uji aksesibilitas WCAG 2.2 AAA dan terkalibrasi HEX, sRGB, CMYK, dan Pantone (PMS).

#### B. Cara Memanggilnya:
Ketik permintaan Anda dengan tag `@brand`. Contoh:
> `@brand buatkan spesifikasi identitas merek lengkap untuk firma arsitektur modern minimalis bernama "KALA STUDIO", mencakup filosofi, konstruksi geometris logo, token warna, dan tipografi`

#### C. Output yang Dihasilkan:
Dokumen formal pedoman merek:
- **Brand Archetype & Personality:** The Creator & The Sage.
- **Logo Geometry & Clear Space:** Zona batas aman minimal $1X$.
- **Tabel Token Warna:** Obsidian `#0B0F19`, Emerald `#10B981`, Alabaster `#F8FAFC`.
- **Hierarki Tipografi:** Inter Display Bold + Inter Regular + JetBrains Mono.
- **Aturan Do's & Don'ts:** Larangan peregangan logo atau bayangan plastik.

---

### SKILL 5: `programmatic-graphics-engine` (Tag: `@programmatic` atau `@svg`)

#### A. Kapan Menggunakannya?
- Saat Anda membutuhkan grafik vektor murni (SVG) yang tajam $100\%$ tanpa pikselasi untuk kartu media sosial, OpenGraph banner, atau poster tipografi geometris.
- Saat butuh skrip automasi FFmpeg untuk memotong, menstabilkan, atau mengonversi video ke 24fps sinematik.

#### B. Cara Memanggilnya:
Ketik permintaan Anda dengan tag `@programmatic`. Contoh:
> `@programmatic buatkan file banner OpenGraph SVG berukuran 1200x630 bertema Swiss Grid Modernist untuk peluncuran fitur baru`

#### C. Output yang Dihasilkan:
Skrip Python atau kode SVG mandiri siap pakai yang dapat dirender instan di browser atau diekspor ke PNG/PDF beresolusi tinggi tanpa penurunan kualitas.

---

## 3. ALUR KERJA TERPADU PRODUKSI MULTIMEDIA (END-TO-END WORKFLOW)

Berikut adalah diagram alur bagaimana ke-5 skill saling bekerja sama dari tahap ide konsep hingga aset final:

```
[TAHAP 1: BRAND STRATEGY]
Panggil @brand ➔ Rumuskan identitas, logo, token warna, dan tipografi.
         │
         ▼
[TAHAP 2: PROMPT ARCHITECTURE]
Panggil @prompt ➔ Susun prompt berstandar internasional IEEE/ISO & 7 segmen fisik.
         │
         ▼
[TAHAP 3: PRODUCTION STAGE]
┌─────────────────────────────────┴─────────────────────────────────┐
▼                                                                   ▼
[PRODUKSI FOTO / STILLS]                            [PRODUKSI VIDEO / MOTION]
Panggil @image ➔ Midjourney v6.1 / FLUX.1          Panggil @video ➔ Runway Gen-3 / Kling
(Prompt fotorealistik pori kulit asli)              (Storyboard shotlist & 24fps cinema)
└─────────────────────────────────┬─────────────────────────────────┘
                                  │
                                  ▼
[TAHAP 4: VECTOR ASSETS & SOCIAL CARDS]
Panggil @programmatic ➔ Render banner OpenGraph SVG 1200x630 & pipeline FFmpeg.
                                  │
                                  ▼
[TAHAP 5: QUALITY GATE & AUDIT OTOMATIS]
Jalankan: python scripts/audit_design_prompt.py (Wajib Skor >= 85/100)
Jalankan: python scripts/generate_palette.py     (Wajib Rasio Kontras >= 7:1 AAA)
```

---

## 4. PERANGKAT VALIDASI MANDIRI (SELF-SERVICE SCRIPTS)

Anda dapat menguji dan memvalidasi pekerjaan Anda secara langsung melalui terminal:

### 1. Mengaudit Kualitas Prompt (Deteksi Slop):
```bash
python scripts/audit_design_prompt.py
```
*Fungsi:* Menilai skor 0–100, mendeteksi kata-kata terlarang (*buzzwords*), dan memastikan optik kamera serta pencahayaan fisik telah dipenuhi.

### 2. Menguji Kontras Warna WCAG 2.2 AAA:
```bash
python scripts/generate_palette.py
```
*Fungsi:* Menghitung rasio kontras teks terhadap latar belakang secara matematis ($\ge 7.0:1$ untuk standar AAA).

### 3. Merender Banner Vektor Swiss:
```bash
python .agents/skills/programmatic-graphics-engine/scripts/generate_svg_card.py
```
*Fungsi:* Menghasilkan file SVG vektor tajam `templates/sample_swiss_card.svg` dalam hitungan milidetik.
