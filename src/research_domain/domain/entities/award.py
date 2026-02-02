from typing import Optional

from eo_lib.domain.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin


class Award(Base, SerializableMixin):
    """
    Award Entity.
    Represents an award or title received by a researcher.
    """
    __tablename__ = "awards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    researcher_id = Column(Integer, ForeignKey("researchers.id"), nullable=False)
    title = Column(String(255), nullable=False)
    year = Column(Integer, nullable=True)

    # Relationships
    researcher = relationship("Researcher", back_populates="awards")

    def __init__(
        self,
        researcher_id: int,
        title: str,
        year: Optional[int] = None,
        id: Optional[int] = None,
        **kwargs
    ):
        self.id = id
        self.researcher_id = researcher_id
        self.title = title
        self.year = year
