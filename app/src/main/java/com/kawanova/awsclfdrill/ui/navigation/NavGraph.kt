package com.kawanova.awsclfdrill.ui.navigation

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.kawanova.awsclfdrill.ui.ArchitectureViewerScreen
import com.kawanova.awsclfdrill.ui.AwsViewModel
import com.kawanova.awsclfdrill.ui.CheatSheetScreen
import com.kawanova.awsclfdrill.ui.HomeScreen
import com.kawanova.awsclfdrill.ui.QuizMode
import com.kawanova.awsclfdrill.ui.QuizScreen

object AwsDestinations {
    const val HOME = "home"
    const val QUIZ = "quiz"
    const val CHEAT_SHEET = "cheat_sheet"
    const val ARCHITECTURE = "architecture"
}

@Composable
fun AwsNavGraph(
    viewModel: AwsViewModel,
    navController: NavHostController = rememberNavController()
) {
    val uiState by viewModel.uiState.collectAsState()

    NavHost(
        navController = navController,
        startDestination = AwsDestinations.HOME
    ) {
        composable(AwsDestinations.HOME) {
            HomeScreen(
                viewModel = viewModel,
                onNavigateQuiz = { mode, category ->
                    viewModel.startQuiz(mode, category)
                    navController.navigate(AwsDestinations.QUIZ)
                },
                onNavigateCheatSheet = {
                    navController.navigate(AwsDestinations.CHEAT_SHEET)
                },
                onNavigateArchitecture = {
                    navController.navigate(AwsDestinations.ARCHITECTURE)
                }
            )
        }

        composable(AwsDestinations.QUIZ) {
            QuizScreen(
                viewModel = viewModel,
                onBack = { navController.popBackStack() }
            )
        }

        composable(AwsDestinations.CHEAT_SHEET) {
            CheatSheetScreen(
                isJapanese = uiState.isJapanese,
                onBack = { navController.popBackStack() }
            )
        }

        composable(AwsDestinations.ARCHITECTURE) {
            ArchitectureViewerScreen(
                isJapanese = uiState.isJapanese
            )
        }
    }
}
