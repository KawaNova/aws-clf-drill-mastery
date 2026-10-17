import os

out_path = r"c:\Users\Kawamoto\Documents\AgentAIDev\mobile-apps\024_aws-clf-drill\app\src\main\java\com\kawanova\awsclfdrill\data\AwsQuestionsData.kt"

content = """package com.kawanova.awsclfdrill.data

object AwsQuestionsData {
    val questions: List<AwsQuestion> = listOf(
        // ==========================================
        // 1. クラウドの概念 (Cloud Concepts) Q1..Q7
        // ==========================================
        AwsQuestion(
            id = 1,
            category = AwsCategory.CLOUD_CONCEPTS,
            titleJa = "クラウド移行における俊敏性 (Agility)",
            titleEn = "Cloud Agility and Speed to Market",
            scenarioJa = "スタートアップ企業が新しいモバイルアプリを立ち上げようとしています。物理ハードウェアの調達に数週間かけることなく、数分で開発環境を構築して市場への投入スピードを最大化したいと考えています。これはクラウドのどのメリットに該当しますか？",
            scenarioEn = "A startup wants to launch a mobile app quickly without waiting weeks for hardware procurement. Provisioning resources in minutes to maximize time-to-market represents which cloud benefit?",
            diagram = \"\"\"
+------------------------------------------------------+
| [従来オンプレミス]  調達・納品待ち (数週間〜数ヶ月)    |
| [AWSクラウド]       数クリックで即時起動 (数分) -> 俊敏性! |
+------------------------------------------------------+
\"\"\".trimIndent(),
            optionsJa = listOf(
                "弾力性 (Elasticity)",
                "俊敏性 (Agility)",
                "高可用性 (High Availability)",
                "耐障害性 (Fault Tolerance)"
            ),
            optionsEn = listOf(
                "Elasticity",
                "Agility",
                "High Availability",
                "Fault Tolerance"
            ),
            correctIndex = 1,
            explanationJa = "【正解: 俊敏性 (Agility)】\\n俊敏性とは、インフラを数分で即座にプロビジョニングし、試行錯誤と実験のサイクルを劇的に加速できる能力です。\\n・弾力性(Elasticity)は需要の増減に応じてリソースを自動拡縮する能力です。\\n・高可用性は障害時でもサービスを継続して利用可能にする能力です。",
            explanationEn = "[Correct: Agility]\\nAgility refers to the ability to rapidly provision tech resources in minutes, drastically accelerating experimentation and time-to-market.\\n- Elasticity is auto-scaling based on demand.\\n- High Availability ensures minimal downtime.",
            examTipJa = "試験頻出: 「数分でプロビジョニング」「イノベーション加速」「市場投入短縮」というキーワードが出たら『俊敏性 (Agility)』を選びます。",
            examTipEn = "Exam Tip: Keywords like 'provision in minutes', 'faster innovation', and 'speed to market' always point to Agility.",
            keyServices = listOf("AWS Cloud", "EC2", "CloudFormation")
        ),

        AwsQuestion(
            id = 2,
            category = AwsCategory.CLOUD_CONCEPTS,
            titleJa = "弾力性 (Elasticity) vs スケーラビリティ",
            titleEn = "Elasticity vs Scalability",
            scenarioJa = "Eコマースサイトがブラックフライデーセールの期間中のみトラフィックが急増し、セール終了後は平時のトラフィックに戻ります。需要の急増に合わせて自動でスケールアウトし、終了後にスケールインして無駄な費用を抑えるクラウドの特性はどれですか？",
            scenarioEn = "An e-commerce site experiences huge traffic spikes during Black Friday. Auto-scaling out during peak and scaling in after the event to prevent waste represents which cloud characteristic?",
            diagram = \"\"\"
[平時トラフィック]  ==> EC2 2台
[セール時急増!]     ==> EC2 10台に自動拡張 (Scale-out)
[セール終了後]      ==> EC2 2台に自動縮小 (Scale-in) => 弾力性!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "信頼性 (Reliability)",
                "弾力性 (Elasticity)",
                "グローバル展開 (Global Reach)",
                "耐障害性 (Fault Tolerance)"
            ),
            optionsEn = listOf(
                "Reliability",
                "Elasticity",
                "Global Reach",
                "Fault Tolerance"
            ),
            correctIndex = 1,
            explanationJa = "【正解: 弾力性 (Elasticity)】\\n弾力性とは、需要の変動に応じてリソースを自動的に拡張（スケールアウト）および縮小（スケールイン）させる能力です。需要が減ったときにリソースを解放してコストを最適化できる点がポイントです。",
            explanationEn = "[Correct: Elasticity]\\nElasticity is the ability to acquire resources as needed and release them when no longer required, matching supply directly with changing demand.",
            examTipJa = "試験頻出: 単に大きくなるだけでなく「需要が減ったら縮小してコスト削減する」という可逆的な伸縮性が『弾力性 (Elasticity)』の本質です。",
            examTipEn = "Exam Tip: Elasticity specifically emphasizes shrinking back down when demand drops to eliminate waste.",
            keyServices = listOf("Auto Scaling", "EC2", "Lambda")
        ),

        AwsQuestion(
            id = 3,
            category = AwsCategory.CLOUD_CONCEPTS,
            titleJa = "CapEx (設備投資) から OpEx (運用費) への転換",
            titleEn = "CapEx to OpEx Transformation",
            scenarioJa = "オンプレミス環境からAWSクラウドへ移行する最大の財務的メリットとして、事前に高額なデータセンター設備やサーバーを購入する必要がなくなる点が挙げられます。この財務モデルの転換を説明する用語はどれですか？",
            scenarioEn = "Moving from on-premises to AWS eliminates massive upfront investments in data centers and servers. What financial model shift describes this benefit?",
            diagram = \"\"\"
[オンプレミス] CapEx (固定費・事前投資) -> 莫大な初期費用
         |
         v (AWS移行)
[AWSクラウド]   OpEx (変動費・従量課金) -> 使った分だけ支払う
\"\"\".trimIndent(),
            optionsJa = listOf(
                "固定費 (CapEx) を変動費 (OpEx) に転換する",
                "変動費 (OpEx) を固定費 (CapEx) に転換する",
                "ライセンス費用を一括前払いする",
                "データセンターの不動産資産を計上する"
            ),
            optionsEn = listOf(
                "Trading capital expense (CapEx) for variable expense (OpEx)",
                "Trading variable expense (OpEx) for capital expense (CapEx)",
                "Paying software licenses completely upfront",
                "Capitalizing data center real estate assets"
            ),
            correctIndex = 0,
            explanationJa = "【正解: 固定費 (CapEx) を変動費 (OpEx) に転換する】\\nAWSの『クラウドの6大メリット』の1つです。事前にデータセンターや物理ハードに資本を投じる(CapEx)代わりに、実際に消費したコンピューティングリソースに対してのみ運用費(OpEx)として支払います。",
            explanationEn = "[Correct: Trading CapEx for OpEx]\\nOne of AWS's 6 Advantages of Cloud Computing. Instead of heavy upfront investment in hardware and facilities, you pay monthly operational expenses for only what you consume.",
            examTipJa = "試験頻出: 『Trade capital expense for variable expense (資本的支出を変動費に転換)』はAWS公式の基本原則として一言一句そのまま出題されます。",
            examTipEn = "Exam Tip: Memorize the exact phrasing: 'Trade capital expense for variable expense'.",
            keyServices = listOf("AWS Billing", "Cost Explorer")
        ),

        AwsQuestion(
            id = 4,
            category = AwsCategory.CLOUD_CONCEPTS,
            titleJa = "責任共有モデル (Shared Responsibility Model)",
            titleEn = "Shared Responsibility Model",
            scenarioJa = "AWSの責任共有モデルにおいて、顧客が責任を負う領域はどれですか？",
            scenarioEn = "Under the AWS Shared Responsibility Model, which component is the sole responsibility of the customer?",
            diagram = \"\"\"
+--------------------------------------------------------+
| 顧客の責任 (Security IN the Cloud):                     |
|  - 顧客データ、IAM認証・アクセス権、OSパッチ(EC2)、暗号化 |
+--------------------------------------------------------+
| AWSの責任 (Security OF the Cloud):                     |
|  - 物理データセンター、サーバーハードウェア、基盤仮想化 |
+--------------------------------------------------------+
\"\"\".trimIndent(),
            optionsJa = listOf(
                "データセンターの物理的入退室管理",
                "ホストOSおよび仮想化レイヤー (ハイパーバイザー) の管理",
                "EC2インスタンスのゲストOSへのパッチ適用とファイアウォール設定",
                "故障したハードディスクドライブの物理的廃棄"
            ),
            optionsEn = listOf(
                "Physical data center access control",
                "Host operating system and hypervisor maintenance",
                "Guest OS patching and firewall configuration on EC2",
                "Physical disposal of decommissioned hard drives"
            ),
            correctIndex = 2,
            explanationJa = "【正解: EC2インスタンスのゲストOSへのパッチ適用とファイアウォール設定】\\nAWSは「クラウド自体のセキュリティ（Security OF the Cloud: 物理設備、ハード、ハイパーバイザー）」を担い、顧客は「クラウド内のセキュリティ（Security IN the Cloud: ゲストOS、IAM、データ、ファイアウォール）」を担います。",
            explanationEn = "[Correct: Guest OS patching and firewall on EC2]\\nAWS is responsible for 'Security OF the Cloud' (hardware, facilities, virtualization). Customers are responsible for 'Security IN the Cloud' (guest OS, user data, IAM, security groups).",
            examTipJa = "試験頻出: 「EC2のゲストOS」は顧客責任ですが、「マネージドサービス（RDSやS3）」の基盤OSパッチはAWSの責任となります！この対比が頻出です。",
            examTipEn = "Exam Tip: EC2 guest OS = Customer responsibility. Managed RDS/S3 underlying OS = AWS responsibility.",
            keyServices = listOf("IAM", "EC2", "Security Groups")
        ),

        AwsQuestion(
            id = 5,
            category = AwsCategory.CLOUD_CONCEPTS,
            titleJa = "高可用性 (High Availability) とマルチAZ構成",
            titleEn = "High Availability and Multi-AZ Design",
            scenarioJa = "1つのデータセンターで停電や自然災害が発生しても、ダウンタイムなしにシステム全体を稼働させ続けたいと考えています。AWSのベストプラクティスに基づき、最も適切な構成はどれですか？",
            scenarioEn = "A company wants to ensure zero downtime even if a single data center suffers a major power outage. What AWS architecture best achieves High Availability?",
            diagram = \"\"\"
[リージョン (Region: 東京)]
  +--- [AZ-a (データセンター群)] : EC2 (Active) + RDS Primary
  |          ^ リアルタイム同期
  +--- [AZ-c (別データセンター群)] : EC2 (Standby) + RDS Standby
\"\"\".trimIndent(),
            optionsJa = listOf(
                "1つのアベイラビリティゾーン (AZ) 内に複数のEC2インスタンスを配置する",
                "複数のアベイラビリティゾーン (マルチAZ) にリソースを分散配置する",
                "単一のEC2インスタンスのスペックを最大まで垂直スケールする",
                "すべてのデータをオンプレミスの単一NASサーバーに同期する"
            ),
            optionsEn = listOf(
                "Deploy multiple instances within a single Availability Zone",
                "Deploy resources across multiple Availability Zones (Multi-AZ)",
                "Vertically scale a single EC2 instance to maximum CPU/RAM",
                "Sync all database writes to a single on-premises NAS"
            ),
            correctIndex = 1,
            explanationJa = "【正解: 複数のアベイラビリティゾーン (マルチAZ) にリソースを分散配置する】\\nアベイラビリティゾーン(AZ)は互いに地理的・電力的に独立した1つ以上のデータセンター群です。マルチAZ構成にすることで、1つのAZが壊滅しても別AZで処理を継続できます。",
            explanationEn = "[Correct: Deploy across multiple Availability Zones]\\nEach AZ consists of isolated data centers with independent power and networking. Deploying across multiple AZs provides fault tolerance and high availability.",
            examTipJa = "試験頻出: 『高可用性 (High Availability)』の正解は9割以上『マルチAZ (Multi-AZ)』がキーワードになります。",
            examTipEn = "Exam Tip: Whenever High Availability is mentioned, look for 'Multi-AZ' in the options.",
            keyServices = listOf("VPC", "Multi-AZ RDS", "ALB")
        ),

        AwsQuestion(
            id = 6,
            category = AwsCategory.CLOUD_CONCEPTS,
            titleJa = "AWSグローバルインフラストラクチャ",
            titleEn = "AWS Global Infrastructure Components",
            scenarioJa = "世界中のユーザーに対して低レイテンシでコンテンツを配信するために、Amazon CloudFrontなどのサービスがキャッシュデータを保持する拠点として利用されるインフラストラクチャコンポーネントはどれですか？",
            scenarioEn = "Which AWS infrastructure component is used by Amazon CloudFront to cache content closer to worldwide users to minimize latency?",
            diagram = \"\"\"
[オリジン (東京リージョン S3)]
       |  (CloudFront配信)
       +---> [エッジロケーション: ニューヨーク] -> 現地ユーザーへ即座に配信!
       +---> [エッジロケーション: ロンドン]
       +---> [エッジロケーション: シドニー]
\"\"\".trimIndent(),
            optionsJa = listOf(
                "アベイラビリティゾーン (AZ)",
                "エッジロケーション (Edge Location)",
                "リージョン (Region)",
                "VPCエンドポイント"
            ),
            optionsEn = listOf(
                "Availability Zone",
                "Edge Location",
                "Region",
                "VPC Endpoint"
            ),
            correctIndex = 1,
            explanationJa = "【正解: エッジロケーション (Edge Location)】\\nエッジロケーションは世界中の大都市に何百箇所も配置されたAWSの配信拠点です。Amazon CloudFront (CDN) や Route 53、AWS Shieldが活用し、ユーザーに最も近い場所からコンテンツを低レイテンシで配信します。",
            explanationEn = "[Correct: Edge Location]\\nEdge Locations are global endpoints deployed worldwide to cache content locally via Amazon CloudFront, Route 53, and AWS Global Accelerator.",
            examTipJa = "試験頻出: 「CloudFront」「低遅延」「キャッシュ」と来たら『エッジロケーション』。「独立したデータセンター群」と来たら『アベイラビリティゾーン』。",
            examTipEn = "Exam Tip: CloudFront + caching closer to users = Edge Location. Redundant data centers in a region = Availability Zone.",
            keyServices = listOf("CloudFront", "Route 53", "AWS Shield")
        ),

        AwsQuestion(
            id = 7,
            category = AwsCategory.CLOUD_CONCEPTS,
            titleJa = "規模の経済によるコスト削減 (Economies of Scale)",
            titleEn = "Massive Economies of Scale",
            scenarioJa = "AWSは世界中で数十万以上もの顧客のリソース利用を集約することで、より安い調達価格を実現し、そのコスト削減分を定期的な値下げとして顧客へ還元しています。このクラウドのメリットはどれですか？",
            scenarioEn = "Aggregating usage from hundreds of thousands of customers allows AWS to achieve higher economies of scale and pass savings back to users as lower pay-as-you-go prices. Which advantage is this?",
            diagram = \"\"\"
[数十万社の利用集約] => 超大量一括購買 => 運用コスト激減 => 定期値下げ還元
\"\"\".trimIndent(),
            optionsJa = listOf(
                "巨大な規模の経済による恩恵 (Benefit from massive economies of scale)",
                "キャパシティの当て推量を排除 (Stop guessing capacity)",
                "数分でグローバル展開 (Go global in minutes)",
                "俊敏性の向上 (Increase agility)"
            ),
            optionsEn = listOf(
                "Benefit from massive economies of scale",
                "Stop guessing capacity",
                "Go global in minutes",
                "Increase speed and agility"
            ),
            correctIndex = 0,
            explanationJa = "【正解: 巨大な規模の経済による恩恵】\\nAWSクラウドの6大メリットの1つです。単一企業では達成不可能な規模で購買・投資を行うため、個々の顧客は自社でデータセンターを構築するよりもはるかに安価に利用できます。",
            explanationEn = "[Correct: Benefit from massive economies of scale]\\nBy aggregating hundreds of thousands of customers in the cloud, AWS achieves higher economies of scale, resulting in lower prices.",
            examTipJa = "試験頻出: 『クラウドの6大メリット』の英文名（Economies of scale, Stop guessing capacity, Go global in minutes等）は丸暗記必須です。",
            examTipEn = "Exam Tip: Memorize all 6 official AWS Cloud Advantages by name.",
            keyServices = listOf("AWS Pricing", "AWS Architecture")
        ),

        // ==========================================
        // 2. セキュリティ & コンプライアンス Q8..Q15
        // ==========================================
        AwsQuestion(
            id = 8,
            category = AwsCategory.SECURITY_COMPLIANCE,
            titleJa = "ルートユーザーの保護と最小権限の原則",
            titleEn = "Root User Protection & Principle of Least Privilege",
            scenarioJa = "AWSアカウントを開設した直後に行うべきセキュリティのベストプラクティスとして、最も適切なものはどれですか？",
            scenarioEn = "Which action represents the absolute security best practice immediately after creating a new AWS account?",
            diagram = \"\"\"
[AWSルートアカウント] -> 危険! 全権限を保有
   |
   +---> ① 多要素認証 (MFA) を有効化!
   +---> ② アクセスキーを削除 (作成しない)
   +---> ③ 日常作業用の個別のIAMユーザーを作成し、最小権限を付与!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "ルートユーザーのアクセスキーを発行し、日常の管理作業で使用する",
                "ルートユーザーにMFAを設定し、日常業務には最小権限を付与したIAMユーザーを作成して使用する",
                "ルートユーザーのパスワードを他のチームメンバーと共有する",
                "セキュリティグループのすべてのインバウンドポート(0-65535)を0.0.0.0/0に開放する"
            ),
            optionsEn = listOf(
                "Generate root access keys and use them for daily administration",
                "Enable MFA on root, and create individual IAM users with least privilege for daily work",
                "Share root login credentials among lead DevOps team members",
                "Open all inbound security group ports to 0.0.0.0/0"
            ),
            correctIndex = 1,
            explanationJa = "【正解: ルートユーザーにMFAを設定し、日常業務にはIAMユーザーを作成して使用する】\\nルートユーザーはアカウントに対する無制限の権限を持つため、MFA(多要素認証)で強固に保護し、日常作業では一切使わず、必要な権限のみを持つ個別IAMユーザーまたはIAMロールを使います。",
            explanationEn = "[Correct: Enable MFA on root and use IAM users with least privilege]\\nRoot account has full unrestricted access. Never use root for daily tasks. Secure with MFA and delegate work to IAM users/roles.",
            examTipJa = "試験頻出: 「ルートユーザーのアクセスキーは削除する」「日常作業には使わない」「MFA必須」はセキュリティ分野の鉄板問題です。",
            examTipEn = "Exam Tip: Remember: Lock away root credentials, turn on MFA, and never use root for everyday administrative tasks.",
            keyServices = listOf("IAM", "MFA", "AWS Organizations")
        ),

        AwsQuestion(
            id = 9,
            category = AwsCategory.SECURITY_COMPLIANCE,
            titleJa = "IAMユーザー vs IAMロール (認証情報の委譲)",
            titleEn = "IAM Users vs IAM Roles",
            scenarioJa = "EC2インスタンス上で動作するアプリケーションが、Amazon S3バケットからデータを読み取る必要があります。長期的なアクセスキーをEC2内の設定ファイルに埋め込むことなく、安全にアクセス権を付与する方法はどれですか？",
            scenarioEn = "An application running on an EC2 instance needs to read files from an Amazon S3 bucket without hardcoding long-term access keys. What is the AWS best practice?",
            diagram = \"\"\"
[EC2インスタンス]
       |
       +---> [IAMロールをアタッチ] (一時的なセキュリティトークンを自動発行)
                   |
                   v 許可
             [Amazon S3 バケット]
\"\"\".trimIndent(),
            optionsJa = listOf(
                "S3の全権限を持つIAMユーザーのアクセスキーをアプリのコードに直接記載する",
                "S3読み取り権限を付与した『IAMロール』を作成し、EC2インスタンスにアタッチする",
                "S3バケットを全インターネット公開 (Public Read) に変更する",
                "ルートユーザーの認証情報をEC2の環境変数にエクスポートする"
            ),
            optionsEn = listOf(
                "Embed permanent IAM user access keys into application source code",
                "Create an IAM Role with S3 read permissions and attach it to the EC2 instance",
                "Make the S3 bucket fully public to allow anonymous reading",
                "Store root credentials inside the EC2 system environment variables"
            ),
            correctIndex = 1,
            explanationJa = "【正解: IAMロールをEC2インスタンスにアタッチする】\\nIAMロールは、AWSリソース（EC2やLambdaなど）に一時的な認証情報（STSトークン）を自動で提供する仕組みです。永続的なアクセスキーを保持する必要がないため、極めて安全です。",
            explanationEn = "[Correct: Create an IAM Role and attach to EC2]\\nIAM roles supply temporary security credentials automatically without storing long-term secret keys on instances.",
            examTipJa = "試験頻出: 「EC2やLambda等のサービスに権限を与える」「アクセスキーの埋め込み防止」「一時的な認証情報」と来たら答えは『IAMロール』です。",
            examTipEn = "Exam Tip: AWS resources accessing other AWS resources without hardcoded keys = IAM Role.",
            keyServices = listOf("IAM Role", "EC2", "S3", "AWS STS")
        ),

        AwsQuestion(
            id = 10,
            category = AwsCategory.SECURITY_COMPLIANCE,
            titleJa = "セキュリティグループ vs ネットワークACL",
            titleEn = "Security Groups vs Network ACLs",
            scenarioJa = "Amazon VPCにおけるセキュリティグループ (Security Group) の特性として正しいものはどれですか？",
            scenarioEn = "Which of the following correctly describes a fundamental characteristic of Amazon VPC Security Groups?",
            diagram = \"\"\"
[セキュリティグループ (SG)] = インスタンス単位 / ステートフル (許可した戻り通信は自動許可)
[ネットワークACL (NACL)]     = サブネット単位 / ステートレス (戻り通信も明示許可が必要)
\"\"\".trimIndent(),
            optionsJa = listOf(
                "サブネット単位で動作し、ステートレスである",
                "インスタンス単位で動作し、ステートフル（戻りの通信は自動的に許可される）である",
                "デフォルトで拒否ルール (Deny) を個別に定義できる",
                "物理ルーターのポート設定を行うハードウェア機能である"
            ),
            optionsEn = listOf(
                "Operates at the subnet level and is stateless",
                "Operates at the instance level and is stateful (return traffic is automatically allowed)",
                "Allows explicit Deny rules to be defined by default",
                "Is a physical hardware configuration applied to physical switches"
            ),
            correctIndex = 1,
            explanationJa = "【正解: インスタンス単位で動作し、ステートフルである】\\nセキュリティグループは仮想ファイアウォールとしてインスタンス単位で適用され、「ステートフル」です（インバウンドで許可された通信の応答は、アウトバウンドルールに関わらず自動で通過できます）。また、許可(Allow)ルールのみ定義可能です。",
            explanationEn = "[Correct: Instance level and stateful]\\nSecurity groups act as a virtual firewall for your EC2 instances. They are stateful, meaning responses to allowed inbound requests are automatically permitted out.",
            examTipJa = "試験頻出: 『SG = インスタンス単位 / ステートフル / Allowのみ』 vs 『NACL = サブネット単位 / ステートレス / AllowとDeny両方可』。この対比表は100%出題されます。",
            examTipEn = "Exam Tip: Security Group = Stateful / Instance-level. Network ACL = Stateless / Subnet-level.",
            keyServices = listOf("VPC", "Security Groups", "NACL")
        ),

        AwsQuestion(
            id = 11,
            category = AwsCategory.SECURITY_COMPLIANCE,
            titleJa = "AWS WAF vs AWS Shield (Web防御とDDoS防御)",
            titleEn = "AWS WAF vs AWS Shield",
            scenarioJa = "Webサイトに対するSQLインジェクションやクロスサイトスクリプティング (XSS) などのレイヤー7 (アプリケーション層) の悪意ある攻撃をブロックするために最適なサービスはどれですか？",
            scenarioEn = "Which AWS service is specifically designed to protect web applications from common Layer 7 vulnerabilities such as SQL injection and Cross-Site Scripting (XSS)?",
            diagram = \"\"\"
[悪意あるリクエスト (SQLインジェクション/XSS)]
             |
             v
      [ AWS WAF ]  <-- レイヤー7 (HTTP/HTTPS) 検査 & ブロック!
             |
             v (正常な通信のみ通過)
   [ ALB / CloudFront ]
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Shield Standard",
                "AWS WAF (Web Application Firewall)",
                "Amazon GuardDuty",
                "AWS KMS"
            ),
            optionsEn = listOf(
                "AWS Shield Standard",
                "AWS WAF (Web Application Firewall)",
                "Amazon GuardDuty",
                "AWS KMS"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS WAF (Web Application Firewall)】\\nAWS WAFはレイヤー7(HTTP/HTTPS)を監視し、SQLインジェクションやXSS、レートリミットなどのカスタムルールで悪意あるWebリクエストを遮断します。AWS ShieldはDDoS攻撃（レイヤー3/4/7）の防御に特化しています。",
            explanationEn = "[Correct: AWS WAF]\\nAWS WAF is a web application firewall that monitors HTTP/HTTPS requests forwarded to Amazon CloudFront, ALB, or API Gateway, protecting against SQL injection and XSS.",
            examTipJa = "試験頻出: 「SQLインジェクション」「XSS」「レイヤー7」と来たら『AWS WAF』。「DDoS攻撃」「SYNフラッド」「UDPリフレクション」と来たら『AWS Shield』です。",
            examTipEn = "Exam Tip: SQL injection / XSS = AWS WAF. DDoS attacks = AWS Shield.",
            keyServices = listOf("AWS WAF", "AWS Shield", "CloudFront", "ALB")
        ),

        AwsQuestion(
            id = 12,
            category = AwsCategory.SECURITY_COMPLIANCE,
            titleJa = "AWS KMS (Key Management Service)",
            titleEn = "AWS KMS (Key Management Service)",
            scenarioJa = "S3バケット内のオブジェクトやEBSボリュームのデータを保管時に暗号化 (Encryption at Rest) するために、暗号化キーを安全に作成・管理できるフルマネージドサービスはどれですか？",
            scenarioEn = "Which managed service allows you to easily create and control cryptographic keys used to encrypt data at rest across AWS services like S3 and EBS?",
            diagram = \"\"\"
[顧客データ] ---> [ AWS KMS (暗号化キー管理) ] ---> 暗号化済みデータ (S3 / EBS)
                        ^ 暗号化/復号の権限をIAMで制御
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS CloudHSM",
                "AWS KMS (Key Management Service)",
                "AWS Secrets Manager",
                "AWS Certificate Manager (ACM)"
            ),
            optionsEn = listOf(
                "AWS CloudHSM",
                "AWS KMS (Key Management Service)",
                "AWS Secrets Manager",
                "AWS Certificate Manager (ACM)"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS KMS (Key Management Service)】\\nAWS KMSはデータの暗号化に使用する暗号化キー（KMSキー）の作成・ローテーション・管理を行うマネージドサービスです。CloudHSMはFIPS 140-2 レベル3準拠の専用ハードウェアアプライアンスを自社専用で占有するサービスです。",
            explanationEn = "[Correct: AWS KMS]\\nAWS Key Management Service (AWS KMS) makes it easy to create and manage cryptographic keys and control their use across a wide range of AWS services.",
            examTipJa = "試験頻出: 「キー管理のマネージドサービス」は『AWS KMS』。「SSL/TLSサーバー証明書の管理」は『ACM』。「パスワードやAPIキーの定期ローテーション」は『Secrets Manager』。",
            examTipEn = "Exam Tip: Encryption keys = KMS. SSL/TLS certificates = ACM. Database passwords = Secrets Manager.",
            keyServices = listOf("AWS KMS", "S3", "EBS")
        ),

        AwsQuestion(
            id = 13,
            category = AwsCategory.SECURITY_COMPLIANCE,
            titleJa = "Amazon GuardDuty (インテリジェント脅威検出)",
            titleEn = "Amazon GuardDuty (Intelligent Threat Detection)",
            scenarioJa = "VPCフローログ、DNSログ、CloudTrailイベントログを機械学習を用いて継続的に分析し、不正な暗号資産マイニングや不審なAPIコールなどの脅威を自動検出するセキュリティサービスはどれですか？",
            scenarioEn = "Which security service uses machine learning to continuously analyze VPC Flow Logs, DNS logs, and CloudTrail events to detect unauthorized cryptocurrency mining and suspicious API behavior?",
            diagram = \"\"\"
[VPCフローログ / DNSログ / CloudTrail]
                |
                v (機械学習による分析)
       [ Amazon GuardDuty ] ---> 異常検知アラート! (暗号資産マイニング・不審な通信)
\"\"\".trimIndent(),
            optionsJa = listOf(
                "Amazon Inspector",
                "Amazon GuardDuty",
                "Amazon Macie",
                "AWS Shield"
            ),
            optionsEn = listOf(
                "Amazon Inspector",
                "Amazon GuardDuty",
                "Amazon Macie",
                "AWS Shield"
            ),
            correctIndex = 1,
            explanationJa = "【正解: Amazon GuardDuty】\\nGuardDutyは、各種ログ（CloudTrail, VPC Flow Logs, DNSログなど）を機械学習で分析し、不正侵入やマイニングマルウェア感染などの脅威をインテリジェントに検知するサービスです。ワンクリックで有効化できます。",
            explanationEn = "[Correct: Amazon GuardDuty]\\nAmazon GuardDuty is an intelligent threat detection service that continuously monitors for malicious activity and unauthorized behavior using ML and integrated threat intelligence.",
            examTipJa = "試験頻出: 「脅威検知・機械学習・VPCログ分析」=『GuardDuty』。「EC2やコンテナの脆弱性診断」=『Inspector』。「S3内の個人情報(PII)検出」=『Macie』。",
            examTipEn = "Exam Tip: Threat detection = GuardDuty. Software vulnerability scanning = Inspector. Sensitive PII data discovery in S3 = Macie.",
            keyServices = listOf("GuardDuty", "CloudTrail", "VPC Flow Logs")
        ),

        AwsQuestion(
            id = 14,
            category = AwsCategory.SECURITY_COMPLIANCE,
            titleJa = "AWS Artifact (コンプライアンスレポート取得)",
            titleEn = "AWS Artifact (Compliance Reports On-Demand)",
            scenarioJa = "企業の監査役から、AWSインフラストラクチャがSOCレポートやPCI DSS、ISOなどのセキュリティ基準を満たしていることを証明するドキュメントの提出を求められました。これらの公式レポートをオンデマンドでダウンロードできるポータルはどれですか？",
            scenarioEn = "An auditor requests official proof that AWS infrastructure complies with SOC, PCI DSS, and ISO standards. Where can you download these compliance reports on demand?",
            diagram = \"\"\"
[監査役・セキュリティ担当]
         | (ダウンロード)
   [ AWS Artifact ] ---> SOC 1/2/3 レポート、ISO認証書、PCI DSS報告書
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Trust & Safety",
                "AWS Artifact",
                "AWS Trusted Advisor",
                "AWS Service Catalog"
            ),
            optionsEn = listOf(
                "AWS Trust & Safety",
                "AWS Artifact",
                "AWS Trusted Advisor",
                "AWS Service Catalog"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS Artifact】\\nAWS Artifactは、AWSのコンプライアンスドキュメント（SOCレポート、PCI報告書など）やAWSとの合意契約（BAAなど）をオンデマンドで無償取得できるセルフサービスポータルです。",
            explanationEn = "[Correct: AWS Artifact]\\nAWS Artifact is your go-to, central resource for compliance-related information, providing on-demand access to AWS security and compliance reports (SOC, PCI, ISO).",
            examTipJa = "試験頻出: 「SOCレポート」「コンプライアンス認証書」「監査」というキーワードが出たら即座に『AWS Artifact』を選びます。",
            examTipEn = "Exam Tip: When an auditor asks for AWS compliance certification or SOC reports, the answer is always AWS Artifact.",
            keyServices = listOf("AWS Artifact", "Compliance")
        ),

        AwsQuestion(
            id = 15,
            category = AwsCategory.SECURITY_COMPLIANCE,
            titleJa = "Amazon Inspector (脆弱性自動スキャン)",
            titleEn = "Amazon Inspector (Automated Vulnerability Management)",
            scenarioJa = "Amazon EC2インスタンスやAmazon ECR内のコンテナイメージに対して、ソフトウェアの既知の脆弱性(CVE)や意図しないネットワーク露出がないかを自動的にスキャンして評価するサービスはどれですか？",
            scenarioEn = "Which service automatedly scans Amazon EC2 instances and Amazon ECR container images for known software vulnerabilities (CVEs) and unintended network exposure?",
            diagram = \"\"\"
[EC2 インスタンス / ECR コンテナ]
                ^
                | (自動スキャン・脆弱性検出)
      [ Amazon Inspector ] ---> CVE脆弱性レポート & 修正優先度スコア
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Config",
                "Amazon Inspector",
                "AWS GuardDuty",
                "Amazon Detective"
            ),
            optionsEn = listOf(
                "AWS Config",
                "Amazon Inspector",
                "AWS GuardDuty",
                "Amazon Detective"
            ),
            correctIndex = 1,
            explanationJa = "【正解: Amazon Inspector】\\nAmazon Inspectorは、EC2やコンテナイメージのソフトウェア脆弱性と意図しないネットワーク露出を自動的かつ継続的に評価する脆弱性管理サービスです。",
            explanationEn = "[Correct: Amazon Inspector]\\nAmazon Inspector is an automated vulnerability management service that scans workloads across EC2 and container registries for software vulnerabilities and network exposure.",
            examTipJa = "試験頻出: GuardDutyが「外部からの攻撃・脅威検出」であるのに対し、Inspectorは「内部のOSパッケージの既知の脆弱性(CVE)スキャン」です。この違いが頻出です。",
            examTipEn = "Exam Tip: GuardDuty = Threat detection (behavioral). Inspector = Vulnerability assessment (CVE software scanning).",
            keyServices = listOf("Inspector", "EC2", "ECR")
        ),

        // ==========================================
        // 3. テクノロジー & サービス Q16..Q24
        // ==========================================
        AwsQuestion(
            id = 16,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "EC2購入オプションの使い分け",
            titleEn = "Amazon EC2 Pricing Models",
            scenarioJa = "ビッグデータのバッチ処理ジョブを実行したいと考えています。処理はいつでも中断・再開が可能で、耐障害性があります。コンピュートコストを最大90%割引で最も安く抑えたい場合、どの購入オプションが最適ですか？",
            scenarioEn = "You need to run a batch processing job that is fault-tolerant and can withstand unexpected interruptions. Which EC2 pricing model offers the deepest discount (up to 90%)?",
            diagram = \"\"\"
[オンデマンド]    定価 / いつでも開始・停止可能 (割引なし)
[Savings Plans]  1〜3年コミットで最大72%割引 (定常ワークロード用)
[スポット]       AWSの未使用キャパシティ / 中断あり / 最大90%割引!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "オンデマンドインスタンス (On-Demand Instances)",
                "スポットインスタンス (Spot Instances)",
                "リザーブドインスタンス (Reserved Instances)",
                "Dedicated Hosts (専用ホスト)"
            ),
            optionsEn = listOf(
                "On-Demand Instances",
                "Spot Instances",
                "Reserved Instances",
                "Dedicated Hosts"
            ),
            correctIndex = 1,
            explanationJa = "【正解: スポットインスタンス (Spot Instances)】\\nスポットインスタンスはAWSの余剰キャパシティを最大90%割引で利用できるオプションです。AWSから2分前に通知されて中断されるリスクがあるため、バッチ処理やステートレス処理など中断に強いワークロードに最適です。",
            explanationEn = "[Correct: Spot Instances]\\nSpot Instances let you take advantage of unused EC2 capacity at steep discounts (up to 90%). Ideal for fault-tolerant, flexible batch workloads.",
            examTipJa = "試験頻出: 「中断可能」「最大の割引率」「バッチ処理」=『スポットインスタンス』。「1年または3年の継続利用」「定常負荷」=『リザーブド/Savings Plans』。",
            examTipEn = "Exam Tip: Interruptible + maximum discount = Spot. Consistent 1-3 year baseline = Reserved / Savings Plans.",
            keyServices = listOf("EC2", "Spot Instances", "Savings Plans")
        ),

        AwsQuestion(
            id = 17,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "Amazon S3 ストレージクラスの選定",
            titleEn = "Amazon S3 Storage Classes",
            scenarioJa = "医療機関のレントゲン画像データを10年間保管する必要があります。データは規制要件のために保持するだけで、年に1回参照されるかどうかであり、取り出しには数時間の待機が許容されます。最もコスト効率の良いS3ストレージクラスはどれですか？",
            scenarioEn = "Medical records must be archived for 10 years for compliance. They are rarely accessed (less than once a year) and retrieval time of several hours is acceptable. Which S3 storage class is most cost-effective?",
            diagram = \"\"\"
[S3 Standard]           頻繁アクセス / 最も高速
[S3 Standard-IA]        低頻度アクセス (月1回程度) / 即時取り出し
[S3 Glacier Flexible]   アーカイブ / 数分〜数時間
[S3 Glacier Deep Archive] 最安アーカイブ / 取り出し12時間以内 / GBあたり超激安!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "Amazon S3 Standard",
                "Amazon S3 Intelligent-Tiering",
                "Amazon S3 Standard-IA",
                "Amazon S3 Glacier Deep Archive"
            ),
            optionsEn = listOf(
                "Amazon S3 Standard",
                "Amazon S3 Intelligent-Tiering",
                "Amazon S3 Standard-IA",
                "Amazon S3 Glacier Deep Archive"
            ),
            correctIndex = 3,
            explanationJa = "【正解: Amazon S3 Glacier Deep Archive】\\nGlacier Deep ArchiveはAWSの中で最も低コストなストレージクラスです。年に1〜2回しかアクセスせず、数時間（12時間以内）の取り出し時間が許容される長期保管・コンプライアンスアーカイブに最適です。",
            explanationEn = "[Correct: S3 Glacier Deep Archive]\\nS3 Glacier Deep Archive is Amazon S3's lowest-cost storage tier for long-term retention where data is accessed once or twice a year and 12-hour retrieval is acceptable.",
            examTipJa = "試験頻出: 「最も安価なアーカイブ」「年に数回」「数時間〜12時間の取得」=『Glacier Deep Archive』。「アクセス頻度が予測不能で自動最適化」=『S3 Intelligent-Tiering』。",
            examTipEn = "Exam Tip: Lowest storage cost for archival = Glacier Deep Archive. Unknown or changing access patterns = Intelligent-Tiering.",
            keyServices = listOf("Amazon S3", "Glacier Deep Archive")
        ),

        AwsQuestion(
            id = 18,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "データベース選定: RDS vs DynamoDB",
            titleEn = "Database Selection: RDS vs DynamoDB",
            scenarioJa = "ゲームのユーザーランキング情報を管理するために、1桁ミリ秒の応答速度で大量のKey-Value読み書きを処理できる、完全マネージドなサーバーレスNoSQLデータベースが必要です。最適なサービスはどれですか？",
            scenarioEn = "A gaming app requires a fully managed serverless NoSQL database capable of single-digit millisecond latency at any scale for user leaderboard key-value queries. Which service should you choose?",
            diagram = \"\"\"
[Amazon RDS]      リレーショナル (SQL, テーブル結合, トランザクション)
[Amazon DynamoDB] NoSQL (Key-Value / ドキュメント, 1桁ミリ秒, サーバーレス, スケーラブル)
\"\"\".trimIndent(),
            optionsJa = listOf(
                "Amazon RDS (MySQL)",
                "Amazon DynamoDB",
                "Amazon Redshift",
                "Amazon DocumentDB"
            ),
            optionsEn = listOf(
                "Amazon RDS (MySQL)",
                "Amazon DynamoDB",
                "Amazon Redshift",
                "Amazon DocumentDB"
            ),
            correctIndex = 1,
            explanationJa = "【正解: Amazon DynamoDB】\\nDynamoDBは、規模に関係なく1桁ミリ秒単位のパフォーマンスを提供するフルマネージドなNoSQL（Key-Valueおよびドキュメント）データベースです。サーバーレスで自動的にスケールします。",
            explanationEn = "[Correct: Amazon DynamoDB]\\nAmazon DynamoDB is a fast and flexible NoSQL database service for single-digit millisecond performance at any scale. It is fully managed and serverless.",
            examTipJa = "試験頻出: 「NoSQL」「Key-Value」「1桁ミリ秒」=『DynamoDB』。「リレーショナル/SQL/結合」=『RDS / Aurora』。「データウェアハウス/ペタバイト分析」=『Redshift』。",
            examTipEn = "Exam Tip: NoSQL + single-digit ms = DynamoDB. Relational / SQL = RDS / Aurora. Data warehousing / analytics = Redshift.",
            keyServices = listOf("DynamoDB", "RDS", "NoSQL")
        ),

        AwsQuestion(
            id = 19,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "Amazon VPC ネットワークの構成要素",
            titleEn = "Amazon VPC Networking Components",
            scenarioJa = "プライベートサブネット内にあるデータベースサーバーなどのEC2インスタンスが、OSのセキュリティパッチをダウンロードするためにインターネットへ発信通信を行う必要があります。ただし、インターネット側からの直接のインバウンド接続は拒否したいと考えています。どのコンポーネントを配置すべきですか？",
            scenarioEn = "EC2 instances in a private subnet need outbound internet access to download security patches, but must prevent external internet clients from initiating inbound connections. What component is required?",
            diagram = \"\"\"
[インターネット]
       ^ (外への発信のみ許可)
       |
[Internet Gateway (IGW)]
       |
[パブリックサブネット: NAT Gateway] <---+
                                       | (パッチ取得リクエスト)
[プライベートサブネット: EC2/DB] --------+ (直接のインバウンドは遮断!)
\"\"\".trimIndent(),
            optionsJa = listOf(
                "Internet Gateway (インターネットゲートウェイ)",
                "NAT Gateway (NATゲートウェイ)",
                "Virtual Private Gateway (VGW)",
                "VPC Peering (VPCピアリング)"
            ),
            optionsEn = listOf(
                "Internet Gateway",
                "NAT Gateway",
                "Virtual Private Gateway",
                "VPC Peering"
            ),
            correctIndex = 1,
            explanationJa = "【正解: NAT Gateway (NATゲートウェイ)】\\nNAT Gatewayをパブリックサブネットに配置することで、プライベートサブネット内のリソースからインターネットへの発信通信（IPv4）を可能にしつつ、外部からの直接アクセスを遮断できます。",
            explanationEn = "[Correct: NAT Gateway]\\nA NAT Gateway enables instances in a private subnet to connect to the internet or other AWS services, but prevents the internet from initiating a connection with those instances.",
            examTipJa = "試験頻出: 「プライベートサブネットからインターネットへ発信のみ許可」=『NAT Gateway』。「VPCとオンプレミスをVPN接続」=『Virtual Private Gateway (VGW)』。",
            examTipEn = "Exam Tip: Outbound-only internet access for private subnets = NAT Gateway. Dedicated direct connection = Direct Connect.",
            keyServices = listOf("VPC", "NAT Gateway", "Internet Gateway")
        ),

        AwsQuestion(
            id = 20,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "AWS Lambda (サーバーレスコンピューティング)",
            titleEn = "AWS Lambda Serverless Computing",
            scenarioJa = "S3に新しい画像がアップロードされた瞬間に、自動的にサムネイル画像を生成する処理を実行したいと考えています。サーバーのプロビジョニングやOSの管理を一切行わず、コードが実行されている時間だけ課金されるサーバーレスサービスはどれですか？",
            scenarioEn = "When images are uploaded to S3, thumbnails must be generated automatically. You want zero server management and only pay for the exact compute execution time. Which serverless service is designed for this?",
            diagram = \"\"\"
[ユーザー] ---> 画像アップロード ---> [ Amazon S3 ]
                                          |
                                          v (S3イベント発火)
                                  [ AWS Lambda ] (サーバー管理ゼロ / 実行時間だけミリ秒課金)
                                          |
                                          v サムネイル保存
                                    [ S3 Bucket ]
\"\"\".trimIndent(),
            optionsJa = listOf(
                "Amazon EC2",
                "AWS Lambda",
                "Amazon ECS",
                "AWS Elastic Beanstalk"
            ),
            optionsEn = listOf(
                "Amazon EC2",
                "AWS Lambda",
                "Amazon ECS",
                "AWS Elastic Beanstalk"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS Lambda】\\nAWS Lambdaはサーバーの管理なしにコードを実行できるサーバーレスコンピューティングサービスです。イベント駆動型で動作し、コードが実行されたミリ秒単位のコンピューティング時間のみ課金されます（最大実行時間は15分）。",
            explanationEn = "[Correct: AWS Lambda]\\nAWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume, with zero charge when code is not running.",
            examTipJa = "試験頻出: 「サーバーレス」「イベント駆動」「アイドル時コストゼロ」「最大実行時間15分」=『AWS Lambda』。",
            examTipEn = "Exam Tip: Serverless event-driven compute with 15-minute max execution = AWS Lambda.",
            keyServices = listOf("Lambda", "S3", "Serverless")
        ),

        AwsQuestion(
            id = 21,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "Amazon CloudFront (コンテンツ配信ネットワーク)",
            titleEn = "Amazon CloudFront (Global CDN)",
            scenarioJa = "静的Webサイトの画像や動画ファイルを、世界中のエンドユーザーに対して最も低いレイテンシと高い転送速度で配信するために利用すべきAWSサービスはどれですか？",
            scenarioEn = "Which service securely delivers videos, data, and applications to customers globally with low latency and high transfer speeds using a worldwide network of edge locations?",
            diagram = \"\"\"
[オリジン (S3 / ALB)]
         | (キャッシュ同期)
   [ Amazon CloudFront ] ===> 世界中のエッジロケーションから超高速配信!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "Amazon Route 53",
                "Amazon CloudFront",
                "AWS Direct Connect",
                "AWS Storage Gateway"
            ),
            optionsEn = listOf(
                "Amazon Route 53",
                "Amazon CloudFront",
                "AWS Direct Connect",
                "AWS Storage Gateway"
            ),
            correctIndex = 1,
            explanationJa = "【正解: Amazon CloudFront】\\nAmazon CloudFrontは世界中のエッジロケーション網を活用してコンテンツをキャッシュし、低遅延・高スループットで配信するコンテンツ配信ネットワーク(CDN)サービスです。DDoS緩和(Shield)やWAFとも統合されています。",
            explanationEn = "[Correct: Amazon CloudFront]\\nAmazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency.",
            examTipJa = "試験頻出: 「CDN」「低レイテンシ配信」「エッジロケーションでのキャッシュ」=『CloudFront』。「DNSサービス」=『Route 53』。",
            examTipEn = "Exam Tip: CDN caching across global edge network = Amazon CloudFront.",
            keyServices = listOf("CloudFront", "S3", "Edge Locations")
        ),

        AwsQuestion(
            id = 22,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "Amazon Route 53 (マネージドDNSサービス)",
            titleEn = "Amazon Route 53 Managed DNS",
            scenarioJa = "ドメイン名の登録、インターネットトラフィックのルーティング、およびリソースの稼働状況を監視して障害時に自動で正常なサーバーへ切り替えるヘルスチェック機能を備えたサービスはどれですか？",
            scenarioEn = "Which highly available and scalable cloud Domain Name System (DNS) web service provides domain registration, traffic routing, and health checking?",
            diagram = \"\"\"
[ユーザー: example.com]
         |
         v
  [ Amazon Route 53 ] ---> ヘルスチェック正常?
         |
         +--- 正常時 ---> [東京リージョン (Primary)]
         +--- 障害時 ---> [大阪リージョン (Failover)]
\"\"\".trimIndent(),
            optionsJa = listOf(
                "Amazon VPC",
                "Amazon Route 53",
                "AWS Direct Connect",
                "AWS Transit Gateway"
            ),
            optionsEn = listOf(
                "Amazon VPC",
                "Amazon Route 53",
                "AWS Direct Connect",
                "AWS Transit Gateway"
            ),
            correctIndex = 1,
            explanationJa = "【正解: Amazon Route 53】\\nRoute 53は可用性99.999%を誇るマネージドDNSサービスです。名前解決だけでなく、地理的ルーティング、レイテンシールーティング、フェイルオーバールーティングなどの高度なトラフィック制御が可能です。",
            explanationEn = "[Correct: Amazon Route 53]\\nAmazon Route 53 is a highly available Domain Name System (DNS) service designed to give developers an extremely reliable way to route end users to internet applications.",
            examTipJa = "試験頻出: ポート番号53（DNSの標準ポート）から名付けられています。「DNS」「ドメイン登録」「フェイルオーバー」=『Route 53』。",
            examTipEn = "Exam Tip: Port 53 = DNS. Route 53 manages DNS records, health checks, and global failover routing.",
            keyServices = listOf("Route 53", "DNS", "CloudFront")
        ),

        AwsQuestion(
            id = 23,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "ELB (Elastic Load Balancing) と Auto Scaling",
            titleEn = "Elastic Load Balancing & Auto Scaling",
            scenarioJa = "Webアプリケーションへのトラフィックを複数のアベイラビリティゾーンにある複数のEC2インスタンスへ均等に自動分散し、単一障害点を排除するためのサービスはどれですか？",
            scenarioEn = "Which service automatically distributes incoming application traffic across multiple targets, such as EC2 instances across multiple Availability Zones, to eliminate single points of failure?",
            diagram = \"\"\"
            [インターネット トラフィック]
                       |
                       v
    [ Elastic Load Balancing (ALB) ]
         |                       |
         v (AZ-a)                v (AZ-c)
    [ EC2 Web-1 ]           [ EC2 Web-2 ]
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Auto Scaling",
                "Elastic Load Balancing (ELB)",
                "Amazon CloudFront",
                "AWS Global Accelerator"
            ),
            optionsEn = listOf(
                "AWS Auto Scaling",
                "Elastic Load Balancing (ELB)",
                "Amazon CloudFront",
                "AWS Global Accelerator"
            ),
            correctIndex = 1,
            explanationJa = "【正解: Elastic Load Balancing (ELB)】\\nELBは受信トラフィックを複数のターゲット（EC2、コンテナ、IPアドレス）に自動で分散します。異常なインスタンスへのトラフィックを停止し、正常なインスタンスのみにルーティングします。",
            explanationEn = "[Correct: Elastic Load Balancing]\\nElastic Load Balancing (ELB) distributes incoming application traffic across multiple targets in one or more Availability Zones, enhancing application fault tolerance.",
            examTipJa = "試験頻出: 「トラフィックの分散」=『ELB』。「需要に応じたインスタンス台数の増減」=『Auto Scaling』。この2つはセットで高可用性を実現します。",
            examTipEn = "Exam Tip: Traffic distribution = ELB. Scaling server count based on CPU/traffic = Auto Scaling.",
            keyServices = listOf("ELB", "ALB", "Auto Scaling")
        ),

        AwsQuestion(
            id = 24,
            category = AwsCategory.TECHNOLOGY_SERVICES,
            titleJa = "Amazon SQS vs Amazon SNS (疎結合アーキテクチャ)",
            titleEn = "Amazon SQS vs Amazon SNS (Decoupling)",
            scenarioJa = "注文受付システムと発送処理システムの間でメッセージをバッファリングし、処理速度の違いによるシステムダウンを防ぐ疎結合(Decoupling)を実現したいと考えています。メッセージをキューに安全に保持するサービスはどれですか？",
            scenarioEn = "You need to buffer orders between a web store and an order processing worker pool to decouple the systems. Which service provides managed message queuing?",
            diagram = \"\"\"
[注文受付Web] ---> メッセージ送信 ---> [ Amazon SQS (キュー) ]
                                              | (プルして非同期処理)
                                              v
                                      [ 発送処理ワーカー (EC2) ]
\"\"\".trimIndent(),
            optionsJa = listOf(
                "Amazon SNS (Simple Notification Service)",
                "Amazon SQS (Simple Queue Service)",
                "Amazon SES (Simple Email Service)",
                "Amazon Kinesis Data Streams"
            ),
            optionsEn = listOf(
                "Amazon SNS",
                "Amazon SQS",
                "Amazon SES",
                "Amazon Kinesis Data Streams"
            ),
            correctIndex = 1,
            explanationJa = "【正解: Amazon SQS (Simple Queue Service)】\\nSQSは信頼性の高いメッセージキューイングサービスで、コンポーネント間を疎結合にしてバッファリングします。SNSはPub/Subモデルで複数の購読者にメッセージを同時配信(ファンアウト)するプッシュ型サービスです。",
            explanationEn = "[Correct: Amazon SQS]\\nAmazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.",
            examTipJa = "試験頻出: 『SQS = キューイング（プル型・バッファ・疎結合）』 vs 『SNS = Pub/Sub通知（プッシュ型・メール/SMS/ファンアウト）』。",
            examTipEn = "Exam Tip: SQS = Pull message queue for decoupling. SNS = Push pub/sub notification service.",
            keyServices = listOf("SQS", "SNS", "Decoupling")
        ),

        // ==========================================
        // 4. 請求・料金 & サポート Q25..Q30
        // ==========================================
        AwsQuestion(
            id = 25,
            category = AwsCategory.BILLING_PRICING,
            titleJa = "AWS Cost Explorer (コスト分析と将来予測)",
            titleEn = "AWS Cost Explorer",
            scenarioJa = "過去12ヶ月間のAWS利用料金の内訳をサービス別・タグ別にグラフで可視化し、さらに今後3ヶ月間の予想支出を機械学習で予測するために最適なツールはどれですか？",
            scenarioEn = "Which tool enables you to visualize, understand, and manage your AWS costs and usage over time, and forecast future spend for the next 3 months?",
            diagram = \"\"\"
[過去12ヶ月のコスト推移]  ======> サービス別・タグ別分析
[今後3ヶ月の予測]        ------> 予算計画 & 異常コスト検知 => Cost Explorer!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Budgets",
                "AWS Cost Explorer",
                "AWS Pricing Calculator",
                "AWS Billing Conductor"
            ),
            optionsEn = listOf(
                "AWS Budgets",
                "AWS Cost Explorer",
                "AWS Pricing Calculator",
                "AWS Billing Conductor"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS Cost Explorer】\\nAWS Cost Explorerは、時間経過に伴うAWSのコストと使用状況を表示・分析し、将来のコスト予測を行うことができる無料のビジュアルツールです。",
            explanationEn = "[Correct: AWS Cost Explorer]\\nAWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time, including 3-month forecasting.",
            examTipJa = "試験頻出: 「過去の支出の可視化・グラフ分析」「将来のコスト予測」=『Cost Explorer』。「しきい値超過アラート」=『AWS Budgets』。",
            examTipEn = "Exam Tip: Visualize historical spend + 3-month forecast = Cost Explorer. Set budget limits + alerts = AWS Budgets.",
            keyServices = listOf("Cost Explorer", "AWS Billing")
        ),

        AwsQuestion(
            id = 26,
            category = AwsCategory.BILLING_PRICING,
            titleJa = "AWS Budgets (予算しきい値アラート)",
            titleEn = "AWS Budgets (Alert Thresholds)",
            scenarioJa = "月間のAWS利用料金が1,000ドル、または予想料金がその80%を超えた場合に、自動的に管理者にEメール通知やSlackアラートを送信したいと考えています。どのサービスを利用すべきですか？",
            scenarioEn = "Which service allows you to set custom cost and usage limits, sending email or SNS alerts when your actual or forecasted spend exceeds 80% of your $1,000 threshold?",
            diagram = \"\"\"
[予算設定: $1,000 / 月]
        |
        v 利用額が $800 (80%) を超過!
[ AWS Budgets ] ---> メール / SNS 通知自動送信!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Cost Explorer",
                "AWS Budgets",
                "AWS Trusted Advisor",
                "AWS CloudWatch Alarms"
            ),
            optionsEn = listOf(
                "AWS Cost Explorer",
                "AWS Budgets",
                "AWS Trusted Advisor",
                "AWS CloudWatch Alarms"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS Budgets】\\nAWS Budgetsを使用すると、カスタムのコストおよび使用状況の予算を設定し、しきい値を超過（または超過すると予測）された際にアラートを受け取ることができます。",
            explanationEn = "[Correct: AWS Budgets]\\nAWS Budgets lets you set custom budgets that alert you when your cost or usage exceed (or are forecasted to exceed) your budgeted amount.",
            examTipJa = "試験頻出: 「しきい値(Threshold)」「予算アラート通知」「実績または予測コストによるトリガー」=『AWS Budgets』。",
            examTipEn = "Exam Tip: Thresholds + custom budget limits + notification triggers = AWS Budgets.",
            keyServices = listOf("AWS Budgets", "SNS", "Billing")
        ),

        AwsQuestion(
            id = 27,
            category = AwsCategory.BILLING_PRICING,
            titleJa = "AWS Pricing Calculator (事前見積もりツール)",
            titleEn = "AWS Pricing Calculator",
            scenarioJa = "AWSアカウントを開設する前に、新しく構築予定のシステム（EC2インスタンス5台、RDS 1台、S3 1TBなど）にかかる月額および年間の想定コストを試算・シミュレーションできる無料のWebツールはどれですか？",
            scenarioEn = "Which free web-based planning tool allows you to estimate monthly and annual costs for new architectures (e.g. 5 EC2 instances, 1 RDS, 1TB S3) before launching them?",
            diagram = \"\"\"
[新規アーキテクチャ設計]
          | (スペック・台数入力)
  [ AWS Pricing Calculator ] ===> 月額・年額の公式見積もり書をPDF/リンク出力!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Cost Explorer",
                "AWS Pricing Calculator",
                "AWS TCO Calculator",
                "AWS Budgets"
            ),
            optionsEn = listOf(
                "AWS Cost Explorer",
                "AWS Pricing Calculator",
                "AWS TCO Calculator",
                "AWS Budgets"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS Pricing Calculator】\\nAWS Pricing Calculatorは、AWSサービスの使用コストを見積もるための無料Webツールです。AWS利用前や新システム構築前の事前見積もりを作成・共有できます。",
            explanationEn = "[Correct: AWS Pricing Calculator]\\nAWS Pricing Calculator is a web-based planning tool to estimate costs for your architecture use cases before building them on AWS.",
            examTipJa = "試験頻出: 「事前見積もり」「クラウドアカウントなしでも試算可能」=『AWS Pricing Calculator』。旧来のSimple Monthly Calculatorの後継です。",
            examTipEn = "Exam Tip: Estimate costs before building architecture = AWS Pricing Calculator.",
            keyServices = listOf("Pricing Calculator", "Architecture")
        ),

        AwsQuestion(
            id = 28,
            category = AwsCategory.BILLING_PRICING,
            titleJa = "AWS Organizations と 一括請求 (Consolidated Billing)",
            titleEn = "AWS Organizations & Consolidated Billing",
            scenarioJa = "複数のAWSアカウントを所有する企業が、すべての請求書を1つに統合して支払い管理を一元化し、さらに全アカウント合算の使用量によるボリュームディスカウントの恩恵を受けられる機能はどれですか？",
            scenarioEn = "Which AWS feature consolidates payment across multiple AWS accounts into a single bill while providing tiered volume discounts by combining usage?",
            diagram = \"\"\"
[親アカウント (管理アカウント)] <--- 一括請求 (1枚の請求書)
     |
     +--- [開発アカウント]    \\
     +--- [本番アカウント]     ===> S3ストレージ等の容量合算でボリューム割引適用!
     +--- [検証アカウント]    /
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Control Tower",
                "AWS Organizations の一括請求 (Consolidated Billing)",
                "AWS Cost Anomaly Detection",
                "AWS Budgets"
            ),
            optionsEn = listOf(
                "AWS Control Tower",
                "Consolidated Billing in AWS Organizations",
                "AWS Cost Anomaly Detection",
                "AWS Budgets"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS Organizations の一括請求 (Consolidated Billing)】\\n一括請求を使用すると、複数アカウントの請求を親アカウントに統合し、1つの請求書として受け取ることができます。全アカウントの使用量が合算されるため、S3などの段階的ボリューム割引の恩恵を最大化できます。",
            explanationEn = "[Correct: Consolidated Billing in AWS Organizations]\\nConsolidated billing enables you to combine usage across all accounts in your organization, earning volume tiering discounts and receiving one central monthly bill.",
            examTipJa = "試験頻出: 「複数アカウントの請求統合」「1枚の請求書」「ボリュームディスカウントの合算適用」=『一括請求 (Consolidated Billing)』。",
            examTipEn = "Exam Tip: Multiple accounts combined into one bill + volume discounts = Consolidated Billing in AWS Organizations.",
            keyServices = listOf("AWS Organizations", "Consolidated Billing")
        ),

        AwsQuestion(
            id = 29,
            category = AwsCategory.BILLING_PRICING,
            titleJa = "AWS サポートプランの比較 (Enterprise vs Business)",
            titleEn = "AWS Support Plan Comparison",
            scenarioJa = "ミッションクリティカルな本番システムを運用している企業が、「24時間365日の電話・チャットサポート」「専任の技術カスタマーマネージャー (TAM)」「重大なシステムダウン時に15分以内の初動対応」を必要としています。どのサポートプランが必須ですか？",
            scenarioEn = "A company running mission-critical workloads requires 24/7 phone support, a dedicated Technical Account Manager (TAM), and <15 minute response time for business-critical outages. Which support plan is required?",
            diagram = \"\"\"
[Developer]  営業時間内メールのみ / 12〜24時間
[Business]   24/7 電話・チャット・メール / 1時間以内 (本番稼働用) / TAMなし
[Enterprise] 24/7 / 15分以内初動 / ★専任TAM (Technical Account Manager) 付属!
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Developer Support",
                "AWS Business Support",
                "AWS Enterprise Support",
                "AWS Basic Support"
            ),
            optionsEn = listOf(
                "AWS Developer Support",
                "AWS Business Support",
                "AWS Enterprise Support",
                "AWS Basic Support"
            ),
            correctIndex = 2,
            explanationJa = "【正解: AWS Enterprise Support】\\nTAM (Technical Account Manager) がアサインされ、重大な障害に15分以内で一次回答が得られるのは「Enterprise Support」のみです。Businessプランは24/7サポートですがTAMは付属せず、最優先対応時間は1時間以内です。",
            explanationEn = "[Correct: AWS Enterprise Support]\\nOnly Enterprise Support includes a designated Technical Account Manager (TAM) and a 15-minute response time for mission-critical system down events.",
            examTipJa = "試験頻出: 『専任TAM (Technical Account Manager)』という単語が出たら100%『Enterprise Support』が正解です！",
            examTipEn = "Exam Tip: Any mention of 'Technical Account Manager' or 'TAM' or '15-minute response' = Enterprise Support.",
            keyServices = listOf("AWS Support", "Enterprise Support", "TAM")
        ),

        AwsQuestion(
            id = 30,
            category = AwsCategory.BILLING_PRICING,
            titleJa = "AWS Trusted Advisor (5つの柱に基づく推奨)",
            titleEn = "AWS Trusted Advisor (5 Pillars)",
            scenarioJa = "AWS環境をスキャンし、ベストプラクティスに従って「コスト最適化」「パフォーマンス」「セキュリティ」「耐障害性」「サービス制限(クォータ)」の5つのカテゴリでリアルタイムの推奨事項と改善アドバイスを提供するツールはどれですか？",
            scenarioEn = "Which online tool acts as a customized cloud advisor, providing real-time recommendations across 5 categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Quotas?",
            diagram = \"\"\"
               +--------------------------------------+
               |        AWS Trusted Advisor           |
               +--------------------------------------+
                 |          |          |          |
                 v          v          v          v
              [コスト]  [セキュリティ] [耐障害性] [クォータ]
            (アイドルEC2 (S3全公開チェック (マルチAZ推奨) (制限接近警告)
\"\"\".trimIndent(),
            optionsJa = listOf(
                "AWS Compute Optimizer",
                "AWS Trusted Advisor",
                "Amazon CloudWatch",
                "AWS Systems Manager"
            ),
            optionsEn = listOf(
                "AWS Compute Optimizer",
                "AWS Trusted Advisor",
                "Amazon CloudWatch",
                "AWS Systems Manager"
            ),
            correctIndex = 1,
            explanationJa = "【正解: AWS Trusted Advisor】\\nAWS Trusted Advisorは、コスト最適化、セキュリティ、耐障害性、パフォーマンス、サービス制限の5つの柱に基づいて、AWS環境を評価しベストプラクティスの推奨事項を提示するオンラインツールです。",
            explanationEn = "[Correct: AWS Trusted Advisor]\\nAWS Trusted Advisor inspects your environment and makes real-time recommendations across five pillars: Cost Optimization, Security, Fault Tolerance, Performance, and Service Quotas.",
            examTipJa = "試験頻出: Trusted Advisorの5つのカテゴリ（コスト、パフォーマンス、セキュリティ、耐障害性、サービス制限）の名称選択はCLF-C02の最頻出問題の1つです。",
            examTipEn = "Exam Tip: Memorize Trusted Advisor's 5 pillars: Cost, Performance, Security, Fault Tolerance, Service Quotas.",
            keyServices = listOf("Trusted Advisor", "AWS Well-Architected")
        )
    )
}
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Generated {out_path}")
