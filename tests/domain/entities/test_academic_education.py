import pytest
from unittest.mock import MagicMock
from research_domain.domain.entities.academic_education import AcademicEducation, EducationType
from research_domain.domain.entities.researcher import Researcher
from eo_lib.domain.entities import Organization

class TestAcademicEducation:
    @pytest.fixture
    def researcher(self):
        return Researcher(name="Dr. Test", id=1)

    @pytest.fixture
    def edu_type(self):
        return EducationType(name="PhD", id=10)
        
    @pytest.fixture
    def university(self):
        return Organization(name="MIT", id=100)
        
    @pytest.fixture
    def advisor(self):
        return Researcher(name="Advisor", id=2)

    def test_create_academic_education_refactored(self, researcher, edu_type, university, advisor):
        education = AcademicEducation(
            researcher_id=researcher.id,
            education_type_id=edu_type.id,
            title="PhD in CS",
            institution_id=university.id,
            start_year=2020,
            end_year=2024,
            advisor_id=advisor.id
        )
        
        assert education.researcher_id == 1
        assert education.education_type_id == 10
        assert education.title == "PhD in CS"
        assert education.institution_id == 100
        assert education.advisor_id == 2
        assert education.co_advisor_id is None
