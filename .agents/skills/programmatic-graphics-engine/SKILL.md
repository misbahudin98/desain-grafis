---
name: programmatic-graphics-engine
description: Autonomous programmatic design engine for algorithmic generation of vector graphics (SVG), layout grids, data visualizations, social media banners, and FFmpeg video pipeline scripts. Triggered by '@programmatic', '@svg', '@code-graphics', or requests to generate graphics via code.
---

# Programmatic Graphics Engine (SKILL.md)
> **Engine:** Desaiin-Grafis Code-to-Design Engine v1.0.0  
> **Teknologi:** Pure SVG, HTML5 Canvas, Python Pillow / Matplotlib, Node.js, FFmpeg.  
> **Output:** Scalable Vector Graphics (SVG), Ultra-sharp Infographics, Dynamic Typography Posters, Programmatic Social Cards.

---

## 1. TUJUAN & PERAN SKILL

`programmatic-graphics-engine` bertindak sebagai *Creative Technologist* dan *Computational Designer*. Berbeda dengan generasi gambar AI berbasis piksel (difusi) yang sering kali tidak presisi dalam garis lurus, teks tajam, dan ukuran eksak, skill ini menghasilkan **desain berbasis kode deterministik (*code-first design*)**:
1. **100% Vector Scalable (SVG):** Menghasilkan file SVG murni yang dapat diskalakan hingga ukuran papan reklame billboard raksasa tanpa kehilangan ketajaman 1 piksel pun.
2. **Presisi Matematika Mutlak:** Mematuhi grid Swiss Müller-Brockmann, rasio emas Fibonacci, dan garis hairline 1px.
3. **Tipografi Tajam:** Teks dirender secara tajam menggunakan font sistemik web atau kurva kurva vektor glif.
4. **Automasi Pembuatan Banner Massal:** Menghasilkan skrip Python untuk menghasilkan puluhan variasi banner sosial media dalam hitungan detik.

---

## 2. STANDAR KUALITAS PEMROGRAMAN SVG KANONIKAL

Setiap kode SVG yang dihasilkan wajib memenuhi standar arsitektur:
1. **Semantic Elements:** Gunakan tag SVG semantik (`<rect>`, `<circle>`, `<path>`, `<text>`, `<linearGradient>`, `<defs>`).
2. **ViewBox Terstandar:** Wajib menyertakan `viewBox="0 0 [WIDTH] [HEIGHT]"` dengan aspek rasio terdefinisi (misal: `0 0 1200 630` untuk OpenGraph Twitter/LinkedIn card).
3. **No External Dependents / Self-Contained:** Seluruh gaya CSS dan gradien wajib berada di dalam blok `<defs>` internal SVG, sehingga file dapat langsung disematkan atau dikonversi tanpa kehilangan gaya.
4. **Responsive & Scalable:** Atribut `width="100%"` dan `height="100%"` yang menginduk pada batas kontainer luar.
5. **Aksesibilitas:** Wajib menyertakan elemen `<title>` dan `<desc>` untuk pembaca layar (*screen reader*).

---

## 3. PIPELINE FFMPEG UNTUK VIDEO MULTIMEDIA

Skill ini juga menyediakan perintah FFmpeg deterministik untuk menggabungkan, memotong, menstabilkan, dan menata warna klip video AI:

### A. Konversi 60fps / 24fps Sinematik:
```bash
ffmpeg -i input.mp4 -r 24 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p output_24fps.mp4
```

### B. Menerapkan 3D LUT Color Grading:
```bash
ffmpeg -i raw_clip.mp4 -vf "lut3d=file=kodak_vision3.cube" -c:v libx264 -crf 17 output_graded.mp4
```

### C. Looping Klip Video Halus Tanpa Patah (*Seamless Crossfade Loop*):
```bash
ffmpeg -i input.mp4 -filter_complex "[0:v]trim=0:4,setpts=PTS-STARTPTS[v1];[0:v]trim=4:5,setpts=PTS-STARTPTS[v2];[v2][v1]gltransition=duration=1:offset=4" -c:v libx264 output_loop.mp4
```

---

## 4. SKRIP OTOMASI TERSAJI
- Skrip generator banner SVG: `scripts/generate_svg_card.py`
- Skrip audit prompt: `../../scripts/audit_design_prompt.py`
- Skrip generator palet warna & kontras WCAG: `../../scripts/generate_palette.py`
