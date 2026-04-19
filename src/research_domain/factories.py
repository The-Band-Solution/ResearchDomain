from research_domain.config import Config
from research_domain.infrastructure.repositories import (
    InMemoryAcademicEducationRepository,
    InMemoryAdvisorshipRepository,
    InMemoryArticleRepository,
    InMemoryCampusRepository,
    InMemoryEducationTypeRepository,
    InMemoryFellowshipRepository,
    InMemoryKnowledgeAreaRepository,
    InMemoryProductionTypeRepository,
    InMemoryProfessionalActivityRepository,
    InMemoryResearchProductionRepository,
    InMemoryResearcherRepository,
    InMemoryResearchGroupRepository,
    InMemoryRoleRepository,
    InMemoryUniversityRepository,
    PostgresAcademicEducationRepository,
    PostgresAdvisorshipRepository,
    PostgresArticleRepository,
    PostgresCampusRepository,
    PostgresEducationTypeRepository,
    PostgresFellowshipRepository,
    PostgresKnowledgeAreaRepository,
    PostgresProductionTypeRepository,
    PostgresProfessionalActivityRepository,
    PostgresResearchProductionRepository,
    PostgresResearcherRepository,
    PostgresResearchGroupRepository,
    PostgresRoleRepository,
    PostgresUniversityRepository,
)
from research_domain.services import (
    AcademicEducationService,
    AdvisorshipService,
    ArticleService,
    CampusService,
    EducationTypeService,
    FellowshipService,
    KnowledgeAreaService,
    ProductionTypeService,
    ProfessionalActivityService,
    ResearchProductionService,
    ResearcherService,
    ResearchGroupService,
    RoleService,
    UniversityService,
)


class ServiceFactory:
    """
    Factory for creating Service instances with the appropriate Repository Strategy.
    """

    _memory_repo_instances = {}

    @staticmethod
    def _get_strategies():
        storage_type = Config.get_storage_type().lower()

        if storage_type in ["postgres", "db"]:
            return {
                "researcher": PostgresResearcherRepository,
                "university": PostgresUniversityRepository,
                "campus": PostgresCampusRepository,
                "research_group": PostgresResearchGroupRepository,
                "knowledge_area": PostgresKnowledgeAreaRepository,
                "role": PostgresRoleRepository,
                "advisorship": PostgresAdvisorshipRepository,
                "fellowship": PostgresFellowshipRepository,
                "academic_education": PostgresAcademicEducationRepository,
                "article": PostgresArticleRepository,
                "education_type": PostgresEducationTypeRepository,
                "production_type": PostgresProductionTypeRepository,
                "research_production": PostgresResearchProductionRepository,
                "professional_activity": PostgresProfessionalActivityRepository,
            }

        return {
            "researcher": InMemoryResearcherRepository,
            "university": InMemoryUniversityRepository,
            "campus": InMemoryCampusRepository,
            "research_group": InMemoryResearchGroupRepository,
            "knowledge_area": InMemoryKnowledgeAreaRepository,
            "role": InMemoryRoleRepository,
            "advisorship": InMemoryAdvisorshipRepository,
            "fellowship": InMemoryFellowshipRepository,
            "academic_education": InMemoryAcademicEducationRepository,
            "article": InMemoryArticleRepository,
            "education_type": InMemoryEducationTypeRepository,
            "production_type": InMemoryProductionTypeRepository,
            "research_production": InMemoryResearchProductionRepository,
            "professional_activity": InMemoryProfessionalActivityRepository,
        }

    @classmethod
    def _build_repository(cls, repo_type):
        if Config.get_storage_type().lower() in ["postgres", "db"]:
            return repo_type()

        if repo_type not in cls._memory_repo_instances:
            cls._memory_repo_instances[repo_type] = repo_type()
        return cls._memory_repo_instances[repo_type]

    @classmethod
    def create_researcher_service(cls) -> ResearcherService:
        repo = cls._build_repository(cls._get_strategies()["researcher"])
        return ResearcherService(repo)

    @classmethod
    def create_university_service(cls) -> UniversityService:
        repo = cls._build_repository(cls._get_strategies()["university"])
        return UniversityService(repo)

    @classmethod
    def create_campus_service(cls) -> CampusService:
        repo = cls._build_repository(cls._get_strategies()["campus"])
        return CampusService(repo)

    @classmethod
    def create_research_group_service(cls) -> ResearchGroupService:
        repo = cls._build_repository(cls._get_strategies()["research_group"])
        return ResearchGroupService(repo)

    @classmethod
    def create_knowledge_area_service(cls) -> KnowledgeAreaService:
        repo = cls._build_repository(cls._get_strategies()["knowledge_area"])
        return KnowledgeAreaService(repo)

    @classmethod
    def create_role_service(cls) -> RoleService:
        repo = cls._build_repository(cls._get_strategies()["role"])
        return RoleService(repo)

    @classmethod
    def create_advisorship_service(cls) -> AdvisorshipService:
        strategies = cls._get_strategies()
        return AdvisorshipService(
            repo=cls._build_repository(strategies["advisorship"]),
            researcher_repo=cls._build_repository(strategies["researcher"]),
            role_repo=cls._build_repository(strategies["role"]),
        )

    @classmethod
    def create_fellowship_service(cls) -> FellowshipService:
        repo = cls._build_repository(cls._get_strategies()["fellowship"])
        return FellowshipService(repo)

    @classmethod
    def create_academic_education_service(cls) -> AcademicEducationService:
        repo = cls._build_repository(cls._get_strategies()["academic_education"])
        return AcademicEducationService(repo)

    @classmethod
    def create_article_service(cls) -> ArticleService:
        strategies = cls._get_strategies()
        return ArticleService(
            cls._build_repository(strategies["article"]),
            cls._build_repository(strategies["researcher"]),
        )

    @classmethod
    def create_professional_activity_service(cls) -> ProfessionalActivityService:
        repo = cls._build_repository(cls._get_strategies()["professional_activity"])
        return ProfessionalActivityService(repo)

    @classmethod
    def create_education_type_service(cls) -> EducationTypeService:
        repo = cls._build_repository(cls._get_strategies()["education_type"])
        return EducationTypeService(repo)

    @classmethod
    def create_production_type_service(cls) -> ProductionTypeService:
        repo = cls._build_repository(cls._get_strategies()["production_type"])
        return ProductionTypeService(repo)

    @classmethod
    def create_research_production_service(cls) -> ResearchProductionService:
        strategies = cls._get_strategies()
        return ResearchProductionService(
            cls._build_repository(strategies["research_production"]),
            cls._build_repository(strategies["researcher"]),
        )
