import os

out_path = r"c:\Users\Kawamoto\Documents\AgentAIDev\mobile-apps\024_aws-clf-drill\app\src\main\java\com\kawanova\awsclfdrill\data\CheatSheetData.kt"

content = """package com.kawanova.awsclfdrill.data

import kotlinx.serialization.Serializable

@Serializable
data class CheatSheetItem(
    val titleJa: String,
    val titleEn: String,
    val categoryJa: String,
    val categoryEn: String,
    val command: String,
    val descJa: String,
    val descEn: String,
    val keywords: List<String>
)

object CheatSheetData {
    val items: List<CheatSheetItem> = listOf(
        // ==========================
        // 1. コンピュート & サーバーレス
        // ==========================
        CheatSheetItem(
            titleJa = "Amazon EC2",
            titleEn = "Amazon EC2 (Virtual Servers)",
            categoryJa = "コンピュート",
            categoryEn = "Compute",
            command = "aws ec2 run-instances --image-id ami-xxxx --instance-type t3.micro",
            descJa = "安全でサイズ変更可能な仮想サーバー。OS（Linux/Windows）のフルコントロールが可能。",
            descEn = "Secure, resizable compute capacity in the cloud. Full OS-level administrative control.",
            keywords = listOf("EC2", "Virtual Machine", "IaaS", "AMI", "Instance Types")
        ),
        CheatSheetItem(
            titleJa = "AWS Lambda",
            titleEn = "AWS Lambda (Serverless Compute)",
            categoryJa = "コンピュート",
            categoryEn = "Compute",
            command = "aws lambda invoke --function-name MyFunction response.json",
            descJa = "サーバー管理不要のイベント駆動型実行基盤。ミリ秒単位の従量課金、最大実行時間15分。",
            descEn = "Run code without provisioning or managing servers. Millisecond pay-as-you-go, 15-min max timeout.",
            keywords = listOf("Lambda", "Serverless", "Event-Driven", "FaaS", "15 minutes")
        ),
        CheatSheetItem(
            titleJa = "Amazon ECS & EKS",
            titleEn = "Amazon ECS & EKS (Containers)",
            categoryJa = "コンピュート",
            categoryEn = "Compute",
            command = "aws ecs list-clusters",
            descJa = "Dockerコンテナ（ECS）およびKubernetes（EKS）のオーケストレーション。Fargateでサーバーレス実行可能。",
            descEn = "Highly scalable container management for Docker (ECS) and Kubernetes (EKS). Pairs with AWS Fargate.",
            keywords = listOf("ECS", "EKS", "Docker", "Kubernetes", "Fargate")
        ),
        CheatSheetItem(
            titleJa = "AWS Elastic Beanstalk",
            titleEn = "AWS Elastic Beanstalk (PaaS)",
            categoryJa = "コンピュート",
            categoryEn = "Compute",
            command = "eb deploy",
            descJa = "Webアプリのコードをアップロードするだけで、デプロイ・容量プロビジョニング・負荷分散を自動化。",
            descEn = "Platform-as-a-Service (PaaS) to deploy web apps without worrying about underlying infrastructure.",
            keywords = listOf("Elastic Beanstalk", "PaaS", "Deployment", "Easy Web")
        ),

        // ==========================
        // 2. ストレージ
        // ==========================
        CheatSheetItem(
            titleJa = "Amazon S3",
            titleEn = "Amazon S3 (Object Storage)",
            categoryJa = "ストレージ",
            categoryEn = "Storage",
            command = "aws s3 cp file.txt s3://my-bucket/",
            descJa = "99.999999999% (11 9's) の耐久性を誇るオブジェクトストレージ。静的Webホスティングも可能。",
            descEn = "Industry-leading scalability, data availability, and 11 9's durability object storage service.",
            keywords = listOf("S3", "Object Storage", "11 9s Durability", "Buckets", "Static Web")
        ),
        CheatSheetItem(
            titleJa = "Amazon EBS",
            titleEn = "Amazon EBS (Block Storage)",
            categoryJa = "ストレージ",
            categoryEn = "Storage",
            command = "aws ec2 attach-volume --volume-id vol-xxxx --instance-id i-xxxx",
            descJa = "EC2インスタンス専用の永続的ブロックストレージ（仮想ハードディスク）。単一AZ内で自動複製。",
            descEn = "High-performance block storage volumes designed for use with Amazon EC2 instances within a single AZ.",
            keywords = listOf("EBS", "Block Storage", "Virtual Hard Drive", "Single AZ", "IOPS")
        ),
        CheatSheetItem(
            titleJa = "Amazon EFS",
            titleEn = "Amazon EFS (Network File System)",
            categoryJa = "ストレージ",
            categoryEn = "Storage",
            command = "sudo mount -t nfs4 fs-xxxx:/ /mnt/efs",
            descJa = "複数のEC2インスタンスから同時にマウント可能な完全マネージド型共有ファイルストレージ (NFS)。",
            descEn = "Serverless, fully elastic network file system (NFS) that can be mounted simultaneously by multiple EC2s.",
            keywords = listOf("EFS", "NFS", "Shared Storage", "Multi-AZ", "POSIX")
        ),
        CheatSheetItem(
            titleJa = "S3 Glacier Deep Archive",
            titleEn = "S3 Glacier Deep Archive",
            categoryJa = "ストレージ",
            categoryEn = "Storage",
            command = "aws s3 cp archive.tar s3://my-bucket/ --storage-class DEEP_ARCHIVE",
            descJa = "AWSで最も安価な長期保管ストレージ。年に1回程度しか取り出さない規制・監査アーカイブ用（12時間以内）。",
            descEn = "Lowest cost storage class in AWS for long-term archiving with retrieval within 12 hours.",
            keywords = listOf("Glacier", "Deep Archive", "Lowest Cost", "Archiving", "12-hour retrieval")
        ),

        // ==========================
        // 3. データベース
        // ==========================
        CheatSheetItem(
            titleJa = "Amazon RDS & Aurora",
            titleEn = "Amazon RDS & Amazon Aurora",
            categoryJa = "データベース",
            categoryEn = "Database",
            command = "aws rds describe-db-instances",
            descJa = "MySQL, PostgreSQL等を簡単設定できるマネージドRDBMS。Auroraは最大5倍高速で3つのAZに6重複製。",
            descEn = "Managed relational database service. Aurora delivers up to 5x throughput with 6-way replication across 3 AZs.",
            keywords = listOf("RDS", "Aurora", "Relational", "SQL", "Multi-AZ Replication")
        ),
        CheatSheetItem(
            titleJa = "Amazon DynamoDB",
            titleEn = "Amazon DynamoDB (NoSQL)",
            categoryJa = "データベース",
            categoryEn = "Database",
            command = "aws dynamodb put-item --table-name Users --item file://user.json",
            descJa = "完全マネージドなサーバーレスNoSQLデータベース。規模に関係なく1桁ミリ秒の超高速パフォーマンス。",
            descEn = "Serverless NoSQL database service delivering single-digit millisecond latency at any scale.",
            keywords = listOf("DynamoDB", "NoSQL", "Key-Value", "Single-Digit ms", "Serverless")
        ),
        CheatSheetItem(
            titleJa = "Amazon Redshift",
            titleEn = "Amazon Redshift (Data Warehouse)",
            categoryJa = "データベース",
            categoryEn = "Database",
            command = "aws redshift describe-clusters",
            descJa = "ペタバイト規模の構造化データを高速クエリ分析できるフルマネージド型クラウドデータウェアハウス(DWH)。",
            descEn = "Fast, fully managed, petabyte-scale cloud data warehouse for business intelligence and complex analytics.",
            keywords = listOf("Redshift", "Data Warehouse", "DWH", "Analytics", "Petabyte")
        ),

        // ==========================
        // 4. ネットワーク & 配信
        // ==========================
        CheatSheetItem(
            titleJa = "Amazon VPC",
            titleEn = "Amazon VPC (Virtual Private Cloud)",
            categoryJa = "ネットワーク",
            categoryEn = "Networking",
            command = "aws ec2 describe-vpcs",
            descJa = "AWS上に論理的に分離された仮想ネットワーク。サブネット、ルートテーブル、ゲートウェイを柔軟に設計。",
            descEn = "Logically isolated virtual network for your AWS resources with complete control over IP ranges and subnets.",
            keywords = listOf("VPC", "Subnet", "Route Table", "CIDR", "Virtual Network")
        ),
        CheatSheetItem(
            titleJa = "Amazon CloudFront",
            titleEn = "Amazon CloudFront (CDN)",
            categoryJa = "ネットワーク",
            categoryEn = "Networking",
            command = "aws cloudfront create-invalidation --distribution-id xxx --paths '/*'",
            descJa = "世界中のエッジロケーション網でデータをキャッシュし、超低レイテンシで配信するグローバルCDNサービス。",
            descEn = "Global content delivery network (CDN) securely caching web assets closer to viewers at edge locations.",
            keywords = listOf("CloudFront", "CDN", "Edge Locations", "Caching", "Low Latency")
        ),
        CheatSheetItem(
            titleJa = "Amazon Route 53",
            titleEn = "Amazon Route 53 (DNS)",
            categoryJa = "ネットワーク",
            categoryEn = "Networking",
            command = "aws route53 list-hosted-zones",
            descJa = "可用性99.999%のマネージドDNS。ドメイン登録、ヘルスチェック、フェイルオーバールーティングに対応。",
            descEn = "Highly available and scalable cloud Domain Name System (DNS) with automated failover and health checks.",
            keywords = listOf("Route 53", "DNS", "Failover", "Domain Registration", "Health Checks")
        ),

        // ==========================
        // 5. セキュリティ & 管理
        // ==========================
        CheatSheetItem(
            titleJa = "AWS IAM",
            titleEn = "AWS Identity and Access Management",
            categoryJa = "セキュリティ",
            categoryEn = "Security",
            command = "aws iam list-roles",
            descJa = "認証と認可を一元管理。IAMユーザー、グループ、ロール、ポリシーで最小権限の原則を徹底。",
            descEn = "Securely manage access to AWS services and resources using users, groups, roles, and JSON policies.",
            keywords = listOf("IAM", "Roles", "Policies", "Least Privilege", "MFA")
        ),
        CheatSheetItem(
            titleJa = "AWS WAF & Shield",
            titleEn = "AWS WAF & AWS Shield",
            categoryJa = "セキュリティ",
            categoryEn = "Security",
            command = "aws wafv2 list-web-acls --scope REGIONAL",
            descJa = "WAFはSQLiやXSS等のレイヤー7攻撃を防ぎ、Shieldはインフラ層のDDoS攻撃を自動緩和。",
            descEn = "WAF protects Layer 7 web traffic against exploits; Shield defends against volumetric Layer 3/4 DDoS attacks.",
            keywords = listOf("WAF", "Shield", "DDoS", "SQLi", "Layer 7")
        ),
        CheatSheetItem(
            titleJa = "AWS Trusted Advisor",
            titleEn = "AWS Trusted Advisor",
            categoryJa = "管理・コスト",
            categoryEn = "Management",
            command = "aws support describe-trusted-advisor-checks --language en",
            descJa = "コスト最適化、セキュリティ、耐障害性、パフォーマンス、サービス制限の5つの柱で環境を自動診断。",
            descEn = "Inspects environment and offers actionable advice for cost, performance, security, fault tolerance, and quotas.",
            keywords = listOf("Trusted Advisor", "5 Pillars", "Best Practices", "Cost Optimization")
        )
    )
}
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Generated {out_path}")
