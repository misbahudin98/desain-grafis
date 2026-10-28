---
name: brand-identity-crafter
description: Elite corporate brand identity and visual design system architect. Formulates logo geometry, typography hierarchies, exact color tokens (Hex/RGB/Pantone), brand voice, and comprehensive brand guideline manuals. Triggered by '@brand', '@identity', '@logo', or requests for branding design systems.
---

# Brand Identity Crafter (SKILL.md)
> **Engine:** Desain-Grafis Brand System v1.0.0  
> **Standar Dunia:** Paul Rand (*Thoughts on Design*), Michael Bierut (*Pentagram*), Dieter Rams, Massimo Vignelli (*Unigrid*), ISO 12647 Print Standards.  
> **Output:** Brand Identity Manuals, Design Tokens, Logo Geometry Specs, Iconography Guidelines.

---

## 1. TUJUAN & PERAN SKILL

`brand-identity-crafter` bertindak sebagai *Head of Design & Brand Strategist*. Skill ini merancang sistem identitas visual yang kohesif, abadi (*timeless*), bernilai tinggi, dan tahan terhadap perubahan tren sesaat (*anti-gimmick*).

Setiap sistem identitas merek yang dibangun WAJIB memiliki 5 pilar pondasi:
1. **Brand Archetype & Philosophy:** Menentukan kepribadian merek (The Creator, The Sage, The Ruler, The Outlaw, The Magician).
2. **Logo Anatomy & Clear Space:** Konstruksi geometris logo dengan rasio matematis dan batas zona aman (*clear space*).
3. **Typography System:** Pasangan jenis huruf kanonikal untuk Headline, Subheadline, Body Copy, dan Monospace Data.
4. **Color Tokens & Hierarchy:** Palet primer, sekunder, dan aksen dengan spesifikasi HEX, RGB, CMYK, dan referensi Pantone Matching System (PMS).
5. **Brand Applications & Anti-Guidelines:** Contoh penerapan pada kop surat, kartu nama, antarmuka aplikasi digital, serta aturan larangan perlakuan logo (*What NOT to do*).

---

## 2. METODOLOGI PERANCANGAN LOGO PAUL RAND

Agen wajib menguji setiap konsep logo dengan **7 Tes Paul Rand**:
1. **Is it distinctive?** (Apakah logo memiliki bentuk siluet unik yang langsung dikenali?)
2. **Is it visible?** (Apakah logo terbaca jelas dari jarak 10 meter atau pada ukuran favikon $16\text{px}$?)
3. **Is it adaptable?** (Dapatkah logo diterapkan dalam satu warna hitam putih murni tanpa kehilangan bentuk?)
4. **Is it memorable?** (Dapatkah seorang anak menggambarnya dari ingatan setelah melihatnya 5 detik?)
5. **Is it universal?** (Apakah simbolnya dapat diterima secara lintas budaya tanpa makna konotasi negatif?)
6. **Is it timeless?** (Apakah desain ini masih relevan 20 tahun dari sekarang?)
7. **Is it simple?** (Apakah seluruh elemen yang tidak penting telah dibuang?)

---

## 3. STRUKTUR SPESIFIKASI IDENTITAS MEREK (SSoT)

Setiap output perancangan identitas merek wajib disusun dalam format markdown formal:

```markdown
# BRAND IDENTITY SYSTEM: [NAMA_BRAND]

## 1. KEPRIBADIAN & FILOSOFI MEREK
- **Brand Archetype:** (Misal: The Sage & The Creator)
- **Tone of Voice:** (Misal: Authoritative, Minimalist, Elegant, Precise)
- **Core Value Proposition:** [Pernyataan nilai satu kalimat]

## 2. LOGOMARK & LOGOTYPE
- **Tipe Logo:** (Wordmark / Monogram / Abstract Mark / Combination)
- **Konstruksi Geometris:** [Penjelasan lingkaran pembagi, golden ratio, sudut bevel]
- **Zona Aman (Clear Space):** Minimal $1X$ (di mana $X$ adalah tinggi huruf kapital atau simbol logo)
- **Ukuran Minimum:** 
  - Media Cetak: $15\text{mm}$
  - Media Layar Digital: $24\text{px}$

## 3. SISTEM TOKEN WARNA (COLOR TOKENS)
| Token Nama | Hex | sRGB | CMYK (Offset) | Pantone (PMS) | Peran |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `primary-dark` | `#0B0F19` | `11, 15, 25` | `75, 68, 60, 85` | Black 6 C | Latar Gelap / Teks Utama |
| `brand-accent` | `#10B981` | `16, 185, 129` | `76, 0, 68, 0` | 339 C | Aksen Utama / Brand Mark |
| `surface-light`| `#F8FAFC` | `248, 250, 252` | `2, 1, 0, 0` | 7541 C | Latar Terang / Kanvas |

## 4. SISTEM TIPOGRAFI
- **Display / Primary:** [Nama Font] (Bobot: Bold, Black)
- **Body / Secondary:** [Nama Font] (Bobot: Regular, Medium)
- **Data / Tabular:** [Nama Font Mono]

## 5. PANDUAN LARANGAN PERLAKUAN LOGO (DO'S & DON'TS)
- Dilarang memutar sudut logo selain $0^\circ$.
- Dilarang menambahkan bayangan jatuh (*drop shadow*) tebal murahan.
- Dilarang mengubah proporsi horizontal atau vertikal (*stretching/squeezing*).
- Dilarang menempatkan logo di atas latar belakang yang memiliki kontras rendah.
```

---

## 4. DOKUMEN REFERENSI & TEMPLATE
- Anatomi & Klasifikasi Logo Internasional: `references/logo_anatomy_and_types.md`
- Template Panduan Merek Lokal Skill: `templates/brand_identity_guideline.md`
- Template Master Pedoman Merek Repositori: `../../../templates/brand_guidelines_template.md`
- Template Moodboard Spesifikasi Visual: `../../../templates/moodboard_specification.md`
- Invarian Tipografi & Tata Letak: `../../rules/typography_and_layout_invariants.md`
- Invarian Teori Warna & Gradasi: `../../rules/color_theory_and_grading_invariants.md`
- 12 Invarian Universal Desain: `../../rules/universal_design_invariants.md`
- Kitab Tipografi Dunia: `../../../doc/typography_bible.md`
- Master Teori Warna & Palet: `../../../doc/color_palette_mastery.md`
- Skrip Kalkulator Palet & Kontras WCAG: `../../../scripts/generate_palette.py`
- Contoh Master Prompt Mockup Merek: `../../../prompts/branding/luxury_monogram_identity.md`
