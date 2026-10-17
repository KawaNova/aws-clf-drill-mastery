package com.kawanova.awsclfdrill.data

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "aws_clf_drill_progress")

class UserProgressRepository(private val context: Context) {

    private val KEY_ANSWERED_QUESTIONS = stringPreferencesKey("answered_questions") // format: "1:true,2:false"
    private val KEY_BOOKMARKS = stringPreferencesKey("bookmarked_questions")       // format: "1,3,7"
    private val KEY_LANGUAGE_JA = booleanPreferencesKey("is_japanese")

    val answeredMapFlow: Flow<Map<Int, Boolean>> = context.dataStore.data.map { prefs ->
        val raw = prefs[KEY_ANSWERED_QUESTIONS] ?: ""
        if (raw.isEmpty()) emptyMap()
        else {
            raw.split(",").mapNotNull { entry ->
                val parts = entry.split(":")
                if (parts.size == 2) {
                    val id = parts[0].toIntOrNull()
                    val correct = parts[1].toBooleanStrictOrNull()
                    if (id != null && correct != null) id to correct else null
                } else null
            }.toMap()
        }
    }

    val bookmarkedIdsFlow: Flow<Set<Int>> = context.dataStore.data.map { prefs ->
        val raw = prefs[KEY_BOOKMARKS] ?: ""
        if (raw.isEmpty()) emptySet()
        else raw.split(",").mapNotNull { it.toIntOrNull() }.toSet()
    }

    val isJapaneseFlow: Flow<Boolean> = context.dataStore.data.map { prefs ->
        prefs[KEY_LANGUAGE_JA] ?: true
    }

    suspend fun saveAnswer(questionId: Int, isCorrect: Boolean) {
        context.dataStore.edit { prefs ->
            val raw = prefs[KEY_ANSWERED_QUESTIONS] ?: ""
            val currentMap = if (raw.isEmpty()) mutableMapOf()
            else {
                raw.split(",").mapNotNull { entry ->
                    val parts = entry.split(":")
                    if (parts.size == 2) {
                        val id = parts[0].toIntOrNull()
                        val correct = parts[1].toBooleanStrictOrNull()
                        if (id != null && correct != null) id to correct else null
                    } else null
                }.toMap().toMutableMap()
            }
            currentMap[questionId] = isCorrect
            prefs[KEY_ANSWERED_QUESTIONS] = currentMap.entries.joinToString(",") { "${it.key}:${it.value}" }
        }
    }

    suspend fun toggleBookmark(questionId: Int) {
        context.dataStore.edit { prefs ->
            val raw = prefs[KEY_BOOKMARKS] ?: ""
            val currentSet = if (raw.isEmpty()) mutableSetOf()
            else raw.split(",").mapNotNull { it.toIntOrNull() }.toMutableSet()

            if (currentSet.contains(questionId)) {
                currentSet.remove(questionId)
            } else {
                currentSet.add(questionId)
            }
            prefs[KEY_BOOKMARKS] = currentSet.joinToString(",")
        }
    }

    suspend fun setLanguage(isJapanese: Boolean) {
        context.dataStore.edit { prefs ->
            prefs[KEY_LANGUAGE_JA] = isJapanese
        }
    }

    suspend fun resetProgress() {
        context.dataStore.edit { prefs ->
            prefs.remove(KEY_ANSWERED_QUESTIONS)
            prefs.remove(KEY_BOOKMARKS)
        }
    }
}
