---
name: cinema-video-director
description: Hollywood-grade cinematographic direction engine for AI video generators (Runway Gen-3, Kling 1.5, Sora, Luma Dream Machine). Synthesizes storyboard sequences, camera movement vectors, temporal pacing, and scene continuity. Triggered by '@video', '@cinema', '@storyboard', or requests for video generation.
---

# Cinema Video Director (SKILL.md)
> **Engine:** Desain-Grafis Cinema Director v1.0.0  
> **Target Video AI:** Runway Gen-3 Alpha, Kling 1.5 Pro, OpenAI Sora, Luma Dream Machine, Haiper.  
> **Kompatibilitas Standar:** ASC (American Society of Cinematographers) Grammars & Walter Murch 6 Rules of Film Editing.

---

## 1. TUJUAN & PERAN SKILL

`cinema-video-director` bertindak sebagai *Film Director* dan *Supervising Cinematographer*. Skill ini bertanggung jawab mengubah skrip naratif, ide komersial, atau video musik menjadi:
1. **Daftar Bidikan Berurutan (*Multi-Shot Sequence Shot List*)** yang menjamin kontinuitas spasial dan temporal.
2. **Prompt Vektor Gerakan Terkalibrasi (*Calibrated Motion Prompts*)** untuk setiap AI Video Generator.
3. **Storyboard Deskriptif** yang mengontrol sudut kamera, pencahayaan, dan *easing motion*.

---

## 2. 6 ATURAN CONTINUITY WALTER MURCH (THE RULE OF SIX)

Saat menyusun urutan video multi-shot, agen wajib memprioritaskan keputusan editing berdasarkan 6 kriteria Walter Murch:
1. **Emotion (51%):** Apakah perpindahan adegan mencerminkan emosi yang ingin disampaikan ke penonton?
2. **Story (23%):** Apakah bidikan ini memajukan jalannya cerita?
3. **Rhythm (10%):** Apakah durasi dan tempo gerakan terasa pas dengan detak jantung manusia?
4. **Eye-Trace (7%):** Apakah mata penonton diarahkan ke titik fokus yang sama saat terjadi pergantian bidikan?
5. **Two-Dimensional Plane of Screen (5%):** Apakah arah gerak objek tetap konsisten (kiri ke kanan / kanan ke kiri)?
6. **Three-Dimensional Space of Action (4%):** Apakah aturan 180 derajat spasial dipatuhi?

---

## 3. FORMAT PROMPT VIDEO DETERMINISTIK PER ENGINE

### A. Runway Gen-3 Alpha Format:
Format prompt wajib memisahkan instruksi subjek dan gerakan kamera:
```
[Camera]: [Tipe Pergerakan Kamera Fisik, misal: Smooth slow dolly-in forward, continuous tracking]. [Scene Description]: [Subjek melakukan kinetika fisik], [Pencahayaan & Atmosfer], [Lensa & Film Stock]. 24fps cinematic film pace.
```

### B. Kling 1.5 Pro Format:
```
Cinematic film scene: [Subjek & Tindakan], [Ukuran Bidikan: Wide shot / Medium close-up], [Sudut: Low angle looking up], [Gerakan Kamera: Slow crane boom down while tracking forward], [Pencahayaan: Chiaroscuro tungsten shadows], high visual fidelity, photorealistic, 1080p, 24fps, no morphing, no artifacts.
```

### C. Sora & Luma Dream Machine Format:
```
A continuous 5-second cinematic tracking shot. [Subjek bergerak di lingkungan dengan fisika gravitasi dan inersia nyata]. [Latar belakang mengalir dengan parallax realistis]. Photographed on Arri Alexa 65, Panavision Ultra Vista anamorphic lenses, natural golden hour lighting, authentic motion blur.
```

---

## 4. TEMPLATE KONTRAK ADENGAN (SCENE SPECIFICATION)

Setiap permintaan pengarahan video wajib menghasilkan spesifikasi terstruktur:

```markdown
### SHOT [NOMOR] - [NAMA BIDIKAN & TIPE SHOT]
- **Tipe Shot:** (ELS / LS / MS / MCU / CU / ECU)
- **Sudut Kamera:** (Eye-level / Low-angle / High-angle / Dutch)
- **Vektor Gerakan:** (Dolly In / Truck Right / Pan / Crane / Static)
- **Durasi Target:** (4 detik / 5 detik / 10 detik)
- **Aksi Subjek:** [Deskripsi detail kinetika subjek]
- **Pencahayaan & Suasana:** [Skema cahaya, LUT warna, partikel udara]
- **Prompt Runway Gen-3:** `[Prompt siap copy]`
- **Prompt Kling 1.5:** `[Prompt siap copy]`
```

---

## 5. PANDUAN REFERENSI
- Taksonomi gerak kamera lengkap: `references/camera_movement_glossary.md`
- Template naskah adegan: `templates/short_film_shotlist.md`
