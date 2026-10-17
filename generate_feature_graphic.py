import os
from PIL import Image, ImageDraw, ImageFont

def generate_aws_feature_graphic():
    width, height = 1024, 500
    img = Image.new("RGB", (width, height), (15, 23, 42)) # Slate 900
    draw = ImageDraw.Draw(img)

    # Background gradient styling
    for y in range(height):
        ratio = y / height
        r = int(15 + ratio * 15)
        g = int(23 + ratio * 20)
        b = int(42 + ratio * 30)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Grid Pattern Accents
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(30, 41, 59), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(30, 41, 59), width=1)

    try:
        title_font = ImageFont.truetype("meiryob.ttc", 40)
        title_en_font = ImageFont.truetype("arialbd.ttf", 24)
        subtitle_font = ImageFont.truetype("meiryo.ttc", 20)
        badge_font = ImageFont.truetype("meiryob.ttc", 18)
        mono_font = ImageFont.truetype("consola.ttf", 18)
    except:
        f = ImageFont.load_default()
        title_font, title_en_font, subtitle_font, badge_font, mono_font = f, f, f, f, f

    # Left Section: Titles & Badges
    # Badges
    badge_x, badge_y = 60, 48
    draw.rounded_rectangle([badge_x, badge_y, badge_x + 190, badge_y + 34], radius=8, fill=(255, 153, 0)) # AWS Orange
    draw.text((badge_x + 95, badge_y + 17), "CLF-C02 突破特訓", fill=(15, 23, 42), font=badge_font, anchor="mm")

    draw.rounded_rectangle([badge_x + 205, badge_y, badge_x + 395, badge_y + 34], radius=8, fill=(35, 47, 62), outline=(255, 153, 0), width=1)
    draw.text((badge_x + 300, badge_y + 17), "日・英バイリンガル", fill=(255, 255, 255), font=badge_font, anchor="mm")

    # Main Title
    draw.text((60, 105), "AWS クラウドプラクティショナー", fill=(248, 250, 252), font=title_font)
    draw.text((60, 160), "AWS Cloud Practitioner Mastery Drill", fill=(255, 153, 0), font=title_en_font)

    # Subtitle
    draw.text((60, 205), "4大カテゴリ厳選30問 × 構成図解 × サービス早見表", fill=(203, 213, 225), font=subtitle_font)

    # Feature List
    features = [
        "✓ クラウド概念・責任共有モデル・コスト最適化の鉄板知識",
        "✓ 3層Web・サーバーレス構成のインタラクティブ図解",
        "✓ 主要サービス（EC2/S3/RDS/Lambda）逆引きチートシート"
    ]
    for idx, feat in enumerate(features):
        fy = 265 + idx * 36
        draw.text((60, fy), feat, fill=(241, 245, 249), font=subtitle_font)

    # Right Section: Architecture Diagram Terminal Card
    card_x0, card_y0 = 620, 60
    card_x1, card_y1 = 964, 440
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=16, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    # Header bar
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y0 + 36], radius=16, fill=(30, 41, 59))
    draw.rectangle([card_x0, card_y0 + 18, card_x1, card_y0 + 36], fill=(30, 41, 59))
    # Dots
    draw.ellipse([card_x0 + 14, card_y0 + 13, card_x0 + 24, card_y0 + 23], fill=(239, 68, 68))
    draw.ellipse([card_x0 + 30, card_y0 + 13, card_x0 + 40, card_y0 + 23], fill=(245, 158, 11))
    draw.ellipse([card_x0 + 46, card_y0 + 13, card_x0 + 56, card_y0 + 23], fill=(16, 185, 129))
    draw.text((card_x0 + 70, card_y0 + 18), "aws-architecture.ascii", fill=(148, 163, 184), font=mono_font)

    # Diagram lines inside terminal
    diag_lines = [
        "[User] -> Route 53 (DNS)",
        "           |",
        "           v",
        "   [ CloudFront (CDN) ]",
        "           |",
        "           v",
        "   [ ALB (Load Balancer) ]",
        "     /                \\",
        " (AZ-a)              (AZ-c)",
        " [EC2 AutoScale]   [EC2 AutoScale]",
        "     \\                /",
        "      v              v",
        "   [ Amazon RDS (Multi-AZ) ]",
        "   [ Amazon S3 (11 9's)   ]"
    ]
    for idx, line in enumerate(diag_lines):
        col = (255, 153, 0) if "CloudFront" in line or "ALB" in line or "RDS" in line else (56, 189, 248)
        draw.text((card_x0 + 18, card_y0 + 52 + idx * 23), line, fill=col, font=mono_font)

    store_dir = r"c:\Users\Kawamoto\Documents\AgentAIDev\mobile-apps\024_aws-clf-drill\store_assets\play"
    os.makedirs(store_dir, exist_ok=True)
    out_path = os.path.join(store_dir, "feature_graphic_1024x500.png")
    img.save(out_path, "PNG")
    print(f"Generated feature graphic at {out_path}")

if __name__ == "__main__":
    generate_aws_feature_graphic()
