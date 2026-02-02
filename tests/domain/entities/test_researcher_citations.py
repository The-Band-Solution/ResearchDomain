import pytest
from research_domain.domain.entities.researcher import Researcher
# Must import AcademicEducation so it is registered in SQLA for Researcher relationship resolution
from research_domain.domain.entities.academic_education import AcademicEducation

class TestResearcherCitations:
    def test_create_researcher_with_citations(self):
        r = Researcher(
            name="Dr. Citation",
            citation_names="CITATION, D.; DR. CITATION"
        )
        assert r.name == "Dr. Citation"
        assert "CITATION, D." in r.citation_names
        
    def test_default_citations_empty(self):
        r = Researcher(name="Dr. No Citation")
        assert r.citation_names is None
