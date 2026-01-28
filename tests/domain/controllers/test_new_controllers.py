import os
from datetime import date

os.environ["STORAGE_TYPE"] = "memory"

from research_domain.controllers.controllers import (AdvisorshipController,
                                                     FellowshipController)


def test_fellowship_controller_creation():
    controller = FellowshipController()

    created = controller.create_fellowship(
        name="PIBIC", value=700.0, description="Test Fellowship"
    )
    assert created.id is not None
    assert created.name == "PIBIC"
    assert created.value == 700.0

    retrieved = controller.get_by_id(created.id)
    assert retrieved.name == "PIBIC"


def test_advisorship_controller_creation():
    controller = AdvisorshipController()

    created = controller.create_advisorship(
        name="Test Advisorship",
        start_date=date(2025, 1, 1),
        description="Test Description",
    )
    assert created.id is not None
    assert created.name == "Test Advisorship"
    assert created.start_date == date(2025, 1, 1)

    retrieved = controller.get_by_id(created.id)
    assert retrieved.name == "Test Advisorship"
