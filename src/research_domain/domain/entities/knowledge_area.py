from typing import Optional

from eo_lib.domain.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

# Association Table for Many-to-Many relationship between
# KnowledgeArea and Initiative
initiative_knowledge_areas = Table(
    "initiative_knowledge_areas",
    Base.metadata,
    Column(
        "initiative_id",
        Integer,
        ForeignKey("initiatives.id"),
        primary_key=True,
    ),
    Column("area_id", Integer, ForeignKey("knowledge_areas.id"), primary_key=True),
)


class KnowledgeArea(Base):
    """
    KnowledgeArea Model.

    Represents a thematic area or field of study for research groups.
    """

    __tablename__ = "knowledge_areas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    # Relationships
    initiatives = relationship(
        "Initiative",
        secondary=initiative_knowledge_areas,
        backref="knowledge_areas",
    )

    def __init__(self, name: str, id: Optional[int] = None):
        """
        Initializes a new KnowledgeArea instance.

        Args:
            name (str): Unique name of the knowledge area.
            id (int, optional): Database ID for existing records.
        """
        self.name = name
        if id:
            self.id = id
