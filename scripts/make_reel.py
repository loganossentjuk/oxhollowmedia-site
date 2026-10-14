#!/usr/bin/env python3
"""
Build a silent 9:16 Instagram Reel (1080x1920, H.264) from still photos, in the
website's look: a slow push-in on each photo, a hook line in Cormorant Garamond,
and a brand end card ("Dare to see." + the Ox Hollow mark) in cream or green.
Logan adds trending audio in the Instagram app, because music can't be
licensed into the file.

    python3 scripts/make_reel.py out.mp4 \
        images/portfolio/ocean/12-marine-iguana.jpg "This lizard sneezes salt." \
        images/portfolio/ocean/04-blue-footed-booby.jpg "" \
        --end cream

Arguments come in pairs: an image path and its overlay text ("" for none).
Options:
  --seconds N      per photo (default 3.0)
  --transition T   ffmpeg xfade transition (default fade; "radial" sweeps like a fan blade)
  --fade N         transition length in seconds (default 0.5)
  --zoom N         push-in amount (default 0.12; 0 for none)
  --end cream|green|none   brand end card (default cream)
  --end-text TEXT  end card line (default "Dare to see.")
  --fit            show each image whole on cream (for framed mockups) instead of filling the frame
Needs ffmpeg and Pillow. Font: scripts/fonts/CormorantGaramond-Medium.ttf (OFL).
"""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "scripts/fonts/CormorantGaramond-Medium.ttf"
LOGO = ROOT / "brand/logos/oxhollow-lockup-green.png"   # moon mark + OX HOLLOW
CREAM, CREAM2, GREEN, INK = (243, 239, 228), (229, 222, 200), (41, 65, 50), (34, 34, 30)


def font(size):
    f = ImageFont.truetype(str(FONT), size)
    try:
        f.set_variation_by_axes([500])   # Cormorant Garamond 500, as on the site
    except Exception:
        pass
    return f


def tracked(draw, cx, y, text, f, fill, track):
    """Draw one centred line with letter-spacing (track is in em, like 0.12em on the site)."""
    gap = f.size * track
    widths = [draw.textlength(ch, font=f) for ch in text]
    x = cx - (sum(widths) + gap * (len(text) - 1)) / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=f, fill=fill)
        x += w + gap


def frame(src, text, out, zoom, fit=False):
    """Fill 9:16 with room for the push-in, then set the hook in the lower third."""
    m = 1 + zoom + 0.03
    im = Image.open(src).convert("RGB")
    if fit:   # whole image on the site's cream, like a print on the wall
        gray = im.convert("L").point(lambda v: 255 if v < 238 else 0)
        bb = gray.getbbox()                    # trim the mockup's white surround to the frame
        if bb:
            im = im.crop(bb)
        im.thumbnail((round(W * 0.86), round(H * 0.72)), Image.LANCZOS)
        bg = Image.new("RGB", (W, H), CREAM2)
        bg.paste(im, ((W - im.width) // 2, round(H * 0.40 - im.height / 2)))
        im = bg
    scale = max(W * m / im.width, H * m / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    x, y = (im.width - round(W * m)) // 2, (im.height - round(H * m)) // 2
    im = im.crop((x, y, x + round(W * m), y + round(H * m))).convert("RGBA")
    if text and fit:   # green type under the print, like the site's captions
        f = font(round(84 * m))
        d = ImageDraw.Draw(im)
        for i, line in enumerate(text.split("\n")):
            tracked(d, im.width / 2, im.height * 0.80 + i * f.size * 1.2, line, f, GREEN + (255,), 0.06)
        text = ""
    if text:
        f = font(round(96 * m))
        lines = text.split("\n")
        lh = f.size * 1.2
        ty = im.height * 0.66 - lh * len(lines) / 2
        band = Image.new("L", (1, im.height), 0)   # soft dark band behind the lower third
        for yy in range(im.height):
            t = abs(yy - (ty + lh * len(lines) / 2)) / (im.height * 0.16)
            band.putpixel((0, yy), int(120 * max(0.0, 1 - t * t)))
        im.alpha_composite(Image.merge("RGBA", [Image.new("L", im.size, 0)] * 3 + [band.resize(im.size)]))
        shade = Image.new("RGBA", im.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(shade)
        for i, line in enumerate(lines):
            tracked(sd, im.width / 2, ty + i * lh + 3, line, f, (0, 0, 0, 150), 0.04)
        im.alpha_composite(shade.filter(ImageFilter.GaussianBlur(10)))
        d = ImageDraw.Draw(im)
        for i, line in enumerate(lines):
            tracked(d, im.width / 2, ty + i * lh, line, f, CREAM + (255,), 0.04)
    im.convert("RGB").save(out, quality=93)


def end_card(style, text, out):
    """Cream or green card: the mark, the line, and the site — the website's footer in 9:16."""
    bg, fg = (CREAM, GREEN) if style == "cream" else (GREEN, CREAM)
    im = Image.new("RGB", (W, H), bg)
    mask = Image.open(LOGO).convert("RGBA").getchannel("A")    # the lockup's ink, recoloured below
    bbox = mask.getbbox()
    mask = mask.crop(bbox)
    mw = 640
    mask = mask.resize((mw, round(mask.height * mw / mask.width)), Image.LANCZOS)
    im.paste(Image.new("RGB", mask.size, fg), ((W - mw) // 2, 640 - mask.height // 2), mask)
    d = ImageDraw.Draw(im)
    tracked(d, W / 2, 1010, text, font(84), fg, 0.06)
    tracked(d, W / 2, 1150, "OXHOLLOWMEDIA.COM", font(40), fg, 0.12)
    im.save(out, quality=93)


def opt(args, name, default):
    if name in args:
        i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
    return default


def main():
    args = sys.argv[1:]
    secs = float(opt(args, "--seconds", 3.0))
    trans = opt(args, "--transition", "fade")
    fade = float(opt(args, "--fade", 0.5))
    zoom = float(opt(args, "--zoom", 0.12))
    end = opt(args, "--end", "cream")
    end_text = opt(args, "--end-text", "Dare to see.")
    fit = "--fit" in args
    if fit: args.remove("--fit")
    if len(args) < 3 or len(args[1:]) % 2:
        sys.exit(__doc__)
    out, pairs = args[0], list(zip(args[1::2], args[2::2]))
    n = round(secs * FPS)
    with tempfile.TemporaryDirectory() as tmp:
        cmd = ["ffmpeg", "-y", "-loglevel", "error"]
        for k, (src, text) in enumerate(pairs):
            f = Path(tmp) / f"{k}.jpg"
            frame(src, text.replace("\\n", "\n"), f, zoom, fit)
            cmd += ["-i", str(f)]   # one frame in; zoompan makes all n frames from it
        parts = []
        for k in range(len(pairs)):
            parts.append(f"[{k}:v]zoompan=z='1+{zoom}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                         f":d={n}:s={W}x{H}:fps={FPS},setsar=1,format=yuv420p[v{k}]")
        clips = [(f"v{k}", secs) for k in range(len(pairs))]
        if end != "none":
            ef = Path(tmp) / "end.jpg"
            end_card(end, end_text, ef)
            cmd += ["-loop", "1", "-t", "2.0", "-i", str(ef)]
            parts.append(f"[{len(pairs)}:v]scale={W}:{H},fps={FPS},setsar=1,format=yuv420p[vend]")
            clips.append(("vend", 2.0))
        last, length = clips[0]
        for k, (name, dur) in enumerate(clips[1:], 1):
            t = "fade" if name == "vend" else trans
            fd = 0.5 if name == "vend" else fade
            parts.append(f"[{last}][{name}]xfade=transition={t}:duration={fd}:offset={length - fd:.3f}[x{k}]")
            last, length = f"x{k}", length + dur - fd
        cmd += ["-filter_complex", ";".join(parts), "-map", f"[{last}]", "-c:v", "libx264",
                "-preset", "medium", "-crf", "22", "-maxrate", "5M", "-bufsize", "10M", "-pix_fmt", "yuv420p",
                "-movflags", "+faststart", "-r", str(FPS), out]
        subprocess.run(cmd, check=True)
    print(f"{out}: {len(pairs)} photos{' + end card' if end != 'none' else ''}, {length:.1f}s")


if __name__ == "__main__":
    main()
