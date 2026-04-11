#!/usr/bin/env python3
"""
Generate the reusable iPhone frame asset.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageChops

DEVICE_W = 1030
DEVICE_H = 2800
DEVICE_CORNER_R = 77
BEZEL = 15
SCREEN_CORNER_R = 62
SCREEN_W = DEVICE_W - 2 * BEZEL
SCREEN_H = DEVICE_H - 2 * BEZEL
OUT = Path(__file__).resolve().parent.parent / "assets" / "device_frame.png"
DI_OUT = Path(__file__).resolve().parent.parent / "assets" / "device_frame_dynamic_island.png"
DI_W = 130
DI_H = 38
DI_TOP = 14


def build_frame(include_dynamic_island: bool = False) -> Image.Image:
    frame = Image.new("RGBA", (DEVICE_W, DEVICE_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    draw.rounded_rectangle([0, 0, DEVICE_W - 1, DEVICE_H - 1], radius=DEVICE_CORNER_R, fill=(30, 30, 30, 255))
    draw.rounded_rectangle([1, 1, DEVICE_W - 2, DEVICE_H - 2], radius=DEVICE_CORNER_R - 1, fill=(20, 20, 20, 255))

    cutout = Image.new("L", (DEVICE_W, DEVICE_H), 255)
    ImageDraw.Draw(cutout).rounded_rectangle(
        [BEZEL, BEZEL, BEZEL + SCREEN_W, BEZEL + SCREEN_H],
        radius=SCREEN_CORNER_R,
        fill=0,
    )
    frame.putalpha(ImageChops.multiply(frame.getchannel("A"), cutout))

    if include_dynamic_island:
        di_x = (DEVICE_W - DI_W) // 2
        di_y = BEZEL + DI_TOP
        ImageDraw.Draw(frame).rounded_rectangle(
            [di_x, di_y, di_x + DI_W, di_y + DI_H],
            radius=DI_H // 2,
            fill=(0, 0, 0, 255),
        )
    return frame


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate reusable iPhone frame asset")
    parser.add_argument("--dynamic-island", action="store_true", help="Include the Dynamic Island cutout")
    parser.add_argument("--output", help="Output PNG path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out = Path(args.output) if args.output else (DI_OUT if args.dynamic_island else OUT)
    out.parent.mkdir(parents=True, exist_ok=True)
    build_frame(include_dynamic_island=args.dynamic_island).save(out, "PNG")
    print(f"ok {out}")


if __name__ == "__main__":
    main()
