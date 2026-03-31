#!/usr/bin/env python3
"""
Create a simple side-by-side showcase image.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PADDING = 60
GAP = 40
BOTTOM_BAR_H = 100
FONT_PATH = "/Library/Fonts/SF-Pro-Display-Regular.otf"
TEXT_COLOR = "#000000"
BG_COLOR = (255, 255, 255)


def load_font(size: int):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except OSError:
        return ImageFont.load_default()


def fit_font(text: str, max_w: int, size_max: int = 48, size_min: int = 16):
    dummy = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    for size in range(size_max, size_min - 1, -2):
        font = load_font(size)
        bbox = dummy.textbbox((0, 0), text, font=font)
        if (bbox[2] - bbox[0]) <= max_w:
            return font
    return load_font(size_min)


def create_showcase(paths: list[str], output_path: str, footer: str | None) -> None:
    images = [Image.open(path).convert("RGBA") for path in paths]
    target_h = 800
    scaled = []
    for image in images:
        ratio = target_h / image.height
        scaled.append(image.resize((int(image.width * ratio), target_h), Image.LANCZOS))

    total_w = sum(image.width for image in scaled) + GAP * (len(scaled) - 1) + PADDING * 2
    total_h = target_h + PADDING * 2 + (BOTTOM_BAR_H if footer else 0)
    canvas = Image.new("RGB", (total_w, total_h), BG_COLOR)

    x = PADDING
    for image in scaled:
        canvas.paste(image, (x, PADDING), image)
        x += image.width + GAP

    if footer:
        draw = ImageDraw.Draw(canvas)
        font = fit_font(footer, total_w - PADDING * 2)
        draw.text((total_w // 2, PADDING + target_h + (BOTTOM_BAR_H // 2)), footer, fill=TEXT_COLOR, font=font, anchor="mm")

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out, "PNG")
    print(f"ok {out}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a showcase image")
    parser.add_argument("--screenshots", nargs="+", required=True, help="Final screenshots")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--footer", default=None, help="Optional footer text")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    create_showcase(args.screenshots, args.output, args.footer)


if __name__ == "__main__":
    main()
