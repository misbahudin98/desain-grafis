# Standar Produksi Grafis & Video Multimedia Internasional (multimedia_production_standards.md)
> **Engine:** Desaiin-Grafis Multimedia Standards Core v1.0.0  
> **Otoritas Rujukan:**  
> - **Grafis & Desain:** International Council of Design (ICoD), Josef Müller-Brockmann (*Swiss Grid*), Dieter Rams (*Braun*), Edward Tufte (*Yale*), Robert Bringhurst (*Typographic Style*), ISO 12647 (*Print Standards*), WCAG 2.2 AAA.  
> - **Fotografi & Sinematografi:** American Society of Cinematographers (ASC Manual), Ansel Adams (*Zone System*), Henri Cartier-Bresson (*The Decisive Moment*), Roger Deakins, ASC, BSC.  
> - **Video, Animasi, & Motion:** Disney's 12 Principles of Animation (Thomas & Johnston), SMPTE Standards (Shutter 180°, Timecode, 24fps), Walter Murch (*The Rule of Six*), Saul Bass (*Kinetic Title Design*).  
> - **Sains Warna:** Academy Color Encoding System (ACES - SMPTE ST 2065-1), CIE 1931 Chromaticity, Johannes Itten Bauhaus.

---

## 1. 8 INVARIAN MUTLAK PRODUKSI MULTIMEDIA KELAS DUNIA

Seluruh aset gambar statis, identitas visual, grafis bergerak (*motion graphics*), dan video sinematik dalam repositori ini terikat oleh **8 Invarian Produksi**:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 8 INVARIAN BAKU PRODUKSI GAMBAR & VIDEO KELAS DUNIA                    │
├────────────────────────────────────────────────────────────────────────┤
│ 1. [MED-01] ICOD_ETHICAL_AND_FUNCTIONAL_CLARITY (Desain Beretika & Jelas│
│ 2. [MED-02] ANSEL_ADAMS_ZONE_SYSTEM (Pre-visualisasi Rentang Dinamis) │
│ 3. [MED-03] ACES_COLOR_MANAGEMENT_PIPELINE (Manajemen Warna Standar)  │
│ 4. [MED-04] TUFTE_DATA_TO_INK_AND_SWISS_GRID (Eliminasi Chartjunk)    │
│ 5. [MED-05] ASC_OPTICAL_CAMERA_GROUNDING (Kamera, Lensa Prime, DOF)   │
│ 6. [MED-06] SMPTE_180_DEGREE_SHUTTER_PHYSICS (24fps Natural Blur)     │
│ 7. [MED-07] DISNEY_12_KINETIC_MOTION (Arcs, Easing Bézier, Follow-thru│
│ 8. [MED-08] WCAG_2_2_AAA_UNIVERSAL_ACCESSIBILITY (Kontras >= 7:1)     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. PILAR FOTOGRAFI & GAMBAR: THE ZONE SYSTEM & OPTIK FISIK

### A. Ansel Adams Zone System (Pre-visualisasi Kontras 10 Zona):
Setiap prompt gambar foto wajib mempertimbangkan pemisahan gradasi cahaya dari Zona 0 (Hitam pekat tanpa detail) hingga Zona X (Putih terbakar murni):
- **Zona II & III (Deep Shadows with Texture):** Bayangan gelap yang tetap mempertahankan tekstur kain wol atau urat kayu.
- **Zona V (18% Middle Gray):** Warna kulit netral atau batu alam.
- **Zona VI & VII (Warm Highlights):** Cahaya jatuh pada tulang pipi, kertas putih, atau kilau air laut.
- **Zona VIII (Soft Highlight Roll-off):** Pantulan cahaya lembut pada kaca tanpa terjadi *digital clipping* (putih mati).

### B. Otoritas Lensa & Optik ASC:
Dilarang mendefinisikan kamera generik. Wajib menentukan:
1. **Lensa Prime Berkarakter:** Leica Summilux ($50\text{mm} / 75\text{mm}$), Zeiss Master Prime ($35\text{mm} / 85\text{mm}$), Hasselblad HC ($100\text{mm}$ macro), Cooke S4/i Anamorphic ($40\text{mm}$).
2. **Bukaan Diafragma Rasional:**
   - Potret Intim: $f/1.4$ s/d $f/2.0$ (separasi subjek dan latar *creamy bokeh*).
   - Produk Komersial: $f/4.0$ s/d $f/8.0$ (tepi produk tajam presisi).
   - Arsitektur & Lanskap: $f/8.0$ s/d $f/11.0$ (seluruh bidang ruang tajam terdefinisi).

---

## 3. PILAR VIDEO & KINEMATIKA: SMPTE, DISNEY, & SAUL BASS

### A. Fisika Sudut Rana SMPTE ($180^\circ$ Shutter Rule):
Untuk menghasilkan kecepatan film bioskop 24 frame per detik (24fps), rana dibuka selama $\frac{1}{48}\text{ detik}$:
$$\text{Shutter Time} = \frac{1}{2 \times \text{FPS}} = \frac{1}{48\text{s}}$$
- **Mandat:** Dilarang menghasilkan video dengan gerakan kaku tanpa blur atau blur buatan yang patah-patah (*stutter*). Selalu sertakan `natural 180-degree shutter motion blur, 24fps cinematic film pace`.

### B. Disney's 12 Animation Principles dalam Video AI & Motion Graphics:
1. **Arcs (Lintasan Melengkung):** Semua gerakan kamera dan makhluk hidup wajib mengikuti busur kurva alam, bukan garis patah-patah komputer.
2. **Slow In & Slow Out (Bézier Easing):** Gerakan dimulai dengan akselerasi halus dan berakhir dengan deselerasi lembut.
3. **Follow-Through & Secondary Action:** Kain pakaian, rambut, dan debu terus bergerak setelah subjek berhenti melangkah.

### C. Kinetic Typography Saul Bass:
Teks bergerak (*motion typography*) dalam video grafis harus memiliki integrasi grafis yang erat dengan musik dan emosi naratif: tidak berputar liar tanpa makna, melainkan bergeser dengan ritme tipografi Swiss yang kokoh.

---

## 4. PILAR WARNA & MANAJEMEN ACES (ACADEMY COLOR ENCODING SYSTEM)

Setiap arahan warna wajib mematuhi standar industri perfilman internasional:
1. **Pemisahan Suhu Warna (Kelvin Temperature):**
   - Cahaya Lilin / Tungsten Hangat: $2400\text{K} - 3200\text{K}$.
   - Cahaya Siang Alami (Daylight): $5500\text{K} - 6500\text{K}$.
   - Jam Biru Senja (Blue Hour Dusk): $7500\text{K} - 9000\text{K}$.
2. **Aturan Distribusi Itten 60-30-10:**
   - 60% Warna Dominan Netral (Latar belakang / Kanvas).
   - 30% Warna Struktural (Teks bodi, elemen kartu, kostum).
   - 10% Warna Aksen Fokus (Titik tangkap mata / Tombol CTA).
3. **ACES / Film Stock Emulation:** Menggunakan emulasi warna kimia Kodak Vision3 500T 5219 (tungsten malam) atau Kodak Portra 400 (daylight potret).

---

## 5. PILAR TATA LETAK & GRAFIS: ICOD & TUFTE DATA-TO-INK

1. **ICoD Professional Ethics:** Desain grafis wajib jujur (*honest*), tidak memanipulasi persepsi, dan memprioritaskan keterbacaan (*legibility*).
2. **Edward Tufte Data-to-Ink Ratio:** Eliminasi seluruh elemen dekorasi palsu (*chartjunk*, 3D timbul murahan, bayangan bertumpuk). Maksimalkan rasio tinta/piksel yang menyampaikan pesan riil.
3. **Grid Modular Swiss 8-Point:** Seluruh padding, margin, dan line-height adalah kelipatan teratur dari $8\text{px}$ atau $4\text{px}$.
