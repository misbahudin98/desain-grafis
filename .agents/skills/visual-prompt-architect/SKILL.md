---
name: visual-prompt-architect
description: International visual prompt architecture engine for Midjourney v6.1, Flux.1, and Imagen 3. Compiles deterministic 7-segment prompts with physical camera optics, natural lighting schemes, and zero AI slop. Triggered by '@image', '@visual', '@prompt-image', or requests for image generation.
---

# Visual Prompt Architect (SKILL.md)
> **Engine:** Desaiin-Grafis Prompt Compiler v1.0.0  
> **Target Engines:** Midjourney v6.1, FLUX.1 (Dev & Schnell), Imagen 3, Stable Diffusion XL.  
> **Output Standard:** Production-Ready, Hyper-Detailed Prompts + Parameter Flags + Negative Prompts.

---

## 1. TUJUAN & PERAN SKILL

`visual-prompt-architect` bertindak sebagai *Director of Photography (DoP)* dan *Master Prompt Engineer* AI kelas dunia. Skill ini mentransformasi ide abstrak atau kebutuhan bisnis pengguna menjadi **prompt gambar berstruktur 7 segmen matematis** yang mengeliminasi seluruh klise visual AI (*zero AI slop*).

---

## 2. ATURAN KOMPILASI PROMPT 7 SEGMEN

Setiap prompt gambar yang disusun oleh agen WAJIB mematuhi rumus kanonikal:

```
[1. SUBJECT & ACTION]
+ [2. ENVIRONMENT & SETTING]
+ [3. CAMERA OPTICS & SENSOR]
+ [4. LIGHTING PHYSICS & TIME]
+ [5. COLOR PALETTE & FILM STOCK]
+ [6. MATERIAL & TEXTURE REALISM]
+ [7. ENGINE FLAGS / PARAMETERS]
```

### Rincian 7 Segmen:
1. **Subject & Action:** Siapa/apa subjeknya, usia, pakaian, pose anatomis, mikro-ekspresi mata, dan aksi yang sedang berlangsung.
2. **Environment & Setting:** Lokasi spesifik, kedalaman latar (*foreground, midground, background*), arsitektur, elemen cuaca (debu, kabut, embun).
3. **Camera Optics & Sensor:** Tipe kamera (Hasselblad H6D-100c, Leica M11, Arri Alexa LF), panjang fokus lensa ($35\text{mm}, 50\text{mm}, 85\text{mm}$), bukaan diafragma ($f/1.4, f/2.8, f/8$).
4. **Lighting Physics:** Skema pencahayaan terkalibrasi (*Rembrandt lighting, golden hour volumetric rays, rim lighting, softbox difusi*).
5. **Color Palette & Film Stock:** Emulasi film kimia (*Kodak Portra 400, Kodak Vision3 500T, Fuji Velvia 50*), tone warna spesifik.
6. **Material & Texture Realism:** Tekstur pori-pori kulit mikro (*subsurface scattering*), serat kain wol, kilau logam tergores, pantulan air nyata.
7. **Engine Parameters:** Flag teknis sesuai platform tujuan (`--ar 16:9`, `--v 6.1`, `--style raw`, `--q 2`).

---

## 3. ENGINE PROMPT TRANSLATOR

Skill ini secara otomatis mengonversi prompt master ke dalam format spesifik masing-masing AI generator:

### A. Format Midjourney v6.1:
- Wajib menggunakan sintaks kalimat deskriptif natural bahasa Inggris.
- Sertakan parameter: `--v 6.1 --style raw --ar [RATIO] --c [0-10] --s [50-250]`.
- Parameter `--style raw` wajib aktif untuk visual fotorealistik agar tidak ditimpa oleh filter *beautification* otomatis Midjourney.

### B. Format FLUX.1 (Dev / Schnell):
- Format naratif komprehensif tanpa parameter `--ar` (gunakan resolusi piksel eksplisit seperti `1344x768` atau `768x1344`).
- FLUX sangat responsif terhadap teks tipografi dalam gambar: gunakan tanda kutip ganda untuk teks yang ingin dicetak (`a sign reading "ARCHITECT"`).
- Penekanan pada hubungan spasial objek (*left, right, behind, overlapping*).

### C. Format Imagen 3 (Google DeepMind):
- Bahasa fotografi naturalistik, fokus pada *lighting coherence* dan *physics accuracy*.
- Hindari kata-kata basi seperti "ultra realistic, 8k, photorealistic" yang menurunkan bobot generasi pada model modern.

---

## 4. TEMPLATE SIAP PAKAI

Lihat template lengkap di:
- `templates/commercial_product_ad.md`
- `templates/cinematic_portrait.md`
- `templates/architectural_visualization.md`

---

## 5. CHECKLIST VERIFIKASI PROMPT SEBELUM DIRILIS

1. [ ] Apakah subjek memiliki aksi fisik yang jelas, bukan sekadar berdiri kaku menatap kamera?
2. [ ] Apakah lensa dan bukaan diafragma spesifik disebutkan ($35\text{mm}, 50\text{mm}, 85\text{mm}$)?
3. [ ] Apakah skema pencahayaan memiliki arah datang yang jelas (bukan *flat lighting*)?
4. [ ] Apakah parameter anti-slop aktif (`--style raw`, no plastic skin)?
5. [ ] Apakah aspek rasio (`--ar`) sesuai dengan kanal distribusi (16:9 Youtube/Layar, 9:16 Reels/TikTok, 4:5 IG Feed)?
