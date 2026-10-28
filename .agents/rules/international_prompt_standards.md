# Standar Internasional Penulisan Prompt AI (international_prompt_standards.md)
> **Engine:** Desaiin-Grafis Prompt Standards Core v1.0.0 (Deterministic Multimodal)  
> **Standar Rujukan Dunia:**  
> - **Formal Standards:** IEEE P3394 (*Standard for Large Language Model Agent Interface*), ISO/IEC TS 42119-8 (*AI Testing: Quality Assessment of Prompt-based Systems*), ISO/IEC 42001.  
> - **Akademik & Taksonomi:** Jonas Oppenlaender (*ACM / ArXiv - Taxonomy of Prompt Modifiers for Text-to-Image Generation*), Vivian Liu et al. (*ACM CHI - Design Guidelines for Prompt Engineering*), DAIR.AI (*Prompt Engineering Guide* - Elvis Saravia).  
> - **Frontier AI Labs:** Anthropic (*Interactive Prompt Engineering & XML Delimiting Standards*), OpenAI (*Prompt Engineering Guide & Six Core Strategies*), Midjourney Research (*v6.1 Natural Language Prompting Architecture*), Black Forest Labs (*FLUX.1 Spatial Binding Guide*), Runway Research (*Gen-3 Alpha Director's Guide*).  
> - **Sinematografi & Seni Fisik:** American Society of Cinematographers (ASC Manual), Walter Murch (*The Rule of Six*), Johannes Itten (*Bauhaus Color Theory*).

---

## 1. 6 PILAR MUTLAK STANDAR PROMPT INTERNASIONAL

Seluruh prompt yang dirancang di repositori ini WAJIB mematuhi **6 Pilar Standar Baku Internasional**:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 6 PILAR BAKU PENULISAN PROMPT INTERNASIONAL (IEEE/ISO/FRONTIER LABS)    │
├────────────────────────────────────────────────────────────────────────┤
│ 1. [STD-01] STRUCTURAL_DELIMITATION (Anthropic XML / OpenAI Delimiters)│
│ 2. [STD-02] NATURAL_DESCRIPTIVE_LANGUAGE (Midjourney v6.1 / FLUX.1)    │
│ 3. [STD-03] PHYSICAL_GROUNDING_AND_NO_SLOP (Eliminasi Buzzwords Basi)  │
│ 4. [STD-04] OPPENLAENDER_6_PART_TAXONOMY (Subjek, Gaya, Cahaya, dll.) │
│ 5. [STD-05] CINEMATIC_DIRECTOR_KINEMATICS (Runway / Kling Camera Tags) │
│ 6. [STD-06] DETERMINISTIC_PARAMETER_FLAGS (--style raw, --ar, ISO/IEC) │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. PILAR 1: PEMBATAS STRUKTURAL (ANTHROPIC XML & OPENAI DELIMITERS)

Berdasarkan pedoman resmi Anthropic dan OpenAI, instruksi prompt untuk agen dan model multimodal harus memisahkan peran teks secara tegas menggunakan tag struktural atau delimiter untuk mencegah *Prompt Injection* dan ambiguitas semantik:

### A. Format Anthropic XML Standard:
```xml
<task_specification>
  <role>Director of Photography & Prompt Architect</role>
  <objective>Generate a world-class luxury watch commercial visual</objective>
  <constraints>
    <item>No plastic/wax smoothing</item>
    <item>Strict 16:9 aspect ratio</item>
    <item>Use physical Hasselblad H6D camera parameters</item>
  </constraints>
  <prompt_payload>
    [7-Segment Compiled Prompt]
  </prompt_payload>
</task_specification>
```

### B. Format OpenAI Triple-Delimiter Standard:
Gunakan tanda pemisah `"""` atau `---` untuk memisahkan instruksi sistem, konteks referensi, dan parameter input:
```text
Instructions:
Compile a cinematic image prompt following the 7-segment physics formula.

Reference Equipment:
"""
Camera: Arri Alexa LF
Lens: Cooke Anamorphic 40mm at T2.0
Film Stock: Kodak Vision3 500T 5219
"""
```

---

## 3. PILAR 2: ELIMINASI "KEYWORD SOUP" & ADOPSI BAHASA NATURAL

Berdasarkan dokumentasi resmi **Midjourney v6.1** dan **Black Forest Labs (FLUX.1)**:
1. **Tinggalkan "Keyword Soup" Era Lama (v4/v5):**  
   DILARANG menumpuk kata kunci acak yang dipisahkan koma tanpa gramatika:  
   ❌ *Salah:* `woman, beautiful, smiling, 8k, realistic, unreal engine, masterpiece, volumetric light, trending`
2. **Wajib Menggunakan Kalimat Deskriptif Berstruktur Alami:**  
   Gunakan kalimat utuh yang menjelaskan hubungan spasial dan aksi dinamis:  
   ✔️ *Benar:* `An intimate medium close-up of a 38-year-old female marine biologist examining a bioluminescent coral sample under a warm desk lamp in a darkened research vessel at sea. Soft sea spray visible on the observation window behind her.`

---

## 4. PILAR 3: ELIMINASI KATA-KATA BASI AI (*ANTI-SLOP POLICY*)

Riset akademik ACM CHI (Liu et al.) dan Midjourney Research membuktikan bahwa kata-kata hiperbolis (*quality buzzwords*) **TIDAK MENINGKATKAN KUALITAS** pada model modern berbasis difusi canggih, melainkan justru mengaktifkan bobot gambar generik yang terkesan murahan (*AI Slop*).

### Daftar Kata Terlarang (Banned Buzzwords):
- ❌ `photorealistic` / `hyper-realistic` / `ultra-realistic`
- ❌ `8k` / `4k wallpaper` / `ultra detailed`
- ❌ `unreal engine render` / `octane render` / `vray render`
- ❌ `trending on artstation` / `deviantart`
- ❌ `masterpiece` / `award winning` / `stunning`
- ❌ `smooth skin` / `perfect porcelain face`

### Pengganti Baku Standar Industri:
| Kata Terlarang (Slop) | Pengganti Berstandar Internasional (Physical Optics & Materials) |
| :--- | :--- |
| `photorealistic` | `Shot on Hasselblad H6D-100c with HC 100mm f/2.2 lens at f/4` |
| `ultra detailed` | `Microscopic tactile texture, authentic skin pores, subsurface scattering, visible fabric weave` |
| `8k / 4k wallpaper` | `Large format 4x5 film resolution, razor-sharp edge definition, zero chromatic aberration` |
| `masterpiece lighting` | `Rembrandt chiaroscuro key lighting from a 45-degree diffused window, gentle silver fill reflector` |
| `smooth skin` | `Luminous natural skin tones with authentic biological pores, fine laugh lines, and catchlight in irises` |

---

## 5. PILAR 4: TAKSONOMI PROMPT 6-BAGIAN JONAS OPPENLAENDER (ACM / ARXIV)

Sesuai taksonomi ilmiah Jonas Oppenlaender (*A Taxonomy of Prompt Modifiers for Text-to-Image Generation*), setiap prompt teks-ke-gambar wajib mengkombinasikan 6 kelompok modifier fungsional:

```
┌────────────────────────────────────────────────────────────────────────┐
│ TAKSONOMI 6-MODIFIER OPPENLAENDER                                      │
├────────────────────────────────────────────────────────────────────────┤
│ 1. SUBJECT MODIFIER: Entitas utama, postur, ekspresi, busana          │
│ 2. ENVIRONMENT MODIFIER: Latar spasial, cuaca, atmosfer, kedalaman     │
│ 3. LIGHTING MODIFIER: Posisi cahaya fisik, suhu Kelvin, rasio bayangan│
│ 4. COLOR MODIFIER: Palet 60-30-10, emulasi film stock (Kodak/Fuji)     │
│ 5. COMPOSITION MODIFIER: Ukuran shot (MS/CU), sudut kamera, lensa (mm)│
│ 6. MATERIAL MODIFIER: Tekstur permukaan nyata (kulit, kain, marmer)   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 6. PILAR 5: STANDAR PENGARAHAN KINEMATIKA SINEMA RUNWAY RESEARCH (VIDEO AI)

Untuk AI video generator (Runway Gen-3 Alpha, Kling 1.5, OpenAI Sora, Luma Dream Machine), penulisan prompt wajib mengadopsi standar sintaks **Runway Director's Guide**:

### Rumus Sintaks Video Kanonikal:
```
[Camera]: [Vektor Gerakan Fisik Kamera, misal: Smooth low-angle dolly-in forward, continuous tracking]. [Scene Description]: [Subjek melakukan aksi dengan kinetika fisik dan inersia], [Pencahayaan & Atmosfer], [Lensa Sinema & Emulasi Film Stock]. 24fps cinematic pacing, natural fluid physics, zero morphing.
```

- **Invarian Vektor:** Wajib menyebutkan sumbu gerakan: *Dolly in/out* (Sumbu Z), *Truck left/right* (Sumbu X), *Pedestal/Crane* (Sumbu Y), *Pan/Tilt* (Rotasi).
- **Invarian Waktu:** Kecepatan 24fps dan shutter 180° untuk mencegah motion blur buatan yang patah-patah (*stutter-free*).

---

## 7. PILAR 6: PARAMETER DETERMINISTIK ENGINE (MIDJOURNEY, FLUX, RUNWAY)

1. **Midjourney v6.1:**
   - `--v 6.1`: Memastikan model generasi terbaru.
   - `--style raw`: **MANDATORI** untuk fotografi dan fotorealisme guna mematikan filter polesan estetika bawaan Midjourney.
   - `--ar [W:H]`: Aspek rasio eksplisit (`16:9`, `9:16`, `4:5`, `1:1`, `21:9`).
   - `--stylize [50-250]`: Standar natural: `100` atau `150`.
2. **FLUX.1 (Dev / Schnell):**
   - Format narasi spasial terperinci.
   - Tipografi dalam gambar diapit tanda petik dua ganda (`a sign reading "METROPOLIS"`).
3. **Runway Gen-3 / Kling 1.5:**
   - Prompt negatif mandatory: `morphing, flickering, unstable limbs, deformed hands, blurry, low-res, cartoon`.
