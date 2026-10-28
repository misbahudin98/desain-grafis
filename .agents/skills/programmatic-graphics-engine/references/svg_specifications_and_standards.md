# Standar Spesifikasi Vektor SVG & Grafik Terprogram (svg_specifications_and_standards.md)
> **Engine:** Desain-Grafis Programmatic Database v1.0.0  
> **Standar:** W3C SVG 1.1 / 2.0 Recommendations, Josef Müller-Brockmann Modular Grid Systems, WCAG 2.2 AAA Contrast Requirements.

---

## 1. HIERARKI & STRUKTUR ELEMEN SVG MANDIRI (SELF-CONTAINED)

Setiap berkas SVG yang dihasilkan oleh `programmatic-graphics-engine` wajib bersifat mandiri (*standalone* / *self-contained*) tanpa ketergantungan aset eksternal:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="100%" height="100%">
  <defs>
    <!-- 1. Skema Gradien & Filter Internal -->
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#1E293B" />
    </linearGradient>

    <!-- 2. Typography Stylesheet Internal -->
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&amp;family=JetBrains+Mono:wght@400;500;700&amp;display=swap');
      .title { font-family: 'Inter', system-ui, -apple-system, sans-serif; font-weight: 800; fill: #F8FAFC; }
      .subtitle { font-family: 'Inter', system-ui, -apple-system, sans-serif; font-weight: 400; fill: #94A3B8; }
      .badge-text { font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13px; fill: #10B981; }
      .grid-line { stroke: #334155; stroke-width: 1; stroke-opacity: 0.35; }
    </style>
  </defs>

  <!-- 3. Aksesibilitas (Screen Readers) -->
  <title>Desain Grafis Master Template</title>
  <desc>Swiss Modular Vector Graphics with WCAG AAA Accessibility Compliance.</desc>

  <!-- 4. Latar Belakang & Kisi Modular -->
  <rect width="1200" height="630" fill="url(#bgGradient)" />

  <!-- 5. Konten Geometris & Tipografi -->
</svg>
```

---

## 2. KETENTUAN KISI MODULAR SWISS & RASIO ASPEK KANONIKAL

| Aspek Rasio | Dimensi Rekomendasi | Modul Grid Primer | Penggunaan Standar |
| :--- | :--- | :--- | :--- |
| **1.91:1** | $1200 \times 630\text{px}$ | Kisi 12 Kolom ($80\text{px}$ pitch + $24\text{px}$ gutter) | OpenGraph Card (Twitter/X Large, LinkedIn, Meta, WhatsApp) |
| **1:1** | $1080 \times 1080\text{px}$ | Kisi 8 Kolom ($100\text{px}$ pitch + $32\text{px}$ gutter) | Instagram Feed, Square Product Catalog, CD Cover Mockup |
| **9:16** | $1080 \times 1920\text{px}$ | Kisi Vertikal ($80\text{px}$ baseline) | Instagram Stories, TikTok Frame Overlay, Mobile Splash Screen |
| **16:9** | $1920 \times 1080\text{px}$ | Kisi 16 Kolom ($96\text{px}$ pitch + $24\text{px}$ gutter) | YouTube Thumbnail, Keynote / Slide Deck Presentation Header |

---

## 3. CHECKLIST INTEGRITAS VEKTOR (SVG PRODUCTION RULES)

1. **ViewBox Terdefinisi Eksplisit:** Dilarang membuat tag `<svg>` tanpa atribut `viewBox`.
2. **Path Precision:** Batasi koordinat desimal hingga maksimum 2 digit desimal untuk efisiensi ukuran berkas.
3. **WCAG 2.2 AAA Contrast:** Teks putih `#F8FAFC` di atas kanvas gelap `#0B0F19` menghasilkan kontras $18.3:1$ (Melampaui batas AAA $7.0:1$).
4. **Font Fallback:** Wajib menyertakan *fallback font* sistemik (`system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`) agar teks tidak patah jika web font gagal termuat.
5. **No Raster Embedding:** Dilarang menyematkan data citra raster base64 (`data:image/png;base64,...`) kecuali disetujui secara eksplisit, demi mempertahankan sifat murni vektor.
