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
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Bookmark
import androidx.compose.material.icons.filled.BookmarkBorder
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Close
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LinearProgressIndicator
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
import com.kawanova.awsclfdrill.ui.components.AdaptiveBannerAd
import com.kawanova.awsclfdrill.ui.components.TerminalCard
import com.kawanova.awsclfdrill.ui.theme.AwsOrange
import com.kawanova.awsclfdrill.ui.theme.AwsOrangeDark
import com.kawanova.awsclfdrill.ui.theme.AwsOrangeLight
import com.kawanova.awsclfdrill.ui.theme.DarkBackground
import com.kawanova.awsclfdrill.ui.theme.DarkBorder
import com.kawanova.awsclfdrill.ui.theme.DarkSurface
import com.kawanova.awsclfdrill.ui.theme.DarkSurfaceElevated
import com.kawanova.awsclfdrill.ui.theme.ErrorRed
import com.kawanova.awsclfdrill.ui.theme.HighlightGold
import com.kawanova.awsclfdrill.ui.theme.TerminalGreen
import com.kawanova.awsclfdrill.ui.theme.TextPrimary
import com.kawanova.awsclfdrill.ui.theme.TextSecondary

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun QuizScreen(
    viewModel: AwsViewModel,
    onBack: () -> Unit
) {
    val state by viewModel.uiState.collectAsState()
    val isJa = state.isJapanese
    val questions = state.currentQuestions
    val currentQ = state.currentQuestion
    val currentIdx = state.currentIndex
    val totalInSession = questions.size

    // If session is empty
    if (questions.isEmpty()) {
        Scaffold(
            topBar = {
                TopAppBar(
                    title = { Text(if (isJa) "演習" else "Practice", color = TextPrimary) },
                    navigationIcon = {
                        IconButton(onClick = onBack) {
                            Icon(Icons.Default.ArrowBack, contentDescription = "Back", tint = TextPrimary)
                        }
                    },
                    colors = TopAppBarDefaults.topAppBarColors(containerColor = DarkBackground)
                )
            },
            containerColor = DarkBackground
        ) { padding ->
            Box(
                modifier = Modifier.fillMaxSize().padding(padding),
                contentAlignment = Alignment.Center
            ) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(
                        text = if (isJa) "該当する問題がありません" else "No questions found",
                        fontSize = 16.sp,
                        color = TextSecondary
                    )
                    Spacer(modifier = Modifier.height(16.dp))
                    Button(
                        onClick = onBack,
                        colors = ButtonDefaults.buttonColors(containerColor = AwsOrange)
                    ) {
                        Text(if (isJa) "ホームへ戻る" else "Back to Home")
                    }
                }
            }
        }
        return
    }

    if (currentQ == null) {
        // Completed Session
        Scaffold(
            topBar = {
                TopAppBar(
                    title = { Text(if (isJa) "特訓結果" else "Drill Results", color = TextPrimary) },
                    navigationIcon = {
                        IconButton(onClick = onBack) {
                            Icon(Icons.Default.ArrowBack, contentDescription = "Back", tint = TextPrimary)
                        }
                    },
                    colors = TopAppBarDefaults.topAppBarColors(containerColor = DarkBackground)
                )
            },
            containerColor = DarkBackground
        ) { padding ->
            Box(
                modifier = Modifier.fillMaxSize().padding(padding).padding(20.dp),
                contentAlignment = Alignment.Center
            ) {
                Card(
                    modifier = Modifier.fillMaxWidth(),
                    colors = CardDefaults.cardColors(containerColor = DarkSurface),
                    shape = RoundedCornerShape(16.dp)
                ) {
                    Column(
                        modifier = Modifier.padding(24.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Text(text = "🎉", fontSize = 48.sp)
                        Spacer(modifier = Modifier.height(12.dp))
                        Text(
                            text = if (isJa) "セッション完了！" else "Session Complete!",
                            fontSize = 20.sp,
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                        Spacer(modifier = Modifier.height(8.dp))
                        Text(
                            text = if (isJa)
                                "スコア: ${state.correctCountInCurrentSession} / $totalInSession 正解"
                            else
                                "Score: ${state.correctCountInCurrentSession} of $totalInSession correct",
                            fontSize = 16.sp,
                            color = AwsOrange,
                            fontWeight = FontWeight.Bold
                        )
                        Spacer(modifier = Modifier.height(24.dp))
                        Button(
                            onClick = onBack,
                            modifier = Modifier.fillMaxWidth(),
                            colors = ButtonDefaults.buttonColors(containerColor = AwsOrange),
                            shape = RoundedCornerShape(10.dp)
                        ) {
                            Text(if (isJa) "ホームへ戻る" else "Back to Home", fontWeight = FontWeight.Bold)
                        }
                    }
                }
            }
        }
        return
    }

    val isBookmarked = state.bookmarkedIds.contains(currentQ.id)
    val options = if (isJa) currentQ.optionsJa else currentQ.optionsEn
    val progress = (currentIdx + 1).toFloat() / totalInSession

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text(
                            text = if (isJa) currentQ.category.titleJa else currentQ.category.titleEn,
                            fontSize = 12.sp,
                            color = AwsOrange
                        )
                        Text(
                            text = "Question ${currentIdx + 1} / $totalInSession",
                            fontSize = 16.sp,
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                    }
                },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back", tint = TextPrimary)
                    }
                },
                actions = {
                    IconButton(onClick = { viewModel.toggleBookmark(currentQ.id) }) {
                        Icon(
                            imageVector = if (isBookmarked) Icons.Default.Bookmark else Icons.Default.BookmarkBorder,
                            contentDescription = "Bookmark",
                            tint = if (isBookmarked) HighlightGold else TextSecondary
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = DarkBackground)
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
            // Session Progress Bar
            item {
                LinearProgressIndicator(
                    progress = { progress },
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(6.dp)
                        .clip(RoundedCornerShape(3.dp)),
                    color = AwsOrange,
                    trackColor = DarkSurfaceElevated
                )
                Spacer(modifier = Modifier.height(14.dp))
            }

            // Question Scenario
            item {
                Card(
                    modifier = Modifier.fillMaxWidth(),
                    colors = CardDefaults.cardColors(containerColor = DarkSurface),
                    shape = RoundedCornerShape(14.dp)
                ) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text(
                            text = if (isJa) currentQ.titleJa else currentQ.titleEn,
                            fontSize = 16.sp,
                            fontWeight = FontWeight.Bold,
                            color = TextPrimary
                        )
                        Spacer(modifier = Modifier.height(8.dp))
                        Text(
                            text = if (isJa) currentQ.scenarioJa else currentQ.scenarioEn,
                            fontSize = 14.sp,
                            lineHeight = 21.sp,
                            color = TextSecondary
                        )
                    }
                }
                Spacer(modifier = Modifier.height(12.dp))
            }

            // ASCII Diagram
            if (currentQ.diagram.isNotEmpty()) {
                item {
                    TerminalCard(
                        title = if (isJa) "構成ダイアグラム" else "Architecture Diagram",
                        content = currentQ.diagram,
                        modifier = Modifier.fillMaxWidth()
                    )
                    Spacer(modifier = Modifier.height(16.dp))
                }
            }

            // Options List
            item {
                Text(
                    text = if (isJa) "選択肢から1つ選んでください:" else "Select the best answer:",
                    fontSize = 13.sp,
                    fontWeight = FontWeight.Medium,
                    color = TextSecondary,
                    modifier = Modifier.padding(bottom = 8.dp)
                )
            }

            items(options.size) { optIdx ->
                val optText = options[optIdx]
                val isSelected = (state.selectedOptionIndex == optIdx)
                val isSubmitted = state.isAnswerSubmitted
                val isCorrectAnswer = (optIdx == currentQ.correctIndex)

                val borderColor = when {
                    !isSubmitted && isSelected -> AwsOrange
                    isSubmitted && isCorrectAnswer -> TerminalGreen
                    isSubmitted && isSelected && !isCorrectAnswer -> ErrorRed
                    else -> DarkBorder
                }

                val bgColor = when {
                    !isSubmitted && isSelected -> DarkSurfaceElevated
                    isSubmitted && isCorrectAnswer -> Color(0xFF063A26)
                    isSubmitted && isSelected && !isCorrectAnswer -> Color(0xFF3B1214)
                    else -> DarkSurface
                }

                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 5.dp)
                        .clip(RoundedCornerShape(10.dp))
                        .clickable(enabled = !isSubmitted) {
                            viewModel.selectOption(optIdx)
                        }
                        .border(1.5.dp, borderColor, RoundedCornerShape(10.dp)),
                    colors = CardDefaults.cardColors(containerColor = bgColor)
                ) {
                    Row(
                        modifier = Modifier.padding(14.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Box(
                            modifier = Modifier
                                .size(24.dp)
                                .clip(CircleShape)
                                .background(if (isSelected || (isSubmitted && isCorrectAnswer)) borderColor else DarkSurfaceElevated),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(
                                text = "${('A'.code + optIdx).toChar()}",
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Bold,
                                color = TextPrimary
                            )
                        }
                        Spacer(modifier = Modifier.width(12.dp))
                        Text(
                            text = optText,
                            fontSize = 14.sp,
                            lineHeight = 20.sp,
                            color = TextPrimary,
                            modifier = Modifier.weight(1f)
                        )

                        if (isSubmitted) {
                            if (isCorrectAnswer) {
                                Icon(Icons.Default.CheckCircle, contentDescription = null, tint = TerminalGreen, modifier = Modifier.size(20.dp))
                            } else if (isSelected) {
                                Icon(Icons.Default.Close, contentDescription = null, tint = ErrorRed, modifier = Modifier.size(20.dp))
                            }
                        }
                    }
                }
            }

            // Action Button (Submit or Next)
            item {
                Spacer(modifier = Modifier.height(16.dp))

                if (!state.isAnswerSubmitted) {
                    Button(
                        onClick = { viewModel.submitAnswer() },
                        enabled = state.selectedOptionIndex != null,
                        modifier = Modifier.fillMaxWidth().height(48.dp),
                        colors = ButtonDefaults.buttonColors(containerColor = AwsOrangeDark),
                        shape = RoundedCornerShape(10.dp)
                    ) {
                        Text(if (isJa) "解答する" else "Submit Answer", fontWeight = FontWeight.Bold)
                    }
                } else {
                    Button(
                        onClick = { viewModel.nextQuestion() },
                        modifier = Modifier.fillMaxWidth().height(48.dp),
                        colors = ButtonDefaults.buttonColors(containerColor = AwsOrange),
                        shape = RoundedCornerShape(10.dp)
                    ) {
                        Text(
                            text = if (currentIdx + 1 < totalInSession) {
                                if (isJa) "次の問題へ ➔" else "Next Question ➔"
                            } else {
                                if (isJa) "結果を見る 🎉" else "View Results 🎉"
                            },
                            fontWeight = FontWeight.Bold
                        )
                    }
                }
                Spacer(modifier = Modifier.height(16.dp))
            }

            // Explanation & Exam Tips Card (Shown after submit)
            if (state.isAnswerSubmitted) {
                item {
                    Card(
                        modifier = Modifier.fillMaxWidth().padding(bottom = 24.dp),
                        colors = CardDefaults.cardColors(containerColor = DarkSurfaceElevated),
                        shape = RoundedCornerShape(14.dp)
                    ) {
                        Column(modifier = Modifier.padding(18.dp)) {
                            // Explanation Header
                            Text(
                                text = if (isJa) "📖 詳細解説" else "📖 Explanation",
                                fontSize = 15.sp,
                                fontWeight = FontWeight.Bold,
                                color = AwsOrangeLight
                            )
                            Spacer(modifier = Modifier.height(8.dp))
                            Text(
                                text = if (isJa) currentQ.explanationJa else currentQ.explanationEn,
                                fontSize = 13.sp,
                                lineHeight = 20.sp,
                                color = TextPrimary
                            )

                            Spacer(modifier = Modifier.height(14.dp))

                            // Exam Tip Box
                            Box(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .clip(RoundedCornerShape(8.dp))
                                    .background(Color(0xFF241906))
                                    .border(1.dp, Color(0xFF78350F), RoundedCornerShape(8.dp))
                                    .padding(12.dp)
                            ) {
                                Column {
                                    Text(
                                        text = if (isJa) "🎯 合格のツボ (Exam Tip)" else "🎯 Exam Tip",
                                        fontSize = 12.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = HighlightGold
                                    )
                                    Spacer(modifier = Modifier.height(4.dp))
                                    Text(
                                        text = if (isJa) currentQ.examTipJa else currentQ.examTipEn,
                                        fontSize = 12.sp,
                                        lineHeight = 18.sp,
                                        color = TextPrimary
                                    )
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
