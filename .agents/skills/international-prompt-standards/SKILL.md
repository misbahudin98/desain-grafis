---
name: international-prompt-standards
description: Global prompt architecture and compilation engine grounded in IEEE P3394, ISO/IEC TS 42119-8, Anthropic XML delimiting, OpenAI core strategies, Oppenlaender ACM taxonomy, Midjourney v6.1 natural language, and Runway Director's kinematics. Triggered by '@prompt', '@prompt-standard', '@standard', or requests to audit, refine, or write international-grade AI prompts.
---

# International Prompt Standards Master Engine (SKILL.md)
> **Engine:** Desain-Grafis Prompt Standards Compiler v1.0.0  
> **Otoritas Rujukan:** IEEE P3394, ISO/IEC TS 42119-8, Jonas Oppenlaender (ACM Taxonomy), Anthropic Claude XML Guidelines, OpenAI Prompt Engineering Guide, Midjourney v6.1 Research, Runway Director's Guide, ASC Manual.  
> **Output:** Deterministic, Slop-Free, Production-Ready Prompts for LLM, Image (Midjourney/Flux), and Video (Runway/Kling/Sora).

---

## 1. TUJUAN & LINGKUP SKILL

Skill `international-prompt-standards` adalah otoritas tertinggi dalam repositori ini untuk:
1. **Mengaudit & Menilai Prompt (Prompt Evaluation):** Memindai prompt pengguna atau agen lain dan memberikan penilaian skor 0–100 berdasarkan kepatuhan standar internasional dan eliminasi kata-kata basi AI (*buzzwords*).
2. **Mentransformasi Ide Mentah Menjadi Prompt Standar Dunia (Prompt Compilation):** Mengubah ide bebas menjadi format deskriptif berstruktur matematis dengan parameter kamera, pencahayaan, material, dan flag teknis.
3. **Menerjemahkan Antar-Engine (Cross-Engine Translation):** Mengonversi prompt master ke dalam sintaks spesifik Midjourney v6.1 (`--style raw`), FLUX.1 (spatial quote-binding), Runway Gen-3 (`[Camera]: ... [Scene]: ...`), dan Kling 1.5.

---

## 2. WORKFLOW 4 TAHAP PENYUSUNAN PROMPT

```
┌────────────────────────────────────────────────────────────────────────┐
│ WORKFLOW REKAYASA PROMPT STANDAR INTERNASIONAL                         │
├────────────────────────────────────────────────────────────────────────┤
│ TAHAP 1: DEKOMPOSISI KEBUTUHAN (EventStorming / Subject Identification)│
│          - Menentukan subjek inti, aksi fisik, emosi, dan pesan kunci. │
├────────────────────────────────────────────────────────────────────────┤
│ TAHAP 2: INJEKSI TAKSONOMI OPPENLAENDER 6-PART                         │
│          - Subjek + Lingkungan + Cahaya Fisik + Warna/Film + Komposisi │
│            + Material & Tekstur Biologis/Fisik.                        │
├────────────────────────────────────────────────────────────────────────┤
│ TAHAP 3: STRUKTURASI BAHASA NATURAL & DIRECTORIAL KINEMATICS           │
│          - Susun kalimat gramatikal alami (tanpa tumpukan koma acak).  │
│          - Jika video: tambahkan vektor gerakan ASC (Dolly/Pan/Crane). │
├────────────────────────────────────────────────────────────────────────┤
│ TAHAP 4: INJEKSI PARAMETER DETERMINISTIK & AUDIT SKOR                  │
│          - Tambahkan flag engine (--v 6.1, --style raw, --ar, 24fps).  │
│          - Jalankan verifikasi audit kualitas (Wajib Skor >= 85/100).  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. TABEL TRANSFORMASI: AMATIR VS STANDAR INTERNASIONAL

| Elemen Prompt | Gaya Amatir / AI Slop (DILARANG) | Gaya Standar Internasional (MANDATORI) |
| :--- | :--- | :--- |
| **Kualitas Umum** | `photorealistic, 8k, ultra realistic, masterpiece` | Spesifikasi kamera & lensa: `Shot on Hasselblad H6D-100c, 80mm at f/4` |
| **Tekstur Wajah** | `smooth beautiful skin, porcelain face` | `Luminous natural skin tones, subsurface scattering, authentic micro-pores, gentle laugh lines` |
| **Pencahayaan** | `epic lighting, volumetric rays everywhere, neon` | `Rembrandt chiaroscuro lighting, single north-facing softbox, subtle silver fill reflector` |
| **Warna** | `vibrant colors, colorful aesthetic` | `Kodak Portra 400 film grain, 60-30-10 color distribution, muted obsidian & warm amber tones` |
| **Gerakan Video**| `camera moves fast dynamically, cool motion` | `[Camera]: Slow, buttery-smooth low-angle dolly-in pushing forward by 15%, tracking subject` |

---

## 4. TEMPLATE KANONIKAL UNIVERSAL COMPILER

Gunakan template resmi di:
- [`templates/universal_prompt_compiler.md`](templates/universal_prompt_compiler.md)
- Daftar pustaka akademik lengkap: [`references/academic_and_industry_citations.md`](references/academic_and_industry_citations.md)

---

## 5. INSTRUKSI AUDIT OTOMATIS (QUALITY GATE)

Sebelum merilis prompt apa pun ke pengguna, agen wajib menguji prompt tersebut secara mandiri:
```bash
python scripts/audit_design_prompt.py
```
Jika skor prompt $< 85$, prompt **DITOLAK SECARA OTOMATIS** dan wajib diperbaiki dengan menambahkan parameter optik, pencahayaan fisik, atau menghapus kata-kata basi AI.
