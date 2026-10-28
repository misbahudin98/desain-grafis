# Universal System Invariants & Autonomous Agent Rules (GEMINI.md)
> **Engine:** Desain-Grafis Core v1.0.0 (SDD-Creative-Deterministic)  
> **Standards:** Bauhaus, Dieter Rams (*10 Principles*), Josef Müller-Brockmann (*Grid Systems*), Robert Bringhurst (*Typographic Style*), American Society of Cinematographers (ASC), Disney's 12 Principles of Animation, WCAG 2.2 AAA, ISO 216 / ISO 12647-2, IAB Tech Lab, Meta/WhatsApp Safe Zones.

---

## 1. ATURAN KERJA UTAMA & ANTI-SLOP POLICY

Seluruh model AI (Gemini, Antigravity, Claude, Cursor) dan perancang kreatif manusia wajib mematuhi aturan baku ini:

1. **[RULE-01-NO-PLACEHOLDER] Kontrak Kode & Prompt 100% Utuh:**
   - Dilarang keras menggunakan komentar pemalas atau prompt rintisan: `// add more details later`, `/* ...rest of prompt... */`, atau kata-kata umum tanpa nilai estetika.
   - Prompt yang dihasilkan wajib tuntas, terkalibrasi parameter optik dan kameranya, serta langsung siap digunakan di engine produksi.

2. **[RULE-02-ZERO-AI-SLOP] Larangan Mutlak Klise Visual AI:**
   - Eliminasi kulit lilin mengkilap, tangan cacat, gradasi ungu-pink murahan, dan teks mengambang fiktif.
   - Setiap visual manusia wajib menyertakan mikrotekstur pori-pori (*subsurface scattering*), garis ekspresi natural, dan *catchlight* bola mata yang koheren.

3. **[RULE-03-GROUNDED-OPTICS] Fisika Kamera & Lensa Eksplisit:**
   - Dilarang menggunakan istilah basi seperti "photorealistic", "ultra realistic", atau "8k wallpaper".
   - Wajib menggantinya dengan spesifikasi kamera nyata (Hasselblad H6D, Leica M11, Arri Alexa LF), panjang fokus lensa ($35\text{mm}, 50\text{mm}, 85\text{mm}$), dan bukaan diafragma ($f/1.4, f/2.8, f/8$).

4. **[RULE-04-CINEMATIC-MOTION] Vektor Gerak Fisik pada Video:**
   - Dilarang membuat video dengan kamera melayang acak tanpa gravitasi (*drifting camera*).
   - Gunakan vektor kamera fisik: Dolly In/Out, Truck Left/Right, Crane Boom, Slow Pan, atau Orbit Arc dengan kecepatan 24fps dan rana 180°.

5. **[RULE-05-COLOR-DISCIPLINE] Aturan Distribusi 60-30-10 & Emulasi Film Kimia:**
   - Terapkan 60% warna dominan netral, 30% warna struktural, dan 10% warna aksen fokus.
   - Gunakan emulasi film kimia nyata (Kodak Vision3 500T, Kodak Portra 400, Fujifilm Eterna) untuk mencegah saturasi berlebih.

6. **[RULE-06-SWISS-TYPOGRAPHY] Tata Letak Grid 8-Point & Ukuran Karakter Bringhurst:**
   - Seluruh susunan grafis terikat pada sistem kisi modular kelipatan 8px.
   - Panjang baris teks baca wajib dikontrol ketat antara 45 hingga 75 karakter per baris (CPL).

7. **[RULE-07-AUTONOMOUS-EXECUTION] Eksekusi Mandiri & Kualitas Terverifikasi:**
   - Eksekusi pembuatan berkas, pengujian skrip Python, dan validasi kontras secara mandiri dan proaktif dalam satu giliran kerja.
   - Wajib memverifikasi skor audit prompt ($\ge 85/100$) menggunakan `scripts/audit_design_prompt.py`.

8. **[RULE-08-PROMPT-STANDARDS] Kepatuhan IEEE P3394 & ISO/IEC TS 42119-8:**
   - Wajib menerapkan taksonomi 6-modifier Jonas Oppenlaender (ACM), pembatas XML Anthropic, dan parameter deterministik `--style raw`.

9. **[RULE-09-MEDIA-STANDARDS] Kepatuhan ICoD, ACES, & SMPTE 180°:**
   - Wajib menerapkan Ansel Adams Zone System, ACES Color pipeline, rasio data-ke-tinta Edward Tufte, dan 12 prinsip animasi Disney.

10. **[RULE-10-COLLATERAL-STANDARDS] Kepatuhan ISO 216, IAB LEAN, & Meta Safe Zones:**
    - Wajib menerapkan bleed $3\text{mm}$ pada cetak, optical center $55\% - 60\%$, batas LEAN IAB $\le 200\text{KB}$, dan zona aman UI cerita 9:16 (Top $270\text{px}$, Bottom $270\text{px}$/$670\text{px}$, Margin $65\text{px}$).

11. **[RULE-11-PURPOSE-DRIVEN-CONTENT] 10 Dimensi Visual Berdampak Tinggi:**
    - Setiap visual dan video wajib difokuskan memuat: Pesan Kunci, Ciri Khas, Branding, Penawaran, Solusi Masalah, Tema, Momen, Monetisasi, Persuasi, dan Kesiapan Lintas Platform (Omnichannel).

---

## 2. PANDUAN PENGGUNAAN CEPAT (QUICK ROUTING)

- Untuk panduan interaktif penggunaan: Panggil `@playbook` atau rujuk [`doc/cara_penggunaan_skill.md`](doc/cara_penggunaan_skill.md)
- Untuk kerangka kerja konten siap pakai & monetisasi: Panggil `@strategy` atau rujuk [`doc/strategic_visual_publishing_framework.md`](doc/strategic_visual_publishing_framework.md)
- Untuk standar media dunia: Panggil `@media` atau rujuk [`doc/international_media_standards.md`](doc/international_media_standards.md)
- Untuk audit standar prompt: Panggil `@prompt` atau rujuk [`.agents/skills/international-prompt-standards/SKILL.md`](.agents/skills/international-prompt-standards/SKILL.md)
- Untuk prompt foto & ilustrasi: Panggil `@image` atau rujuk [`.agents/skills/visual-prompt-architect/SKILL.md`](.agents/skills/visual-prompt-architect/SKILL.md)
- Untuk video & storyboard: Panggil `@video` atau rujuk [`.agents/skills/cinema-video-director/SKILL.md`](.agents/skills/cinema-video-director/SKILL.md)
- Untuk brand identity & logo: Panggil `@brand` atau rujuk [`.agents/skills/brand-identity-crafter/SKILL.md`](.agents/skills/brand-identity-crafter/SKILL.md)
- Untuk flayer, banner, carousel, status/stories: Panggil `@marketing` atau `@collateral` atau rujuk [`.agents/skills/marketing-collateral-architect/SKILL.md`](.agents/skills/marketing-collateral-architect/SKILL.md)
- Untuk grafik kode SVG: Panggil `@programmatic` atau jalankan `python .agents/skills/programmatic-graphics-engine/scripts/generate_architecture_banner.py`
- Untuk audit kualitas prompt: Jalankan `python scripts/audit_design_prompt.py`
- Untuk validasi safe zones & spesifikasi marketing: Jalankan `python scripts/verify_collateral_specs.py`
