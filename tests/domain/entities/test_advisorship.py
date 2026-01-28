from datetime import date

import pytest
from eo_lib.domain.entities import Initiative, Person

from research_domain.domain.entities.advisorship import Advisorship
from research_domain.domain.entities.fellowship import Fellowship


def test_advisorship_inheritance():
    """Test that Advisorship inherits from Initiative and has its own attributes."""
    advisorship = Advisorship(
        name="Study AI",
        description="Deep learning research",
        start_date=date(2025, 1, 1),
    )

    assert isinstance(advisorship, Initiative)
    assert advisorship.name == "Study AI"
    assert advisorship.description == "Deep learning research"


def test_advisorship_relationships():
    """Test that Advisorship correctly links to Student (Person) and Supervisor (Person)."""
    student = Person(name="Alice Student")
    supervisor = Person(name="Dr. Bob")

    advisorship = Advisorship(
        name="Advisorship 2025",
        student=student,
        supervisor=supervisor,
        start_date=date(2025, 1, 1),
    )

    assert advisorship.student == student
    assert advisorship.supervisor == supervisor
    assert advisorship.start_date == date(2025, 1, 1)


def test_advisorship_with_fellowship():
    """Test that Advisorship correctly links to Fellowship."""
    student = Person(name="Charlie")
    supervisor = Person(name="Dr. Dave")
    fellowship = Fellowship(name="PIBIC", value=700.0, sponsor_id=1)

    advisorship = Advisorship(
        name="Fellowship Advisorship",
        student=student,
        supervisor=supervisor,
        fellowship=fellowship,
        start_date=date(2023, 1, 1),
    )

    assert advisorship.student == student
    assert advisorship.fellowship == fellowship
    assert advisorship.is_volunteer is False


def test_advisorship_volunteer():
    """Test that Advisorship without fellowship is voluntary."""
    advisorship = Advisorship(
        name="Volunteer Project",
        start_date=date(2024, 1, 1),
    )

    assert advisorship.fellowship is None
    assert advisorship.is_volunteer is True


def test_advisorship_serialization():
    """Test that Advisorship correctly serializes to dict."""
    student_id = 10
    supervisor_id = 20
    fellowship_id = 30

    advisorship = Advisorship(
        name="Serialized Advisorship",
        student_id=student_id,
        supervisor_id=supervisor_id,
        fellowship_id=fellowship_id,
        start_date=date(2023, 1, 1),
    )

    data = advisorship.to_dict()
    assert data["name"] == "Serialized Advisorship"
    assert data["student_id"] == 10
    assert data["supervisor_id"] == 20
    assert data["fellowship_id"] == 30
    assert data["start_date"] == date(2023, 1, 1)
