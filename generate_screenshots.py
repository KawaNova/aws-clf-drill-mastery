import os
from PIL import Image, ImageDraw, ImageFont

def get_fonts():
    try:
        title_font = ImageFont.truetype("meiryob.ttc", 44)
        h1_font = ImageFont.truetype("meiryob.ttc", 34)
        h2_font = ImageFont.truetype("meiryo.ttc", 28)
        body_font = ImageFont.truetype("meiryo.ttc", 25)
        body_bold = ImageFont.truetype("meiryob.ttc", 26)
        jp_bold_font = ImageFont.truetype("meiryob.ttc", 30)
        tag_font = ImageFont.truetype("meiryob.ttc", 24)
        mono_font = ImageFont.truetype("consola.ttf", 22)
        mono_bold = ImageFont.truetype("consolab.ttf", 24)
        sb_font = ImageFont.truetype("arialbd.ttf", 36)
    except:
        f = ImageFont.load_default()
        return f, f, f, f, f, f, f, f, f, f
    return title_font, h1_font, h2_font, body_font, body_bold, jp_bold_font, tag_font, mono_font, mono_bold, sb_font

def create_base_canvas():
    img = Image.new("RGB", (1080, 2400), (15, 23, 42)) # Slate 900
    draw = ImageDraw.Draw(img)
    title_font, _, h2_font, _, _, jp_bold_font, tag_font, _, _, sb_font = get_fonts()

    # Status Bar
    draw.text((64, 40), "10:00", fill=(255, 255, 255), font=sb_font)

    # Top App Bar
    # Icon box
    draw.rounded_rectangle([48, 110, 144, 206], radius=24, fill=(255, 153, 0)) # AWS Orange
    # Cloud outline
    draw.arc([66, 130, 98, 162], 180, 360, fill=(255, 255, 255), width=4)
    draw.arc([86, 122, 126, 162], 210, 360, fill=(255, 255, 255), width=4)
    draw.line([(66, 162), (126, 162)], fill=(255, 255, 255), width=4)
    # Smile arrow
    draw.arc([68, 166, 124, 186], 15, 165, fill=(255, 255, 255), width=4)

    draw.text((168, 116), "AWS クラウド超入門", fill=(255, 255, 255), font=title_font)
    draw.text((168, 176), "CLF-C02 突破 ＆ 構成図シミュレータ", fill=(255, 179, 71), font=h2_font)

    # Top Right Buttons: [早見表] [JA]
    draw.rounded_rectangle([750, 130, 875, 190], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((812, 160), "早見表", fill=(255, 179, 71), font=tag_font, anchor="mm")

    draw.rounded_rectangle([895, 130, 1032, 190], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((963, 160), "🇯🇵 JA", fill=(255, 255, 255), font=jp_bold_font, anchor="mm")

    # Bottom Home Bar
    draw.rounded_rectangle([390, 2360, 690, 2372], radius=6, fill=(255, 255, 255))

    return img, draw

# -------------------------------------------------------------
# Screen 1: Home Dashboard
# -------------------------------------------------------------
def generate_screen_01_home():
    img, draw = create_base_canvas()
    _, h1_font, h2_font, body_font, body_bold, jp_bold_font, tag_font, _, _, _ = get_fonts()

    # Progress Summary Card
    draw.rounded_rectangle([48, 240, 1032, 600], radius=28, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((88, 280), "AWS CLF-C02 習得ステータス", fill=(255, 255, 255), font=h1_font)
    draw.text((990, 285), "18 / 30", fill=(255, 179, 71), font=h2_font, anchor="ra")

    # Progress Bar
    draw.rounded_rectangle([88, 350, 992, 368], radius=9, fill=(15, 23, 42))
    draw.rounded_rectangle([88, 350, 630, 368], radius=9, fill=(255, 153, 0))

    # 3 Metrics
    draw.text((230, 430), "60%", fill=(255, 255, 255), font=h1_font, anchor="mm")
    draw.text((230, 480), "進捗率", fill=(148, 163, 184), font=body_font, anchor="mm")

    draw.text((540, 430), "92%", fill=(16, 185, 129), font=h1_font, anchor="mm")
    draw.text((540, 480), "正答率", fill=(148, 163, 184), font=body_font, anchor="mm")

    draw.text((850, 430), "5問", fill=(251, 191, 36), font=h1_font, anchor="mm")
    draw.text((850, 480), "ブックマーク", fill=(148, 163, 184), font=body_font, anchor="mm")

    # Interactive Simulator Banner
    draw.rounded_rectangle([48, 630, 1032, 790], radius=24, fill=(234, 88, 12), outline=(255, 153, 0), width=2)
    draw.text((90, 670), "⚡ AWSアーキテクチャ図解シミュレータ", fill=(255, 255, 255), font=h1_font)
    draw.text((90, 725), "3層Web・サーバーレス・VPC構成をタップして直感理解！", fill=(254, 215, 170), font=body_font)

    # Quick Practice Section
    draw.text((48, 830), "クイック演習モード", fill=(255, 255, 255), font=h1_font)

    modes = [
        ([48, 890, 520, 1050], "🔥 全30問 総特訓", "全ドメインマラソン演習", (255, 153, 0)),
        ([560, 890, 1032, 1050], "🎯 弱点克服", "間違えた問題だけ復習", (236, 72, 153)),
        ([48, 1080, 520, 1240], "⚡ ランダム10問", "スキマ時間の集中特訓", (251, 191, 36)),
        ([560, 1080, 1032, 1240], "⭐ 保存した問題", "5問 保存中", (6, 182, 212)),
    ]
    for box, title, desc, clr in modes:
        draw.rounded_rectangle(box, radius=20, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
        draw.text((box[0] + 30, box[1] + 40), title, fill=(255, 255, 255), font=jp_bold_font)
        draw.text((box[0] + 30, box[1] + 95), desc, fill=(148, 163, 184), font=body_font)

    # Category Focus Drills
    draw.text((48, 1290), "4大試験分野別 集中ドリル", fill=(255, 255, 255), font=h1_font)

    cats = [
        ("☁️ クラウドの概念 (Cloud Concepts)", "8問中 7問完了", 1350),
        ("🛡️ セキュリティとコンプライアンス", "7問中 5問完了", 1490),
        ("⚙️ テクノロジー & クラウドサービス", "9問中 4問完了", 1630),
        ("💰 請求、料金、およびサポート", "6問中 2問完了", 1770),
    ]
    for title, progress, cy in cats:
        draw.rounded_rectangle([48, cy, 1032, cy + 115], radius=20, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
        draw.text((88, cy + 24), title, fill=(255, 255, 255), font=jp_bold_font)
        draw.text((88, cy + 68), progress, fill=(148, 163, 184), font=body_font)
        draw.text((980, cy + 40), "▶", fill=(255, 153, 0), font=h2_font, anchor="ra")

    # Sister Apps Banner
    draw.rounded_rectangle([48, 1930, 1032, 2100], radius=20, fill=(17, 24, 39), outline=(75, 85, 99), width=2)
    draw.text((88, 1965), "🚀 姉妹アプリでITスキルを多角武装！", fill=(255, 255, 255), font=jp_bold_font)
    draw.text((88, 2020), "Dockerドリル ・ ネットワーク特訓 ・ 基本情報科目A ・ 正規表現", fill=(156, 163, 175), font=body_font)

    out_path = r"c:\Users\Kawamoto\Documents\AgentAIDev\mobile-apps\024_aws-clf-drill\store_assets\play\screenshot_01_home.png"
    img.save(out_path, "PNG")
    print(f"Generated screenshot 1 at {out_path}")

# -------------------------------------------------------------
# Screen 2: Quiz with ASCII Diagram & Exam Tip
# -------------------------------------------------------------
def generate_screen_02_quiz():
    img, draw = create_base_canvas()
    title_font, h1_font, h2_font, body_font, body_bold, jp_bold_font, tag_font, mono_font, mono_bold, _ = get_fonts()

    # Top Bar: Question Count & Category
    draw.rectangle([0, 100, 1080, 210], fill=(15, 23, 42))
    draw.text((64, 135), "←", fill=(255, 255, 255), font=title_font)
    draw.text((150, 135), "問題 5 / 30", fill=(255, 255, 255), font=h1_font)
    draw.text((980, 135), "⭐", fill=(251, 191, 36), font=h1_font, anchor="ra")

    # Category Badge
    draw.rounded_rectangle([48, 230, 460, 280], radius=12, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((68, 255), "🛡️ セキュリティとコンプライアンス", fill=(255, 179, 71), font=tag_font, anchor="lm")

    # Question Card
    draw.rounded_rectangle([48, 305, 1032, 530], radius=24, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((88, 345), "AWSの責任共有モデルにおいて、顧客側（クラウド内の", fill=(255, 255, 255), font=jp_bold_font)
    draw.text((88, 395), "セキュリティ）が担う責任範囲として正しいものはどれか？", fill=(255, 255, 255), font=jp_bold_font)
    draw.text((88, 460), "※ AWSインフラ側の責任と利用者の責任の境界を問う頻出問題", fill=(148, 163, 184), font=body_font)

    # ASCII Architecture / Concept Diagram Box
    draw.rounded_rectangle([48, 555, 1032, 920], radius=20, fill=(9, 13, 22), outline=(51, 65, 85), width=2)
    draw.text((88, 580), "ARCHITECTURE CONCEPT DIAGRAM", fill=(255, 153, 0), font=mono_bold)

    ascii_lines = [
        "============================================================",
        " [ 顧客の責任 (クラウド「内」のセキュリティ) ]               ",
        "  - 顧客データ、IAM認証・アクセス権限管理                   ",
        "  - ゲストOS・アプリケーションのパッチ適用 ★               ",
        "  - ネットワークトラフィック保護、ファイアウォール設定      ",
        "------------------------------------------------------------",
        " [ AWSの責任 (クラウド「の」セキュリティ) ]                 ",
        "  - データセンター物理セキュリティ、施設管理                ",
        "  - ホストOS、ハイパーバイザー、ストレージ、物理ネットワーク",
        "============================================================",
    ]
    dy = 620
    for line in ascii_lines:
        color = (16, 185, 129) if "★" in line else (203, 213, 225)
        if "AWSの責任" in line or "顧客の責任" in line:
            color = (255, 179, 71)
        draw.text((88, dy), line, fill=color, font=mono_font)
        dy += 28

    # 4 Choices
    choices = [
        ("A", "データセンターの物理セキュリティおよび環境管理", False, False),
        ("B", "物理サーバーのハイパーバイザーおよびホストOSの更新", False, False),
        ("C", "EC2 ゲストOSのパッチ適用およびIAMアクセス権限管理", True, True),
        ("D", "AWS グローバル基幹ネットワーク機器のハードウェア保守", False, False),
    ]

    cy = 945
    for letter, text, is_correct, is_selected in choices:
        bg_col = (16, 185, 129, 40) if is_correct else (30, 41, 59)
        border_col = (16, 185, 129) if is_correct else (51, 65, 85)

        draw.rounded_rectangle([48, cy, 1032, cy + 95], radius=16, fill=(20, 45, 35) if is_correct else (30, 41, 59), outline=border_col, width=2)

        # Letter badge
        badge_fill = (16, 185, 129) if is_correct else (51, 65, 85)
        draw.rounded_rectangle([68, cy + 18, 128, cy + 77], radius=12, fill=badge_fill)
        draw.text((98, cy + 47), letter, fill=(255, 255, 255), font=jp_bold_font, anchor="mm")

        draw.text((150, cy + 30), text, fill=(255, 255, 255) if is_correct else (203, 213, 225), font=body_bold if is_correct else body_font)
        if is_correct:
            draw.text((990, cy + 47), "✓ 正解", fill=(16, 185, 129), font=jp_bold_font, anchor="rm")

        cy += 115

    # Explanation & Exam Tip Card
    draw.rounded_rectangle([48, 1425, 1032, 1920], radius=20, fill=(26, 36, 56), outline=(255, 153, 0), width=2)
    draw.text((88, 1460), "💡 合格のツボ (Exam Tip)", fill=(255, 153, 0), font=h1_font)
    draw.text((88, 1520), "「クラウド『の』セキュリティはAWS、クラウド『内』は顧客」！", fill=(255, 255, 255), font=body_bold)
    draw.text((88, 1575), "試験では「誰が何を保守するか」が極めて高頻度で問われます。", fill=(203, 213, 225), font=body_font)
    draw.text((88, 1620), "・EC2のOSパッチ・セキュリティグループ設定・IAM設定 ＝ 顧客責任", fill=(254, 215, 170), font=body_font)
    draw.text((88, 1665), "・物理データセンター・ハードウェア・ハイパーバイザー ＝ AWS責任", fill=(148, 163, 184), font=body_font)
    draw.text((88, 1710), "※ マネージド型（RDS/S3）ではOSパッチもAWSが担当する点も重要！", fill=(148, 163, 184), font=body_font)

    # Next Button
    draw.rounded_rectangle([48, 1960, 1032, 2060], radius=20, fill=(255, 153, 0))
    draw.text((540, 2010), "解説を理解して次の問題へ  ▶", fill=(15, 23, 42), font=jp_bold_font, anchor="mm")

    out_path = r"c:\Users\Kawamoto\Documents\AgentAIDev\mobile-apps\024_aws-clf-drill\store_assets\play\screenshot_02_quiz.png"
    img.save(out_path, "PNG")
    print(f"Generated screenshot 2 at {out_path}")

# -------------------------------------------------------------
# Screen 3: Interactive Architecture Simulator
# -------------------------------------------------------------
def generate_screen_03_architecture():
    img, draw = create_base_canvas()
    title_font, h1_font, h2_font, body_font, body_bold, jp_bold_font, tag_font, mono_font, mono_bold, _ = get_fonts()

    # Top Bar: Architecture Viewer Title
    draw.rectangle([0, 100, 1080, 210], fill=(15, 23, 42))
    draw.text((64, 135), "←", fill=(255, 255, 255), font=title_font)
    draw.text((150, 135), "AWS アーキテクチャ図解シミュレータ", fill=(255, 255, 255), font=h1_font)

    # Scenario Selection Chips
    scenarios = [
        ("3層Web高可用性", True),
        ("サーバーレスAPI", False),
        ("セキュアVPC構成", False),
    ]
    cx = 48
    for sc_title, is_active in scenarios:
        box_w = 300
        bg_col = (255, 153, 0) if is_active else (30, 41, 59)
        txt_col = (15, 23, 42) if is_active else (203, 213, 225)
        draw.rounded_rectangle([cx, 230, cx + box_w, 295], radius=16, fill=bg_col, outline=(51, 65, 85) if not is_active else None, width=2)
        draw.text((cx + box_w // 2, 262), sc_title, fill=txt_col, font=body_bold, anchor="mm")
        cx += box_w + 20

    # Architecture Canvas Box
    draw.rounded_rectangle([48, 320, 1032, 1260], radius=24, fill=(17, 24, 39), outline=(51, 65, 85), width=2)
    draw.text((88, 350), "MULTI-TIER HIGH AVAILABILITY WEB SYSTEM", fill=(255, 153, 0), font=mono_bold)
    draw.text((88, 390), "各コンポーネントをタップして役割と試験対策ポイントを確認", fill=(148, 163, 184), font=body_font)

    # Architecture Nodes Diagram
    nodes = [
        ("Route 53", "DNS & ルーティング", [88, 450, 480, 560], False),
        ("CloudFront", "CDN & エッジ配信", [552, 450, 992, 560], False),
        ("ALB", "Application Load Balancer", [88, 600, 992, 700], False),
        ("EC2 (AZ-1a)", "Auto Scaling Group", [88, 740, 520, 850], False),
        ("EC2 (AZ-1c)", "Auto Scaling Group", [560, 740, 992, 850], False),
        ("Aurora (Primary)", "Multi-AZ 高可用DB", [88, 890, 520, 1000], True), # Selected!
        ("Aurora (Standby)", "自動フェイルオーバー", [560, 890, 992, 1000], False),
        ("Amazon S3", "静的アセット・高耐久性", [88, 1040, 992, 1140], False),
    ]

    for name, sub, box, is_sel in nodes:
        bg = (40, 55, 80) if is_sel else (30, 41, 59)
        border = (255, 153, 0) if is_sel else (51, 65, 85)
        border_w = 4 if is_sel else 2
        draw.rounded_rectangle(box, radius=16, fill=bg, outline=border, width=border_w)
        draw.text((box[0] + 24, box[1] + 20), name, fill=(255, 179, 71) if is_sel else (255, 255, 255), font=jp_bold_font)
        draw.text((box[0] + 24, box[1] + 62), sub, fill=(255, 255, 255) if is_sel else (148, 163, 184), font=body_font)
        if is_sel:
            draw.text((box[2] - 30, box[1] + 45), "👈 選択中", fill=(255, 153, 0), font=jp_bold_font, anchor="rm")

    # Selected Service Detailed Inspection Card
    draw.rounded_rectangle([48, 1300, 1032, 1950], radius=24, fill=(30, 41, 59), outline=(255, 153, 0), width=2)
    draw.text((88, 1340), "🌟 詳細解説: Amazon Aurora (Multi-AZ)", fill=(255, 153, 0), font=h1_font)
    draw.text((88, 1400), "分類: フルマネージド・エンタープライズ RDBMS", fill=(148, 163, 184), font=body_bold)

    desc_lines = [
        "・MySQL / PostgreSQL と完全互換のクラウド専用リレーショナルDB",
        "・標準MySQLの最大5倍、PostgreSQLの最大3倍の圧倒的スループット",
        "・3つのアベイラビリティゾーン (AZ) にデータを6重レプリケーション",
        "・障害時は30秒未満で自動フェイルオーバー（ダウンタイム最小化）",
        "・最大15個のリードレプリカを追加可能で読み取り負荷を劇的分散",
        "・ストレージは10GBから128TBまで自動拡張（手動操作不要）",
    ]
    dy = 1460
    for dl in desc_lines:
        draw.text((88, dy), dl, fill=(255, 255, 255), font=body_font)
        dy += 46

    draw.rounded_rectangle([88, 1760, 992, 1890], radius=16, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    draw.text((118, 1785), "🎯 試験頻出ポイント (CLF-C02)", fill=(251, 191, 36), font=body_bold)
    draw.text((118, 1835), "「高可用性・Multi-AZ 自動フェイルオーバー・クラウドネイティブ」が出たらAurora！", fill=(203, 213, 225), font=body_font)

    out_path = r"c:\Users\Kawamoto\Documents\AgentAIDev\mobile-apps\024_aws-clf-drill\store_assets\play\screenshot_03_feedback.png"
    img.save(out_path, "PNG")
    print(f"Generated screenshot 3 at {out_path}")

# -------------------------------------------------------------
# Screen 4: CheatSheet Screen
# -------------------------------------------------------------
def generate_screen_04_cheatsheet():
    img, draw = create_base_canvas()
    title_font, h1_font, h2_font, body_font, body_bold, jp_bold_font, tag_font, mono_font, mono_bold, _ = get_fonts()

    # Top Bar: CheatSheet Title
    draw.rectangle([0, 100, 1080, 210], fill=(15, 23, 42))
    draw.text((64, 135), "←", fill=(255, 255, 255), font=title_font)
    draw.text((150, 135), "AWS 主要サービス逆引きチートシート", fill=(255, 255, 255), font=h1_font)

    # Search Box
    draw.rounded_rectangle([48, 230, 1032, 310], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((88, 270), "🔍  サービス名や用途で検索 (例: EC2, S3, サーバーレス, VPC)...", fill=(148, 163, 184), font=body_font, anchor="lm")

    # Tabs
    tabs = ["コンピュート", "ストレージ", "ネットワーク", "セキュリティ"]
    tx = 48
    for i, t in enumerate(tabs):
        is_sel = (i == 0)
        t_w = 230
        if is_sel:
            draw.text((tx + t_w // 2, 360), t, fill=(255, 153, 0), font=jp_bold_font, anchor="mm")
            draw.rounded_rectangle([tx + 20, 395, tx + t_w - 20, 403], radius=4, fill=(255, 153, 0))
        else:
            draw.text((tx + t_w // 2, 360), t, fill=(148, 163, 184), font=jp_bold_font, anchor="mm")
        tx += t_w + 12

    # Cheat Sheet Cards
    cards = [
        ("Amazon EC2", "コンピュート", "aws ec2 run-instances --image-id ami-xxxx", "安全でサイズ変更可能な仮想サーバー。オンデマンド、リザーブド、Spotなどの柔軟な課金体系。", 430),
        ("AWS Lambda", "サーバーレス", "aws lambda invoke --function-name MyFunction", "サーバー管理不要でイベント駆動型コードを実行。ミリ秒単位の課金でコストを最適化。", 710),
        ("Amazon S3", "ストレージ", "aws s3 sync ./dist s3://my-bucket --delete", "99.999999999% (11 9's) の高耐久性を誇るオブジェクトストレージ。静的Webホスティング対応。", 990),
        ("AWS IAM", "セキュリティ", "aws iam create-role --role-name LambdaExecutionRole", "認証・認可を一元管理。最小権限の原則に基づくロール・ポリシーで安全なアクセス統制。", 1270),
    ]

    for title, tag, syntax, desc, cy in cards:
        draw.rounded_rectangle([48, cy, 1032, cy + 250], radius=20, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
        # Title & Tag
        draw.text((88, cy + 30), title, fill=(255, 255, 255), font=jp_bold_font)
        draw.rounded_rectangle([820, cy + 25, 990, cy + 65], radius=10, fill=(51, 65, 85))
        draw.text((905, cy + 45), tag, fill=(255, 179, 71), font=tag_font, anchor="mm")

        # Syntax Bar (Terminal Style with Copy Icon)
        draw.rounded_rectangle([88, cy + 85, 992, cy + 160], radius=12, fill=(9, 13, 22), outline=(51, 65, 85), width=1)
        draw.text((115, cy + 122), syntax, fill=(255, 153, 0), font=mono_bold, anchor="lm")
        draw.text((965, cy + 122), "📋", fill=(148, 163, 184), font=tag_font, anchor="rm")

        # Description
        draw.text((88, cy + 185), desc, fill=(148, 163, 184), font=body_font)

    out_path = r"c:\Users\Kawamoto\Documents\AgentAIDev\mobile-apps\024_aws-clf-drill\store_assets\play\screenshot_04_cheatsheet.png"
    img.save(out_path, "PNG")
    print(f"Generated screenshot 4 at {out_path}")

if __name__ == "__main__":
    generate_screen_01_home()
    generate_screen_02_quiz()
    generate_screen_03_architecture()
    generate_screen_04_cheatsheet()
