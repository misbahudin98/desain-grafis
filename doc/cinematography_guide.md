# Buku Panduan Sinematografi & Pengarahan Kamera Film (cinematography_guide.md)
> **Engine:** Desain-Grafis Cinema Master Guide v1.0.0  
> **Standar Dunia:** American Society of Cinematographers (ASC), British Society of Cinematographers (BSC), Walter Murch (*In the Blink of an Eye*).  
> **Tujuan:** Panduan Komprehensif Sutradara & DoP AI untuk Menghasilkan Klip Video & Gambar Setara Sinema Layar Lebar Hollywood.

---

## 1. OPTIK KAMERA, SENSOR, & ATURAN 180 DERAJAT SHUTTER

### 1.1 Ukuran Sensor & Format Sinema
1. **Large Format Cinema (Arri Alexa LF, RED Monstro 8K, Sony Venice 2):**
   - Dimensi sensor: $\sim 36 \times 24\text{mm}$ atau lebih besar.
   - Karakteristik: Bidang pandang (*field of view*) sangat luas dengan *depth of field* tipis. Highlight roll-off sangat organik; kulit aktor tampak bercahaya alami tanpa saturasi berlebih.
2. **Super 35mm (Arri Alexa Mini, RED Komodo):**
   - Format standar sinema Hollywood selama lebih dari 80 tahun.
   - Karakteristik: Proporsi gambar tajam, kontras seimbang, lensa vintage sinema (Cooke Panchro, Zeiss Super Speed) menghasilkan *bokeh swirl* artistik.
3. **Anamorphic Format (2.39:1 Aspect Ratio):**
   - Menggunakan lensa anamorphic bersilinder optik yang mengompresi gambar secara horizontal $2\times$ pada sensor.
   - Karakteristik visual: *Oval bokeh*, garis flare horizontal biru atau emas (*anamorphic streak*), dan distorsi tepi yang memberikan ilusi sinematik khas bioskop IMAX.

---

### 1.2 Aturan Sudut Rana 180 Derajat (180° Shutter Rule)
Dalam sinema standar 24 frame per detik (24fps), rana kamera dibuka selama setengah siklus putaran:
$$\text{Shutter Speed} = \frac{1}{2 \times \text{Frame Rate}} = \frac{1}{2 \times 24} = \frac{1}{48\text{ detik}}$$
- **Efek:** Menghasilkan keburaman gerakan alami (*natural cinematic motion blur*) yang sesuai dengan respons visual otak manusia.
- **Dalam Prompt Video AI:** Selalu sertakan instruksi: `natural 180-degree shutter motion blur, 24fps cinema pace, no jitter, no frame stutter`.

---

## 2. 5 SKEMA PENCAHAYAAN SINEMATOGRAFI UTAMA

Cahaya bukan sekadar alat penerangan; cahaya adalah pahat yang membentuk emosi dan psikologi adegan.

```
                  [BACK / RIM LIGHT]
                           │
                           ▼
                       [SUBJEK]
                      ▲        ▲
                     /          \
                    /            \
                   /              \
         [KEY LIGHT]               [FILL LIGHT]
       (Cahaya Utama 100%)       (Cahaya Pengisi 30-50%)
```

### 1. Skema Tiga Titik Klasik (Three-Point Lighting):
- **Key Light (Utama):** Sumber cahaya paling kuat (biasanya bersudut $45^\circ$ dari subjek).
- **Fill Light (Pengisi):** Melembutkan bayangan pekat yang dibuat oleh Key Light (rasio daya $1:2$ hingga $1:4$).
- **Rim / Hair Light (Pemisah Belakang):** Cahaya tipis dari arah belakang kepala subjek untuk memisahkan rambut dan pundak dari latar belakang gelap.

### 2. Pencahayaan Rembrandt (Chiaroscuro Drama):
- Menempatkan Key Light tinggi di satu sisi sehingga sisi wajah yang berseberangan membentuk bayangan dengan satu segitiga cahaya kecil (*triangle of light*) tepat di bawah tulang pipi dan mata.
- Menciptakan suasana misterius, introspektif, intelektual, dan berbobot psikologis berat.

### 3. Pencahayaan Volumetrik (Volumetric God Rays & Atmospheric Haze):
- Partikel kabut halus, asap tipis, atau partikel debu suspensi di udara yang ditembus oleh berkas sinar matahari miring atau lampu sorot.
- Menghasilkan kedalaman visual tiga dimensi (*spatial atmospheric perspective*).

### 4. Pencahayaan Alami Jam Emas (Golden Hour) & Jam Biru (Blue Hour):
- **Golden Hour (30 menit setelah fajar / sebelum senja):** Suhu warna hangat $2500\text{K} - 3200\text{K}$, bayangan panjang merambat di tanah, kontras lembut.
- **Blue Hour (20 menit setelah matahari tenggelam):** Suhu warna sejuk $7000\text{K} - 9000\text{K}$, langit biru indigo dalam dipadukan dengan lampu praktis jalanan berwarna kuning jingga (*cold-warm complementary split*).

### 5. Cahaya Praktis dalam Frame (Practical Lighting):
- Menggunakan sumber cahaya yang tampak nyata di dalam adegan: lampu meja belajar, layar monitor komputer, lentera lilin, papan reklame neon toko di pinggir jalan.

---

## 3. TAKSONOMI GERAKAN KAMERA FISIK (MOTION TAXONOMY)

Gerakan kamera yang baik selalu memiliki **tujuan naratif**, bukan digerakkan secara acak:
1. **Dolly In (Push In):** Realisasi pemikiran, intimasi, ancaman yang mendekat.
2. **Dolly Out (Pull Back):** Pelepasan, kehilangan, pengungkapan skala kehancuran atau kesendirian subjek.
3. **Lateral Tracking (Truck):** Menjaga penonton berjalan berdampingan dengan karakter di dunia cerita.
4. **Pedestal / Vertical Boom:** Mengubah perspektif dari sepatu berlumpur ke tatapan mata penuh determinasi.
5. **Slow Pan / Horizon Scan:** Membaca medan pertempuran atau kota metropolitan dari kejauhan.
6. **Dutch Angle (Tilt Optik 10°-15°):** Disorientasi psikologis, dunia yang kehilangan keseimbangan moral.

---

## 4. ATURAN 180 DERAJAT SPASIAL (SPATIAL AXIS OF ACTION)

Dalam adegan percakapan antara dua karakter, tarik garis lurus khayalan antara Karakter A dan Karakter B (*the line of action*).
- **Invarian Mutlak:** Seluruh posisi kamera WAJIB berada di sisi garis yang sama ($180^\circ$ hemisphere).
- **Konsekuensi Pelanggaran (Jumping the Line):** Karakter A yang sebelumnya menatap ke arah kanan layar tiba-tiba tampak menatap ke arah yang sama di shot berikutnya, membingungkan orientasi arah mata penonton.

---

## 5. MATRIKS ASPEK RASIO GLOBAL (ASPECT RATIOS)

| Aspek Rasio | Format | Platform & Penggunaan Industri | Nilai Estetika |
| :--- | :--- | :--- | :--- |
| **$2.39:1$** | Anamorphic Widescreen | Bioskop Layar Lebar Hollywood, Film Aksi Epik, Sci-Fi | Epik, sinematik murni, dramatis |
| **$1.85:1$** | Theatrical Standard | Film Drama Teater, Komedi Amerika | Seimbang untuk dialog manusia |
| **$16:9$ ($1.77:1$)**| DCI Broadcast | TV 4K, YouTube, Dokumenter Streaming, Monitor Laptop | Standar universal modern |
| **$4:3$ ($1.33:1$)** | Academy Ratio Klasik | Film Indie Bernuansa Nostalgia, Potret Intim, Vintage 1950s | Klaustrofobik, fokus ketat pada wajah |
| **$9:16$** | Vertical Cinema | TikTok, Instagram Reels, YouTube Shorts, Iklan Mobile | Intimasi vertikal, aksi vertikal |
| **$4:5$** | Social Portrait | Feed Instagram Komersial | Memaksimalkan area layar ponsel |
