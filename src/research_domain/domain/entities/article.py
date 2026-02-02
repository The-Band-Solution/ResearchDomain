import enum
from typing import List, Optional

from eo_lib.domain.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Table, UniqueConstraint, Enum
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin

class ArticleType(enum.Enum):
    JOURNAL = "Journal"
    CONFERENCE_EVENT = "Conference Event"

# Association Table for Many-to-Many relationship between Article and Researcher (Authors)
article_authors = Table(
    "article_authors",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id"), primary_key=True),
    Column("researcher_id", Integer, ForeignKey("researchers.id"), primary_key=True),
)

class Article(Base, SerializableMixin):
    """
    Scientific Article Entity.
    Represents a scientific publication with multiple authors.
    """
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    doi = Column(String(255), nullable=True)
    year = Column(Integer, nullable=False)
    
    type = Column(Enum(ArticleType), nullable=False)
    
    journal_conference = Column(String(255), nullable=True)
    volume = Column(String(100), nullable=True)
    pages = Column(String(100), nullable=True)

    # Relationships
    authors = relationship(
        "Researcher",
        secondary=article_authors,
        back_populates="articles",
        lazy="joined"
    )

    def __init__(
        self,
        title: str,
        year: int,
        type: ArticleType,
        authors: Optional[List] = None,
        doi: Optional[str] = None,
        journal_conference: Optional[str] = None,
        volume: Optional[str] = None,
        pages: Optional[str] = None,
        id: Optional[int] = None,
        **kwargs
    ):
        self.id = id
        self.title = title
        self.year = year
        self.type = type
        self.doi = doi
        self.journal_conference = journal_conference
        self.volume = volume
        self.pages = pages
        
        if authors:
            self.authors = authors
