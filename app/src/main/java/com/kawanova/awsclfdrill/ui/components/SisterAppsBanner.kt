package com.kawanova.awsclfdrill.ui.components

import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.kawanova.awsclfdrill.ui.theme.AwsOrange
import com.kawanova.awsclfdrill.ui.theme.DarkBorder
import com.kawanova.awsclfdrill.ui.theme.DarkSurface
import com.kawanova.awsclfdrill.ui.theme.TextPrimary
import com.kawanova.awsclfdrill.ui.theme.TextSecondary

data class SisterApp(
    val nameJa: String,
    val nameEn: String,
    val descJa: String,
    val descEn: String,
    val icon: String,
    val packageName: String
)

val sisterApps = listOf(
    SisterApp(
        nameJa = "正規表現超入門",
        nameEn = "Regex Drill",
        descJa = "実務パターン逆引き ＆ リアルタイムテスター",
        descEn = "Practical Pattern Matching & Live Regex Tester",
        icon = "🔤",
        packageName = "com.kawanova.regexdrill"
    ),
    SisterApp(
        nameJa = "ネットワーク超入門",
        nameEn = "Network Drill",
        descJa = "HTTPステータス・DNS・TCP/IP実務特訓",
        descEn = "Master HTTP status, DNS, and Web Protocols",
        icon = "🌐",
        packageName = "com.kawanova.networkdrill"
    ),
    SisterApp(
        nameJa = "Docker & コンテナ超入門",
        nameEn = "Docker Drill",
        descJa = "実務で使えるDockerfile・compose特訓",
        descEn = "Container & Compose Practical Drills",
        icon = "🐳",
        packageName = "com.kawanova.dockerdrill"
    ),
    SisterApp(
        nameJa = "基本情報技術者 科目A 突破",
        nameEn = "FE Drill (Subject A)",
        descJa = "新シラバス・テクノロジ系全肢解説",
        descEn = "IT Fundamentals & Computer Science Exam Prep",
        icon = "🎓",
        packageName = "com.kawanova.fekamokua"
    )
)

@Composable
fun SisterAppsBanner(
    isJapanese: Boolean,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current

    Column(
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(16.dp))
            .background(DarkSurface)
            .border(1.dp, DarkBorder, RoundedCornerShape(16.dp))
            .padding(16.dp)
    ) {
        Text(
            text = if (isJapanese) "🚀 クラウド・エンジニア向け姉妹アプリ" else "🚀 Engineering & Cloud Sister Apps",
            fontSize = 15.sp,
            fontWeight = FontWeight.Bold,
            color = AwsOrange
        )
        Spacer(modifier = Modifier.height(12.dp))

        sisterApps.forEach { app ->
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(10.dp))
                    .clickable {
                        try {
                            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("market://details?id=${app.packageName}"))
                            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                            context.startActivity(intent)
                        } catch (e: Exception) {
                            val webIntent = Intent(Intent.ACTION_VIEW, Uri.parse("https://play.google.com/store/apps/details?id=${app.packageName}"))
                            webIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                            context.startActivity(webIntent)
                        }
                    }
                    .padding(vertical = 8.dp, horizontal = 6.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(text = app.icon, fontSize = 24.sp)
                Column(modifier = Modifier.weight(1f).padding(start = 12.dp)) {
                    Text(
                        text = if (isJapanese) app.nameJa else app.nameEn,
                        fontSize = 14.sp,
                        fontWeight = FontWeight.SemiBold,
                        color = TextPrimary
                    )
                    Text(
                        text = if (isJapanese) app.descJa else app.descEn,
                        fontSize = 12.sp,
                        color = TextSecondary
                    )
                }
                Text(
                    text = "無料",
                    fontSize = 12.sp,
                    color = AwsOrange,
                    fontWeight = FontWeight.Bold
                )
            }
        }
    }
}
