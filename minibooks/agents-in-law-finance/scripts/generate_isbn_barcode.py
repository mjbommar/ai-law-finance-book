#!/usr/bin/env python3
"""
Generate professional ISBN barcode with READABLE text.

APPROACH:
- Python generates clean base barcode with LARGE, VISIBLE text
- LaTeX/TikZ adds creative wave/geometric masks on top

Usage:
    uv run --with python-barcode,pillow python scripts/generate_isbn_barcode.py
"""

import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import io
from pathlib import Path

ISBN_NUMBER = '9798994345702'
OUTPUT_DIR = Path('back-matter')
OUTPUT_NAME = 'isbn-barcode'

# Barcode settings
BARCODE_OPTIONS = {
    'module_width': 0.35,      # Bar width
    'module_height': 16.0,     # Bar height
    'quiet_zone': 4.5,
    'font_size': 0,            # We add our own text
    'text_distance': 0,
    'background': 'white',
    'foreground': 'black',
    'write_text': False,
    'dpi': 300,
}

# Text sizing - MASSIVE
ISBN_LABEL_SIZE = 22          # ISBN-13 label
ISBN_DIGITS_SIZE = 20          # Digit size - REALLY BIG


def get_font(paths: list, size: int):
    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue
    return ImageFont.load_default()


def format_isbn(isbn: str) -> str:
    """979-8-99434-570-2"""
    if len(isbn) == 13:
        return f"{isbn[0:3]}-{isbn[3]}-{isbn[4:9]}-{isbn[9:12]}-{isbn[12]}"
    return isbn


def create_barcode(isbn: str) -> Image.Image:
    # Generate bars only
    ISBN = barcode.get_barcode_class('isbn13')
    my_isbn = ISBN(isbn, writer=ImageWriter())

    buffer = io.BytesIO()
    my_isbn.write(buffer, options=BARCODE_OPTIONS)
    buffer.seek(0)

    bars = Image.open(buffer).convert('RGBA')
    w, h = bars.size

    # Add space for text (much larger for massive fonts)
    top = 40
    bottom = 35
    final = Image.new('RGBA', (w, h + top + bottom), (255, 255, 255, 255))
    final.paste(bars, (0, top))

    draw = ImageDraw.Draw(final)

    # Fonts
    label_font = get_font([
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    ], ISBN_LABEL_SIZE)

    digit_font = get_font([
        '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf',
    ], ISBN_DIGITS_SIZE)

    # ISBN-13 label above
    label = "ISBN-13"
    bbox = draw.textbbox((0, 0), label, font=label_font)
    lw = bbox[2] - bbox[0]
    draw.text(((w - lw) / 2, 6), label, fill=(0, 0, 0, 255), font=label_font)

    # ISBN digits below
    digits = format_isbn(isbn)
    bbox = draw.textbbox((0, 0), digits, font=digit_font)
    dw = bbox[2] - bbox[0]
    draw.text(((w - dw) / 2, top + h + 4), digits, fill=(0, 0, 0, 255), font=digit_font)

    return final


def save(img: Image.Image):
    OUTPUT_DIR.mkdir(exist_ok=True)
    w, h = img.size

    # PNG
    png = OUTPUT_DIR / f'{OUTPUT_NAME}.png'
    img.save(png, 'PNG', dpi=(300, 300))
    print(f"✓ PNG: {png}")

    # PDF
    pdf = OUTPUT_DIR / f'{OUTPUT_NAME}.pdf'
    pdf_img = Image.new('RGBA', (w, h), (255, 255, 255, 255))
    pdf_img = Image.alpha_composite(pdf_img, img).convert('RGB')
    pdf_img.save(pdf, 'PDF', resolution=300)
    print(f"✓ PDF: {pdf}")

    print(f"✓ Size: {w/300:.2f}\" × {h/300:.2f}\"")


def main():
    print(f"Generating ISBN barcode: {ISBN_NUMBER}")
    img = create_barcode(ISBN_NUMBER)
    save(img)
    print("✓ Done - LaTeX will add creative masks")


if __name__ == '__main__':
    main()
