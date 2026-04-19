from datetime import date

from eo_lib.domain.entities import Organization

from research_domain.domain.entities.fellowship import Fellowship


def test_fellowship_creation():
    """Test creating a Fellowship instance."""
    fellowship = Fellowship(
        name="PIBITI",
        value=700.0,
        description="Technological Innovation Fellowship",
    )

    assert fellowship.name == "PIBITI"
    assert fellowship.value == 700.0
    assert fellowship.description == "Technological Innovation Fellowship"
    assert fellowship.sponsor_id is None
    assert fellowship.cancelled is False
    assert fellowship.cancellation_date is None


def test_fellowship_serialization():
    """Test serializing a Fellowship instance to dict."""
    fellowship = Fellowship(name="IC", value=400.0, id=5, sponsor_id=1)

    data = fellowship.to_dict()
    assert data["name"] == "IC"
    assert data["value"] == 400.0
    assert data["id"] == 5
    assert data["sponsor_id"] == 1
    assert data["cancelled"] is False
    assert data["cancellation_date"] is None


def test_fellowship_can_be_created_as_cancelled():
    """Test creating a cancelled Fellowship with a cancellation date."""
    cancellation_date = date(2026, 4, 19)

    fellowship = Fellowship(
        name="PIBIC",
        value=700.0,
        cancelled=True,
        cancellation_date=cancellation_date,
    )

    assert fellowship.cancelled is True
    assert fellowship.cancellation_date == cancellation_date


def test_fellowship_with_sponsor():
    """Test creating a Fellowship with a sponsor organization."""
    sponsor = Organization(name="CNPq")
    fellowship = Fellowship(
        name="PIBIC",
        value=700.0,
        description="Scientific Initiation",
        sponsor=sponsor,
    )

    assert fellowship.sponsor == sponsor
    assert fellowship.name == "PIBIC"


def test_fellowship_with_sponsor_id():
    """Test creating a Fellowship with sponsor_id."""
    fellowship = Fellowship(name="PIBIC", value=700.0, sponsor_id=10)

    assert fellowship.sponsor_id == 10
    assert fellowship.value == 700.0


def test_fellowship_serialization_with_sponsor():
    """Test serializing a Fellowship with a sponsor to dict."""
    fellowship = Fellowship(name="IC", value=400.0, id=5, sponsor_id=2)

    data = fellowship.to_dict()
    assert data["name"] == "IC"
    assert data["value"] == 400.0
    assert data["id"] == 5
    assert data["sponsor_id"] == 2
