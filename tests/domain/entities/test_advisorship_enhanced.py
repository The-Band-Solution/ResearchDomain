import pytest
from datetime import date
from unittest.mock import MagicMock
from research_domain.domain.entities.advisorship import Advisorship, AdvisorshipType

class TestAdvisorshipEnhanced:
    def test_create_advisorship_with_new_fields(self):
        adv = Advisorship(
            name="PhD Thesis Supervision",
            type=AdvisorshipType.PHD_THESIS,
            program="Computer Science",
            defense_date=date(2026, 12, 1),
            start_date=date(2024, 1, 1)
        )
        assert adv.type == AdvisorshipType.PHD_THESIS
        assert adv.type.value == "PhD Thesis"
        assert adv.program == "Computer Science"
        assert adv.defense_date == date(2026, 12, 1)

    def test_create_advisorship_pibicjr(self):
        adv = Advisorship(
            name="PIBIC Jr",
            type=AdvisorshipType.JUNIOR_SCIENTIFIC_INITIATION
        )
        assert adv.type == AdvisorshipType.JUNIOR_SCIENTIFIC_INITIATION
