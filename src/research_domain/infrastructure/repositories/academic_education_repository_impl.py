from typing import List, Optional

from eo_lib.infrastructure.repositories.base_repository import BaseRepository
from sqlalchemy.orm import Session

from research_domain.domain.entities.academic_education import AcademicEducation
from research_domain.domain.repositories.academic_education_repository import IAcademicEducationRepository


class AcademicEducationRepository(BaseRepository[AcademicEducation], IAcademicEducationRepository):
    """
    SQLAlchemy implementation of AcademicEducationRepository.
    Inherits generic CRUD from BaseRepository.
    """
    def __init__(self, session: Session):
        super().__init__(session, AcademicEducation)

    def add(self, education: AcademicEducation) -> AcademicEducation:
        # Base implementation might need override if special handling required, 
        # but generic add usually works for simple entities.
        return super().add(education)

    def list_by_researcher(self, researcher_id: int) -> List[AcademicEducation]:
        return self.session.query(AcademicEducation).filter_by(researcher_id=researcher_id).all()
