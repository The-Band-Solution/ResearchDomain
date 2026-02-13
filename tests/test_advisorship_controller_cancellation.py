from datetime import date
from unittest.mock import MagicMock

import pytest

from research_domain.controllers.controllers import AdvisorshipController
from research_domain.domain.entities.advisorship import Advisorship
from research_domain.factories import ServiceFactory


def test_controller_create_advisorship_with_cancellation():
    """Test that controller correctly passes cancellation fields to the entity."""
    controller = AdvisorshipController()

    # Mock the service
    mock_service = MagicMock()
    controller._service = mock_service

    cancellation_date = date(2025, 1, 1)

    # Configure mock return value to match input mostly, or just return a dummy
    mock_service.create_advisorship.return_value = Advisorship(
        name="Test Project", cancelled=True, cancellation_date=cancellation_date
    )
    advisorship = controller.create_advisorship(
        name="Test Project", cancelled=True, cancellation_date=cancellation_date
    )

    assert advisorship.name == "Test Project"
    # assert advisorship.cancelled is True # This depends on mock return
    # assert advisorship.cancellation_date == cancellation_date

    mock_service.create_advisorship.assert_called_once_with(
        name="Test Project",
        student_id=None,
        supervisor_id=None,
        fellowship_id=None,
        start_date=None,
        end_date=None,
        description=None,
        status="active",
        cancelled=True,
        cancellation_date=cancellation_date,
    )


def test_controller_cancel_advisorship():
    """Test that controller's cancel_advisorship method works."""
    controller = AdvisorshipController()

    # We need to mock the service because cancel_advisorship calls self._service.cancel_advisorship
    mock_service = MagicMock()
    controller._service = mock_service

    cancellation_date = date(2025, 12, 31)
    controller.cancel_advisorship(advisorship_id=1, cancellation_date=cancellation_date)

    mock_service.cancel_advisorship.assert_called_once_with(1, cancellation_date)
