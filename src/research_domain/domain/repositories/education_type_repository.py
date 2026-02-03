from abc import ABC
from libbase.infrastructure.interface import IRepository
from research_domain.domain.entities.academic_education import EducationType

class IEducationTypeRepository(IRepository[EducationType], ABC):
    """
    Interface for EducationType Repository.
    """
    pass
