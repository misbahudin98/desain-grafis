# Referensi Akademik & Standar Industri Kredibel Penulisan Prompt (academic_and_industry_citations.md)
> **Engine:** Desain-Grafis Bibliography & Reference Database v1.0.0  
> **Status:** Single Source of Truth (SSoT) untuk Standar Ilmiah dan Otoritas Industri Prompt Engineering.

---

## 1. STANDAR FORMAL INTERNASIONAL (STANDARDS BODIES)

1. **IEEE P3394 — Standard for Large Language Model Agent Interface:**
   - *Lembaga:* IEEE Computer Society & Artificial Intelligence Standards Committee (AISC).
   - *Fokus:* Standar antarmuka bahasa alami, protokol pesan, interoperabilitas agen, dan spesifikasi pertukaran konteks prompt antara manusia dan sistem kecerdasan buatan.
2. **ISO/IEC TS 42119-8 — Artificial Intelligence — Testing of AI — Part 8: Quality assessment of prompt-based text-to-text systems that utilize generative AI:**
   - *Lembaga:* International Organization for Standardization (ISO) & International Electrotechnical Commission (IEC) JTC 1/SC 42.
   - *Fokus:* Metodologi evaluasi mutu, reliabilitas, pengujian batas (*stress testing*), dan akurasi deterministik dari sistem berbasis prompt.
3. **ISO/IEC 42001:2023 — Artificial Intelligence Management System (AIMS):**
   - *Lembaga:* ISO/IEC.
   - *Fokus:* Tata kelola etika, mitigasi risiko halusinasi, dan transparansi operasional sistem generatif AI.

---

## 2. PENELITIAN AKADEMIK & TAKSONOMI ILMIAH (PEER-REVIEWED)

1. **Jonas Oppenlaender (2022/2023) — *A Taxonomy of Prompt Modifiers for Text-To-Image Generation*:**
   - *Publikasi:* ACM / ArXiv:2204.13788.
   - *Kontribusi:* Riset etnografi multi-bulan yang mendefinisikan 6 taksonomi pengubah prompt (*Prompt Modifiers*): *Subject, Style, Quality/Detail, Environment/Lighting, Color, Composition/Framing*. Membuktikan pentingnya struktur modifier dalam mengarahkan model difusi.
2. **Vivian Liu, Qisheng Li, & Lydia B. Chilton (2022) — *Design Guidelines for Prompt Engineering Text-to-Image Generative Models*:**
   - *Publikasi:* ACM CHI Conference on Human Factors in Computing Systems (Columbia University).
   - *Kontribusi:* Membedah trial-and-error dalam prompt engineering dan merumuskan panduan berbasis bukti (*evidence-based guidelines*) untuk menggabungkan subjek, gaya, dan hiperparameter teknis (guidance scale, sampling steps).
3. **Elvis Saravia et al. (2023-2024) — *Prompt Engineering Guide* (DAIR.AI):**
   - *Lembaga:* Demographic AI Research (DAIR.AI).
   - *Kontribusi:* Kurikulum global paling banyak dirujuk yang mengkodifikasi teknik Zero-Shot, Few-Shot, Chain-of-Thought (CoT), Self-Consistency, Directional Stimulus, dan ReAct (Reasoning + Acting).
4. **Pranab Sahoo et al. (2024) — *A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications*:**
   - *Publikasi:* ArXiv:2402.07927.
   - *Kontribusi:* Survei komprehensif atas lebih dari 30 metodologi rekayasa prompt, mengklasifikasikan teknik berbasis instruksi, penguraian masalah (*decomposition*), dan evaluasi otomatis.

---

## 3. PANDUAN RESMI FRONTIER AI LABS (INDUSTRY BENCHMARKS)

1. **Anthropic PBC — *Claude Interactive Prompt Engineering Tutorial & Documentation*:**
   - *Rujukan:* `docs.anthropic.com`
   - *Prinsip Utama:* Penggunaan tag XML (`<instructions>`, `<context>`, `<rules>`), pemisahan data dari instruksi, peran kanonikal (*Role Prompting*), dan teknik *prefilling assistant response* untuk output deterministik.
2. **OpenAI — *Prompt Engineering Guide & Best Practices*:**
   - *Rujukan:* `platform.openai.com/docs/guides/prompt-engineering`
   - *Prinsip Utama:* 6 Strategi Inti: (1) Tulis instruksi jelas, (2) Sediakan teks rujukan, (3) Pecah tugas kompleks menjadi sub-tugas, (4) Beri model waktu untuk "berpikir" (Chain of Thought), (5) Gunakan alat eksternal (tools), (6) Uji perubahan secara sistematis.
3. **Midjourney Research — *Midjourney v6 & v6.1 Documentation & Prompt Architecture*:**
   - *Rujukan:* `docs.midjourney.com`
   - *Prinsip Utama:* Menghentikan "keyword soup" era lama (v4/v5). Mengadopsi tata bahasa alami deskriptif. Penggunaan parameter `--style raw` untuk fotorealisme murni tanpa filter kecantikan otomatis, kontrol aspek rasio `--ar`, dan stylize `--s`.
4. **Black Forest Labs — *FLUX.1 Model Architecture & Prompting Guide*:**
   - *Rujukan:* `blackforestlabs.ai`
   - *Prinsip Utama:* Ikatan spasial berbasis preposisi alami (*spatial binding*), rendering tipografi tajam dalam gambar menggunakan tanda kutip dua ganda (`"..."`), dan keakuratan sensor fotografi.
5. **Runway Research — *Runway Gen-3 Alpha Director's Prompting Guide*:**
   - *Rujukan:* `runwayml.com/research`
   - *Prinsip Utama:* Pemisahan tegas antara instruksi kamera (`[Camera]: ...`) dan deskripsi adegan fisik (`[Scene]: ...`), kontrol kecepatan rana 180°, dan kontinuitas 24fps.

---

## 4. STANDAR KINEMATOGRAFI & SENI FISIK

1. **American Society of Cinematographers (ASC):**
   - *Pustaka:* *The American Cinematographer Manual* (10th/11th Edition).
   - *Standar:* Taksonomi ukuran bidikan (ELS s/d ECU), rasio pencahayaan (Key-to-Fill ratios), lensa sinema prima (Cooke, Zeiss, Angénieux), dan sudut rana 180°.
2. **Walter Murch — *In the Blink of an Eye: A Perspective on Film Editing*:**
   - *Prinsip Utama:* *The Rule of Six* (Emotion 51%, Story 23%, Rhythm 10%, Eye-trace 7%, Two-dimensional screen plane 5%, Three-dimensional space 4%).
3. **Johannes Itten — *The Art of Color* (Bauhaus):**
   - *Standar:* Roda warna 12 bagian dan 7 kontrak kontras visual.
