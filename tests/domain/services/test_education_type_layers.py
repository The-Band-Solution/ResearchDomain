import pytest
from unittest.mock import MagicMock
from research_domain.domain.entities.academic_education import EducationType
from research_domain.services.education_type_service import EducationTypeService
from research_domain.controllers.education_type_controller import EducationTypeController
from research_domain.domain.repositories.education_type_repository import IEducationTypeRepository

class TestEducationTypeLayers:
    @pytest.fixture
    def mock_repo(self):
        return MagicMock(spec=IEducationTypeRepository)

    @pytest.fixture
    def service(self, mock_repo):
        return EducationTypeService(mock_repo)

    @pytest.fixture
    def controller(self, service):
        return EducationTypeController(service)

    def test_create_education_type_service(self, service, mock_repo):
        # Arrange
        # GenericService.create is void, so no return value needed for add
        
        # Act
        result = service.create_education_type("PhD")

        # Assert
        assert result.name == "PhD"
        # assert result.id == 1 # Mock doesn't simulate DB autoincrement
        mock_repo.add.assert_called_once()

    def test_get_by_name_service(self, service, mock_repo):
        # Arrange
        et1 = EducationType(name="PhD", id=1)
        et2 = EducationType(name="Master", id=2)
        mock_repo.get_all.return_value = [et1, et2]

        # Act
        found = service.get_by_name("Master")
        not_found = service.get_by_name("Bachelors")

        # Assert
        assert found == et2
        assert not_found is None

    def test_controller_create_success(self, controller, service, mock_repo):
        # Arrange
        service.create_education_type = MagicMock(return_value=EducationType(name="Master", id=2))

        # Act
        response = controller.create_education_type(name="Master")

        # Assert
        assert response["success"] is True
        assert response["education_type"]["name"] == "Master"
        assert response["education_type"]["id"] == 2

    def test_controller_list_types(self, controller, service, mock_repo):
        # Arrange
        service.get_all = MagicMock(return_value=[
            EducationType(name="PhD", id=1),
            EducationType(name="Master", id=2)
        ])

        # Act
        response = controller.list_education_types()

        # Assert
        assert response["success"] is True
        assert len(response["education_types"]) == 2
        assert response["education_types"][0]["name"] == "PhD"
