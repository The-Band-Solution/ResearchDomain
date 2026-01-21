from typing import Optional

from eo_lib.domain.base import Base
from eo_lib.domain.entities import Team
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

# Association Table
initiative_external_groups = Table(
    "initiative_external_groups",
    Base.metadata,
    Column(
        "initiative_id",
        Integer,
        ForeignKey("initiatives.id"),
        primary_key=True,
    ),
    Column(
        "group_id",
        Integer,
        ForeignKey("external_research_groups.id"),
        primary_key=True,
    ),
)


class ExternalResearchGroup(Team):
    """
    ExternalResearchGroup Model.

    Represents a research group from an external institution associated
    with an initiative. Inherits from Team.
    """

    __tablename__ = "external_research_groups"

    id = Column(Integer, ForeignKey("teams.id"), primary_key=True)
    contact_email = Column(String, nullable=True)

    initiatives = relationship(
        "Initiative",
        secondary=initiative_external_groups,
        backref="external_groups",
    )

    def __init__(
        self,
        name: str,
        contact_email: Optional[str] = None,
        description: Optional[str] = None,
        short_name: Optional[str] = None,
        organization_id: Optional[int] = None,
        id: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            description=description,
            short_name=short_name,
            organization_id=organization_id,
            id=id,
        )
        self.contact_email = contact_email
