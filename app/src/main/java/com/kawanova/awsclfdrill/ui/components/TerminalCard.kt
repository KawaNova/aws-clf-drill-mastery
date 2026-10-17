package com.kawanova.awsclfdrill.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.kawanova.awsclfdrill.ui.theme.DarkBorder
import com.kawanova.awsclfdrill.ui.theme.TerminalBg
import com.kawanova.awsclfdrill.ui.theme.TerminalCyan
import com.kawanova.awsclfdrill.ui.theme.TextSecondary

@Composable
fun TerminalCard(
    title: String,
    content: String,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(12.dp))
            .background(TerminalBg)
            .border(1.dp, DarkBorder, RoundedCornerShape(12.dp))
    ) {
        // Terminal Header Bar
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .background(Color(0xFF131A2A))
                .padding(horizontal = 12.dp, vertical = 8.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Box(modifier = Modifier.size(10.dp).clip(CircleShape).background(Color(0xFFEF4444)))
            Spacer(modifier = Modifier.width(6.dp))
            Box(modifier = Modifier.size(10.dp).clip(CircleShape).background(Color(0xFFF59E0B)))
            Spacer(modifier = Modifier.width(6.dp))
            Box(modifier = Modifier.size(10.dp).clip(CircleShape).background(Color(0xFF10B981)))
            Spacer(modifier = Modifier.width(12.dp))
            Text(
                text = title,
                fontSize = 12.sp,
                fontFamily = FontFamily.Monospace,
                color = TextSecondary,
                fontWeight = FontWeight.Medium
            )
        }

        // Terminal Content
        Text(
            text = content,
            modifier = Modifier.padding(14.dp),
            fontFamily = FontFamily.Monospace,
            fontSize = 13.sp,
            lineHeight = 19.sp,
            color = TerminalCyan
        )
    }
}
