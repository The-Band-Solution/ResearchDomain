from research_domain.config import Config
from research_domain.infrastructure.repositories import (
    InMemoryAdvisorshipRepository, InMemoryCampusRepository,
    InMemoryFellowshipRepository, InMemoryKnowledgeAreaRepository,
    InMemoryResearcherRepository, InMemoryResearchGroupRepository,
    InMemoryRoleRepository, InMemoryUniversityRepository,
    PostgresAdvisorshipRepository, PostgresCampusRepository,
    PostgresFellowshipRepository, PostgresKnowledgeAreaRepository,
    PostgresResearcherRepository, PostgresResearchGroupRepository,
    PostgresRoleRepository, PostgresUniversityRepository)
from research_domain.services import (AdvisorshipService, CampusService,
                                      FellowshipService, KnowledgeAreaService,
                                      ResearcherService, ResearchGroupService,
                                      RoleService, UniversityService)


class ServiceFactory:
    """
    Factory for creating Service instances with the appropriate Repository Strategy.
    """

    @staticmethod
    def _get_strategies():
        t = Config.get_storage_type().lower()
        if t in ["postgres", "db"]:
            return (
                PostgresResearcherRepository,
                PostgresUniversityRepository,
                PostgresCampusRepository,
                PostgresResearchGroupRepository,
                PostgresKnowledgeAreaRepository,
                PostgresRoleRepository,
                PostgresAdvisorshipRepository,
                PostgresFellowshipRepository,
            )
        # Default to memory
        return (
            InMemoryResearcherRepository,
            InMemoryUniversityRepository,
            InMemoryCampusRepository,
            InMemoryResearchGroupRepository,
            InMemoryKnowledgeAreaRepository,
            InMemoryRoleRepository,
            InMemoryAdvisorshipRepository,
            InMemoryFellowshipRepository,
        )

    @staticmethod
    def create_researcher_service() -> ResearcherService:
        (ResearcherRepo, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearcherService(ResearcherRepo())

    @staticmethod
    def create_university_service() -> UniversityService:
        (_, UniversityRepo, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return UniversityService(UniversityRepo())

    @staticmethod
    def create_campus_service() -> CampusService:
        (_, _, CampusRepo, _, _, _, _, _) = ServiceFactory._get_strategies()
        return CampusService(CampusRepo())

    @staticmethod
    def create_research_group_service() -> ResearchGroupService:
        (_, _, _, GroupRepo, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearchGroupService(GroupRepo())

    @staticmethod
    def create_knowledge_area_service() -> KnowledgeAreaService:
        (_, _, _, _, AreaRepo, _, _, _) = ServiceFactory._get_strategies()
        return KnowledgeAreaService(AreaRepo())

    @staticmethod
    def create_role_service() -> RoleService:
        (_, _, _, _, _, RoleRepo, _, _) = ServiceFactory._get_strategies()
        return RoleService(RoleRepo())

    @staticmethod
    def create_advisorship_service() -> AdvisorshipService:
        (
            _,
            _,
            _,
            _,
            _,
            _,
            AdvisorshipRepo,
            _,
        ) = ServiceFactory._get_strategies()
        return AdvisorshipService(AdvisorshipRepo())

    @staticmethod
    def create_fellowship_service() -> FellowshipService:
        (
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            FellowshipRepo,
        ) = ServiceFactory._get_strategies()
        return FellowshipService(FellowshipRepo())
