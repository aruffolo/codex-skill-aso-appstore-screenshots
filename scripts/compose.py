#!/usr/bin/env python3
"""
Compose one App Store screenshot scaffold.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DEFAULT_CANVAS_W = 1320
DEFAULT_CANVAS_H = 2868
DEVICE_W_RATIO = 0.798
BEZEL = 15
SCREEN_CORNER_R = 62
DEVICE_Y_RATIO = 0.257
VERB_SIZE_MAX = 256
VERB_SIZE_MIN = 150
DESC_SIZE = 124
VERB_DESC_GAP = 20
DESC_LINE_GAP = 24
SAFE_MARGIN_RATIO = 0.055
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


def draw_centered(draw: ImageDraw.ImageDraw, canvas_w: int, y: int, text: str, font, fill: str, max_w: int | None = None) -> int:
    lines = word_wrap(draw, text, font, max_w) if max_w else [text]
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        height = bbox[3] - bbox[1]
        draw.text((canvas_w // 2, y - bbox[1]), line, fill=fill, font=font, anchor="mt")
        y += height + DESC_LINE_GAP
    return y


def parse_size(value: str) -> tuple[int, int]:
    width, height = value.lower().split("x", 1)
    return int(width), int(height)


def focus_offset(focus: str, container_h: int, content_h: int) -> int:
    if content_h <= container_h or focus == "top":
        return 0
    if focus == "center":
        return -((content_h - container_h) // 2)
    return -(content_h - container_h)


def resize_screenshot(shot: Image.Image, screen_w: int) -> Image.Image:
    scale = screen_w / shot.width
    height = int(shot.height * scale)
    return shot.resize((screen_w, height), Image.LANCZOS)


def build_screen_layer(
    canvas_size: tuple[int, int],
    shot: Image.Image,
    screen_x: int,
    screen_y: int,
    screen_w: int,
    screen_h: int,
    focus: str,
) -> Image.Image:
    mask = Image.new("L", canvas_size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [screen_x, screen_y, screen_x + screen_w, screen_y + screen_h],
        radius=SCREEN_CORNER_R,
        fill=255,
    )

    layer = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(
        [screen_x, screen_y, screen_x + screen_w, screen_y + screen_h],
        radius=SCREEN_CORNER_R,
        fill=(0, 0, 0, 255),
    )
    layer.paste(shot, (screen_x, screen_y + focus_offset(focus, screen_h, shot.height)))
    layer.putalpha(mask)
    return layer


def compose(
    bg_hex: str,
    verb: str,
    desc: str,
    screenshot_path: str,
    output_path: str,
    font_path: str,
    frame_path: str,
    text_color: str,
    size: tuple[int, int],
    frame_style: str,
    focus: str,
) -> None:
    canvas_w, canvas_h = size
    safe_margin = int(canvas_w * SAFE_MARGIN_RATIO)
    max_text_w = canvas_w - 2 * safe_margin
    max_verb_w = canvas_w - 2 * safe_margin
    device_w = int(canvas_w * DEVICE_W_RATIO)
    device_y = int(canvas_h * DEVICE_Y_RATIO)
    bezel = 0 if frame_style == "frameless" else BEZEL
    screen_w = device_w - 2 * bezel
    screen_h = canvas_h - device_y - safe_margin

    canvas = Image.new("RGBA", (canvas_w, canvas_h), (*hex_to_rgb(bg_hex), 255))
    draw = ImageDraw.Draw(canvas)

    verb_font = fit_font(verb.upper(), max_verb_w, VERB_SIZE_MAX, VERB_SIZE_MIN, font_path)
    desc_font = load_font(font_path, DESC_SIZE)

    text_y = 200
    text_y = draw_centered(draw, canvas_w, text_y, verb.upper(), verb_font, text_color)
    text_y += VERB_DESC_GAP
    draw_centered(draw, canvas_w, text_y, desc.upper(), desc_font, text_color, max_w=max_text_w)

    device_x = (canvas_w - device_w) // 2
    screen_x = device_x + bezel
    screen_y = device_y + bezel

    shot = resize_screenshot(Image.open(screenshot_path).convert("RGBA"), screen_w)
    canvas = Image.alpha_composite(
        canvas,
        build_screen_layer(canvas.size, shot, screen_x, screen_y, screen_w, screen_h, focus),
    )

    if frame_style == "framed":
        frame = Image.open(frame_path).convert("RGBA")
        frame_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        frame_layer.paste(frame.resize((device_w, frame.height * device_w // frame.width), Image.LANCZOS), (device_x, device_y))
        canvas = Image.alpha_composite(canvas, frame_layer)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(out, "PNG")
    print(f"ok {out} {canvas_w}x{canvas_h}")


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
    parser.add_argument("--size", default=f"{DEFAULT_CANVAS_W}x{DEFAULT_CANVAS_H}", help="Canvas size WIDTHxHEIGHT")
    parser.add_argument("--frame-style", default="framed", choices=["framed", "frameless"], help="Render with or without device frame")
    parser.add_argument("--focus", default="top", choices=["top", "center", "bottom"], help="Vertical crop focus")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    compose(
        args.bg,
        args.verb,
        args.desc,
        args.screenshot,
        args.output,
        args.font,
        args.frame,
        args.text_color,
        parse_size(args.size),
        args.frame_style,
        args.focus,
    )


if __name__ == "__main__":
    main()
