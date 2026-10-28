#!/usr/bin/env python3
"""
Desaiin-Grafis Prompt Quality & Anti-Slop Auditor
Evaluates AI Image and Video prompts against international cinematography,
optics, lighting physics, and anti-slop criteria. Outputs a score from 0-100.
"""

import sys
import re

# Ensure UTF-8 console output on Windows
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SLOP_KEYWORDS = [
    "photorealistic", "ultra realistic", "8k", "hyper realistic", "hyper-realistic",
    "unreal engine", "octane render", "trending on artstation", "masterpiece",
    "4k wallpaper", "smooth plastic skin", "wax skin", "neon purple", "neon cyan",
    "cyberpunk glow", "vivid neon"
]

OPTICS_KEYWORDS = [
    "mm", "lens", "f/", "t/", "aperture", "hasselblad", "leica", "arri", "cooke",
    "zeiss", "anamorphic", "depth of field", "bokeh", "shutter", "macro"
]

LIGHTING_KEYWORDS = [
    "rembrandt", "chiaroscuro", "volumetric", "softbox", "key light", "fill light",
    "rim light", "golden hour", "blue hour", "tungsten", "candlelight", "diffused",
    "atmospheric", "sunbeam", "falloff", "backlit"
]

MATERIAL_KEYWORDS = [
    "subsurface scattering", "pores", "texture", "grain", "linen", "wool", "cotton",
    "marble", "granite", "concrete", "patina", "imperfection", "wrinkles", "refraction"
]

CAMERA_MOTION_KEYWORDS = [
    "dolly", "truck", "pan", "tilt", "crane", "jib", "pedestal", "tracking",
    "rack focus", "orbit", "arc", "slow push-in", "pull-back"
]

def audit_prompt(prompt_text: str, is_video: bool = False) -> dict:
    text_lower = prompt_text.lower()
    total_score = 100
    deductions = []
    bonuses = []

    # 1. Check for AI Slop keywords
    found_slop = [kw for kw in SLOP_KEYWORDS if kw in text_lower]
    if found_slop:
        penalty = len(found_slop) * 8
        total_score -= penalty
        deductions.append(f"Contains AI Slop / Buzzwords ({', '.join(found_slop)}): -{penalty} pts")

    # 2. Check for physical camera & lens specifications
    found_optics = [kw for kw in OPTICS_KEYWORDS if kw in text_lower]
    if not found_optics:
        total_score -= 20
        deductions.append("Lacks specific camera optics or lens focal length: -20 pts")
    else:
        bonuses.append(f"Physical optics grounded ({', '.join(found_optics[:3])})")

    # 3. Check for physical lighting schema
    found_lighting = [kw for kw in LIGHTING_KEYWORDS if kw in text_lower]
    if not found_lighting:
        total_score -= 20
        deductions.append("Lacks physical lighting scheme or directional light: -20 pts")
    else:
        bonuses.append(f"Physical lighting defined ({', '.join(found_lighting[:3])})")

    # 4. Check for authentic material & texture realism
    found_material = [kw for kw in MATERIAL_KEYWORDS if kw in text_lower]
    if not found_material:
        total_score -= 15
        deductions.append("Lacks physical texture or material authenticity triggers: -15 pts")
    else:
        bonuses.append(f"Authentic material/texture included ({', '.join(found_material[:3])})")

    # 5. Check video specific kinematics if video
    if is_video:
        found_motion = [kw for kw in CAMERA_MOTION_KEYWORDS if kw in text_lower]
        if not found_motion:
            total_score -= 25
            deductions.append("Video prompt lacks specific camera movement vector (dolly/truck/pan/crane): -25 pts")
        else:
            bonuses.append(f"Calibrated camera motion vector ({', '.join(found_motion[:2])})")

    total_score = max(0, min(100, total_score))
    status = "MASTERPIECE (WORLD-CLASS)" if total_score >= 90 else (
        "PRODUCTION-READY" if total_score >= 85 else "REJECTED (REQUIRES REFINEMENT)"
    )

    return {
        "score": total_score,
        "status": status,
        "deductions": deductions,
        "strengths": bonuses
    }

def print_audit_report(prompt: str, is_video: bool = False):
    result = audit_prompt(prompt, is_video)
    print("=" * 70)
    print(f"DESAIIN-GRAFIS PROMPT AUDIT REPORT (Target: {'Video' if is_video else 'Image'})")
    print("=" * 70)
    print(f"PROMPT TEXT:\n\"{prompt[:140]}...\"\n")
    print(f"QUALITY SCORE: {result['score']}/100")
    print(f"AUDIT STATUS:  {result['status']}")
    print("-" * 70)
    if result["strengths"]:
        print("STRENGTHS / SOUND INVARIANTS:")
        for s in result["strengths"]:
            print(f"  [+] {s}")
    if result["deductions"]:
        print("CRITICAL DEFECTS / DEDUCTIONS:")
        for d in result["deductions"]:
            print(f"  [-] {d}")
    print("=" * 70)

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
