from datetime import date

import pytest
from eo_lib.domain.entities import Initiative, Person, Role

from research_domain.domain.entities.advisorship import Advisorship, AdvisorshipRole
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


def test_advisorship_roles_student_supervisor():
    """Test that Advisorship correctly links to Student and Supervisor via Roles."""
    student = Person(name="Alice Student")
    supervisor = Person(name="Dr. Bob")
    
    # Mock Roles for testing context (In real app, these come from DB)
    role_student = Role(name=AdvisorshipRole.STUDENT.value)
    role_supervisor = Role(name=AdvisorshipRole.SUPERVISOR.value)

    advisorship = Advisorship(
        name="Advisorship 2025",
        start_date=date(2025, 1, 1),
    )
    
    # Use generic Team/Initiative methods to add members
    advisorship.add_member(person=student, role=role_student)
    advisorship.add_member(person=supervisor, role=role_supervisor)

    # Check via convenience properties
    assert advisorship.student == student
    assert advisorship.supervisor == supervisor
    assert advisorship.start_date == date(2025, 1, 1)


def test_advisorship_board_members():
    """Test adding Board Members using Roles."""
    advisorship = Advisorship(name="Board Exam")
    member1 = Person(name="Prof. External")
    member2 = Person(name="Prof. Internal")
    
    role_board = Role(name=AdvisorshipRole.BOARD_MEMBER.value)
    
    advisorship.add_member(member1, role_board)
    advisorship.add_member(member2, role_board)
    
    assert len(advisorship.board_members) == 2
    assert member1 in advisorship.board_members
    assert member2 in advisorship.board_members


def test_advisorship_with_fellowship():
    """Test that Advisorship correctly links to Fellowship."""
    student = Person(name="Charlie")
    role_student = Role(name=AdvisorshipRole.STUDENT.value)
    
    fellowship = Fellowship(name="PIBIC", value=700.0, sponsor_id=1)

    advisorship = Advisorship(
        name="Fellowship Advisorship",
        fellowship=fellowship,
        start_date=date(2023, 1, 1),
    )
    advisorship.add_member(student, role_student)

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


def test_advisorship_cancellation():
    """Test that Advisorship can be cancelled and stores the cancellation date."""
    cancellation_date = date(2025, 6, 1)
    advisorship = Advisorship(
        name="Cancelled Project",
        cancelled=True,
        cancellation_date=cancellation_date,
    )

    assert advisorship.cancelled is True
    assert advisorship.cancellation_date == cancellation_date
