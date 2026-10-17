# アプリケーション仕様書 (app_spec.md)
# AWS クラウド超入門 - CLF-C02 突破 ＆ 構成図シミュレータ

- **ドキュメントバージョン**: 1.0.0
- **作成日**: 2026-10-17
- **プロジェクトディレクトリ**: `024_aws-clf-drill`
- **対象プラットフォーム**: Android (Jetpack Compose)
- **GitHub リポジトリ**: [KawaNova/aws-clf-drill-mastery](https://github.com/KawaNova/aws-clf-drill-mastery)

---

## 1. アプリ基本情報

| 項目 | 設定値 / 内容 |
| :--- | :--- |
| **アプリ正式名称 (JA)** | AWS クラウド超入門 - 特訓ドリル |
| **アプリ正式名称 (EN)** | AWS Drill - CLF-C02 Exam Prep |
| **パッケージ名** | `com.kawanova.awsclfdrill` (デバッグ: `.debug`) |
| **バージョン** | Version 1.0.0 (versionCode: 1) |
| **最小SDK (minSdk)** | API 24 (Android 7.0 Nougat) |
| **ターゲットSDK (targetSdk)** | API 36 (Android 15+) |
| **開発言語** | Kotlin 2.0.21 |
| **UIフレームワーク** | Jetpack Compose (Material Design 3) |
| **データ永続化** | Jetpack DataStore Preferences + kotlinx.serialization |
| **広告・収益化** | Google Mobile Ads (AdMob) SDK + 姉妹アプリ相互送客 |

---

## 2. 開発背景と提供価値 (Value Proposition)

### 2.1 ターゲットユーザーの課題
- AWS Certified Cloud Practitioner (CLF-C02) 受験者（エンジニア、ITコンサルタント、営業・企画職など）が、多岐にわたるサービス名や概念の暗記に苦戦している。
- 「責任共有モデルにおける顧客責任 vs AWS責任」「Well-Architected 6大柱」「Multi-AZとリードレプリカの使い分け」「各サポートプラン（Developer/Business/Enterprise）の違い」など、試験頻出のひっかけ問題で失点しやすい。
- 書籍やWebの文字解説だけでは、クラウド全体のアーキテクチャやサービス間の連携（Route 53 -> ALB -> EC2 -> Aurora）のイメージが湧きにくい。

### 2.2 本アプリが提供する3大価値
1. **⚡ インタラクティブ！AWSアーキテクチャ図解シミュレータ**:
   3層Web高可用性、サーバーレスAPI、セキュアVPCの代表的クラウド構成をスマホ上で視覚的に操作可能。各サービスノードをタップして、役割や試験頻出のツボを直感的に学習できる。
2. **🧩 全問ASCIIアーキテクチャ図解 ＆ 合格のツボ (Exam Tip)**:
   全30問にターミナル風ダイアグラムを付与。全選択肢の詳細解説に加え、本番試験の引っかけを見破る「合格のツボ」を徹底解説。
3. **📋 実務・直前総復習用 AWS 主要サービス逆引きチートシート**:
   EC2, Lambda, S3, RDS, IAM, VPC などの仕様概要と実務必須の代表的AWS CLIコマンドを網羅。ワンタップでクリップボードにコピー可能。

---

## 3. システムアーキテクチャ

```mermaid
flowchart TD
    UI[UI Layer: Jetpack Compose] --> VM[ViewModel: AwsViewModel]
    VM --> Repo[Repository: UserProgressRepository]
    VM --> QData[Data: AwsQuestionsData (30 Questions)]
    VM --> CSData[Data: CheatSheetData (24 Services)]
    Repo --> DataStore[Jetpack DataStore Preferences]
    
    subgraph Screens
        Home[HomeScreen]
        Quiz[QuizScreen]
        Sim[ArchitectureViewerScreen]
        Cheat[CheatSheetScreen]
    end
    UI -.-> Screens
```

---

## 4. 画面・機能仕様

### 4.1 ホーム画面 (`HomeScreen.kt`)
- **学習ステータスサマリー**: 進捗率（%）、正答率（%）、ブックマーク件数をグラフィカルに表示。
- **アーキテクチャシミュレータバナー**: ワンタップで構成図ビューアへ遷移。
- **クイック演習モード**:
  - 全30問 総特訓（全ドメインマラソン）
  - 弱点克服モード（誤答問題のみ出題）
  - ランダム10問モード（スキマ時間の特訓）
  - ブックマーク演習（保存した問題のみ）
- **4大ドメイン集中ドリル**:
  - ☁️ クラウドの概念 (Cloud Concepts) - 8問
  - 🛡️ セキュリティとコンプライアンス - 7問
  - ⚙️ テクノロジー & クラウドサービス - 9問
  - 💰 請求、料金、およびサポート - 6問
- **姉妹アプリ相互送客バナー**: Docker特訓、ネットワーク特訓、FE科目A、正規表現などへのリンク。

### 4.2 特訓クイズ画面 (`QuizScreen.kt`)
- 問題番号、カテゴリバッジ、ブックマークトグル。
- 問題文 ＆ 視覚的ASCIIアーキテクチャ構成図。
- 4択選択肢（即時正誤判定、選択肢タップでアニメーション）。
- 正解・全肢解説・「合格のツボ (Exam Tip)」表示。
- 次の問題へ進むナビゲーション。

### 4.3 AWSアーキテクチャ図解シミュレータ (`ArchitectureViewerScreen.kt`)
- シナリオ切替チップ:
  - 「3層Web高可用性（ALB + Auto Scaling EC2 + Multi-AZ Aurora + S3）」
  - 「サーバーレスAPI（Route 53 + API Gateway + Lambda + DynamoDB）」
  - 「セキュアVPC構成（IGW + Public/Private Subnet + NAT Gateway）」
- インタラクティブなコンポーネント選択:
  - 選択したサービスの役割、主要機能、試験対策のツボ（CLF-C02頻出キーワード）を下部カードに詳細展開。

### 4.4 サービス逆引きチートシート (`CheatSheetScreen.kt`)
- リアルタイム検索バー（サービス名・キーワード・コマンドで即座に絞り込み）。
- カテゴリタブ（コンピュート、ストレージ、ネットワーク、セキュリティ、データベース、運用管理）。
- CLIコマンドワンタップコピー機能。

---

## 5. デザインシステム

| トークン | カラーコード | 用途 |
| :--- | :--- | :--- |
| Primary (AWS Orange) | `#FF9900` | ブランドアクセント、メインボタン、選択状態 |
| Secondary (AWS Orange Dark) | `#EA580C` | グラデーション、バナー背景 |
| Accent Gold | `#FBBF24` | ブックマーク、重要ハイライト |
| Dark Background | `#0F172A` | Slate 900 アプリ全体背景 |
| Card Surface | `#1E293B` | Slate 800 カード背景 |
| Card Border | `#334155` | Slate 700 カード境界線 |
| Terminal Dark | `#090D16` | ASCIIダイアグラム・コード背景 |
| Success Green | `#10B981` | 正解・高正答率インジケータ |

---

## 6. リリース検証基準
1. `assembleDebug` および `bundleRelease` のビルドが成功すること。
2. 全30問の日本語および英語テキスト、解説、合格のツボが正しくレンダリングされること。
3. アーキテクチャシミュレータの全3シナリオおよびコンポーネント選択がスムーズに動作すること。
4. DataStoreによる学習進捗（回答履歴・ブックマーク・言語設定）が正しく永続化されること。
5. Google Play ストア提出用アセット（アイコン512、フィーチャー画像1024x500、スクリーンショット4枚、ストア掲載文ja/en）が完備されていること。
