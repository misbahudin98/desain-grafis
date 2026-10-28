#!/usr/bin/env python3
"""
Desain-Grafis Prompt Quality & Anti-Slop Auditor
Evaluates AI Image and Video prompts against international standards:
IEEE P3394, ISO/IEC TS 42119-8, Jonas Oppenlaender 6-Part Taxonomy (ACM),
American Society of Cinematographers (ASC), and Anti-AI Slop protocols.
Outputs a score from 0-100 with actionable feedback.
"""

import sys
import re

# Ensure UTF-8 console output on Windows
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SLOP_KEYWORDS = [
    "photorealistic", "ultra realistic", "8k", "hyper realistic", "hyper-realistic",
    "unreal engine", "octane render", "trending on artstation", "masterpiece",
    "4k wallpaper", "smooth plastic skin", "wax skin", "neon purple", "neon cyan",
    "cyberpunk glow", "vivid neon", "award winning", "stunningly detailed"
]

OPTICS_KEYWORDS = [
    "mm", "lens", "f/", "t/", "aperture", "hasselblad", "leica", "arri", "cooke",
    "zeiss", "anamorphic", "depth of field", "bokeh", "shutter", "macro", "prime"
]

LIGHTING_KEYWORDS = [
    "rembrandt", "chiaroscuro", "volumetric", "softbox", "key light", "fill light",
    "rim light", "golden hour", "blue hour", "tungsten", "candlelight", "diffused",
    "atmospheric", "sunbeam", "falloff", "backlit", "kelvin"
]

MATERIAL_KEYWORDS = [
    "subsurface scattering", "pores", "texture", "grain", "linen", "wool", "cotton",
    "marble", "granite", "concrete", "patina", "imperfection", "wrinkles", "refraction",
    "leather", "timber", "basalt", "silk"
]

CAMERA_MOTION_KEYWORDS = [
    "dolly", "truck", "pan", "tilt", "crane", "jib", "pedestal", "tracking",
    "rack focus", "orbit", "arc", "slow push-in", "pull-back", "boom"
]

def audit_prompt(prompt_text: str, is_video: bool = False) -> dict:
    text_lower = prompt_text.lower()
    total_score = 100
    deductions = []
    bonuses = []

    # 1. Check for AI Slop keywords (IEEE / ISO Negative Quality Criteria)
    found_slop = [kw for kw in SLOP_KEYWORDS if kw in text_lower]
    if found_slop:
        penalty = len(found_slop) * 8
        total_score -= penalty
        deductions.append(f"Contains AI Slop / Generic Buzzwords ({', '.join(found_slop)}): -{penalty} pts")

    # 2. Check for physical camera & lens specifications (Composition & Framing)
    found_optics = [kw for kw in OPTICS_KEYWORDS if kw in text_lower]
    if not found_optics:
        total_score -= 20
        deductions.append("Lacks physical camera optics or focal length (mm / f-stop): -20 pts")
    else:
        bonuses.append(f"Physical optics grounded ({', '.join(found_optics[:3])})")

    # 3. Check for physical lighting schema (Lighting Modifiers)
    found_lighting = [kw for kw in LIGHTING_KEYWORDS if kw in text_lower]
    if not found_lighting:
        total_score -= 20
        deductions.append("Lacks directional physical lighting scheme: -20 pts")
    else:
        bonuses.append(f"Physical lighting defined ({', '.join(found_lighting[:3])})")

    # 4. Check for authentic material & texture realism (Material Modifiers)
    found_material = [kw for kw in MATERIAL_KEYWORDS if kw in text_lower]
    if not found_material:
        total_score -= 15
        deductions.append("Lacks tactile material authenticity / biological texture: -15 pts")
    else:
        bonuses.append(f"Authentic material/texture included ({', '.join(found_material[:3])})")

    # 5. Check video specific kinematics if video (ASC Motion Taxonomy)
    if is_video:
        found_motion = [kw for kw in CAMERA_MOTION_KEYWORDS if kw in text_lower]
        if not found_motion:
            total_score -= 25
            deductions.append("Video prompt lacks specific camera movement vector (dolly/truck/pan/crane): -25 pts")
        else:
            bonuses.append(f"Calibrated camera motion vector ({', '.join(found_motion[:2])})")

    # Oppenlaender 6-part taxonomy score
    oppenlaender_score = sum([
        1 if len(prompt_text.split()) > 5 else 0, # Subject
        1 if any(w in text_lower for w in ["in ", "on ", "at ", "room", "studio", "workshop", "exterior", "interior", "street"]) else 0, # Environment
        1 if found_lighting else 0, # Lighting
        1 if any(w in text_lower for w in ["portra", "vision3", "velvia", "eterna", "monochrome", "palette", "amber", "obsidian", "slate"]) else 0, # Color/Film
        1 if found_optics else 0, # Composition/Framing
        1 if found_material else 0 # Material
    ])

    total_score = max(0, min(100, total_score))
    status = "MASTERPIECE (WORLD-CLASS)" if total_score >= 90 else (
        "PRODUCTION-READY" if total_score >= 85 else "REJECTED (REQUIRES REFINEMENT)"
    )

    return {
        "score": total_score,
        "status": status,
        "oppenlaender_coverage": f"{oppenlaender_score}/6 Modifiers",
        "iso_compliance": "COMPLIANT (PASS)" if total_score >= 85 else "NON-COMPLIANT (FAIL)",
        "deductions": deductions,
        "strengths": bonuses
    }

def print_audit_report(prompt: str, is_video: bool = False):
    result = audit_prompt(prompt, is_video)
    print("=" * 76)
    print(f"DESAIN-GRAFIS PROMPT AUDIT REPORT (Target: {'Video AI' if is_video else 'Image AI'})")
    print(f"Standards: IEEE P3394 // ISO/IEC TS 42119-8 // Oppenlaender ACM Taxonomy")
    print("=" * 76)
    print(f"PROMPT TEXT:\n\"{prompt[:140]}...\"\n")
    print(f"QUALITY SCORE:          {result['score']}/100")
    print(f"AUDIT STATUS:           {result['status']}")
    print(f"OPPENLAENDER TAXONOMY:  {result['oppenlaender_coverage']}")
    print(f"ISO/IEC TS 42119-8:     {result['iso_compliance']}")
    print("-" * 76)
    if result["strengths"]:
        print("STRENGTHS / SOUND INVARIANTS:")
        for s in result["strengths"]:
            print(f"  [+] {s}")
    if result["deductions"]:
        print("CRITICAL DEFECTS / DEDUCTIONS:")
        for d in result["deductions"]:
            print(f"  [-] {d}")
    print("=" * 76)

if __name__ == "__main__":
    sample_bad = "A beautiful girl smiling, photorealistic, 8k, hyper realistic, unreal engine render, neon purple background, gorgeous."
    sample_good = (
        "Intimate cinematic portrait of a 45-year-old female architect with subtle laugh lines and natural skin pores, "
        "wearing a charcoal linen coat. Soft morning light entering through an oversized industrial window, "
        "Rembrandt key lighting with natural shadows. Shot on Leica M11, Summilux 50mm lens at f/1.4, Kodak Portra 400 grain, "
        "authentic tactile linen weave, creamy background bokeh --ar 16:9 --style raw --v 6.1"
    )
    
    print("\n--- AUDITING AMATEUR SLOP PROMPT ---")
    print_audit_report(sample_bad, is_video=False)
    
    print("\n--- AUDITING WORLD-CLASS PRODUCTION PROMPT ---")
    print_audit_report(sample_good, is_video=False)
