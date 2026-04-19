import os
from unittest.mock import MagicMock

import pytest

os.environ["STORAGE_TYPE"] = "memory"

from research_domain.controllers import ProfessionalActivityController
from research_domain.domain.entities.professional_activity import ProfessionalActivity
from research_domain.domain.repositories import (
    ProfessionalActivityRepositoryInterface as IProfessionalActivityRepository,
)
from research_domain.services import ProfessionalActivityService


class TestProfessionalActivityRepository:
    def test_repository_interface(self):
        assert hasattr(IProfessionalActivityRepository, "add")
        assert hasattr(IProfessionalActivityRepository, "list_by_researcher")


class TestProfessionalActivityService:
    @pytest.fixture
    def mock_repo(self):
        return MagicMock(spec=IProfessionalActivityRepository)

    @pytest.fixture
    def service(self, mock_repo):
        return ProfessionalActivityService(mock_repo)

    def test_create_activity(self, service, mock_repo):
        result = service.create_activity(
            researcher_id=1,
            institution="Instituto Federal do Espírito Santo, IFES, Brasil.",
            institution_name="Instituto Federal do Espírito Santo",
            institution_acronym="IFES",
            start_year=2012,
            current=True,
        )

        assert result.researcher_id == 1
        assert result.institution_name == "Instituto Federal do Espírito Santo"
        assert result.current is True
        mock_repo.add.assert_called_once()

    def test_create_from_dict(self, service, mock_repo):
        payload = {
            "instituicao": "Instituto Federal do Espírito Santo, IFES, Brasil.",
            "instituicao_nome": "Instituto Federal do Espírito Santo",
            "instituicao_sigla": "IFES",
            "ano_inicio": "2012",
            "ano_fim": "Atual",
        }

        result = service.create_from_dict(researcher_id=1, data=payload)

        assert result.institution == payload["instituicao"]
        assert result.current is True
        mock_repo.add.assert_called_once()

    def test_get_by_researcher(self, service, mock_repo):
        mock_repo.list_by_researcher.return_value = [
            ProfessionalActivity(
                researcher_id=1,
                institution="Instituto Federal do Espírito Santo, IFES, Brasil.",
            )
        ]

        result = service.get_by_researcher(1)

        assert len(result) == 1
        assert result[0].researcher_id == 1
        mock_repo.list_by_researcher.assert_called_once_with(1)


class TestProfessionalActivityController:
    @pytest.fixture
    def mock_service(self):
        return MagicMock()

    def test_create_professional_activity(self, mock_service):
        controller = ProfessionalActivityController()
        controller._service = mock_service

        mock_service.create_activity.return_value = ProfessionalActivity(
            id=1,
            researcher_id=1,
            institution="Instituto Federal do Espírito Santo, IFES, Brasil.",
        )

        result = controller.create_professional_activity(
            researcher_id=1,
            institution="Instituto Federal do Espírito Santo, IFES, Brasil.",
        )

        assert result.id == 1
        assert result.researcher_id == 1
        mock_service.create_activity.assert_called_once()

    def test_list_history(self, mock_service):
        controller = ProfessionalActivityController()
        controller._service = mock_service

        mock_service.get_by_researcher.return_value = [
            ProfessionalActivity(
                id=1,
                researcher_id=1,
                institution="Instituto Federal do Espírito Santo, IFES, Brasil.",
            )
        ]

        result = controller.list_history(1)

        assert len(result) == 1
        assert result[0].id == 1
        mock_service.get_by_researcher.assert_called_once_with(1)
