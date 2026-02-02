from abc import abstractmethod
from typing import List, Optional, Protocol

from research_domain.domain.entities.academic_education import AcademicEducation


class IAcademicEducationRepository(Protocol):
    """Interface for Academic Education Repository."""
    
    @abstractmethod
    def add(self, education: AcademicEducation) -> AcademicEducation:
        """Adds a new academic education record."""
        ...

    @abstractmethod
    def get_by_id(self, education_id: int) -> Optional[AcademicEducation]:
        """Retrieves an education record by ID."""
        ...

    @abstractmethod
    def list_by_researcher(self, researcher_id: int) -> List[AcademicEducation]:
        """Lists all education records for a researcher."""
        ...
        
    @abstractmethod
    def update(self, education: AcademicEducation) -> AcademicEducation:
        """Updates an existing education record."""
        ...
        
    @abstractmethod
    def delete(self, education_id: int) -> bool:
        """Deletes an education record."""
        ...
