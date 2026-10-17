package com.kawanova.awsclfdrill.ui

import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import android.widget.Toast
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
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.ContentCopy
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.ScrollableTabRow
import androidx.compose.material3.Tab
import androidx.compose.material3.Text
import androidx.compose.material3.TextFieldDefaults
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.kawanova.awsclfdrill.data.CheatSheetData
import com.kawanova.awsclfdrill.data.CheatSheetItem
import com.kawanova.awsclfdrill.ui.components.AdaptiveBannerAd
import com.kawanova.awsclfdrill.ui.theme.AwsOrange
import com.kawanova.awsclfdrill.ui.theme.AwsOrangeLight
import com.kawanova.awsclfdrill.ui.theme.DarkBackground
import com.kawanova.awsclfdrill.ui.theme.DarkBorder
import com.kawanova.awsclfdrill.ui.theme.DarkSurface
import com.kawanova.awsclfdrill.ui.theme.DarkSurfaceElevated
import com.kawanova.awsclfdrill.ui.theme.HighlightGold
import com.kawanova.awsclfdrill.ui.theme.TerminalBg
import com.kawanova.awsclfdrill.ui.theme.TerminalCyan
import com.kawanova.awsclfdrill.ui.theme.TextPrimary
import com.kawanova.awsclfdrill.ui.theme.TextSecondary

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CheatSheetScreen(
    isJapanese: Boolean,
    onBack: () -> Unit
) {
    val context = LocalContext.current
    var selectedCategoryIndex by remember { mutableIntStateOf(0) }
    var searchQuery by remember { mutableStateOf("") }

    val categories = listOf(
        Pair("すべて", "All"),
        Pair("コンピュート", "Compute"),
        Pair("ストレージ", "Storage"),
        Pair("データベース", "Database"),
        Pair("ネットワーク", "Networking"),
        Pair("セキュリティ", "Security"),
        Pair("管理・コスト", "Management")
    )

    val currentCategory = categories[selectedCategoryIndex]

    val filteredItems = CheatSheetData.items.filter { item ->
        val matchesCategory = if (selectedCategoryIndex == 0) true
        else (item.categoryJa == currentCategory.first || item.categoryEn == currentCategory.second)

        val query = searchQuery.trim().lowercase()
        val matchesSearch = if (query.isEmpty()) true
        else {
            item.titleJa.lowercase().contains(query) ||
            item.titleEn.lowercase().contains(query) ||
            item.command.lowercase().contains(query) ||
            item.descJa.lowercase().contains(query) ||
            item.descEn.lowercase().contains(query) ||
            item.keywords.any { it.lowercase().contains(query) }
        }

        matchesCategory && matchesSearch
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = if (isJapanese) "📋 AWS サービス早見表" else "📋 AWS Cheat Sheet",
                        fontWeight = FontWeight.Bold,
                        color = TextPrimary
                    )
                },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back", tint = TextPrimary)
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
            // Search Input
            item {
                OutlinedTextField(
                    value = searchQuery,
                    onValueChange = { searchQuery = it },
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = 8.dp, bottom = 12.dp),
                    placeholder = {
                        Text(
                            text = if (isJapanese) "サービス名やキーワードで検索..." else "Search services or keywords...",
                            color = TextSecondary,
                            fontSize = 13.sp
                        )
                    },
                    leadingIcon = {
                        Icon(Icons.Default.Search, contentDescription = null, tint = TextSecondary)
                    },
                    colors = TextFieldDefaults.colors(
                        focusedContainerColor = DarkSurface,
                        unfocusedContainerColor = DarkSurface,
                        focusedTextColor = TextPrimary,
                        unfocusedTextColor = TextPrimary,
                        focusedIndicatorColor = AwsOrange,
                        unfocusedIndicatorColor = DarkBorder
                    ),
                    shape = RoundedCornerShape(12.dp),
                    singleLine = true
                )
            }

            // Category Filter Tabs
            item {
                ScrollableTabRow(
                    selectedTabIndex = selectedCategoryIndex,
                    containerColor = DarkSurface,
                    contentColor = AwsOrange,
                    edgePadding = 0.dp,
                    modifier = Modifier
                        .fillMaxWidth()
                        .clip(RoundedCornerShape(12.dp))
                ) {
                    categories.forEachIndexed { index, (ja, en) ->
                        Tab(
                            selected = selectedCategoryIndex == index,
                            onClick = { selectedCategoryIndex = index },
                            text = {
                                Text(
                                    text = if (isJapanese) ja else en,
                                    fontSize = 13.sp,
                                    fontWeight = if (selectedCategoryIndex == index) FontWeight.Bold else FontWeight.Normal
                                )
                            }
                        )
                    }
                }
                Spacer(modifier = Modifier.height(14.dp))
            }

            // Cheat Sheet Items
            items(filteredItems) { item ->
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 5.dp)
                        .clip(RoundedCornerShape(12.dp))
                        .border(1.dp, DarkBorder, RoundedCornerShape(12.dp)),
                    colors = CardDefaults.cardColors(containerColor = DarkSurface)
                ) {
                    Column(modifier = Modifier.padding(14.dp)) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.SpaceBetween,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Text(
                                text = if (isJapanese) item.titleJa else item.titleEn,
                                fontSize = 15.sp,
                                fontWeight = FontWeight.Bold,
                                color = TextPrimary
                            )
                            Box(
                                modifier = Modifier
                                    .clip(RoundedCornerShape(6.dp))
                                    .background(DarkSurfaceElevated)
                                    .padding(horizontal = 8.dp, vertical = 3.dp)
                            ) {
                                Text(
                                    text = if (isJapanese) item.categoryJa else item.categoryEn,
                                    fontSize = 11.sp,
                                    color = AwsOrangeLight,
                                    fontWeight = FontWeight.Medium
                                )
                            }
                        }

                        Spacer(modifier = Modifier.height(6.dp))
                        Text(
                            text = if (isJapanese) item.descJa else item.descEn,
                            fontSize = 13.sp,
                            lineHeight = 18.sp,
                            color = TextSecondary
                        )

                        Spacer(modifier = Modifier.height(10.dp))

                        // CLI Command / Code snippet with Copy button
                        Box(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clip(RoundedCornerShape(8.dp))
                                .background(TerminalBg)
                                .border(1.dp, DarkBorder, RoundedCornerShape(8.dp))
                                .clickable {
                                    val clipboard = context.getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
                                    clipboard.setPrimaryClip(ClipData.newPlainText("AWS Command", item.command))
                                    Toast.makeText(
                                        context,
                                        if (isJapanese) "コピーしました: ${item.command}" else "Copied to clipboard",
                                        Toast.LENGTH_SHORT
                                    ).show()
                                }
                                .padding(10.dp)
                        ) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.SpaceBetween,
                                modifier = Modifier.fillMaxWidth()
                            ) {
                                Text(
                                    text = item.command,
                                    fontFamily = FontFamily.Monospace,
                                    fontSize = 12.sp,
                                    color = TerminalCyan,
                                    modifier = Modifier.weight(1f)
                                )
                                Spacer(modifier = Modifier.width(8.dp))
                                Icon(
                                    imageVector = Icons.Default.ContentCopy,
                                    contentDescription = "Copy",
                                    tint = HighlightGold,
                                    modifier = Modifier.size(16.dp)
                                )
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
