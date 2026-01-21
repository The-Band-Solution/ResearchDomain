from eo_lib.domain.base import Base
from eo_lib.domain.entities import Initiative
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

# Association Table for Many-to-One
# One Initiative has One Demandante.
# One Organization can be Demandante for Many Initiatives.
# We enforce unique on initiative_id to ensure 1-to-1 from Initiative side.
initiative_demandantes = Table(
    "initiative_demandantes",
    Base.metadata,
    Column(
        "initiative_id",
        Integer,
        ForeignKey("initiatives.id"),
        primary_key=True,
    ),
    Column(
        "organization_id",
        Integer,
        ForeignKey("organizations.id"),
        nullable=False,
    ),
    # Organization refers to "organizations" table.
)

# Runtime injection
if not hasattr(Initiative, "demandante"):
    Initiative.demandante = relationship(
        "Organization",
        secondary=initiative_demandantes,
        uselist=False,  # One-to-One scalar access
        backref="requested_initiatives",
    )
