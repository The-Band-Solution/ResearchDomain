import pytest
from research_domain.domain.entities.researcher import Researcher
# Must import AcademicEducation so it is registered in SQLA for Researcher relationship resolution
from research_domain.domain.entities.academic_education import AcademicEducation
from research_domain.domain.entities.language import Language
from research_domain.domain.entities.proficiency import Proficiency, ProficiencyLevel
from research_domain.domain.entities.professional_activity import ProfessionalActivity
from research_domain.domain.entities.award import Award

class TestResearcherMetadata:
    def test_create_researcher_with_metadata(self):
        r = Researcher(
            name="Dr. Polyglot",
            citation_names="Dr. P; Polyglot, D."
        )
        
        # Test Awards relationship
        award1 = Award(researcher_id=1, title="Best Paper 2023")
        r.awards.append(award1)

        # Test ProfessionalActivity relationship
        activity = ProfessionalActivity(
            researcher_id=1,
            institution="Instituto Federal do Espirito Santo, IFES, Brasil.",
            institution_name="Instituto Federal do Espirito Santo",
            start_year=2022,
            current=True
        )
        r.professional_activities.append(activity)
        
        # Test Proficiency relationship
        lang = Language(name="English", id=1)
        prof = Proficiency(
            researcher_id=1, 
            language_id=1, 
            comprehension=ProficiencyLevel.ALTO
        )
        prof.language = lang # manually set relation for test if needed
        r.proficiencies.append(prof)
        
        assert len(r.awards) == 1
        assert r.awards[0].title == "Best Paper 2023"

        assert len(r.professional_activities) == 1
        assert r.professional_activities[0].institution_name == "Instituto Federal do Espirito Santo"

        assert len(r.proficiencies) == 1
        assert r.proficiencies[0].comprehension == ProficiencyLevel.ALTO
        assert r.citation_names == "Dr. P; Polyglot, D."

    def test_default_metadata_empty(self):
        r = Researcher(name="Dr. Empty")
        # Ensure defaults are empty lists/None
        assert r.proficiencies == []
        assert r.professional_activities == []
        assert r.awards == []
        assert r.citation_names is None
