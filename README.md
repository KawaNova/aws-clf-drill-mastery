# AWS Drill - CLF-C02 Exam Prep ☁️

> **AWS クラウド超入門 - CLF-C02 突破 ＆ 構成図シミュレータ**  
> Jetpack Compose 製、実務 ＆ 試験直結の30問一問一答 ＆ アーキテクチャ図解シミュレータ内蔵のAndroid学習アプリ。

[![Platform](https://img.shields.io/badge/Platform-Android-green.svg)](https://www.android.com/)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.0.21-blue.svg)](https://kotlinlang.org/)
[![Target SDK](https://img.shields.io/badge/Target%20SDK-36-orange.svg)](https://developer.android.com/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)]()

---

## 🌟 概要 (Overview)

「AWS Certified Cloud Practitioner (CLF-C02)」の合格を目指すエンジニア、ITコンサルタント、ビジネス職のための実践特訓アプリです。出題頻度の高い4大ドメインから厳選した30問を一問一答形式で演習でき、全問に**ASCIIアーキテクチャ図解**と**全肢解説**、さらに**合格のツボ (Exam Tip)**を完備しています。

また、3層Web高可用性、サーバーレスAPI、セキュアVPC構成を直感的に操作して学べる**AWSアーキテクチャ図解シミュレータ**を標準装備。暗記にとどまらない本質的なクラウド設計の知識が身につきます。

### 🚀 主な機能
- **CLF-C02 最新シラバス完全準拠30問**: 4大ドメイン（クラウドの概念、セキュリティ＆コンプライアンス、テクノロジー＆サービス、請求＆料金）
- **視覚的ASCII構成図**: 各問題にネットワーク・サービス関係性を表すターミナル風ダイアグラムを掲載
- **⚡ AWSアーキテクチャ図解シミュレータ**: 3大代表構成をタップしてコンポーネントの役割・試験頻出ポイントを視覚的学習
- **主要サービス逆引きチートシート**: 代表的CLIコマンド付・ワンタップコピー機能
- **日英バイリンガル対応**: ワンタップで日本語・英語をシームレス切替
- **学習サポート機能**: 弱点克服モード、ブックマーク機能、DataStore進捗永続化
- **完全オフライン対応 ＆ 広告なし**: 通信環境なしでサクサク学習可能

---

## 🏗️ 技術スタック (Tech Stack)

- **言語**: Kotlin 2.0.21
- **UI**: Jetpack Compose + Material 3
- **アーキテクチャ**: MVVM + Repository Pattern
- **永続化**: Jetpack DataStore Preferences
- **広告**: Google Mobile Ads (AdMob) SDK (Adaptive Banner) / 姉妹アプリ送客
- **ビルドツール**: Gradle 8.13 + AGP 8.8.x
- **署名 & 難読化**: R8 ProGuard + V1/V2 Release Keystore

---

## 📁 ディレクトリ構成 (Structure)

```
024_aws-clf-drill/
├── app/
│   ├── src/main/java/com/kawanova/awsclfdrill/
│   │   ├── data/                  # Question data (30 Qs) & CheatSheet & DataStore
│   │   ├── ui/                    # Screens & ViewModel & Theme
│   │   │   ├── components/        # TerminalCard, AdaptiveBannerAd, SisterAppsBanner
│   │   │   ├── navigation/        # Compose Navigation
│   │   │   └── theme/             # AWS Orange & Midnight Slate Palette
│   │   └── MainActivity.kt
│   └── src/test/                  # Unit tests
├── doc/
│   └── app_spec.md                # 包括的アプリ仕様書
├── store_assets/play/             # Google Play ストア提出用アセット
│   ├── app_icon_512.png           # 512x512 高解像度アプリアイコン
│   ├── feature_graphic_1024x500.png # 1024x500 フィーチャー画像
│   ├── screenshot_01..04.png      # 1080x2400 スクリーンショット4枚
│   ├── listing_ja.md              # 日本語ストア掲載文
│   ├── listing_en.md              # 英語ストア掲載文
│   ├── release_notes.md           # リリースノート
│   └── data_safety.yml            # データセーフティ宣言
├── generate_icons.py              # アプリアイコン・mipmap生成スクリプト
├── generate_feature_graphic.py    # フィーチャーグラフィック生成スクリプト
└── generate_screenshots.py        # Playストア用実機風スクリーンショット生成
```

---

## 📱 姉妹アプリシリーズ
- [021_docker-drill](https://github.com/KawaNova/docker-drill-mastery) - Docker 実践特訓
- [022_network-drill](https://github.com/KawaNova/network-drill-mastery) - ネットワーク基礎特訓
- [023_regex-drill](https://github.com/KawaNova/regex-drill-mastery) - 正規表現超入門
- [015_fe-drill](https://github.com/KawaNova/fe-drill-mastery) - 基本情報技術者 科目A特訓
