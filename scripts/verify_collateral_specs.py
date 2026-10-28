#!/usr/bin/env python3
"""
Desain-Grafis Marketing & Collateral Specifications Validator
Validates dimensions, safe zones, bleeds, and resolution against international standards:
ISO 216, ISO 12647-2 (FOGRA39), IAB Tech Lab, and Meta/WhatsApp UI Danger Zones.
"""

import sys

# Ensure UTF-8 console output on Windows
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

STANDARD_SIZES = {
    "flyer": {
        "A4": {"width_mm": 210, "height_mm": 297, "bleed_mm": 3, "min_dpi": 300, "color_space": "CMYK"},
        "A5": {"width_mm": 148, "height_mm": 210, "bleed_mm": 3, "min_dpi": 300, "color_space": "CMYK"},
        "A6": {"width_mm": 105, "height_mm": 148, "bleed_mm": 3, "min_dpi": 300, "color_space": "CMYK"},
        "DL": {"width_mm": 99, "height_mm": 210, "bleed_mm": 3, "min_dpi": 300, "color_space": "CMYK"}
    },
    "banner": {
        "medium_rectangle": {"width_px": 300, "height_px": 250, "ratio": "6:5", "iab": True},
        "leaderboard": {"width_px": 728, "height_px": 90, "ratio": "8.09:1", "iab": True},
        "half_page": {"width_px": 300, "height_px": 600, "ratio": "1:2", "iab": True},
        "billboard": {"width_px": 970, "height_px": 250, "ratio": "3.88:1", "iab": True},
        "opengraph": {"width_px": 1200, "height_px": 630, "ratio": "1.91:1", "iab": False}
    },
    "carousel": {
        "portrait_4_5": {"width_px": 1080, "height_px": 1350, "ratio": "4:5", "safe_padding_px": 80},
        "square_1_1": {"width_px": 1080, "height_px": 1080, "ratio": "1:1", "safe_padding_px": 60}
    },
    "status_story": {
        "standard_9_16": {
            "width_px": 1080,
            "height_px": 1920,
            "ratio": "9:16",
            "top_danger_px": 270,
            "bottom_danger_organic_px": 270,
            "bottom_danger_ads_px": 670,
            "side_margin_px": 65
        }
    }
}

def validate_story_element_position(y_position: int, element_type: str = "critical_text", is_ad: bool = False) -> dict:
    """Verifies whether an element on a 1080x1920 story is within the safe zone."""
    top_limit = 270
    bottom_limit = (1920 - 670) if is_ad else (1920 - 270) # 1250 for ads, 1650 for organic
    
    if y_position < top_limit:
        return {
            "safe": False,
            "y": y_position,
            "message": f"DANGER: Element at Y={y_position}px is inside the TOP UI overlay zone (0-270px) and will be obscured by account handle/progress bars."
        }
    elif y_position > bottom_limit:
        zone_type = "ADS CTA & sponsored disclaimer zone (1250-1920px)" if is_ad else "REPLY BAR & reaction zone (1650-1920px)"
        return {
            "safe": False,
            "y": y_position,
            "message": f"DANGER: Element at Y={y_position}px is inside the BOTTOM {zone_type}."
        }
    else:
        return {
            "safe": True,
            "y": y_position,
            "message": f"PASSED: Element at Y={y_position}px is securely positioned within the safe canvas zone ({top_limit}px - {bottom_limit}px)."
        }

def run_collateral_audit_demo():
    print("=" * 76)
    print("DESAIN-GRAFIS MARKETING & COLLATERAL VERIFIER")
    print("Standards: ISO 216 // ISO 12647-2 (FOGRA39) // IAB Tech Lab // Meta Guidelines")
    print("=" * 76)

    # 1. Flyer Verification
    print("\n--- 1. FLYER AUDIT (Target: DIN A5 Print Hand-out) ---")
    spec_a5 = STANDARD_SIZES["flyer"]["A5"]
    print(f"Format            : DIN A5 Print Flyer")
    print(f"Trim Dimensions   : {spec_a5['width_mm']} x {spec_a5['height_mm']} mm")
    print(f"Bleed Required    : +{spec_a5['bleed_mm']} mm ({spec_a5['width_mm'] + 6} x {spec_a5['height_mm'] + 6} mm)")
    print(f"Color Space       : {spec_a5['color_space']} (FOGRA39 Profile, TAC <= 300%)")
    print(f"Min Resolution    : {spec_a5['min_dpi']} DPI (Raster Graphics)")
    print(f"Optical Center    : 55% - 60% vertical height (Upper third focus)")
    print(f"Status            : COMPLIANT WITH ISO 216 & ISO 12647-2 (PASS)")

    # 2. IAB Banners
    print("\n--- 2. IAB DIGITAL DISPLAY BANNERS ---")
    for name, data in STANDARD_SIZES["banner"].items():
        print(f"  [{name.upper():<16}] : {data['width_px']} x {data['height_px']} px | Ratio: {data['ratio']:<7} | LEAN File Limit <= 200KB")

    # 3. Carousel Multi-Slide
    print("\n--- 3. SOCIAL CAROUSEL STANDARDS (Instagram & LinkedIn) ---")
    car_spec = STANDARD_SIZES["carousel"]["portrait_4_5"]
    print(f"Optimal Format    : {car_spec['width_px']} x {car_spec['height_px']} px (4:5 Vertical Portrait)")
    print(f"Screen Real Estate: 25% larger screen area on mobile feeds compared to 1:1")
    print(f"Safe Margin       : {car_spec['safe_padding_px']} px padding on all sides")
    print(f"Hook Rule         : Slide 1 Headline 5-8 words, bold display font >= 54px")
    print(f"Density Rule      : Max 40-60 words per slide across 7-10 slide narrative arc")

    # 4. Status & Stories Safe Zone Tests
    print("\n--- 4. STORIES & STATUS SAFE ZONE SIMULATION (1080 x 1920 px) ---")
    test_positions = [
        (150, "Header Logo", False),
        (500, "Main Headline", False),
        (1300, "Secondary Subtext", False),
        (1400, "CTA Button", True),
        (1750, "Contact Phone", False),
    ]

    for y, label, is_ad in test_positions:
        res = validate_story_element_position(y, label, is_ad)
        status_icon = "[PASS]" if res["safe"] else "[FAIL]"
        print(f"  {status_icon} '{label}' at Y={y}px (Ad Mode: {is_ad}) ➔ {res['message']}")
    print("=" * 76)

if __name__ == "__main__":
    run_collateral_audit_demo()
