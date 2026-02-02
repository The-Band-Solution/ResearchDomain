from typing import List, Optional

from research_domain.domain.entities.academic_education import AcademicEducation
from research_domain.services.academic_education_service import AcademicEducationService
# Assuming we have a way to get the service, for now we inject or use a factory pattern if available
# But per standard simple controller pattern:

class AcademicEducationController:
    """
    Controller for Academic Education operations.
    """
    
    def __init__(self, service: AcademicEducationService = None):
        # In a real app, this would use dependency injection or a Factory
        # For simplicity/testability, allowing injection.
        self.service = service

    def add_education(
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
    ) -> AcademicEducation:
        """
        Adds a new education entry to a researcher's profile.
        """
        if not self.service:
            raise RuntimeError("Service not initialized")
            
        return self.service.create_education(
            researcher_id=researcher_id,
            education_type_id=education_type_id,
            title=title,
            institution_id=institution_id,
            start_year=start_year,
            end_year=end_year,
            thesis_title=thesis_title,
            advisor_id=advisor_id,
            co_advisor_id=co_advisor_id
        )

    def list_history(self, researcher_id: int) -> List[AcademicEducation]:
        """
        Lists academic history for a researcher.
        """
        if not self.service:
            raise RuntimeError("Service not initialized")
            
        return self.service.get_by_researcher(researcher_id)
