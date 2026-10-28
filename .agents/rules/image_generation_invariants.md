# Invarian Rekayasa Prompt Gambar & Ilustrasi AI (image_generation_invariants.md)
> **Engine:** Desain-Grafis Core v1.0.0 (SDD-Creative-Deterministic)  
> **Platform Target:** Midjourney v6.1, Flux.1 Pro/Dev, Imagen 3, Stable Diffusion XL (SDXL).  
> **Standar Mutu:** Hasselblad Master Photography, National Geographic Documentary, Vogue Editorial, Architectural Digest, WCAG AAA.

---

## 1. FORMULA BAKU ANATOMI PROMPT GAMBAR (7-SEGMENT PROMPT SYNTAX)

Setiap prompt pembuatan gambar AI berstandar internasional WAJIB disusun mengikuti **Struktur 7 Segmen Kaskade**:

```
┌────────────────────────────────────────────────────────────────────────┐
│ ANATOMI 7 SEGMEN PROMPT GAMBAR KELAS DUNIA                             │
├────────────────────────────────────────────────────────────────────────┤
│ [1. SUBJEK UTAMA & TINDAKAN]                                           │
│     Siapa / apa objeknya? Deskripsi fisik detail, pakaian, ekspresi,    │
│     tindakan spesifik tanpa kata sifat abstrak.                        │
├────────────────────────────────────────────────────────────────────────┤
│ [2. LINGKUNGAN & RUANG LATAR]                                          │
│     Di mana adegan berlangsung? Arsitektur, waktu hari, atmosfer cuaca,│
│     elemen latar belakang yang mendukung cerita.                       │
├────────────────────────────────────────────────────────────────────────┤
│ [3. KOMPOSISI & SUDUT PANDANG]                                         │
│     Framing: Eye-level, Low-angle, Golden Ratio, Rule of Thirds,       │
│     Negative space ratio, Leading lines.                               │
├────────────────────────────────────────────────────────────────────────┤
│ [4. PENCAHAYAAN & DERAJAT KONTRAS]                                     │
│     Arah cahaya: Rembrandt lighting, Golden hour, Volumetric rays,     │
│     Soft diffused window light, Chiaroscuro high-contrast.             │
├────────────────────────────────────────────────────────────────────────┤
│ [5. SPESIFIKASI OPTIK KAMERA & LENSA]                                  │
│     Bodi: Hasselblad H6D-100c, Leica M11, Sony A1 35mm full-frame.     │
│     Lensa: 35mm f/1.4, 50mm f/1.2, 85mm f/1.4, Tilt-shift 24mm.       │
│     Karakter fokus: Shallow depth of field, creamy bokeh, edge sharp.  │
├────────────────────────────────────────────────────────────────────────┤
│ [6. KELAS WARNA & TEKSTUR MATERIAL]                                    │
│     Color grade: Kodak Portra 400 tone, muted earth palette, LUT warm, │
│     Tekstur: Tangible skin pores, fabric weave, natural patina.        │
├────────────────────────────────────────────────────────────────────────┤
│ [7. PARAMETER MESIN & RASIO ASPEK]                                     │
│     Midjourney: --ar 16:9 --style raw --stylize 250 --v 6.1            │
│     Flux: Guidance scale 3.5, 30 steps.                                │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. MATRIKS STANDAR RASIO ASPEK (ASPECT RATIO MATRIX)

Gunakan rasio aspek yang tepat sesuai tujuan media publikasi:

| Rasio Aspek | Flag Parameter | Peruntukan Media & Komposisi | Alasan Desain |
| :---: | :---: | :--- | :--- |
| **16:9** | `--ar 16:9` | YouTube Banner, Website Hero Banner, Desktop Wallpapers | Sinematik lanskap luas, lapang, standar monitor layar lebar. |
| **9:16** | `--ar 9:16` | Instagram Reels, TikTok, YouTube Shorts, WhatsApp Status | Pengalaman vertikal imersif layar penuh smartphone. |
| **4:5** | `--ar 4:5` | Instagram Feed Portrait Post | Memaksimalkan area pandang layar feed vertikal di aplikasi mobile. |
| **1:1** | `--ar 1:1` | Profil Avatar, Square Feed Post, E-Commerce Thumbnail | Keseimbangan simetris sempurna di ruang terbatas. |
| **21:9** | `--ar 21:9` | Layar Lebar Ultra-Wide, Poster Sinema Anamorphic | Komposisi megah epik dengan kompresi lateral anamorphic lens. |
| **3:2** | `--ar 3:2` | Fotografi Cetak Standar 35mm (Majalah, Galeri Seni) | Rasio klasik fotografi analog profesional. |

---

## 3. KAMUS LENSA & OPTIK FOTOGRAFI NYATA

Dilarang menggunakan istilah generik *"photorealistic"* atau *"hyper-detailed"*! Sebutkan lensa dan bodi kamera nyata untuk mengaktifkan representasi optik fisik pada model AI:

```markdown
# 1. Potret Wajah Sinematik (Cinematic Portraiture):
"Shot on Hasselblad H6D-100c, 85mm f/1.4 lens, shallow depth of field, razor-sharp eye focus with natural catchlight, authentic subsurface scattering skin texture, creamy background bokeh."

# 2. Fotografi Dokumenter & Cerita Lingkungan (Environmental Storytelling):
"Captured with Leica M11, 35mm Summilux f/1.4 lens, eye-level framing, deep depth of field, authentic film grain, documentary street photography aesthetics."

# 3. Fotografi Arsitektur & Desain Interior (Architectural Interiors):
"Shot on Sony A1 with 24mm tilt-shift lens, perfectly vertical lines without converging perspective distortion, natural daylight pouring through floor-to-ceiling windows, f/8 aperture, edge-to-edge sharpness."

# 4. Makro Detail & Tekstur Produk (Product Macro Craftsmanship):
"100mm macro f/2.8 lens, high-magnification close-up, tactile leather grain and micro-stitching detail, directional studio rim lighting highlighting edge contours."
```

---

## 4. FORMULA NEGATIVE PROMPT STANDAR (ANTI-SLOP SHIELD)

Untuk model yang mendukung negative prompt (Stable Diffusion, Midjourney `--no`, Flux):

```text
--no plastic skin, wax skin, extra fingers, deformed hands, mutated limbs, blurry eyes, oversaturated colors, neon purple glow, floating text, watermark, signature, horror vacui, oversaturated magenta, cartoonish clay render, airbrushed skin, symmetrical duplicate faces
```

---

## 5. CIRI KHAS PERBEDAAN MESIN & GAYA BAHASA PROMPT

1. **Midjourney v6.1:**
   - Gunakan format koma deklaratif padat (*Comma-separated descriptive clauses*).
   - Selalu sertakan `--style raw` untuk menekan estetika "AI default shiny".
   - Gunakan `--stylize` bernilai terukur: $100 - 250$ untuk fotorealisme murni; $300 - 600$ untuk visual artistik editorial.
2. **Flux.1 Pro / Dev:**
   - Menyukai bahasa deskriptif naratif utuh (*Natural language descriptive paragraphs*).
   - Sangat piawai menghasilkan teks tipografi yang tertera pada objek (misal: *"A minimalist coffee bag with clean black typography reading 'NORDIC COFFEE' in geometric sans-serif"*).
3. **Imagen 3 (Google DeepMind):**
   - Sangat sensitif terhadap kepatuhan prompt (*prompt adherence*) dan pencahayaan fisik nyata. Deskripsikan material dan interaksi cahaya secara rinci.
