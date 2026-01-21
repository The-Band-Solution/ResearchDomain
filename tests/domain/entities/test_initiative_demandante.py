import pytest
from eo_lib.domain.entities import Initiative, Organization

# We need to import the module to trigger the relationship injection
import research_domain.domain.entities.initiative_demandante
from research_domain.domain.entities.initiative_demandante import \
    initiative_demandantes


def test_initiative_demandante_association():
    """Test associating an Initiative with a Demandante (Organization)."""
    # Create Organization (Demandante)
    org1 = Organization(name="Funding Agency A")
    org2 = Organization(name="Tech Corp B")

    # Create Initiatives
    init1 = Initiative(name="Project X", description="Research X")
    init2 = Initiative(name="Project Y", description="Research Y")

    # Associate
    # Since we injected 'demandante' property on Initiative
    init1.demandante = org1
    init2.demandante = org2

    # Verify
    assert init1.demandante == org1
    assert init2.demandante == org2

    # Verify backref if we defined it (e.g., requested_initiatives)
    assert init1 in org1.requested_initiatives
    assert init2 in org2.requested_initiatives

    # Re-assign
    init1.demandante = org2
    assert init1.demandante == org2
    assert init1 in org2.requested_initiatives
    # Should be removed from org1 list if it's 1-to-N properly managed by ORM,
    # but with secondary tables sometimes list semantics apply.
    # However, we used uselist=False for initiative.demandante, so it behaves like scalar.
    # checking if it was removed from org1 might depend on autoflush/commit state
    # but in memory objects it should update.
    assert init1 not in org1.requested_initiatives
