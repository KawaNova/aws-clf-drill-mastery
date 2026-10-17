package com.kawanova.awsclfdrill.ui

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.kawanova.awsclfdrill.data.AwsCategory
import com.kawanova.awsclfdrill.data.AwsQuestion
import com.kawanova.awsclfdrill.data.AwsQuestionsData
import com.kawanova.awsclfdrill.data.UserProgressRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.launch

data class AwsUiState(
    val answeredMap: Map<Int, Boolean> = emptyMap(),
    val bookmarkedIds: Set<Int> = emptySet(),
    val isJapanese: Boolean = true,
    val currentQuestions: List<AwsQuestion> = emptyList(),
    val currentIndex: Int = 0,
    val selectedOptionIndex: Int? = null,
    val isAnswerSubmitted: Boolean = false,
    val correctCountInCurrentSession: Int = 0
) {
    val totalCount: Int = AwsQuestionsData.questions.size
    val answeredCount: Int = answeredMap.size
    val correctCount: Int = answeredMap.values.count { it }
    val progressRate: Float = if (totalCount > 0) answeredCount.toFloat() / totalCount else 0f
    val accuracyRate: Float = if (answeredCount > 0) correctCount.toFloat() / answeredCount else 0f

    val currentQuestion: AwsQuestion?
        get() = currentQuestions.getOrNull(currentIndex)
}

enum class QuizMode {
    ALL,
    CATEGORY,
    WEAKNESS,
    RANDOM10,
    BOOKMARKS
}

class AwsViewModel(application: Application) : AndroidViewModel(application) {

    private val repository = UserProgressRepository(application)

    private val _uiState = MutableStateFlow(AwsUiState())
    val uiState: StateFlow<AwsUiState> = _uiState.asStateFlow()

    init {
        viewModelScope.launch {
            combine(
                repository.answeredMapFlow,
                repository.bookmarkedIdsFlow,
                repository.isJapaneseFlow
            ) { answered, bookmarks, isJa ->
                Triple(answered, bookmarks, isJa)
            }.collect { (answered, bookmarks, isJa) ->
                _uiState.value = _uiState.value.copy(
                    answeredMap = answered,
                    bookmarkedIds = bookmarks,
                    isJapanese = isJa
                )
            }
        }
    }

    fun toggleLanguage() {
        val nextLang = !_uiState.value.isJapanese
        viewModelScope.launch {
            repository.setLanguage(nextLang)
        }
    }

    fun startQuiz(mode: QuizMode, category: AwsCategory? = null) {
        val all = AwsQuestionsData.questions
        val filtered = when (mode) {
            QuizMode.ALL -> all
            QuizMode.CATEGORY -> if (category != null) all.filter { it.category == category } else all
            QuizMode.WEAKNESS -> {
                val answered = _uiState.value.answeredMap
                all.filter { answered[it.id] == false }
            }
            QuizMode.RANDOM10 -> all.shuffled().take(10)
            QuizMode.BOOKMARKS -> {
                val bookmarked = _uiState.value.bookmarkedIds
                all.filter { bookmarked.contains(it.id) }
            }
        }

        _uiState.value = _uiState.value.copy(
            currentQuestions = filtered,
            currentIndex = 0,
            selectedOptionIndex = null,
            isAnswerSubmitted = false,
            correctCountInCurrentSession = 0
        )
    }

    fun selectOption(index: Int) {
        if (!_uiState.value.isAnswerSubmitted) {
            _uiState.value = _uiState.value.copy(selectedOptionIndex = index)
        }
    }

    fun submitAnswer() {
        val currentQ = _uiState.value.currentQuestion ?: return
        val selected = _uiState.value.selectedOptionIndex ?: return
        if (_uiState.value.isAnswerSubmitted) return

        val isCorrect = (selected == currentQ.correctIndex)
        val newCorrectCount = if (isCorrect) _uiState.value.correctCountInCurrentSession + 1 else _uiState.value.correctCountInCurrentSession

        _uiState.value = _uiState.value.copy(
            isAnswerSubmitted = true,
            correctCountInCurrentSession = newCorrectCount
        )

        viewModelScope.launch {
            repository.saveAnswer(currentQ.id, isCorrect)
        }
    }

    fun nextQuestion() {
        val nextIdx = _uiState.value.currentIndex + 1
        if (nextIdx < _uiState.value.currentQuestions.size) {
            _uiState.value = _uiState.value.copy(
                currentIndex = nextIdx,
                selectedOptionIndex = null,
                isAnswerSubmitted = false
            )
        }
    }

    fun toggleBookmark(questionId: Int) {
        viewModelScope.launch {
            repository.toggleBookmark(questionId)
        }
    }

    fun resetAllProgress() {
        viewModelScope.launch {
            repository.resetProgress()
        }
    }
}
