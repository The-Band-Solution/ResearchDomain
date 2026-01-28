from typing import Optional

from eo_lib.domain.base import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin


class Fellowship(Base, SerializableMixin):
    """
    Fellowship Model.

    Represents a scholarship or funding for a student in an advisorship.
    A fellowship can have a sponsor organization that provides the funding.
    """

    __tablename__ = "fellowships"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    value = Column(Float, nullable=False)
    sponsor_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)

    # Relationships
    sponsor = relationship("Organization", foreign_keys=[sponsor_id])

    def __init__(
        self,
        name: str,
        value: float,
        description: Optional[str] = None,
        sponsor_id: Optional[int] = None,
        sponsor: Optional[object] = None,
        id: Optional[int] = None,
        **kwargs,
    ):
        """
        Initializes a new Fellowship instance.

        Args:
            name: Name of the fellowship
            value: Monetary value of the fellowship
            description: Optional description
            sponsor_id: Optional ID of the sponsoring organization
            sponsor: Optional sponsor Organization object
            id: Optional fellowship ID
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.value = value
        self.description = description
        self.sponsor_id = sponsor_id
        self.sponsor = sponsor
