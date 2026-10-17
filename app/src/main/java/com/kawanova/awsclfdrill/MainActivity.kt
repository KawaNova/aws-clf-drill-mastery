package com.kawanova.awsclfdrill

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import com.google.android.gms.ads.MobileAds
import com.kawanova.awsclfdrill.ui.AwsViewModel
import com.kawanova.awsclfdrill.ui.navigation.AwsNavGraph
import com.kawanova.awsclfdrill.ui.theme.AwsClfDrillTheme

class MainActivity : ComponentActivity() {

    private val viewModel: AwsViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        // Initialize Google Mobile Ads SDK in background
        MobileAds.initialize(this) {}

        setContent {
            AwsClfDrillTheme {
                AwsNavGraph(viewModel = viewModel)
            }
        }
    }
}
