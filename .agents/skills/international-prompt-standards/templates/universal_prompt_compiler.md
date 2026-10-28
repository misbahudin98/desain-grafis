# Template Master: Universal Prompt Compiler (universal_prompt_compiler.md)
> **Engine:** Desaiin-Grafis International Prompt Compiler v1.0.0  
> **Kompatibilitas:** Anthropic XML, OpenAI Delimited, Midjourney v6.1, FLUX.1, Runway Gen-3, Kling 1.5.

---

## 1. TEMPLATE A: PROMPT TEXT-TO-TEXT / MULTIMODAL AGENT (ANTHROPIC XML)

Gunakan struktur ini untuk menginstruksikan model bahasa atau agen otonom:

```xml
<prompt_architecture version="1.0" standard="IEEE-P3394">
  <system_context>
    Anda adalah seorang Director of Photography dan Master Creative Director kelas dunia yang menerapkan standar Bauhaus, Dieter Rams, dan American Society of Cinematographers (ASC).
  </system_context>

  <task_objective>
    Rancang prompt gambar fotorealistik dan naskah visual untuk peluncuran arloji mewah Swiss.
  </task_objective>

  <strict_invariants>
    <rule id="NO_SLOP">Dilarang menggunakan kata 'photorealistic', '8k', 'unreal engine', atau 'masterpiece'.</rule>
    <rule id="PHYSICS_GROUNDED">Wajib menyebutkan sensor medium format Hasselblad dan lensa macro spesifik.</rule>
    <rule id="LIGHTING">Wajib menggunakan pencahayaan studio komersial Chiaroscuro.</rule>
  </strict_invariants>

  <output_format>
    Sajikan dalam format:
    1. Analisis Konseptual & Bounded Context
    2. Prompt Master Midjourney v6.1 (--style raw)
    3. Prompt Master FLUX.1
    4. Evaluasi Kualitas berdasarkan 25 Poin Audit
  </output_format>
</prompt_architecture>
```

---

## 2. TEMPLATE B: PROMPT TEXT-TO-IMAGE (7-SEGMENT PHYSICAL COMPILER)

Gunakan struktur ini untuk Midjourney v6.1, FLUX.1, atau Imagen 3:

```text
[1. SUBJECT & ACTION]:
A thoughtful 50-year-old Scandinavian master cabinetmaker with fine sawdust in his beard, carefully inspecting the mortise-and-tenon joint of a solid walnut chair with a brass depth gauge.

[2. ENVIRONMENT & SETTING]:
Set inside a sun-drenched minimalist timber workshop overlooking a misty pine forest in Norway. In the background, hand planes and chisels hang in precise alignment on a pegboard wall.

[3. CAMERA OPTICS & SENSOR]:
Shot on Leica M11 with Summilux-M 50mm f/1.4 lens at f/2.0. Sharp focus locked on the craftsman's focused iris and the wood joint.

[4. LIGHTING PHYSICS]:
Soft directional morning daylight streaming through oversized north-facing windows, casting natural gentle penumbra shadows, paired with warm tungsten ambient glow from a task light.

[5. COLOR PALETTE & FILM STOCK]:
Kodak Portra 400 film grain texture, natural warm skin tones with authentic subsurface scattering, rich walnut wood browns, and cool forest green exterior accents.

[6. MATERIAL & TEXTURE REALISM]:
Visible wood grain pores, tactile rough denim apron weave, authentic micro-wrinkles, zero wax/plastic skin smoothing.

[7. ENGINE PARAMETER FLAGS]:
--ar 16:9 --style raw --v 6.1 --s 100
```

---

## 3. TEMPLATE C: PROMPT TEXT-TO-VIDEO (RUNWAY GEN-3 / KLING 1.5 DIRECTOR FORMAT)

Gunakan struktur ini untuk generator video:

```text
[Camera]: Slow, buttery-smooth low-angle tracking dolly forward, moving at 0.5 meters per second along the workshop floor, maintaining eye-level perspective with the artisan.

[Scene Description]: The master cabinetmaker slowly blows away a thin veil of wood dust from the polished walnut surface, the tiny wood motes swirling realistically into the morning lightbeam. He runs his thumb smoothly across the seamless joint with a subtle satisfied smile.

[Lighting & Atmosphere]: High-contrast morning sunbeams cutting through floating dust particles in the air, creating authentic atmospheric perspective and natural volumetric haze.

[Optics & Cinema Pacing]: Arri Alexa Mini LF, Panavision Ultra Vista anamorphic 50mm lens at T1.8, authentic 180-degree shutter motion blur, Kodak Vision3 500T grain, 24fps cinema pace, zero morphing, zero flickering.
```
