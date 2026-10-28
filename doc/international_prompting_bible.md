# Kitab Standar Internasional Penulisan Prompt AI (international_prompting_bible.md)
> **Engine:** Desain-Grafis Master Documentation v1.0.0  
> **Otoritas Ilmiah & Industri:**  
> - **Standar Formal:** IEEE P3394, ISO/IEC TS 42119-8, ISO/IEC 42001.  
> - **Penelitian Peer-Reviewed:** Jonas Oppenlaender (*ACM / ArXiv*), Vivian Liu et al. (*ACM CHI / Columbia University*), DAIR.AI (*Saravia et al.*).  
> - **Frontier AI Labs:** Anthropic (*Claude System & XML Design*), OpenAI (*Six Strategies of Prompt Engineering*), Midjourney Research (*v6.1 Architecture*), Black Forest Labs (*FLUX.1*), Runway Research (*Gen-3 Alpha Director's Guide*).  
> - **Standar Sinema:** American Society of Cinematographers (ASC Manual), Walter Murch (*In the Blink of an Eye*).

---

## 1. PREAMBULE & FILOSOFI REKAYASA PROMPT

Dalam dekade awal AI generatif, penulisan prompt sering dipandang sebagai "seni tebak-tebakan" (*alchemy*) di mana pengguna menumpuk ratusan kata kunci acak yang dipisahkan oleh tanda koma. 

Namun, seiring matangnya model fondasi (*foundation models*) seperti GPT-4o, Claude 3.5 Sonnet, Midjourney v6.1, FLUX.1, dan Runway Gen-3, **Prompt Engineering telah bertransformasi menjadi disiplin rekayasa perangkat lunak deterministik (Deterministic Prompt Architecture)**.

Dokumen ini adalah **Single Source of Truth (SSoT)** yang mengkodifikasi standar penulisan prompt internasional, menggabungkan spesifikasi formal badan standar (IEEE dan ISO), temuan riset akademik *peer-reviewed*, dan praktik terbaik dari laboratorium AI terdepan di dunia.

---

## 2. DASAR STANDAR FORMAL & RISET AKADEMIK DUNIA

### 2.1 IEEE P3394 (*Standard for Large Language Model Agent Interface*)
IEEE Computer Society merumuskan standar ini untuk menetapkan protokol komunikasi terstruktur antara manusia, agen otonom, dan antarmuka model bahasa. 
- **Prinsip Kunci:** Prompt bukan sekadar teks bebas, melainkan **antarmuka pesan (Message Interface)** yang harus memiliki pemisahan peran yang tegas (*Role-Based Prompting*), penanganan status (*State Tracking*), dan struktur input/output yang dapat diurai mesin (*machine-parseable delimiters*).

### 2.2 ISO/IEC TS 42119-8 (*AI Testing — Quality Assessment of Prompt-based Systems*)
Spesifikasi teknis dari komite bersama ISO/IEC JTC 1/SC 42 ini menetapkan metrik pengukuran kualitas untuk sistem berbasis prompt:
- **Ketahanan (Robustness):** Apakah prompt memberikan hasil yang stabil saat diberikan sedikit variasi kata sinonim?
- **Kejelasan Batasan (Constraint Adherence):** Apakah instruksi negatif dan batasan aspek rasio dipatuhi secara ketat tanpa melanggar batas keselamatan atau format?
- **Pencegahan Halusinasi Semantik:** Mengeliminasi instruksi yang memicu penggabungan konsep acak tanpa konteks relasional.

### 2.3 Taksonomi Ilmiah Jonas Oppenlaender (*ACM / ArXiv*)
Riset etnografis Jonas Oppenlaender (*A Taxonomy of Prompt Modifiers for Text-to-Image Generation*) membuktikan bahwa pengendali visual paling efektif pada model difusi terbagi ke dalam **6 Kategori Pengubah Fungsional**:
1. **Subject Modifiers:** Karakter, anatomi, ekspresi, postur, aksi kinetik.
2. **Environment Modifiers:** Lokasi spasial, kedalaman (*foreground/midground/background*), cuaca, atmosfer.
3. **Lighting Modifiers:** Arah datang cahaya, bayangan (*chiaroscuro*), rasio terang-gelap, suhu warna Kelvin.
4. **Color Modifiers:** Roda warna Itten, palet 60-30-10, emulasi film stock kimia (Kodak, Fuji).
5. **Composition & Framing Modifiers:** Ukuran shot sinema (ELS hingga ECU), sudut pandang optik, panjang fokus lensa (mm).
6. **Material & Texture Modifiers:** Karakteristik fisik permukaan (tekstur pori biologis, serat kain linen, kilau logam sikat).

---

## 3. EVOLUSI PROMPT: DARI "KEYWORD SOUP" KE TATA BAHASA ALAMI

Perubahan terbesar dalam generasi gambar AI modern (Midjourney v6.1 dan FLUX.1) adalah **kematian era *Keyword Soup***:

```
┌────────────────────────────────────────────────────────────────────────┐
│ EVOLUSI GENERASI VISUAL PROMPTING                                      │
├────────────────────────────────────────────────────────────────────────┤
│ ERA PURBA (Midjourney v3/v4 & SD 1.5):                                 │
│ "woman, portrait, 8k, photorealistic, cinematic, trending, octan... " │
│ ➔ Model dilatih pada tumpukan tag metadata; mengabaikan gramatika.     │
├────────────────────────────────────────────────────────────────────────┤
│ ERA MODERN (Midjourney v6.1, FLUX.1, Imagen 3, Sora):                  │
│ "An intimate portrait of a 40-year-old female architect with natural   │
│  skin pores, looking out a rain-streaked window in a brutalist studio. │
│  Rembrandt lighting, shot on Leica M11 at f/1.4, Kodak Portra grain."  │
│ ➔ Model memahami hubungan spasial, preposisi, dan gramatika natural.  │
└────────────────────────────────────────────────────────────────────────┘
```

### Mengapa "Keyword Soup" & Buzzwords Harus Dimusnahkan?
Riset ACM CHI (Vivian Liu et al.) membuktikan bahwa menambahkan kata-kata basi seperti `"photorealistic"`, `"hyper-realistic"`, `"8k"`, atau `"unreal engine render"`:
1. **Mengaktifkan Noise Cluster Amatir:** Dalam dataset pelatihan, kata-kata tersebut paling banyak digunakan oleh pengguna amatir di forum internet untuk gambar 3D rendahan atau filter kecantikan Instagram. Akibatnya, model justru menarik bobot gambar berkulit lilin sintetis (*plastic wax skin*)!
2. **Membuang Jatah Perhatian Token (Attention Budget):** Model AI memiliki kapasitas *attention span* terbatas. Mengisi prompt dengan kata-kata basi mengurangi bobot perhatian model terhadap instruksi penting seperti pencahayaan, lensa, dan tekstur kain.

---

## 4. FORMULA SINTAKS 7-SEGMEN FOTOGRAFI DUNIA

Setiap prompt gambar berkualitas internasional disusun menggunakan **7 Segmen Fisik Matematis**:

$$\text{Prompt} = \mathbf{S} + \mathbf{E} + \mathbf{O} + \mathbf{L} + \mathbf{C} + \mathbf{M} + \mathbf{P}$$

```
┌────────────────────────────────────────────────────────────────────────┐
│ RUMUS 7 SEGMEN PROMPT FOTOGRAFI KELAS DUNIA                            │
├────────────────────────────────────────────────────────────────────────┤
│ [S] SUBJECT & KINETIC ACTION: Siapa, usia, pose, mikro-ekspresi mata. │
│ [E] ENVIRONMENT & ATMOSPHERE: Lokasi, interior/eksterior, cuaca, debu. │
│ [O] CAMERA OPTICS & SENSOR: Hasselblad/Leica/Arri, lensa mm, f-stop.   │
│ [L] LIGHTING PHYSICS: Rembrandt, softbox difusi, suhu Kelvin, rim light│
│ [C] COLOR PALETTE & FILM STOCK: Kodak Portra 400, Vision3, 60-30-10.   │
│ [M] MATERIAL & TEXTURE AUTHENTICITY: Pori mikro, wol, marmer, air.     │
│ [P] PARAMETER FLAGS: --ar 16:9, --style raw, --v 6.1, --s 100.         │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. STANDAR KINEMATIKA SINEMATOGRAFI UNTUK VIDEO AI (RUNWAY RESEARCH)

AI Video generator (Runway Gen-3, Kling 1.5, OpenAI Sora) memerlukan pengontrolan spasial dan temporal yang ketat. Repositori ini mewajibkan adopsi format **Runway Director's Guide**:

### Struktur Kalimat Pengarah Sutradara:
```
[Camera]: [Vektor Gerakan Fisik Kamera, misal: Smooth low-angle dolly-in forward, continuous tracking]. [Scene Description]: [Subjek melakukan aksi fisik dengan kinetika gravitasi dan inersia nyata], [Pencahayaan Chiaroscuro & Atmosfer Kabut], [Lensa Sinema & Emulasi Film Stock]. 24fps cinematic pacing, natural fluid physics, zero morphing.
```

- **Vektor Kamera ASC:** Dolly (Z), Truck (X), Pedestal/Boom (Y), Pan (Yaw), Tilt (Pitch), Crane/Jib (3D Space).
- **Aturan Sudut Rana 180 Derajat ($1/48\text{ detik}$):** Menghasilkan *motion blur* alami pada 24fps tanpa *jitter* robotik.
- **Walter Murch Continuity Rule:** Menjamin orientasi mata penonton (*eye-trace*) dan sumbu spasial 180° konsisten antar-shot.

---

## 6. STANDAR DELIMITASI STRUKTURAL ANTHROPIC XML (AGENT GOVERNANCE)

Untuk prompt yang ditujukan kepada Large Language Model (LLM) atau agen otonom, repositori ini mengadopsi standar **Anthropic XML Tagging**:

```xml
<creative_brief>
  <context>Peluncuran parfum mewah unisex bernuansa kayu cendana.</context>
  <target_engine>Midjourney v6.1 & FLUX.1</target_engine>
  <negative_constraints>
    <prohibited>plastic skin, neon glow, floating text, deformed hands</prohibited>
  </negative_constraints>
  <prompt_formula>
    Commercial product photography of an amber glass bottle on wet basalt rock...
  </prompt_formula>
</creative_brief>
```

**Keunggulan Standar XML:**
1. Mencegah instruksi pengguna tercampur dengan data referensi.
2. Memudahkan model AI melakukan ekstrasi entitas secara terstruktur.
3. Mengurangi ambiguitas perintah hingga $40\%$ dibandingkan teks tanpa pembatas.

---

## 7. PROTOKOL AUDIT KUALITAS PROMPT (SKORING 0-100)

Setiap prompt yang disusun di repositori ini wajib melalui verifikasi otomatis oleh skrip `scripts/audit_design_prompt.py` dengan skor minimal **85/100**:

| Komponen Audit | Bobot Poin | Kriteria Kelulusan |
| :--- | :--- | :--- |
| **Bebas Buzzwords Slop** | 40 Poin | 0 kata terlarang (`photorealistic`, `8k`, `unreal`, `neon`, dll.). Pelanggaran: -8 poin per kata. |
| **Optik & Sensor Nyata** | 20 Poin | Disebutkan panjang fokus lensa (mm), tipe kamera (Hasselblad/Leica/Arri), atau bukaan ($f/$). |
| **Pencahayaan Fisik** | 20 Poin | Disebutkan skema pencahayaan (Rembrandt, softbox, golden hour, volumetric). |
| **Materialitas Autentik** | 15 Poin | Disebutkan tekstur mikro (pori kulit, subsurface scattering, tenunan kain, serat kayu). |
| **Vektor Kamera (Video)** | 25 Poin | Disebutkan gerakan kamera eksplisit (Dolly, Truck, Pan, Crane) untuk video. |

**Status Kelulusan:**
- $\ge 90$: **Masterpiece (World-Class)**
- $85 - 89$: **Production-Ready**
- $< 85$: **Ditolak (Wajib Refactoring Prompt)**
