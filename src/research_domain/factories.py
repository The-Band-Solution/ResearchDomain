from research_domain.config import Config
from research_domain.infrastructure.repositories import (
    InMemoryAdvisorshipRepository, InMemoryCampusRepository,
    InMemoryExternalResearchGroupRepository, InMemoryFellowshipRepository,
    InMemoryKnowledgeAreaRepository, InMemoryResearcherRepository,
    InMemoryResearchGroupRepository, InMemoryRoleRepository,
    InMemoryUniversityRepository, PostgresAdvisorshipRepository,
    PostgresCampusRepository, PostgresExternalResearchGroupRepository,
    PostgresFellowshipRepository, PostgresKnowledgeAreaRepository,
    PostgresResearcherRepository, PostgresResearchGroupRepository,
    PostgresRoleRepository, PostgresUniversityRepository)
from research_domain.services import (AdvisorshipService, CampusService,
                                      ExternalResearchGroupService,
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
            return {
                "researcher": PostgresResearcherRepository,
                "university": PostgresUniversityRepository,
                "campus": PostgresCampusRepository,
                "research_group": PostgresResearchGroupRepository,
                "knowledge_area": PostgresKnowledgeAreaRepository,
                "role": PostgresRoleRepository,
                "fellowship": PostgresFellowshipRepository,
                "external_research_group": PostgresExternalResearchGroupRepository,
                "advisorship": PostgresAdvisorshipRepository,
            }
        # Default to memory
        return {
            "researcher": InMemoryResearcherRepository,
            "university": InMemoryUniversityRepository,
            "campus": InMemoryCampusRepository,
            "research_group": InMemoryResearchGroupRepository,
            "knowledge_area": InMemoryKnowledgeAreaRepository,
            "role": InMemoryRoleRepository,
            "fellowship": InMemoryFellowshipRepository,
            "external_research_group": InMemoryExternalResearchGroupRepository,
            "advisorship": InMemoryAdvisorshipRepository,
        }

    @staticmethod
    def create_researcher_service() -> ResearcherService:
        strategies = ServiceFactory._get_strategies()
        return ResearcherService(strategies["researcher"]())

    @staticmethod
    def create_university_service() -> UniversityService:
        strategies = ServiceFactory._get_strategies()
        return UniversityService(strategies["university"]())

    @staticmethod
    def create_campus_service() -> CampusService:
        strategies = ServiceFactory._get_strategies()
        return CampusService(strategies["campus"]())

    @staticmethod
    def create_research_group_service() -> ResearchGroupService:
        strategies = ServiceFactory._get_strategies()
        return ResearchGroupService(strategies["research_group"]())

    @staticmethod
    def create_knowledge_area_service() -> KnowledgeAreaService:
        strategies = ServiceFactory._get_strategies()
        return KnowledgeAreaService(strategies["knowledge_area"]())

    @staticmethod
    def create_role_service() -> RoleService:
        strategies = ServiceFactory._get_strategies()
        return RoleService(strategies["role"]())

    @staticmethod
    def create_fellowship_service() -> FellowshipService:
        strategies = ServiceFactory._get_strategies()
        return FellowshipService(strategies["fellowship"]())

    @staticmethod
    def create_external_research_group_service() -> ExternalResearchGroupService:
        strategies = ServiceFactory._get_strategies()
        return ExternalResearchGroupService(strategies["external_research_group"]())

    @staticmethod
    def create_advisorship_service() -> AdvisorshipService:
        strategies = ServiceFactory._get_strategies()
        return AdvisorshipService(strategies["advisorship"]())
