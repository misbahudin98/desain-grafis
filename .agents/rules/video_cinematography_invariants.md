# Invarian Sinematografi & Pengarahan Video Internasional (video_cinematography_invariants.md)
> **Engine:** Desain-Grafis Cinema Core v1.0.0  
> **Standar Dunia:** American Society of Cinematographers (ASC), British Society of Cinematographers (BSC), Walter Murch (*In the Blink of an Eye*), Disney's 12 Principles of Animation, SMPTE Standards.  
> **Target AI Engines:** Sora, Runway Gen-3 Alpha, Kling 1.5, Luma Dream Machine, Haiper, Pika 2.0, Midjourney Video.

---

## 1. MANDAT SINEMATOGRAFI TINGKAT DUNIA

AI Video generator sering kali menghasilkan klip dengan gerakan acak (*drifting camera*), distorsi bentuk (*morphing*), atau kecepatan tidak wajar. Repositori ini menerapkan **Invarian Sinematografi Ketat** agar setiap video yang dirancang memiliki gramatika film profesional, koherensi temporal, dan kualitas visual setara sinema layar lebar Hollywood.

```
┌────────────────────────────────────────────────────────────────────────┐
│ 8 PILAR SINEMATOGRAFI & GERAKAN KAMERA DETERMINISTIK                   │
├────────────────────────────────────────────────────────────────────────┤
│ 1. [CIN-01] SHOT_SIZING_GRAMMAR (ELS, LS, MS, MCU, CU, ECU)           │
│ 2. [CIN-02] CAMERA_MOVEMENT_VECTORS (Dolly, Truck, Pan, Tilt, Crane)   │
│ 3. [CIN-03] TEMPORAL_SPEED_AND_FRAME_RATES (24fps Film Pacing, Easing) │
│ 4. [CIN-04] LIGHTING_CONTINUITY_AND_ATMOSPHERE (Key/Fill/Rim, Volum)  │
│ 5. [CIN-05] 180_DEGREE_SPATIAL_AXIS_RULE (Konsistensi Orientasi Arah)  │
│ 6. [CIN-06] DISNEY_12_PRINCIPLES_OF_MOTION (Anticipation, Follow-thru) │
│ 7. [CIN-07] FOCAL_DEPTH_AND_RACK_FOCUS (Bokeh, Anamorphic, Flare)     │
│ 8. [CIN-08] PROMPT_SYNTAX_FOR_VIDEO_ENGINES (Runway, Kling, Sora)     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. TAKSONOMI UKURAN BIDIKAN (SHOT SIZING GRAMMAR)

Setiap pengarah adegan (*scene director*) wajib mendefinisikan ukuran bidikan secara eksplisit menggunakan istilah kanonikal ASC:

| Kode Shot | Nama Bidikan | Deskripsi Visual & Psikologis | Rekomendasi Lensa |
| :--- | :--- | :--- | :--- |
| **ELS** | *Extreme Long Shot* | Subjek tampak sangat kecil dalam lanskap megah. Membangun skala, kesepian, isolasi, atau keagungan alam semesta. | 18mm – 24mm Ultra Wide |
| **LS / WS** | *Long Shot / Wide Shot* | Seluruh tubuh subjek terlihat dari kepala hingga kaki beserta lingkungan sekitar. Menetapkan relasi spasial. | 28mm – 35mm Wide |
| **MS** | *Medium Shot* | Subjek terlihat dari pinggang ke atas (*waist-up*). Menyeimbangkan ekspresi karakter dan interaksi dengan lingkungan. | 50mm Standard Prime |
| **MCU** | *Medium Close-Up* | Subjek terlihat dari dada ke atas (*chest-up*). Bidikan standar wawancara dan dialog dramatis intim. | 65mm – 85mm Portrait Prime |
| **CU** | *Close-Up* | Membingkai wajah penuh dari dagu hingga puncak kepala. Menyorot emosi mendalam, ketakutan, keteguhan hati. | 85mm – 105mm Prime |
| **ECU** | *Extreme Close-Up* | Detail mikroskopis: bola mata, tetesan keringat, jari gemetar, detik jam mekanis. Menciptakan ketegangan ekstrem. | 100mm Macro / Telephoto |

---

## 3. TAKSONOMI GERAKAN KAMERA (CAMERA MOVEMENT VECTORS)

DILARANG menghasilkan perintah gerak samar seperti "camera moves nicely" atau "cool dynamic movement". Gunakan vektor gerakan fisik terkalibrasi:

1. **Dolly / Push In (Z-Axis Forward):** Kamera bergerak maju mendekati subjek di atas rel. Menandakan realisasi emosi, ketegangan meningkat, atau penetrasi ke alam pikiran karakter.
2. **Dolly Out / Pull Back (Z-Axis Backward):** Kamera mundur meninggalkan subjek. Menandakan keterasingan, perpisahan, atau mengungkap lingkungan tersembunyi (*the reveal*).
3. **Truck Left / Right (X-Axis Lateral Tracking):** Kamera bergerak menyamping sejajar dengan subjek yang sedang berjalan. Memberikan ritme pergerakan horizontal yang stabil.
4. **Pedestal / Boom (Y-Axis Vertical Shift):** Kamera naik lurus ke atas atau turun lurus ke bawah tanpa mengubah sudut kemiringan lensa.
5. **Pan Left / Right (Yaw Rotation):** Kamera diam di titik tumpu, berputar horizontal menoleh ke kiri atau kanan untuk mengikuti pandangan mata.
6. **Tilt Up / Down (Pitch Rotation):** Kamera mengangguk vertikal ke atas (mengagumi menara/raksasa) atau ke bawah (menatap jurang/kehancuran).
7. **Crane / Jib Shot:** Kamera melayang naik dari bidikan rendah tanah hingga membumbung tinggi ke udara (*sweeping aerial perspective*).
8. **Roll / Dutch Angle:** Kamera dimiringkan pada sumbu optik (5° hingga 20°). Mengindikasikan kegilaan, ketidakstabilan psikologis, atau ancaman bahaya.
9. **Orbit / 360 Arc Shot:** Kamera bergerak melingkari subjek yang sedang diam atau bergerak perlahan. Menegaskan momen epik atau krisis eksistensial.
10. **Rack Focus / Pull Focus:** Pergeseran titik fokus optik secara halus dari latar depan (*foreground*) ke latar belakang (*background*), atau sebaliknya.

---

## 4. FORMULA STRUKTUR PROMPT AI VIDEO TINGKAT LANJUT

Setiap prompt video untuk Runway Gen-3, Kling 1.5, atau Sora wajib dirangkai menggunakan **6-Lapisan Sintaks Sinematik**:

```
[UKURAN BIDIKAN & SUDUT] + [SUBJEK UTAMA & TINDAKAN DINAMIS DENGAN KINETIKA FISIK] + [VEKTOR GERAKAN KAMERA] + [PENCAHAYAAN & ATMOSFER] + [PERALATAN KAMERA & TEKSTUR FILM STOCK] + [PANDUAN TEMPORAL & PACING]
```

### Contoh Blueprint Sempurna:
> **Medium close-up, eye-level angle:** An elderly master watchmaker with weathered hands meticulously inserts a tiny ruby gear into an intricate antique mechanical clock using brass tweezers. **Camera motion:** Slow buttery-smooth dolly-in pushing forward by 15%, tracking the tweezers. **Lighting:** Chiaroscuro candlelight illuminating dust motes suspended in air, deep warm shadows in background. **Camera & Film:** Shot on Arri Alexa Mini LF, Zeiss Master Prime 85mm at T1.4, shallow depth of field, natural filmic motion blur, Kodak Vision3 500T 5219 grain texture, hyper-realistic, 24fps cinematic pacing, zero morphing.

---

## 5. PENERAPAN 12 PRINSIP ANIMASI DISNEY DALAM VIDEO AI

Setiap arahan gerak (*motion direction*) wajib mengacu pada prinsip kinetika alami:

1. **Squash and Stretch:** Objek lentur bereaksi terhadap benturan dan gravitasi tanpa kehilangan volume massanya.
2. **Anticipation (Antisipasi):** Karakter melakukan gerakan ancang-ancang sebelum aksi utama (contoh: menekuk lutut sebelum melompat).
3. **Staging:** Komposisi frame mengarahkan perhatian mata penonton tepat ke titik aksi tanpa ada distraksi.
4. **Straight Ahead & Pose to Pose:** Pengontrolan keyframe agar gerakan tetap proporsional dan tidak terjadi *limbs morphing*.
5. **Follow Through & Overlapping Action:** Rambut, kain, dan jubah terus bergerak sesaat setelah tubuh subjek berhenti melangkah.
6. **Slow In and Slow Out (Easing Curve):** Gerakan alami dimulai perlahan, berakselerasi di tengah, dan melambat saat berhenti (kurva Bézier alami, bukan linier kaku robotik).
7. **Arcs (Lintasan Busur):** Semua makhluk hidup dan kamera bergerak membentuk kurva melengkung alami, bukan garis patah-patah bersudut tajam.
8. **Secondary Action:** Gerakan tambahan yang memperkuat karakter (contoh: kepulan uap napas dingin saat seorang prajurit berbicara).
9. **Timing & Spacing:** Ritme jeda waktu yang menentukan berat, bobot fisik, dan skala suatu objek.
10. **Exaggeration (Dosis Terukur):** Melebih-lebihkan ekspresi atau dampak fisik secara elegan tanpa menjadi kartun murahan.
11. **Solid Drawing / Three-Dimensional Space:** Konsistensi perspektif dan kedalaman spasial saat kamera bergerak mengitari objek.
12. **Appeal (Daya Tarik Karismatik):** Desain karakter dan pencahayaan memiliki karisma magnetis yang memikat penonton.

---

## 6. PARAMETER KONTROL GENERATOR (ENGINE MATRICES)

### A. Runway Gen-3 Alpha:
- Format pergerakan kamera: Gunakan keyword eksplisit `[Camera]: Continuous slow pan left`, `Dolly in with static horizon`.
- Kontrol gerak (*Motion scale*): 3 s/d 5 (untuk film naratif tenang); 6 s/d 8 (untuk adegan aksi cepat).
- Resolusi & Aspect Ratio: `--ar 16:9` (Cinema Standard), `--ar 9:16` (Vertical Reels/TikTok), `--ar 2.39:1` (Anamorphic Widescreen).

### B. Kling AI 1.5:
- Mode: **Professional Mode (1080p High Quality)**.
- Camera Controls: Set Yaw, Pitch, Roll, Zoom, dan Pan secara matematis jika menggunakan interface antarmuka slider, atau deskripsikan secara deskriptif pada prompt teks.
- Negative Prompting: `morphing, flickering, unstable anatomy, distorted hands, erratic movements, blurry, low resolution, 3d cartoon, oversaturated`.

### C. Sora & Luma Dream Machine:
- Terapkan detail kontinuitas fisika (*fluid dynamics, collision mechanics, light refraction through glass*).
