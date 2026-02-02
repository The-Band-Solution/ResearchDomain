from typing import List, Optional

from research_domain.domain.entities.academic_education import AcademicEducation
from research_domain.domain.repositories.academic_education_repository import IAcademicEducationRepository


class AcademicEducationService:
    """
    Service for managing Academic Education history.
    """

    def __init__(self, repository: IAcademicEducationRepository):
        self.repository = repository

    def create_education(
        self,
        researcher_id: int,
        education_type_id: int,
        title: str,
        institution_id: int,
        start_year: int,
        end_year: Optional[int] = None,
        thesis_title: Optional[str] = None,
        advisor_id: Optional[int] = None,
        co_advisor_id: Optional[int] = None,
        knowledge_areas: list = None
    ) -> AcademicEducation:
        """
        Creates and persists a new academic education record.
        """
        education = AcademicEducation(
            researcher_id=researcher_id,
            education_type_id=education_type_id,
            title=title,
            institution_id=institution_id,
            start_year=start_year,
            end_year=end_year,
            thesis_title=thesis_title,
            advisor_id=advisor_id,
            co_advisor_id=co_advisor_id,
            knowledge_areas=knowledge_areas
        )
        
        return self.repository.add(education)

    def get_by_researcher(self, researcher_id: int) -> List[AcademicEducation]:
        """
        Retrieves all education records for a researcher.
        """
        return self.repository.list_by_researcher(researcher_id)
        
    def delete_education(self, education_id: int) -> bool:
        """
        Deletes an education record.
        """
        return self.repository.delete(education_id)
