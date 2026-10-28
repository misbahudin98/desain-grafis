---
name: marketing-collateral-architect
description: International marketing collateral and social media design architect for flayers, IAB web display banners, multi-slide carousels (Instagram/LinkedIn 4:5), and full-screen status/stories (WhatsApp/IG/FB 9:16). Governed by ISO 216, ISO 12647-2 FOGRA39, IAB LEAN standards, and Meta UI safe zones. Triggered by '@marketing', '@collateral', '@social', '@flyer', '@carousel', or '@status'.
---

# Marketing Collateral Architect (SKILL.md)
> **Engine:** Desain-Grafis Marketing & Social Collateral Engine v1.0.0  
> **Standar Dunia:** ISO 216 (Paper Standards), ISO 12647-2 (FOGRA39 CMYK Pre-press), IAB Tech Lab (LEAN Display Guidelines), Meta Platform Safe Zones (Instagram, Facebook, WhatsApp), LinkedIn Document Solutions.  
> **Output:** Spesifikasi Flayer Siap Cetak (A4/A5), IAB Web Banners, Dek Carousel Multi-Slide (4:5), & Image Status/Stories 9:16 Bebas Potongan UI.

---

## 1. TUJUAN & PERAN SKILL

`marketing-collateral-architect` bertindak sebagai *Marketing Art Director & Collateral Production Engineer*. Skill ini memastikan materi promosi dan distribusi visual memiliki konversi tinggi, daya pikat henti scrolling (*scroll-stopping power*), tata letak gravitasi optik yang terkalibrasi, serta mematuhi batas fisik media cetak maupun antarmuka digital:

1. **Flayer Cetak & Digital Presisi:** Mengontrol ukuran DIN A4/A5/A6, bleed $3\text{mm}$, margin aman $5\text{mm}$, resolusi 300 DPI, dan titik pusat optik (*optical center* 55–60%).
2. **IAB Display Banners:** Mematuhi 4 ukuran kanonikal web (300x250, 728x90, 300x600, 970x250) dan prinsip LEAN ($\le 200\text{KB}$, 15 detik loop limit, 1px border).
3. **Carousel Multi-Slide Media Sosial:** Menerapkan rasio emas vertikal 4:5 ($1080\times 1350\text{px}$) pada Instagram dan LinkedIn dengan busur narasi 7–10 slide (Hook ➔ Context ➔ Meat ➔ Climax ➔ CTA).
4. **Image Status & Stories (WhatsApp/IG/FB):** Mengisolasi teks krusial agar tidak tertutup oleh zona bahaya UI antarmuka sistem (Bilah atas 270px, bilah reply bawah 270px/670px, margin samping 65px).

---

## 2. 4 PILAR MEDIA MARKETING & SPESIFIKASI MUTLAK

### A. Flayer (Print & Digital Flyer):
- **Standar Ukuran:** DIN A4 ($210\times 297\text{mm}$) atau DIN A5 ($148\times 210\text{mm}$).
- **Bleed Margin:** Wajib $+3\text{mm}$ keliling di luar garis potong.
- **Margin Teks Aman:** Minimal $5\text{mm}$ di dalam garis potong.
- **Pre-Press:** Mode CMYK FOGRA39, $300\text{ DPI}$, TAC $\le 300\%$.
- **Optical Sweet Spot:** Headline utama berada di $55\% - 60\%$ dari bawah kanvas.

### B. Banner Web & Display (IAB Standards):
- **Ukuran Kanonikal:** MPU $300\times 250$, Leaderboard $728\times 90$, Half-Page $300\times 600$, Billboard $970\times 250$, OpenGraph $1200\times 630$.
- **Prinsip LEAN:** Bobot awal $\le 150 - 200\text{KB}$, loop animasi maksimal 15 detik, bingkai 1px abu-abu jika berlatar putih, audio mute default.

### C. Carousel Multi-Slide (Instagram & LinkedIn):
- **Dimensi:** $1080\times 1350\text{px}$ (Rasio 4:5 vertikal, 25% lebih luas dari 1:1).
- **Busur Narasi:**
  - Slide 1: Hook janji hasil konkret (5–8 kata display bold $\ge 54\text{px}$, swipe cue arrow).
  - Slide 2: Context / Agitation masalah.
  - Slide 3–7: Framework inti (1 ide per slide, max 40–60 kata).
  - Slide 8–9: Cheat-sheet rangkuman bernilai simpan tinggi (*high saveability*).
  - Slide 10: Call to Action (CTA) konversi tunggal.
- **Margin Aman:** Padding batas dalam $80\text{px} - 100\text{px}$.

### D. Image Status & Stories (WhatsApp, IG, FB):
- **Dimensi Layar:** $1080\times 1920\text{px}$ (9:16).
- **Zona Bahaya Atas ($0\text{px} - 270\text{px}$):** Dilarang menaruh teks penting / logo (tertutup header sistem).
- **Zona Bahaya Bawah ($1650\text{px} - 1920\text{px}$ Organik // $1250\text{px} - 1920\text{px}$ Iklan Ads):** Dilarang menaruh teks / CTA (tertutup reply bar & tombol swipe).
- **Margin Samping:** $65\text{px}$ kiri dan kanan.
- **Area Aman Konten (Safe Box):** $950\times 1380\text{px}$ (Organik) atau $950\times 980\text{px}$ (Iklan).

---

## 3. FORMAT SPESIFIKASI MATERI MARKETING (OUTPUT KANONIKAL)

Setiap rancangan collateral wajib menghasilkan kontrak spesifikasi terstruktur:

```markdown
# MARKETING COLLATERAL SPECIFICATION: [NAMA_PROJEK]
- **Tipe Media:** [Flyer A4/A5 / IAB Banner / Carousel 4:5 / Status Stories 9:16]
- **Target Platform:** [Print / Instagram / WhatsApp / LinkedIn / Web Display]
- **Dimensi Bersih:** [Width x Height]
- **Batas Margin / Bleed / Safe Zone:** [Rincian ukuran batas aman]
- **Skema Warna:** [60-30-10 Hex / CMYK Tokens]
- **Hierarki Tipografi:** [Headline Font, Body Font, CPL Limit]
- **Copywriting Framework:** [AIDA / PAS / Outcome-Driven Hook]
- **Rincian Zonal Layout / Slide Breakdown:** [Rincian per zona atau per slide]
- **Status Audit Safe Zone:** [Lulus verifikasi verify_collateral_specs.py]
```

---

## 4. DOKUMEN REFERENSI & TEMPLATE
- Pustaka Standar Dimensi & Spesifikasi: `references/international_marketing_specs.md`
- Template Spesifikasi Flayer Cetak/Digital: `templates/flyer_print_and_digital_spec.md`
- Template Dek Carousel Multi-Slide 4:5: `templates/carousel_narrative_deck_spec.md`
- Template Image Status & Stories 9:16: `templates/social_stories_status_spec.md`
- Template IAB Display Banners: `templates/iab_display_banners_spec.md`
- Invarian Desain Marketing & Media Sosial: `../../rules/social_and_marketing_design_invariants.md`
- Kitab Standar Desain Pemasaran Dunia: `../../../doc/marketing_and_social_media_bible.md`
- Standar Produksi Media Dunia: `../../../doc/international_media_standards.md`
- Invarian Tipografi & Tata Letak: `../../rules/typography_and_layout_invariants.md`
- Invarian Teori Warna & Kontras: `../../rules/color_theory_and_grading_invariants.md`

---

## 5. SKRIP VALIDASI MANDIRI
Eksekusi validator terminal untuk menguji dimensi, bleed, dan zona aman status/stories:
```bash
python scripts/verify_collateral_specs.py
```
Menghasilkan verifikasi kepatuhan ISO 216, ISO 12647-2 FOGRA39, IAB Tech Lab, dan kalkulasi batas bahaya antarmuka Meta/WhatsApp.
