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
import androidx.compose.material.icons.filled.Bookmark
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Cloud
import androidx.compose.material.icons.filled.MenuBook
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.kawanova.awsclfdrill.data.AwsCategory
import com.kawanova.awsclfdrill.data.AwsQuestionsData
import com.kawanova.awsclfdrill.ui.components.AdaptiveBannerAd
import com.kawanova.awsclfdrill.ui.components.SisterAppsBanner
import com.kawanova.awsclfdrill.ui.theme.AwsOrange
import com.kawanova.awsclfdrill.ui.theme.AwsOrangeDark
import com.kawanova.awsclfdrill.ui.theme.AwsOrangeLight
import com.kawanova.awsclfdrill.ui.theme.DarkBackground
import com.kawanova.awsclfdrill.ui.theme.DarkBorder
import com.kawanova.awsclfdrill.ui.theme.DarkSurface
import com.kawanova.awsclfdrill.ui.theme.DarkSurfaceElevated
import com.kawanova.awsclfdrill.ui.theme.HighlightGold
import com.kawanova.awsclfdrill.ui.theme.TerminalGreen
import com.kawanova.awsclfdrill.ui.theme.TextPrimary
import com.kawanova.awsclfdrill.ui.theme.TextSecondary

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen(
    viewModel: AwsViewModel,
    onNavigateQuiz: (QuizMode, AwsCategory?) -> Unit,
    onNavigateCheatSheet: () -> Unit,
    onNavigateArchitecture: () -> Unit
) {
    val state by viewModel.uiState.collectAsState()
    val isJa = state.isJapanese

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text(
                            text = if (isJa) "AWS クラウド超入門" else "AWS Drill",
                            fontWeight = FontWeight.Bold,
                            fontSize = 19.sp,
                            color = TextPrimary
                        )
                        Text(
                            text = if (isJa) "CLF-C02 突破特訓 ＆ アーキテクチャ" else "CLF-C02 Exam Prep & Architecture",
                            fontSize = 12.sp,
                            color = TextSecondary
                        )
                    }
                },
                actions = {
                    // Language Switch Button
                    Box(
                        modifier = Modifier
                            .padding(end = 8.dp)
                            .clip(RoundedCornerShape(8.dp))
                            .background(DarkSurfaceElevated)
                            .border(1.dp, DarkBorder, RoundedCornerShape(8.dp))
                            .clickable { viewModel.toggleLanguage() }
                            .padding(horizontal = 10.dp, vertical = 6.dp)
                    ) {
                        Text(
                            text = if (isJa) "🌐 EN" else "🌐 日本語",
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Bold,
                            color = AwsOrange
                        )
                    }
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
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(horizontal = 16.dp)
        ) {
            // Overall Stats Card
            item {
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = 10.dp, bottom = 16.dp),
                    colors = CardDefaults.cardColors(containerColor = DarkSurface),
                    shape = RoundedCornerShape(16.dp)
                ) {
                    Column(modifier = Modifier.padding(18.dp)) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.SpaceBetween,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Column {
                                Text(
                                    text = if (isJa) "📊 学習進捗ステータス" else "📊 Learning Progress",
                                    fontSize = 15.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = TextPrimary
                                )
                                Text(
                                    text = if (isJa) "厳選全30問中 ${state.answeredCount}問 完了" else "${state.answeredCount} of ${state.totalCount} completed",
                                    fontSize = 13.sp,
                                    color = TextSecondary
                                )
                            }
                            // Reset Button
                            IconButton(onClick = { viewModel.resetAllProgress() }) {
                                Icon(
                                    imageVector = Icons.Default.Refresh,
                                    contentDescription = "Reset",
                                    tint = TextSecondary
                                )
                            }
                        }

                        Spacer(modifier = Modifier.height(14.dp))

                        // Progress Bar
                        LinearProgressIndicator(
                            progress = { state.progressRate },
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(8.dp)
                                .clip(RoundedCornerShape(4.dp)),
                            color = AwsOrange,
                            trackColor = DarkSurfaceElevated,
                        )

                        Spacer(modifier = Modifier.height(14.dp))

                        // Score metrics
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            MetricBadge(
                                label = if (isJa) "正答率" else "Accuracy",
                                value = "${(state.accuracyRate * 100).toInt()}%",
                                color = TerminalGreen
                            )
                            MetricBadge(
                                label = if (isJa) "正解数" else "Correct",
                                value = "${state.correctCount} / ${state.totalCount}",
                                color = AwsOrangeLight
                            )
                            MetricBadge(
                                label = if (isJa) "ブックマーク" else "Bookmarks",
                                value = "${state.bookmarkedIds.size}",
                                color = HighlightGold
                            )
                        }
                    }
                }
            }

            // Quick Tool Shortcuts (Architecture Explorer & Cheat Sheet)
            item {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 16.dp),
                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    // Architecture Explorer Button
                    Card(
                        modifier = Modifier
                            .weight(1f)
                            .clip(RoundedCornerShape(12.dp))
                            .clickable { onNavigateArchitecture() }
                            .border(1.dp, AwsOrange.copy(alpha = 0.5f), RoundedCornerShape(12.dp)),
                        colors = CardDefaults.cardColors(containerColor = Color(0xFF1E2433))
                    ) {
                        Column(modifier = Modifier.padding(14.dp)) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(
                                    imageVector = Icons.Default.Cloud,
                                    contentDescription = null,
                                    tint = AwsOrange,
                                    modifier = Modifier.size(20.dp)
                                )
                                Spacer(modifier = Modifier.width(6.dp))
                                Text(
                                    text = if (isJa) "構成図解" else "Architecture",
                                    fontSize = 14.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = TextPrimary
                                )
                            }
                            Spacer(modifier = Modifier.height(4.dp))
                            Text(
                                text = if (isJa) "3層Web・サーバーレス" else "Interactive diagrams",
                                fontSize = 11.sp,
                                color = TextSecondary
                            )
                        }
                    }

                    // Cheat Sheet Button
                    Card(
                        modifier = Modifier
                            .weight(1f)
                            .clip(RoundedCornerShape(12.dp))
                            .clickable { onNavigateCheatSheet() }
                            .border(1.dp, HighlightGold.copy(alpha = 0.4f), RoundedCornerShape(12.dp)),
                        colors = CardDefaults.cardColors(containerColor = Color(0xFF22241F))
                    ) {
                        Column(modifier = Modifier.padding(14.dp)) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(
                                    imageVector = Icons.Default.MenuBook,
                                    contentDescription = null,
                                    tint = HighlightGold,
                                    modifier = Modifier.size(20.dp)
                                )
                                Spacer(modifier = Modifier.width(6.dp))
                                Text(
                                    text = if (isJa) "早見表" else "Cheat Sheet",
                                    fontSize = 14.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = TextPrimary
                                )
                            }
                            Spacer(modifier = Modifier.height(4.dp))
                            Text(
                                text = if (isJa) "主要サービス逆引き" else "Core services reference",
                                fontSize = 11.sp,
                                color = TextSecondary
                            )
                        }
                    }
                }
            }

            // Quick Play Actions
            item {
                Text(
                    text = if (isJa) "⚡ クイック特訓モード" else "⚡ Quick Modes",
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Bold,
                    color = TextPrimary,
                    modifier = Modifier.padding(bottom = 10.dp)
                )

                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 16.dp),
                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    Button(
                        onClick = { onNavigateQuiz(QuizMode.ALL, null) },
                        modifier = Modifier.weight(1f),
                        colors = ButtonDefaults.buttonColors(containerColor = AwsOrangeDark),
                        shape = RoundedCornerShape(10.dp)
                    ) {
                        Icon(Icons.Default.PlayArrow, contentDescription = null, modifier = Modifier.size(16.dp))
                        Spacer(modifier = Modifier.width(4.dp))
                        Text(if (isJa) "全問一気特訓" else "All 30 Qs", fontSize = 12.sp, fontWeight = FontWeight.Bold)
                    }

                    Button(
                        onClick = { onNavigateQuiz(QuizMode.RANDOM10, null) },
                        modifier = Modifier.weight(1f),
                        colors = ButtonDefaults.buttonColors(containerColor = DarkSurfaceElevated),
                        shape = RoundedCornerShape(10.dp)
                    ) {
                        Text(if (isJa) "🎲 ランダム10問" else "🎲 Random 10", fontSize = 12.sp)
                    }
                }
            }

            // Category Drills
            item {
                Text(
                    text = if (isJa) "📂 4大カテゴリ別ドリル (CLF-C02)" else "📂 CLF-C02 Category Domains",
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Bold,
                    color = TextPrimary,
                    modifier = Modifier.padding(bottom = 10.dp)
                )
            }

            items(AwsCategory.entries.size) { idx ->
                val cat = AwsCategory.entries[idx]
                val catQuestions = AwsQuestionsData.questions.filter { it.category == cat }
                val catAnswered = catQuestions.count { state.answeredMap.containsKey(it.id) }
                val catCorrect = catQuestions.count { state.answeredMap[it.id] == true }
                val progress = if (catQuestions.isNotEmpty()) catAnswered.toFloat() / catQuestions.size else 0f

                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 10.dp)
                        .clip(RoundedCornerShape(12.dp))
                        .clickable { onNavigateQuiz(QuizMode.CATEGORY, cat) }
                        .border(1.dp, DarkBorder, RoundedCornerShape(12.dp)),
                    colors = CardDefaults.cardColors(containerColor = DarkSurface)
                ) {
                    Column(modifier = Modifier.padding(14.dp)) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.SpaceBetween,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Box(
                                    modifier = Modifier
                                        .size(10.dp)
                                        .clip(CircleShape)
                                        .background(AwsOrange)
                                )
                                Spacer(modifier = Modifier.width(8.dp))
                                Text(
                                    text = if (isJa) cat.titleJa else cat.titleEn,
                                    fontSize = 14.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = TextPrimary
                                )
                            }
                            Text(
                                text = "$catCorrect / ${catQuestions.size}",
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Bold,
                                color = AwsOrange
                            )
                        }

                        Spacer(modifier = Modifier.height(4.dp))
                        Text(
                            text = if (isJa) cat.descriptionJa else cat.descriptionEn,
                            fontSize = 12.sp,
                            color = TextSecondary
                        )

                        Spacer(modifier = Modifier.height(10.dp))
                        LinearProgressIndicator(
                            progress = { progress },
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(6.dp)
                                .clip(RoundedCornerShape(3.dp)),
                            color = AwsOrange,
                            trackColor = DarkSurfaceElevated
                        )
                    }
                }
            }

            // Weakness & Bookmarks
            item {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 10.dp),
                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    OutlinedButton(
                        onClick = { onNavigateQuiz(QuizMode.WEAKNESS, null) },
                        modifier = Modifier.weight(1f),
                        shape = RoundedCornerShape(10.dp)
                    ) {
                        Icon(Icons.Default.Warning, contentDescription = null, tint = HighlightGold, modifier = Modifier.size(16.dp))
                        Spacer(modifier = Modifier.width(6.dp))
                        Text(if (isJa) "間違えた問題" else "Weak Points", fontSize = 12.sp, color = TextPrimary)
                    }

                    OutlinedButton(
                        onClick = { onNavigateQuiz(QuizMode.BOOKMARKS, null) },
                        modifier = Modifier.weight(1f),
                        shape = RoundedCornerShape(10.dp)
                    ) {
                        Icon(Icons.Default.Bookmark, contentDescription = null, tint = HighlightGold, modifier = Modifier.size(16.dp))
                        Spacer(modifier = Modifier.width(6.dp))
                        Text(if (isJa) "ブックマーク" else "Saved", fontSize = 12.sp, color = TextPrimary)
                    }
                }
            }

            // Sister Apps Banner
            item {
                Spacer(modifier = Modifier.height(10.dp))
                SisterAppsBanner(isJapanese = isJa)
                Spacer(modifier = Modifier.height(24.dp))
            }
        }
    }
}

@Composable
fun MetricBadge(label: String, value: String, color: Color) {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text(text = label, fontSize = 11.sp, color = TextSecondary)
        Spacer(modifier = Modifier.height(2.dp))
        Text(text = value, fontSize = 16.sp, fontWeight = FontWeight.Bold, color = color)
    }
}
