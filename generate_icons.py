import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"c:\Users\Kawamoto\Documents\AgentAIDev\mobile-apps\024_aws-clf-drill"
RES_DIR = os.path.join(BASE_DIR, r"app\src\main\res")
STORE_DIR = os.path.join(BASE_DIR, r"store_assets\play")

SLATE_BG = (15, 23, 42)       # #0F172A (Midnight Slate)
WHITE = (255, 255, 255)
ORANGE = (255, 153, 0)        # #FF9900 (AWS Orange)

def draw_aws_symbol(draw, ox, oy, scale=1.0):
    by = oy + int(24 * scale)
    w_base = int(130 * scale)
    bx1 = ox - w_base // 2
    bx2 = ox + w_base // 2
    
    # Left puff
    draw.ellipse([ox - int(65*scale), by - int(48*scale), ox - int(15*scale), by], fill=WHITE)
    # Center-left (highest)
    draw.ellipse([ox - int(42*scale), by - int(84*scale), ox + int(18*scale), by - int(18*scale)], fill=WHITE)
    # Center-right
    draw.ellipse([ox - int(6*scale), by - int(70*scale), ox + int(48*scale), by - int(12*scale)], fill=WHITE)
    # Right puff
    draw.ellipse([ox + int(15*scale), by - int(46*scale), ox + int(65*scale), by], fill=WHITE)
    # Base fill
    draw.rectangle([bx1 + int(16*scale), by - int(34*scale), bx2 - int(16*scale), by], fill=WHITE)
    
    # Orange arrow curve
    arc_box = [ox - int(60*scale), oy + int(12*scale), ox + int(60*scale), oy + int(50*scale)]
    draw.arc(arc_box, start=25, end=155, fill=ORANGE, width=int(10*scale))
    
    # Arrow head
    hx = ox + int(50 * scale)
    hy = oy + int(24 * scale)
    draw.polygon([
        (hx + int(12*scale), hy - int(6*scale)),
        (hx - int(4*scale), hy - int(14*scale)),
        (hx + int(2*scale), hy + int(8*scale))
    ], fill=ORANGE)

def generate_512_icon():
    img = Image.new("RGBA", (512, 512), SLATE_BG)
    draw = ImageDraw.Draw(img)
    draw_aws_symbol(draw, 256, 175, scale=1.9)
    font = ImageFont.truetype("arialbd.ttf", 52)
    draw.text((256, 385), "AWS Drill", fill=WHITE, font=font, anchor="mm")

    os.makedirs(STORE_DIR, exist_ok=True)
    out_path = os.path.join(STORE_DIR, "app_icon_512.png")
    img.save(out_path, "PNG")
    print(f"Saved 512x512 icon to {out_path}")
    return img

def generate_foreground_1080():
    img = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_aws_symbol(draw, 540, 395, scale=3.8)
    font = ImageFont.truetype("arialbd.ttf", 108)
    draw.text((540, 815), "AWS Drill", fill=WHITE, font=font, anchor="mm")

    drawable_dir = os.path.join(RES_DIR, "drawable")
    os.makedirs(drawable_dir, exist_ok=True)
    out_path = os.path.join(drawable_dir, "ic_launcher_foreground_img.png")
    img.save(out_path, "PNG")
    print(f"Saved 1080x1080 adaptive foreground to {out_path}")

def generate_mipmaps(base_512):
    targets = [
        ("mipmap-mdpi", 48),
        ("mipmap-hdpi", 72),
        ("mipmap-xhdpi", 96),
        ("mipmap-xxhdpi", 144),
        ("mipmap-xxxhdpi", 192),
    ]

    for folder, size in targets:
        folder_path = os.path.join(RES_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)

        # 1. Square launcher
        square_img = base_512.resize((size, size), Image.Resampling.LANCZOS)
        square_path = os.path.join(folder_path, "ic_launcher.png")
        square_img.save(square_path, "PNG")

        # 2. Round launcher (circle mask)
        round_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        mask = Image.new("L", (size, size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse([0, 0, size, size], fill=255)
        round_img.paste(square_img, (0, 0), mask)

        round_path = os.path.join(folder_path, "ic_launcher_round.png")
        round_img.save(round_path, "PNG")
        print(f"Saved {size}x{size} icons to {folder}")

if __name__ == "__main__":
    icon_512 = generate_512_icon()
    generate_foreground_1080()
    generate_mipmaps(icon_512)
    print("All AWS Drill icons successfully generated!")
