from typing import List, Dict, Any
from libbase.controllers.generic_controller import GenericController
from research_domain.services.education_type_service import EducationTypeService
from research_domain.domain.entities.academic_education import EducationType

class EducationTypeController(GenericController[EducationType]):
    """
    Controller for Education Types.
    """
    def __init__(self, service: EducationTypeService):
        super().__init__(service)
        # self._service is available from parent

    def create_education_type(self, name: str) -> Dict[str, Any]:
        """
        Creates a new Education Type.
        """
        try:
            # Cast self._service to EducationTypeService to access specific methods
            education_type = self._service.create_education_type(name=name)
            return {"success": True, "education_type": education_type.to_dict()}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def list_education_types(self) -> Dict[str, Any]:
        """
        Lists all Education Types.
        """
        try:
            types = self.get_all() # Uses GenericController.get_all
            return {"success": True, "education_types": [t.to_dict() for t in types]}
        except Exception as e:
            return {"success": False, "error": str(e)}
