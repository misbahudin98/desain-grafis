#!/usr/bin/env python3
"""
Desain-Grafis Color Palette & WCAG 2.2 AAA Contrast Calculator
Computes Relative Luminance and verifies mathematical contrast ratios
according to W3C WCAG 2.2 AAA standards (>= 7:1 for normal text, >= 4.5:1 for large text).
"""

import sys

# Ensure UTF-8 console output on Windows
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    hex_clean = hex_str.lstrip('#')
    if len(hex_clean) == 3:
        hex_clean = ''.join([c*2 for c in hex_clean])
    return (int(hex_clean[0:2], 16), int(hex_clean[2:4], 16), int(hex_clean[4:6], 16))

def get_relative_luminance(rgb: tuple[int, int, int]) -> float:
    """Calculates relative luminance according to sRGB formula."""
    channels = []
    for c in rgb:
        sc = c / 255.0
        if sc <= 0.03928:
            linear = sc / 12.92
        else:
            linear = ((sc + 0.055) / 1.055) ** 2.4
        channels.append(linear)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]

def calculate_contrast_ratio(hex1: str, hex2: str) -> float:
    """Calculates contrast ratio between two hex colors (1:1 to 21:1)."""
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    l1 = get_relative_luminance(rgb1)
    l2 = get_relative_luminance(rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def verify_wcag(hex_fg: str, hex_bg: str) -> dict:
    ratio = calculate_contrast_ratio(hex_fg, hex_bg)
    pass_aa_normal = ratio >= 4.5
    pass_aaa_normal = ratio >= 7.0
    pass_aaa_large = ratio >= 4.5
    
    return {
        "ratio": round(ratio, 2),
        "pass_aa": pass_aa_normal,
        "pass_aaa": pass_aaa_normal,
        "pass_aaa_large": pass_aaa_large,
        "grade": "AAA MASTER" if pass_aaa_normal else ("AA PASS" if pass_aa_normal else "FAIL (REJECT)")
    }

def print_palette_report(name: str, colors: dict):
    print("=" * 70)
    print(f"PALETTE: {name.upper()}")
    print("=" * 70)
    for role, hex_val in colors.items():
        rgb = hex_to_rgb(hex_val)
        print(f"  {role:20}: {hex_val} (sRGB: {rgb[0]}, {rgb[1]}, {rgb[2]})")
    
    print("-" * 70)
    print("ACCESSIBILITY & WCAG 2.2 CONTRAST AUDIT:")
    bg = colors.get("background", colors.get("base_60", colors.get("base_60 (Dominant)", "#0B0F19")))
    text = colors.get("text_primary", colors.get("structure_30", "#F8FAFC"))
    accent = colors.get("accent_10", colors.get("accent_10 (Emerald)", colors.get("accent_10 (Cobalt)", "#10B981")))
    
    audit_text = verify_wcag(text, bg)
    print(f"  [Text on Background] Ratio: {audit_text['ratio']}:1 | Status: {audit_text['grade']}")
    
    audit_accent = verify_wcag(accent, bg)
    print(f"  [Accent on Background] Ratio: {audit_accent['ratio']}:1 | Status: {audit_accent['grade']}")
    print("=" * 70)

if __name__ == "__main__":
    palette_obsidian = {
        "base_60 (Dominant)": "#0B0F19",
        "structure_30 (Card)": "#1E293B",
        "text_primary": "#F8FAFC",
        "accent_10 (Emerald)": "#10B981",
        "subtle_border_1px": "#334155"
    }
    
    palette_nordic = {
        "base_60 (Dominant)": "#F8FAFC",
        "structure_30 (Card)": "#FFFFFF",
        "text_primary": "#0F172A",
        "accent_10 (Cobalt)": "#0284C7",
        "subtle_border_1px": "#E2E8F0"
    }

    print("\n--- PALETTE 1: QUIET LUXURY OBSIDIAN ---")
    print_palette_report("Heritage Obsidian", palette_obsidian)

    print("\n--- PALETTE 2: NORDIC MINIMALISM ---")
    print_palette_report("Nordic Daylight", palette_nordic)
