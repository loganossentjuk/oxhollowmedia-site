#!/usr/bin/env python3
"""
Build a silent 9:16 Instagram Reel (1080x1920, H.264) from still photos:
a slow push-in on each photo, soft crossfades, and an optional line of text
over each clip. Logan adds trending audio in the Instagram app, because music
can't be licensed into the file.

    python3 scripts/make_reel.py out.mp4 \
        images/portfolio/ocean/04-blue-footed-booby.jpg "Galápagos, 2021" \
        images/portfolio/ocean/03-sea-lion-pup.jpg "" \
        images/portfolio/ocean/12-marine-iguana.jpg "Five prints from one trip"

Arguments come in pairs: an image path and its overlay text ("" for none).
Options: --seconds N (per photo, default 3.0). Needs ffmpeg and Pillow.
"""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, FADE = 1080, 1920, 30, 0.5
FONT = next((f for f in ("/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
                         "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
                         "/System/Library/Fonts/Supplemental/Georgia.ttf") if Path(f).exists()), None)


def frame(src, text, out):
    """Fill 9:16 at 1.15x so the push-in never shows an edge; add the text."""
    im = Image.open(src).convert("RGB")
    scale = max(W * 1.15 / im.width, H * 1.15 / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    x, y = (im.width - round(W * 1.15)) // 2, (im.height - round(H * 1.15)) // 2
    im = im.crop((x, y, x + round(W * 1.15), y + round(H * 1.15)))
    if text:
        font = ImageFont.truetype(FONT, 76) if FONT else ImageFont.load_default()
        layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        box = d.multiline_textbbox((0, 0), text, font=font, align="center", spacing=12)
        tx = (im.width - (box[2] - box[0])) // 2
        ty = int(im.height * 0.62)
        shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(shadow).multiline_text((tx, ty), text, font=font, fill=(0, 0, 0, 170),
                                              align="center", spacing=12)
        layer.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(6)))
        d.multiline_text((tx, ty), text, font=font, fill=(255, 255, 255, 240), align="center", spacing=12)
        im = Image.alpha_composite(im.convert("RGBA"), layer).convert("RGB")
    im.save(out, quality=92)


def main():
    args = sys.argv[1:]
    secs = 3.0
    if "--seconds" in args:
        i = args.index("--seconds"); secs = float(args[i + 1]); del args[i:i + 2]
    if len(args) < 3 or len(args[1:]) % 2:
        sys.exit(__doc__)
    out, pairs = args[0], list(zip(args[1::2], args[2::2]))
    n = round(secs * FPS)
    with tempfile.TemporaryDirectory() as tmp:
        cmd = ["ffmpeg", "-y", "-loglevel", "error"]
        for k, (src, text) in enumerate(pairs):
            f = Path(tmp) / f"{k}.jpg"
            frame(src, text.replace("\\n", "\n"), f)
            cmd += ["-loop", "1", "-t", str(secs), "-i", str(f)]
        parts, last = [], None
        for k in range(len(pairs)):
            parts.append(f"[{k}:v]zoompan=z='1+0.12*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                         f":d={n}:s={W}x{H}:fps={FPS},setsar=1,format=yuv420p[v{k}]")
        last, length = "v0", secs
        for k in range(1, len(pairs)):
            parts.append(f"[{last}][v{k}]xfade=transition=fade:duration={FADE}:offset={length - FADE:.3f}[x{k}]")
            last, length = f"x{k}", length + secs - FADE
        cmd += ["-filter_complex", ";".join(parts), "-map", f"[{last}]", "-c:v", "libx264",
                "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                "-r", str(FPS), out]
        subprocess.run(cmd, check=True)
    print(f"{out}: {len(pairs)} photos, {length:.1f}s")


if __name__ == "__main__":
    main()
