import pytest
from unittest.mock import MagicMock
from research_domain.domain.entities.academic_education import AcademicEducation, EducationType
from research_domain.domain.entities.researcher import Researcher
from research_domain.domain.repositories import AcademicEducationRepositoryInterface as IAcademicEducationRepository

class TestAcademicEducationRepository:
    def test_repository_interface(self):
        """Ensure Protocol/Interface is defined correctly"""
        # This is a bit meta, but ensures the interface exists and has methods
        assert hasattr(IAcademicEducationRepository, "add")
        assert hasattr(IAcademicEducationRepository, "list_by_researcher")

class TestAcademicEducationService:
    @pytest.fixture
    def mock_repo(self):
        return MagicMock(spec=IAcademicEducationRepository)

    def test_create_education(self, mock_repo):
        from research_domain.services import AcademicEducationService
        
        service = AcademicEducationService(repository=mock_repo)
        
        # Mock repo side effect to set ID
        def add_side_effect(edu):
            edu.id = 1
            return edu
        mock_repo.add.side_effect = add_side_effect
        
        result = service.create_education(
            researcher_id=1,
            education_type_id=1,
            title="PhD",
            institution_id=100,
            start_year=2020
        )
        
        assert result.id == 1
        assert result.title == "PhD"
        mock_repo.add.assert_called_once()

class TestAcademicEducationController:
    @pytest.fixture
    def mock_service(self):
        # We'll mock the service factory or just the service instance
        return MagicMock()

    def test_add_education(self, mock_service):
        from research_domain.controllers import AcademicEducationController
        
        controller = AcademicEducationController()
        controller._service = mock_service
        
        # Mock service return
        mock_service.create_education.return_value = AcademicEducation(
            id=1, researcher_id=1, education_type_id=1,
            title="PhD", institution_id=100, start_year=2020
        )
        
        result = controller.create_academic_education(
            researcher_id=1,
            education_type_id=1,
            title="PhD",
            institution_id=100,
            start_year=2020
        )
        
        assert result.id == 1
        assert result.title == "PhD"
        mock_service.create_education.assert_called_once() 
