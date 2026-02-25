import pytest
from research_domain.domain.entities.research_production import ResearchProduction
from research_domain.domain.entities.production_type import ProductionType
from research_domain.domain.entities.researcher import Researcher

class TestResearchProduction:
    def test_create_production_type(self):
        pt = ProductionType(name="BOOK")
        assert pt.name == "BOOK"

    def test_create_research_production_with_authors(self):
        r1 = Researcher(name="Author 1")
        pt = ProductionType(name="BOOK")
        
        prod = ResearchProduction(
            title="Clean Architecture in Python",
            year=2024,
            production_type=pt,
            publisher="Tech Press",
            isbn="123-456-789",
            authors=[r1]
        )
        
        assert prod.title == "Clean Architecture in Python"
        assert prod.year == 2024
        assert prod.production_type.name == "BOOK"
        assert prod.publisher == "Tech Press"
        assert prod.isbn == "123-456-789"
        assert len(prod.authors) == 1
        assert prod.authors[0].name == "Author 1"

    def test_production_type_software(self):
        pt = ProductionType(name="SOFTWARE")
        prod = ResearchProduction(
            title="Research Manager",
            year=2024,
            production_type=pt,
            version="1.0.0",
            platform="Web",
            link="https://github.com/example/research-manager"
        )
        assert prod.production_type.name == "SOFTWARE"
        assert prod.version == "1.0.0"
        assert prod.platform == "Web"
        assert prod.link == "https://github.com/example/research-manager"

    def test_production_type_chapter(self):
        pt = ProductionType(name="BOOK_CHAPTER")
        prod = ResearchProduction(
            title="Layered Design",
            year=2024,
            production_type=pt,
            book_title="Software Architecture Patterns",
            pages="45-60"
        )
        assert prod.production_type.name == "BOOK_CHAPTER"
        assert prod.book_title == "Software Architecture Patterns"
        assert prod.pages == "45-60"
