import pytest

from research_domain.domain.entities.fellowship import Fellowship


def test_fellowship_creation():
    """Test creating a Fellowship instance."""
    fellowship = Fellowship(
        name="PIBITI", value=700.0, description="Technological Innovation Fellowship"
    )

    assert fellowship.name == "PIBITI"
    assert fellowship.value == 700.0
    assert fellowship.description == "Technological Innovation Fellowship"


def test_fellowship_serialization():
    """Test serializing a Fellowship instance to dict."""
    fellowship = Fellowship(name="IC", value=400.0, id=5)

    data = fellowship.to_dict()
    assert data["name"] == "IC"
    assert data["value"] == 400.0
    assert data["id"] == 5
