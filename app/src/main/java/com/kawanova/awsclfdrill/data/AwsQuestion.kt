package com.kawanova.awsclfdrill.data

import kotlinx.serialization.Serializable

@Serializable
enum class AwsCategory(
    val titleJa: String,
    val titleEn: String,
    val iconName: String,
    val descriptionJa: String,
    val descriptionEn: String
) {
    CLOUD_CONCEPTS(
        "クラウドの概念",
        "Cloud Concepts",
        "Cloud",
        "高可用性・弾力性・責任共有モデル・コストメリット",
        "High availability, elasticity, shared responsibility & economics"
    ),
    SECURITY_COMPLIANCE(
        "セキュリティ & コンプライアンス",
        "Security & Compliance",
        "Security",
        "IAM・KMS・WAF・Shield・GuardDuty・暗号化と責任境界",
        "IAM, KMS, WAF, Shield, GuardDuty & security boundary"
    ),
    TECHNOLOGY_SERVICES(
        "テクノロジー & 主要サービス",
        "Technology & Services",
        "Storage",
        "EC2・S3・RDS・Lambda・VPC・Route 53・CloudFront",
        "Core services: EC2, S3, RDS, Lambda, VPC, Route 53 & CloudFront"
    ),
    BILLING_PRICING(
        "請求・料金 & サポート",
        "Billing & Pricing",
        "ReceiptLong",
        "Cost Explorer・Budgets・サポートプラン・Trusted Advisor",
        "Cost Explorer, Budgets, Support Tiers & Trusted Advisor"
    )
}

@Serializable
data class AwsQuestion(
    val id: Int,
    val category: AwsCategory,
    val titleJa: String,
    val titleEn: String,
    val scenarioJa: String,
    val scenarioEn: String,
    val diagram: String,
    val optionsJa: List<String>,
    val optionsEn: List<String>,
    val correctIndex: Int,
    val explanationJa: String,
    val explanationEn: String,
    val examTipJa: String,
    val examTipEn: String,
    val keyServices: List<String>
)
