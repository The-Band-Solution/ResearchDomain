from typing import List, Optional

from eo_lib.domain.base import Base
from eo_lib.domain.entities import Person
from sqlalchemy import Column, ForeignKey, Integer, String, Table, JSON
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin
# Use string forward reference to avoid circular import issues if possible, 
# but for foreign_keys resolution we might need the class or specific string syntax.
# Let's try importing inside the file but after imports? 
# Actually, let's use the string syntax "AcademicEducation.researcher_id" and ensure the class is available 
# OR just import it here if academic_education doesn't import Researcher.
# academic_education.py DOES NOT import Researcher (uses string). So we can import it.
from research_domain.domain.entities.academic_education import AcademicEducation
from research_domain.domain.entities.article import Article # Make sure Article is registered

# Association Table for Many-to-Many relationship between Researcher and KnowledgeArea
researcher_knowledge_areas = Table(
    "researcher_knowledge_areas",
    Base.metadata,
    Column("researcher_id", Integer, ForeignKey("researchers.id"), primary_key=True),
    Column("area_id", Integer, ForeignKey("knowledge_areas.id"), primary_key=True),
)


class Researcher(Person, SerializableMixin):
    """
    Researcher Model.

    A Researcher represents a person in the research domain, extending eo_lib Person.
    It includes academic metadata like CNPq and Google Scholar links.
    """

    __tablename__ = "researchers"

    id = Column(Integer, ForeignKey("persons.id"), primary_key=True)
    cnpq_url = Column(String(255), nullable=True)
    google_scholar_url = Column(String(255), nullable=True)
    # Storing list of strings as JSON/ARRAY. 
    # Using JSON for better compatibility with SQLite (testing) and Postgres.
    
    citation_names = Column(String(500), nullable=True) # Separated by semicolon

    # Relationships
    knowledge_areas = relationship(
        "KnowledgeArea", secondary=researcher_knowledge_areas, lazy="joined"
    )
    academic_educations = relationship(
        "AcademicEducation",
        back_populates="researcher",
        cascade="all, delete-orphan",
        foreign_keys=[AcademicEducation.researcher_id]
    )
    proficiencies = relationship(
        "Proficiency",
        back_populates="researcher",
        cascade="all, delete-orphan"
    )
    awards = relationship(
        "Award",
        back_populates="researcher",
        cascade="all, delete-orphan"
    )
    articles = relationship(
        "Article",
        # We need article_authors here. If we can't import it at top, we can use string "article_authors" 
        # IF it is in the same metadata/registry. But typically secondary expects the Table object.
        # Let's import it inside the file but correctly.
        secondary="article_authors", 
        back_populates="authors",
        lazy="joined"
    )

    def __init__(
        self,
        name: str,
        cnpq_url: Optional[str] = None,
        google_scholar_url: Optional[str] = None,
        citation_names: Optional[str] = None,
        knowledge_areas: Optional[List] = None,
        articles: Optional[List] = None, # Add to init
        id: Optional[int] = None,
        **kwargs,
    ):
        """
        Initializes a new Researcher instance.
        """
        super().__init__(name=name, id=id, **kwargs)
        self.cnpq_url = cnpq_url
        self.google_scholar_url = google_scholar_url
        self.citation_names = citation_names
        
        if knowledge_areas:
            self.knowledge_areas = knowledge_areas
        if articles:
            self.articles = articles
