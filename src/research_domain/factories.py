from research_domain.config import Config
from research_domain.infrastructure.repositories import (
    InMemoryAdvisorshipRepository, InMemoryArticleRepository,
    InMemoryCampusRepository, InMemoryEducationTypeRepository,
    InMemoryFellowshipRepository, InMemoryKnowledgeAreaRepository,
    InMemoryProductionTypeRepository, InMemoryResearchProductionRepository,
    InMemoryResearcherRepository, InMemoryResearchGroupRepository,
    InMemoryRoleRepository, InMemoryUniversityRepository,
    InMemoryAcademicEducationRepository,
    PostgresAcademicEducationRepository, PostgresAdvisorshipRepository,
    PostgresArticleRepository, PostgresCampusRepository,
    PostgresEducationTypeRepository, PostgresFellowshipRepository,
    PostgresKnowledgeAreaRepository, PostgresProductionTypeRepository,
    PostgresResearchProductionRepository, PostgresResearcherRepository,
    PostgresResearchGroupRepository, PostgresRoleRepository,
    PostgresUniversityRepository)
from research_domain.services import (
    AcademicEducationService, AdvisorshipService, ArticleService,
    CampusService, EducationTypeService, FellowshipService,
    KnowledgeAreaService, ProductionTypeService, ResearchProductionService,
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
                PostgresAcademicEducationRepository,
                PostgresArticleRepository,
                PostgresEducationTypeRepository,
                PostgresProductionTypeRepository,
                PostgresResearchProductionRepository,
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
            InMemoryProductionTypeRepository,
            InMemoryResearchProductionRepository,
        )

    @staticmethod
    def create_researcher_service() -> ResearcherService:
        (ResearcherRepo, _, _, _, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearcherService(ResearcherRepo())

    @staticmethod
    def create_university_service() -> UniversityService:
        (_, UniversityRepo, _, _, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return UniversityService(UniversityRepo())

    @staticmethod
    def create_campus_service() -> CampusService:
        (_, _, CampusRepo, _, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return CampusService(CampusRepo())

    @staticmethod
    def create_research_group_service() -> ResearchGroupService:
        (_, _, _, GroupRepo, _, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return ResearchGroupService(GroupRepo())

    @staticmethod
    def create_knowledge_area_service() -> KnowledgeAreaService:
        (_, _, _, _, AreaRepo, _, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return KnowledgeAreaService(AreaRepo())

    @staticmethod
    def create_role_service() -> RoleService:
        (_, _, _, _, _, RoleRepo, _, _, _, _, _, _, _) = ServiceFactory._get_strategies()
        return RoleService(RoleRepo())

    @staticmethod
    def create_advisorship_service() -> AdvisorshipService:
        (
            ResearcherRepo,
            _,
            _,
            _,
            _,
            RoleRepo,
            AdvisorshipRepo,
            _,
            _,
            _,
            _,
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return AdvisorshipService(
            repo=AdvisorshipRepo(),
            researcher_repo=ResearcherRepo(),
            role_repo=RoleRepo()
        )

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
            _,
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
            _,
            _,
        ) = ServiceFactory._get_strategies()
        return EducationTypeService(EducationTypeRepo())

    @staticmethod
    def create_production_type_service() -> ProductionTypeService:
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
            _,
            ProductionTypeRepo,
            _,
        ) = ServiceFactory._get_strategies()
        return ProductionTypeService(ProductionTypeRepo())

    @staticmethod
    def create_research_production_service() -> ResearchProductionService:
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
            _,
            _,
            _,
            ProductionRepo,
        ) = ServiceFactory._get_strategies()
        return ResearchProductionService(ProductionRepo(), ResearcherRepo())
