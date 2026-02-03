from typing import List, Optional
from libbase.services.generic_service import GenericService
from research_domain.domain.entities.academic_education import EducationType
from research_domain.domain.repositories.education_type_repository import IEducationTypeRepository

class EducationTypeService(GenericService[EducationType]):
    """
    Service for managing Education Types.
    """
    def __init__(self, repository: IEducationTypeRepository):
        super().__init__(repository)

    def create_education_type(self, name: str) -> EducationType:
        """
        Creates a new Education Type.
        """
        education_type = EducationType(name=name)
        self.create(education_type) # Uses GenericService.create which calls repository.add
        return education_type

    def get_by_name(self, name: str) -> Optional[EducationType]:
        """
        Retrieves an Education Type by name.
        """
        # Assuming repository has common find/filter methods or iterating generic list 
        # For efficiency, a custom method in repo would be better, but generic get_all works for small tables
        all_types = self.get_all()
        for et in all_types:
            if et.name == name:
                return et
        return None
