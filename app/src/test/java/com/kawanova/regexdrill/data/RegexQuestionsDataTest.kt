package com.kawanova.regexdrill.data

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Test
import java.util.regex.Pattern

class RegexQuestionsDataTest {

    @Test
    fun testQuestionsTotalCountIs30() {
        assertEquals("Total questions should be exactly 30", 30, RegexQuestionsData.questions.size)
    }

    @Test
    fun testQuestionIdsAreUniqueAndSequential() {
        val ids = RegexQuestionsData.questions.map { it.id }
        assertEquals(30, ids.toSet().size)
        assertEquals((1..30).toList(), ids)
    }

    @Test
    fun testAllQuestionsHaveFourOptions() {
        RegexQuestionsData.questions.forEach { q ->
            assertEquals("Question ${q.id} should have 4 JA options", 4, q.optionsJa.size)
            assertEquals("Question ${q.id} should have 4 EN options", 4, q.optionsEn.size)
            assertTrue("Question ${q.id} correctIndex must be within 0..3", q.correctIndex in 0..3)
        }
    }

    @Test
    fun testAllQuestionsHaveNonEmptyFields() {
        RegexQuestionsData.questions.forEach { q ->
            assertTrue("Q${q.id} titleJa not empty", q.titleJa.isNotBlank())
            assertTrue("Q${q.id} titleEn not empty", q.titleEn.isNotBlank())
            assertTrue("Q${q.id} situationJa not empty", q.situationJa.isNotBlank())
            assertTrue("Q${q.id} situationEn not empty", q.situationEn.isNotBlank())
            assertTrue("Q${q.id} visualDiagram not empty", q.visualDiagram.isNotBlank())
            assertTrue("Q${q.id} explanationJa not empty", q.explanationJa.isNotBlank())
            assertTrue("Q${q.id} explanationEn not empty", q.explanationEn.isNotBlank())
            assertTrue("Q${q.id} proTipJa not empty", q.proTipJa.isNotBlank())
            assertTrue("Q${q.id} proTipEn not empty", q.proTipEn.isNotBlank())
        }
    }

    @Test
    fun testAllCategoriesAreValid() {
        val validCatIds = RegexCategories.list.map { it.id }.toSet()
        RegexQuestionsData.questions.forEach { q ->
            assertTrue("Category ${q.category} of Q${q.id} must be registered", validCatIds.contains(q.category))
        }
    }

    @Test
    fun testCheatSheetSectionsArePopulated() {
        assertTrue("CheatSheet must have sections", CheatSheetData.sections.isNotEmpty())
        CheatSheetData.sections.forEach { section ->
            assertTrue("Section ${section.id} items not empty", section.items.isNotEmpty())
            section.items.forEach { item ->
                assertTrue(item.titleJa.isNotBlank())
                assertTrue(item.syntax.isNotBlank())
                assertTrue(item.descJa.isNotBlank())
            }
        }
    }
}
