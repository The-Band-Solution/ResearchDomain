from typing import List, Optional

from eo_lib.domain.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin

# Association Table for Many-to-Many relationship between ResearchProduction and Researcher (Authors)
production_authors = Table(
    "production_authors",
    Base.metadata,
    Column("production_id", Integer, ForeignKey("research_productions.id"), primary_key=True),
    Column("researcher_id", Integer, ForeignKey("researchers.id"), primary_key=True),
)

class ResearchProduction(Base, SerializableMixin):
    """
    Research Production Entity.
    Represents academic outputs like Books, Chapters, and Software.
    """
    __tablename__ = "research_productions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    year = Column(Integer, nullable=False)
    
    production_type_id = Column(Integer, ForeignKey("production_types.id"), nullable=False)
    
    # Generic fields
    publisher = Column(String(255), nullable=True)
    isbn = Column(String(100), nullable=True)
    edition = Column(String(100), nullable=True)
    book_title = Column(String(500), nullable=True)
    pages = Column(String(100), nullable=True)
    version = Column(String(100), nullable=True)
    platform = Column(String(100), nullable=True)
    link = Column(String(500), nullable=True)

    # Relationships
    production_type = relationship("ProductionType")
    authors = relationship(
        "Researcher",
        secondary=production_authors,
        back_populates="productions",
        lazy="joined"
    )

    def __init__(
        self,
        title: str,
        year: int,
        production_type: Optional[object] = None,
        production_type_id: Optional[int] = None,
        authors: Optional[List] = None,
        publisher: Optional[str] = None,
        isbn: Optional[str] = None,
        edition: Optional[str] = None,
        book_title: Optional[str] = None,
        pages: Optional[str] = None,
        version: Optional[str] = None,
        platform: Optional[str] = None,
        link: Optional[str] = None,
        id: Optional[int] = None,
        **kwargs
    ):
        self.id = id
        self.title = title
        self.year = year
        self.production_type_id = production_type_id
        if production_type:
            self.production_type = production_type
            if hasattr(production_type, 'id'):
                self.production_type_id = production_type.id
        
        self.publisher = publisher
        self.isbn = isbn
        self.edition = edition
        self.book_title = book_title
        self.pages = pages
        self.version = version
        self.platform = platform
        self.link = link
        
        if authors:
            self.authors = authors
