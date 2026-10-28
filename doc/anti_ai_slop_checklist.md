# Checklist Audit Kualitas Visual & Anti-AI Slop 25 Poin (anti_ai_slop_checklist.md)
> **Engine:** Desain-Grafis Quality Assurance v1.0.0  
> **Standar Audit:** Zero AI Slop Protocol, Hollywood Visual Effects Standards, WCAG 2.2 AAA.  
> **Target:** Evaluasi Setiap Hasil Generasi Gambar (Midjourney, Flux, Imagen) dan Video (Runway, Kling, Sora) Sebelum Dipublikasikan.

---

## 1. SISTEM PENILAIAN & KRITERIA KELULUSAN

Setiap karya visual (gambar statis maupun klip video) wajib diaudit menggunakan **25 Kriteria Pemeriksaan** (masing-masing bernilai 4 poin, Total: 100 poin):

- **Skor 90 – 100:** **Masterpiece (Kelas Dunia).** Siap dipublikasikan untuk kampanye komersial global, layar bioskop, atau editorial high-end.
- **Skor 85 – 89:** **Production-Ready.** Lulus standar industri dengan sedikit penyesuaian grading mikro.
- **Skor < 85:** **DITOLAK (REJECTED).** Wajib dilakukan penyempurnaan prompt (*prompt refinement*) atau regenerasi.

---

## 2. 5 KRITERIA DEAL-BREAKER (DISKUALIFIKASI OTOMATIS)
Jika sebuah karya melanggar salah satu dari 5 kriteria di bawah, karya tersebut **LANGSUNG DINYATAKAN GAGAL (SKOR 0)** tanpa memandang keindahan aspek lainnya:
1. ❌ **Kulit Lilin/Plastik Murahan (*Plastic/Wax Skin*):** Wajah manusia tampak seperti manekin toko atau boneka lilin tanpa pori-pori dan kerutan alami.
2. ❌ **Anomali Anatomi Tangan:** Jari tangan berjumlah selain 5, kuku melebur, atau sendi melengkung tidak wajar.
3. ❌ **Gradasi Neon Ungu-Pink Toksik AI:** Latar belakang diwarnai gradasi magenta-cyan murah tanpa ada sumber cahaya lampu fisik yang jelas.
4. ❌ **Teks Mengambang Liar (*Nonsense Gibberish Text*):** Terdapat huruf-huruf aneh fiktif yang melayang di udara atau tertulis di pakaian tanpa makna.
5. ❌ **Distorsi Bentuk Temporal Ekstrem (*Severe Video Morphing*):** Pada video, objek atau tubuh karakter melebur atau berubah bentuk secara gaib saat bergerak.

---

## 3. LEMBAR AUDIT LENGKAP 25 POIN PEMERIKSAAN

### KATEGORI A: AKURASI ANATOMI & BIOLOGI MANUSIA (20 POIN)
- [ ] **A1. Struktur Tangan & Jari (4 Poin):** Tepat 5 jari di setiap tangan dengan panjang falang proporsional dan artikulasi sendi yang anatomis.
- [ ] **A2. Bola Mata & Iris Catchlight (4 Poin):** Refleksi titik cahaya (*catchlight*) di kornea mata kiri dan kanan konsisten secara optik terhadap posisi sumber cahaya utama.
- [ ] **A3. Tekstur Pori Kulit & Subsurface Scattering (4 Poin):** Kulit menunjukkan permeabilitas biologis asli (cahaya menembus lembut di daun telinga dan cuping hidung), memiliki pori-pori mikro dan garis ekspresi alami.
- [ ] **A4. Gigi & Bibir Natural (4 Poin):** Struktur gigi tersusun dalam satu lengkung rahang tunggal alami, gusi berwarna merah muda sehat, tidak ada baris gigi ganda.
- [ ] **A5. Postur Gravitasi Tubuh (4 Poin):** Berat badan subjek bertumpu secara alami pada telapak kaki atau kursi; pakaian meregang dan berlipat sesuai tarikan gravitasi bumi.

---

### KATEGORI B: FISIKA KAMERA & KETEPATAN OPTIK (20 POIN)
- [ ] **B1. Kedalaman Bidang Rasional (Depth of Field) (4 Poin):** Keburaman latar belakang (*bokeh*) konsisten dengan panjang fokus lensa dan bukaan diafragma yang didefinisikan ($f/1.4$ vs $f/8$).
- [ ] **B2. Konsistensi Titik Fokus (Focal Plane) (4 Poin):** Bidang fokus berada tajam pada subjek utama (biasanya pupil mata manusia atau detail produk), bukan meleset ke rambut atau latar belakang.
- [ ] **B3. Aberasi Kromatik & Distorsi Lensa Terkontrol (4 Poin):** Tidak ada bias warna ungu/hijau liar di tepi objek kontras (*fringe-free*), distorsi tepi sesuai dengan jenis lensa (misal: ultra-wide vs telephoto).
- [ ] **B4. Motion Blur Sinematik 180° (Video) (4 Poin):** Keburaman objek yang bergerak di video halus dan terdistribusi merata sesuai standar shutter film 24fps (tidak ada stutter kaku atau frame robek).
- [ ] **B5. Parallaks Spasial Tiga Dimensi (4 Poin):** Saat kamera bergerak, latar depan bergerak lebih cepat daripada latar belakang, menciptakan ilusi volume ruang 3D yang meyakinkan.

---

### KATEGORI C: INTEGRITAS PENCAHAYAAN & BAYANGAN (20 POIN)
- [ ] **C1. Arah Sumber Cahaya Koheren (4 Poin):** Semua bayangan objek di lantai atau dinding jatuh ke arah yang sama sesuai dengan posisi Key Light atau matahari.
- [ ] **C2. Transisi Bayangan Alami (Penumbra Falloff) (4 Poin):** Bayangan dekat objek bertepi tajam (*umbra*), dan berangsur melembut di ujungnya (*penumbra*), tidak ada bayangan hitam pekat mengambang yang terpotong garis lurus.
- [ ] **C3. Pantulan Spekular & Refleksi Fisik (4 Poin):** Pantulan cahaya pada kaca, logam, dan genangan air menampilkan bayangan lingkungan sekitar secara matematis akurat.
- [ ] **C4. Highlight Roll-Off Lembut (4 Poin):** Area paling terang tidak meledak menjadi putih solid mati (*clipping*); transisi ke putih berlangsung lembut menyerupai film kimia Kodak/Arri.
- [ ] **C5. Suhu Warna Konsisten (Kelvin Balance) (4 Poin):** Suhu warna cahaya alami (matahari/langit) dan cahaya buatan (lampu pijar/neon) harmonis tanpa benturan spektrum acak.

---

### KATEGORI D: KEJUJURAN MATERIAL & TEKSTUR REALISTIS (20 POIN)
- [ ] **D1. Tekstur Kain & Pakaian (4 Poin):** Serat kain (katun, linen, wol, sutra) terlihat detail dan berpori, tidak tampak seperti lembaran plastik licin.
- [ ] **D2. Logam & Refleksi Permukaan (4 Poin):** Logam memiliki pantulan yang tepat sesuai tipenya: pantulan tegas untuk krom/emas poles, atau pantulan teredam lembut untuk titanium/baja sikat (*brushed finish*).
- [ ] **D3. Pembiasan Kaca & Air (Refraction Index) (4 Poin):** Objek di dalam atau di belakang gelas air mengalami distorsi pembiasan optik yang akurat (hukum Snellius).
- [ ] **D4. Partikel Lingkungan & Atmosfer (4 Poin):** Udara memiliki kedalaman atmosferik (kabut tipis, butir debu melayang dalam sinar cahaya, rintik embun).
- [ ] **D5. Imperfeksi Mikro yang Memanusiakan (4 Poin):** Benda-benda tidak tampak seperti steril dari pabrik 3D; ada sedikit keausan mikro, butiran film (*organic grain*), atau patina alami.

---

### KATEGORI E: KOMPOSISI, TIPOGRAFI, & HIERARKI NARATIF (20 POIN)
- [ ] **E1. Ruang Bernapas Lapang (Spacious Negative Space) (4 Poin):** Frame tidak penuh sesak (*no horror vacui*); ada ruang kosong yang memberi kenyamanan mata penonton.
- [ ] **E2. Penerapan Garis Sepertiga / Golden Spiral (4 Poin):** Titik fokus terkuat jatuh tepat pada perpotongan garis sepertiga (*Rule of Thirds*) atau pusaran rasio emas.
- [ ] **E3. Keterbacaan Tipografi & Kontras WCAG (4 Poin):** Seluruh elemen teks terbaca seketika dengan kontras tinggi ($\ge 7:1$), tidak tenggelam dalam latar belakang yang ramai.
- [ ] **E4. Kesesuaian Bounded Context & Identitas Brand (4 Poin):** Suasana visual selaras dengan emosi merek (misal: tenang dan mewah untuk perbankan, berani dan energetik untuk olahraga).
- [ ] **E5. Pacing Gerak Video & Kontinuitas 180° (Video) (4 Poin):** Gerakan kamera tenang, stabil, dan tidak melanggar garis aksi spasial saat terjadi perpindahan shot.

---

## 4. FORMULIR REKAPITULASI AUDIT HASIL KERJA

```
HASIL AUDIT KUALITAS DESAIN VISUAL:
- Nama Aset / Prompt: _____________________________
- Kategori A (Anatomi & Biologi):      ____ / 20
- Kategori B (Optik & Kamera):         ____ / 20
- Kategori C (Pencahayaan & Bayangan): ____ / 20
- Kategori D (Material & Tekstur):     ____ / 20
- Kategori E (Komposisi & Hierarki):   ____ / 20
- TOTAL SKOR KUALITAS:                 ____ / 100
- STATUS KELULUSAN:                    [ ] LULUS (>=85)   [ ] REJECT (<85)
- Catatan Penyempurnaan:               _____________________________
```
