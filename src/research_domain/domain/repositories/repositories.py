from typing import List, Optional

from eo_lib.domain.repositories import (OrganizationalUnitRepositoryInterface,
                                        OrganizationRepositoryInterface,
                                        PersonRepositoryInterface,
                                        TeamRepositoryInterface)
from libbase.infrastructure.interface import \
    IRepository as GenericRepositoryInterface
from research_domain.domain.entities.academic_education import (
    AcademicEducation, EducationType)
from research_domain.domain.entities.article import Article


class ResearcherRepositoryInterface(PersonRepositoryInterface):
    """Interface for Researcher Repository."""

    pass


class UniversityRepositoryInterface(OrganizationRepositoryInterface):
    """Interface for University Repository."""

    pass


class CampusRepositoryInterface(OrganizationalUnitRepositoryInterface):
    """Interface for Campus Repository."""

    pass


class ResearchGroupRepositoryInterface(TeamRepositoryInterface):
    """Interface for ResearchGroup Repository."""

    pass


class KnowledgeAreaRepositoryInterface(GenericRepositoryInterface):
    """Interface for KnowledgeArea Repository."""

    pass


class RoleRepositoryInterface(GenericRepositoryInterface):
    """Interface for Role Repository."""

    pass


class AdvisorshipRepositoryInterface(GenericRepositoryInterface):
    """Interface for Advisorship Repository."""

    pass


class FellowshipRepositoryInterface(GenericRepositoryInterface):
    """Interface for Fellowship Repository."""

    pass


class AcademicEducationRepositoryInterface(GenericRepositoryInterface):
    """Interface for Academic Education Repository."""

    def list_by_researcher(self, researcher_id: int) -> List[AcademicEducation]:
        """Lists all education records for a researcher."""
        ...


class ArticleRepositoryInterface(GenericRepositoryInterface):
    """
    Interface for Article Repository.
    """

    def list_by_year(self, year: int) -> List[Article]:
        """
        List all articles published in a specific year.
        """
        ...

    def find_by_doi(self, doi: str) -> Optional[Article]:
        """
        Find an article by its DOI.
        """
        ...


class EducationTypeRepositoryInterface(GenericRepositoryInterface):
    """
    Interface for EducationType Repository.
    """

    pass


class ProductionTypeRepositoryInterface(GenericRepositoryInterface):
    """
    Interface for ProductionType Repository.
    """

    pass


class ResearchProductionRepositoryInterface(GenericRepositoryInterface):
    """
    Interface for ResearchProduction Repository.
    """

    pass
