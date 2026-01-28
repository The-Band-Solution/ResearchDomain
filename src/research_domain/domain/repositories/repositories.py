from eo_lib.domain.repositories import (OrganizationalUnitRepositoryInterface,
                                        OrganizationRepositoryInterface,
                                        PersonRepositoryInterface,
                                        TeamRepositoryInterface)
from libbase.infrastructure.interface import \
    IRepository as GenericRepositoryInterface


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
