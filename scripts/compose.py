#!/usr/bin/env python3
"""
Compose one App Store screenshot scaffold.
"""

import argparse
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageChops

CANVAS_W = 1290
CANVAS_H = 2796
DEVICE_W = 1030
BEZEL = 15
SCREEN_W = DEVICE_W - 2 * BEZEL
SCREEN_CORNER_R = 62
DEVICE_Y = 720
VERB_SIZE_MAX = 256
VERB_SIZE_MIN = 150
DESC_SIZE = 124
VERB_DESC_GAP = 20
DESC_LINE_GAP = 24
MAX_TEXT_W = int(CANVAS_W * 0.92)
MAX_VERB_W = int(CANVAS_W * 0.92)
DEFAULT_BOLD_FONT = "/Library/Fonts/SF-Pro-Display-Black.otf"
DEFAULT_FRAME_PATH = Path(__file__).resolve().parent.parent / "assets" / "device_frame.png"


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def word_wrap(draw: ImageDraw.ImageDraw, text: str, font, max_w: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        probe = f"{current} {word}".strip()
        if draw.textlength(probe, font=font) <= max_w:
            current = probe
            continue
        if current:
            lines.append(current)
        current = word
    if current:
        lines.append(current)
    return lines


def fit_font(text: str, max_w: int, size_max: int, size_min: int, font_path: str):
    dummy = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    for size in range(size_max, size_min - 1, -4):
        font = load_font(font_path, size)
        bbox = dummy.textbbox((0, 0), text, font=font)
        if (bbox[2] - bbox[0]) <= max_w:
            return font
    return load_font(font_path, size_min)


def draw_centered(draw: ImageDraw.ImageDraw, y: int, text: str, font, fill: str, max_w: int | None = None) -> int:
    lines = word_wrap(draw, text, font, max_w) if max_w else [text]
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        height = bbox[3] - bbox[1]
        draw.text((CANVAS_W // 2, y - bbox[1]), line, fill=fill, font=font, anchor="mt")
        y += height + DESC_LINE_GAP
    return y


def resize_screenshot(shot: Image.Image) -> Image.Image:
    scale = SCREEN_W / shot.width
    height = int(shot.height * scale)
    return shot.resize((SCREEN_W, height), Image.LANCZOS)


def build_screen_layer(canvas_size: tuple[int, int], shot: Image.Image, screen_x: int, screen_y: int) -> Image.Image:
    screen_h = CANVAS_H - screen_y + 500
    mask = Image.new("L", canvas_size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [screen_x, screen_y, screen_x + SCREEN_W, screen_y + screen_h],
        radius=SCREEN_CORNER_R,
        fill=255,
    )

    layer = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(
        [screen_x, screen_y, screen_x + SCREEN_W, screen_y + screen_h],
        radius=SCREEN_CORNER_R,
        fill=(0, 0, 0, 255),
    )
    layer.paste(shot, (screen_x, screen_y))
    layer.putalpha(mask)
    return layer


def compose(bg_hex: str, verb: str, desc: str, screenshot_path: str, output_path: str, font_path: str, frame_path: str, text_color: str) -> None:
    canvas = Image.new("RGBA", (CANVAS_W, CANVAS_H), (*hex_to_rgb(bg_hex), 255))
    draw = ImageDraw.Draw(canvas)

    verb_font = fit_font(verb.upper(), MAX_VERB_W, VERB_SIZE_MAX, VERB_SIZE_MIN, font_path)
    desc_font = load_font(font_path, DESC_SIZE)

    text_y = 200
    text_y = draw_centered(draw, text_y, verb.upper(), verb_font, text_color)
    text_y += VERB_DESC_GAP
    draw_centered(draw, text_y, desc.upper(), desc_font, text_color, max_w=MAX_TEXT_W)

    device_x = (CANVAS_W - DEVICE_W) // 2
    screen_x = device_x + BEZEL
    screen_y = DEVICE_Y + BEZEL

    shot = resize_screenshot(Image.open(screenshot_path).convert("RGBA"))
    canvas = Image.alpha_composite(canvas, build_screen_layer(canvas.size, shot, screen_x, screen_y))

    frame = Image.open(frame_path).convert("RGBA")
    frame_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    frame_layer.paste(frame, (device_x, DEVICE_Y))
    canvas = Image.alpha_composite(canvas, frame_layer)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(out, "PNG")
    print(f"ok {out} {CANVAS_W}x{CANVAS_H}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compose App Store screenshot scaffold")
    parser.add_argument("--bg", required=True, help="Background hex color")
    parser.add_argument("--verb", required=True, help="Action verb")
    parser.add_argument("--desc", required=True, help="Benefit text")
    parser.add_argument("--screenshot", required=True, help="Input screenshot path")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--font", default=DEFAULT_BOLD_FONT, help="Font path")
    parser.add_argument("--frame", default=str(DEFAULT_FRAME_PATH), help="Device frame PNG path")
    parser.add_argument("--text-color", default="#FFFFFF", help="Text hex color")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    compose(args.bg, args.verb, args.desc, args.screenshot, args.output, args.font, args.frame, args.text_color)


if __name__ == "__main__":
    main()
