import pytest
from research_domain.domain.entities.article import Article, ArticleType
from research_domain.domain.entities.researcher import Researcher
# Import other entities to ensure they are registered for relationship resolution
from research_domain.domain.entities.proficiency import Proficiency
from research_domain.domain.entities.award import Award
from research_domain.domain.entities.academic_education import AcademicEducation
from research_domain.domain.entities.language import Language

class TestArticle:
    def test_create_article_with_authors(self):
        r1 = Researcher(name="Author 1")
        r2 = Researcher(name="Author 2")
        
        article = Article(
            title="Advanced AI Coding",
            year=2024,
            type=ArticleType.JOURNAL,
            doi="10.1000/xyz123",
            journal_conference="AI Journal",
            authors=[r1, r2]
        )
        
        assert article.title == "Advanced AI Coding"
        assert article.year == 2024
        assert article.type == ArticleType.JOURNAL
        assert article.doi == "10.1000/xyz123"
        assert len(article.authors) == 2
        
    def test_article_without_optional_fields(self):
        article = Article(title="Simple Paper", year=2023, type=ArticleType.CONFERENCE_EVENT)
        assert article.title == "Simple Paper"
        assert article.type == ArticleType.CONFERENCE_EVENT
        assert article.doi is None
        assert article.authors == []

    def test_add_author_to_article(self):
        article = Article(title="Dynamic Paper", year=2024, type=ArticleType.JOURNAL)
        r = Researcher(name="Dynamic Author")
        article.authors.append(r)
        
        assert len(article.authors) == 1
        assert article.authors[0].name == "Dynamic Author"
