from research_domain.config import Config
from research_domain.infrastructure.repositories import (
    InMemoryAdvisorshipRepository, InMemoryArticleRepository,
    InMemoryCampusRepository, InMemoryEducationTypeRepository,
    InMemoryFellowshipRepository, InMemoryKnowledgeAreaRepository,
    InMemoryResearcherRepository, InMemoryResearchGroupRepository,
    InMemoryRoleRepository, InMemoryUniversityRepository,
    PostgresAcademicEducationRepository, PostgresAdvisorshipRepository,
    PostgresArticleRepository, PostgresCampusRepository,
    PostgresEducationTypeRepository, PostgresFellowshipRepository,
    PostgresKnowledgeAreaRepository, PostgresResearcherRepository,
    PostgresResearchGroupRepository, PostgresRoleRepository,
    PostgresUniversityRepository)
from research_domain.services import (
    AcademicEducationService, AdvisorshipService, ArticleService,
    CampusService, EducationTypeService, FellowshipService,
    KnowledgeAreaService, ResearcherService, ResearchGroupService,
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
                PostgresAcademicEducationRepository,
                PostgresArticleRepository,
                PostgresEducationTypeRepository,
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
            InMemoryAcademicEducationRepository,
            InMemoryArticleRepository,
            InMemoryEducationTypeRepository,
        )

    @staticmethod
    def create_researcher_service() -> ResearcherService:
        (ResearcherRepo, _, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearcherService(ResearcherRepo())

    @staticmethod
    def create_university_service() -> UniversityService:
        (_, UniversityRepo, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return UniversityService(UniversityRepo())

    @staticmethod
    def create_campus_service() -> CampusService:
        (_, _, CampusRepo, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return CampusService(CampusRepo())

    @staticmethod
    def create_research_group_service() -> ResearchGroupService:
        (_, _, _, GroupRepo, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearchGroupService(GroupRepo())

    @staticmethod
    def create_knowledge_area_service() -> KnowledgeAreaService:
        (_, _, _, _, AreaRepo, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return KnowledgeAreaService(AreaRepo())

    @staticmethod
    def create_role_service() -> RoleService:
        (_, _, _, _, _, RoleRepo, _, _, _, _, _) = ServiceFactory._get_strategies()
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
            _,
            _,
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
            _,
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return FellowshipService(FellowshipRepo())

    @staticmethod
    def create_academic_education_service() -> AcademicEducationService:
        (
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            AcademicEducationRepo,
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return AcademicEducationService(AcademicEducationRepo())

    @staticmethod
    def create_article_service() -> ArticleService:
        (
            ResearcherRepo,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            ArticleRepo,
            _,
        ) = ServiceFactory._get_strategies()
        return ArticleService(ArticleRepo(), ResearcherRepo())

    @staticmethod
    def create_education_type_service() -> EducationTypeService:
        (
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
            EducationTypeRepo,
        ) = ServiceFactory._get_strategies()
        return EducationTypeService(EducationTypeRepo())
