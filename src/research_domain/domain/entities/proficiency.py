import enum
from typing import Optional

from eo_lib.domain.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin


class ProficiencyLevel(enum.Enum):
    BASICO = "Basico"
    MEDIO = "Medio"
    ALTO = "Alto"
    NAO_SE_APLICA = "NaoSeAplica"


class Proficiency(Base, SerializableMixin):
    """
    Language Proficiency Entity.
    Links a Researcher to a Language with specific skill levels.
    """
    __tablename__ = "proficiencies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    researcher_id = Column(Integer, ForeignKey("researchers.id"), nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    
    comprehension = Column(Enum(ProficiencyLevel), nullable=True)
    speaking = Column(Enum(ProficiencyLevel), nullable=True)
    reading = Column(Enum(ProficiencyLevel), nullable=True)
    writing = Column(Enum(ProficiencyLevel), nullable=True)

    # Relationships
    researcher = relationship("Researcher", back_populates="proficiencies")
    language = relationship("Language")

    def __init__(
        self,
        researcher_id: int,
        language_id: int,
        comprehension: Optional[ProficiencyLevel] = None,
        speaking: Optional[ProficiencyLevel] = None,
        reading: Optional[ProficiencyLevel] = None,
        writing: Optional[ProficiencyLevel] = None,
        id: Optional[int] = None,
        **kwargs
    ):
        self.id = id
        self.researcher_id = researcher_id
        self.language_id = language_id
        self.comprehension = comprehension
        self.speaking = speaking
        self.reading = reading
        self.writing = writing
