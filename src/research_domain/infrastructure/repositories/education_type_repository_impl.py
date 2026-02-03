from sqlalchemy.orm import Session
from libbase.infrastructure.sql_repository import GenericSqlRepository
from research_domain.domain.entities.academic_education import EducationType
from research_domain.domain.repositories.education_type_repository import IEducationTypeRepository

class EducationTypeRepositoryImpl(GenericSqlRepository[EducationType], IEducationTypeRepository):
    """
    SQLAlchemy implementation of EducationType Repository.
    """
    def __init__(self, session: Session):
        super().__init__(session, EducationType)
