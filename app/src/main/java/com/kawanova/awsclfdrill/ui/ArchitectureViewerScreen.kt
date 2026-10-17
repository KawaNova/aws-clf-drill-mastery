package com.kawanova.awsclfdrill.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Cloud
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.Security
import androidx.compose.material.icons.filled.Storage
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.Scaffold
import androidx.compose.material3.ScrollableTabRow
import androidx.compose.material3.Tab
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.kawanova.awsclfdrill.ui.components.AdaptiveBannerAd
import com.kawanova.awsclfdrill.ui.components.TerminalCard
import com.kawanova.awsclfdrill.ui.theme.AwsOrange
import com.kawanova.awsclfdrill.ui.theme.AwsOrangeLight
import com.kawanova.awsclfdrill.ui.theme.DarkBackground
import com.kawanova.awsclfdrill.ui.theme.DarkBorder
import com.kawanova.awsclfdrill.ui.theme.DarkSurface
import com.kawanova.awsclfdrill.ui.theme.DarkSurfaceElevated
import com.kawanova.awsclfdrill.ui.theme.HighlightGold
import com.kawanova.awsclfdrill.ui.theme.TextPrimary
import com.kawanova.awsclfdrill.ui.theme.TextSecondary

data class ArchitecturePattern(
    val titleJa: String,
    val titleEn: String,
    val subtitleJa: String,
    val subtitleEn: String,
    val asciiDiagram: String,
    val components: List<ArchComponent>
)

data class ArchComponent(
    val name: String,
    val roleJa: String,
    val roleEn: String,
    val examPointJa: String,
    val examPointEn: String
)

val architecturePatterns = listOf(
    ArchitecturePattern(
        titleJa = "3層Web高可用性",
        titleEn = "3-Tier High Availability",
        subtitleJa = "Multi-AZ・自動スケーリング・静的キャッシュの鉄板構成",
        subtitleEn = "Multi-AZ, Auto Scaling, & Edge Caching Standard",
        asciiDiagram = """
[ユーザー] ---> Route 53 (DNS)
                  |
                  v
         [ CloudFront (CDN) ] ---> [ S3 (画像/静的資産) ]
                  |
                  v (動的API)
         [ ALB (負荷分散) ]
           /              \
    (AZ-a) /                \ (AZ-c)
    [ EC2 (Auto Scaling) ]  [ EC2 (Auto Scaling) ]
           \                /
            v              v
         [ Amazon RDS (Multi-AZ 同期レプリケーション) ]
        """.trimIndent(),
        components = listOf(
            ArchComponent(
                name = "Amazon Route 53",
                roleJa = "高可用性DNS & トラフィックルーティング",
                roleEn = "Highly Available DNS & Global Routing",
                examPointJa = "可用性99.999%、ヘルスチェックによる自動フェイルオーバーが試験頻出。",
                examPointEn = "99.999% SLA, automated health checks and latency/failover routing."
            ),
            ArchComponent(
                name = "Amazon CloudFront",
                roleJa = "グローバルコンテンツ配信ネットワーク (CDN)",
                roleEn = "Global Content Delivery Network",
                examPointJa = "世界中のエッジロケーションでキャッシュし、レイテンシとS3負荷を激減。",
                examPointEn = "Caches content at edge locations worldwide to minimize latency."
            ),
            ArchComponent(
                name = "Application Load Balancer (ALB)",
                roleJa = "レイヤー7負荷分散",
                roleEn = "Layer 7 Load Balancing",
                examPointJa = "複数AZの正常なEC2インスタンスのみにトラフィックを均等分散。",
                examPointEn = "Evenly routes HTTP/HTTPS traffic to healthy targets across multiple AZs."
            ),
            ArchComponent(
                name = "Amazon EC2 + Auto Scaling",
                roleJa = "弾力的な仮想サーバー群",
                roleEn = "Elastic Virtual Server Pool",
                examPointJa = "CPU負荷に応じて自動で台数を増減（弾力性）。スポット活用で最大90%削減。",
                examPointEn = "Dynamically scales capacity based on demand (elasticity)."
            ),
            ArchComponent(
                name = "Amazon RDS (Multi-AZ)",
                roleJa = "リレーショナルデータベース",
                roleEn = "Managed Relational Database",
                examPointJa = "Primary障害時に別AZのStandbyへ自動フェイルオーバー（高可用性）。",
                examPointEn = "Synchronous replication to standby replica in another AZ for instant failover."
            )
        )
    ),
    ArchitecturePattern(
        titleJa = "サーバーレスAPI",
        titleEn = "Serverless API",
        subtitleJa = "サーバー管理ゼロ・完全従量課金のモダン構成",
        subtitleEn = "Zero Server Management & Event-Driven Architecture",
        asciiDiagram = """
[クライアント (Web/Mobile)]
          | (HTTPSリクエスト)
          v
  [ Amazon API Gateway ]  <-- 認証(Cognito) / スロットリング
          | (イベント発火)
          v
  [ AWS Lambda ]          <-- ビジネスロジック (最大15分実行)
          |
     +----+----+
     |         |
     v         v
[ DynamoDB ] [ Amazon S3 ]
(NoSQL DB)   (ファイル保存)
        """.trimIndent(),
        components = listOf(
            ArchComponent(
                name = "Amazon API Gateway",
                roleJa = "フルマネージドAPIエンドポイント",
                roleEn = "Fully Managed API Gateway",
                examPointJa = "トラフィック管理、CORSサポート、認可、アクセス制御を統合。",
                examPointEn = "Handles traffic management, authorization, throttling, and API versioning."
            ),
            ArchComponent(
                name = "AWS Lambda",
                roleJa = "イベント駆動型サーバーレス実行環境",
                roleEn = "Event-Driven Serverless Compute",
                examPointJa = "アイドル時のコストは完全ゼロ。実行時間（ミリ秒）のみ課金。",
                examPointEn = "Zero cost when idle. Pay only for compute time consumed (15-min max)."
            ),
            ArchComponent(
                name = "Amazon DynamoDB",
                roleJa = "フルマネージドNoSQLデータベース",
                roleEn = "Serverless NoSQL Database",
                examPointJa = "規模に関係なく1桁ミリ秒の応答速度。自動スケーリング。",
                examPointEn = "Single-digit millisecond latency at any scale. Fully serverless."
            )
        )
    ),
    ArchitecturePattern(
        titleJa = "セキュアVPCネットワーク",
        titleEn = "Secure VPC Network",
        subtitleJa = "多層防御・パブリック/プライベートサブネット分離",
        subtitleEn = "Defense-in-Depth & Network Segmentation",
        asciiDiagram = """
[インターネット]
       | (双方向通信)
[ Internet Gateway (IGW) ]
       |
[ パブリックサブネット ]
  +--- ALB (Web受信)
  +--- NAT Gateway (外向き通信のみプロキシ)
       |
       | (内部プライベート通信)
       v
[ プライベートサブネット (インターネット直接接続なし) ]
  +--- EC2 App サーバー (SG: ALBからのみ8080許可)
  +--- RDS DB サーバー (SG: Appからのみ3306許可)
        """.trimIndent(),
        components = listOf(
            ArchComponent(
                name = "Internet Gateway (IGW)",
                roleJa = "VPCとインターネットの出入口",
                roleEn = "VPC Internet Connectivity",
                examPointJa = "VPCに1つだけアタッチ可能。高可用性かつ水平スケーラブル。",
                examPointEn = "Horizontally scalable, redundant, and highly available VPC connection."
            ),
            ArchComponent(
                name = "NAT Gateway",
                roleJa = "外向き専用インターネットアクセス",
                roleEn = "Outbound-Only Internet Access",
                examPointJa = "パブリックサブネットに配置し、プライベート側のパッチ取得を可能にする。",
                examPointEn = "Placed in public subnet to allow private instances to reach the internet."
            ),
            ArchComponent(
                name = "セキュリティグループ (SG)",
                roleJa = "インスタンスレベル仮想ファイアウォール",
                roleEn = "Stateful Instance Firewall",
                examPointJa = "ステートフル（戻り通信自動許可）。許可(Allow)ルールのみ定義可能。",
                examPointEn = "Stateful virtual firewall applied directly at the instance network interface."
            )
        )
    )
)

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ArchitectureViewerScreen(
    isJapanese: Boolean,
    modifier: Modifier = Modifier
) {
    var selectedPatternIndex by remember { mutableStateOf(0) }
    var selectedComponent by remember { mutableStateOf<ArchComponent?>(null) }

    val currentPattern = architecturePatterns[selectedPatternIndex]

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = if (isJapanese) "☁️ AWSアーキテクチャ図解" else "☁️ Architecture Explorer",
                        fontWeight = FontWeight.Bold,
                        color = TextPrimary
                    )
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = DarkBackground
                )
            )
        },
        bottomBar = {
            AdaptiveBannerAd()
        },
        containerColor = DarkBackground
    ) { paddingValues ->
        LazyColumn(
            modifier = modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(horizontal = 16.dp)
        ) {
            // Pattern Tabs
            item {
                ScrollableTabRow(
                    selectedTabIndex = selectedPatternIndex,
                    containerColor = DarkSurface,
                    contentColor = AwsOrange,
                    edgePadding = 0.dp,
                    modifier = Modifier
                        .fillMaxWidth()
                        .clip(RoundedCornerShape(12.dp))
                ) {
                    architecturePatterns.forEachIndexed { index, pattern ->
                        Tab(
                            selected = selectedPatternIndex == index,
                            onClick = {
                                selectedPatternIndex = index
                                selectedComponent = null
                            },
                            text = {
                                Text(
                                    text = if (isJapanese) pattern.titleJa else pattern.titleEn,
                                    fontWeight = if (selectedPatternIndex == index) FontWeight.Bold else FontWeight.Normal,
                                    fontSize = 13.sp
                                )
                            }
                        )
                    }
                }
                Spacer(modifier = Modifier.height(14.dp))
            }

            // Subtitle Card
            item {
                Text(
                    text = if (isJapanese) currentPattern.subtitleJa else currentPattern.subtitleEn,
                    fontSize = 13.sp,
                    color = TextSecondary,
                    modifier = Modifier.padding(bottom = 12.dp)
                )

                // ASCII Diagram Card
                TerminalCard(
                    title = if (isJapanese) "システム構成図 (ASCII)" else "System Diagram (ASCII)",
                    content = currentPattern.asciiDiagram,
                    modifier = Modifier.fillMaxWidth()
                )
                Spacer(modifier = Modifier.height(18.dp))
            }

            // Interactive Components Header
            item {
                Text(
                    text = if (isJapanese) "👆 サービスをタップして試験のポイントを確認" else "👆 Tap a service to inspect key exam points",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = AwsOrangeLight,
                    modifier = Modifier.padding(bottom = 8.dp)
                )
            }

            // Component Cards
            items(currentPattern.components.size) { idx ->
                val comp = currentPattern.components[idx]
                val isSelected = (selectedComponent == comp)

                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp)
                        .clip(RoundedCornerShape(10.dp))
                        .clickable { selectedComponent = if (isSelected) null else comp }
                        .border(
                            width = if (isSelected) 2.dp else 1.dp,
                            color = if (isSelected) AwsOrange else DarkBorder,
                            shape = RoundedCornerShape(10.dp)
                        ),
                    colors = CardDefaults.cardColors(
                        containerColor = if (isSelected) DarkSurfaceElevated else DarkSurface
                    )
                ) {
                    Column(modifier = Modifier.padding(14.dp)) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Box(
                                modifier = Modifier
                                    .size(8.dp)
                                    .clip(CircleShape)
                                    .background(if (isSelected) AwsOrange else HighlightGold)
                            )
                            Spacer(modifier = Modifier.width(8.dp))
                            Text(
                                text = comp.name,
                                fontSize = 15.sp,
                                fontWeight = FontWeight.Bold,
                                color = TextPrimary,
                                modifier = Modifier.weight(1f)
                            )
                            Icon(
                                imageVector = Icons.Default.Info,
                                contentDescription = null,
                                tint = if (isSelected) AwsOrange else TextSecondary,
                                modifier = Modifier.size(18.dp)
                            )
                        }

                        Spacer(modifier = Modifier.height(4.dp))
                        Text(
                            text = if (isJapanese) comp.roleJa else comp.roleEn,
                            fontSize = 13.sp,
                            color = TextSecondary
                        )

                        if (isSelected) {
                            Spacer(modifier = Modifier.height(10.dp))
                            Box(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .clip(RoundedCornerShape(8.dp))
                                    .background(Color(0xFF241906))
                                    .border(1.dp, Color(0xFF78350F), RoundedCornerShape(8.dp))
                                    .padding(10.dp)
                            ) {
                                Column {
                                    Text(
                                        text = if (isJapanese) "🎯 CLF-C02 合格のツボ" else "🎯 Key Exam Takeaway",
                                        fontSize = 12.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = AwsOrange
                                    )
                                    Spacer(modifier = Modifier.height(4.dp))
                                    Text(
                                        text = if (isJapanese) comp.examPointJa else comp.examPointEn,
                                        fontSize = 12.sp,
                                        lineHeight = 17.sp,
                                        color = TextPrimary
                                    )
                                }
                            }
                        }
                    }
                }
            }

            item {
                Spacer(modifier = Modifier.height(24.dp))
            }
        }
    }
}
