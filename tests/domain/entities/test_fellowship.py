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


def test_fellowship_serialization():
    """Test serializing a Fellowship instance to dict."""
    fellowship = Fellowship(name="IC", value=400.0, id=5)

    data = fellowship.to_dict()
    assert data["name"] == "IC"
    assert data["value"] == 400.0
    assert data["id"] == 5


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
