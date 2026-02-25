from typing import List

from eo_lib.domain.entities import Role, TeamMember
from eo_lib.infrastructure.database.postgres_client import PostgresClient
from libbase.infrastructure.sql_repository import GenericSqlRepository

from research_domain.domain.entities.academic_education import (
    AcademicEducation, EducationType)
from research_domain.domain.entities.article import Article
from research_domain.domain.entities import (Advisorship, Campus, Fellowship,
                                             KnowledgeArea, ProductionType,
                                             ResearchProduction, Researcher,
                                             ResearchGroup, University)
from research_domain.domain.repositories import (
    AcademicEducationRepositoryInterface, AdvisorshipRepositoryInterface,
    ArticleRepositoryInterface, CampusRepositoryInterface,
    EducationTypeRepositoryInterface, FellowshipRepositoryInterface,
    KnowledgeAreaRepositoryInterface, ProductionTypeRepositoryInterface,
    ResearchProductionRepositoryInterface, ResearcherRepositoryInterface,
    ResearchGroupRepositoryInterface, RoleRepositoryInterface,
    UniversityRepositoryInterface)


class PostgresResearcherRepository(
    GenericSqlRepository[Researcher], ResearcherRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Researcher)


class PostgresUniversityRepository(
    GenericSqlRepository[University], UniversityRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), University)


class PostgresCampusRepository(GenericSqlRepository[Campus], CampusRepositoryInterface):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Campus)


class PostgresResearchGroupRepository(
    GenericSqlRepository[ResearchGroup], ResearchGroupRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), ResearchGroup)

    def add_member(self, member: TeamMember) -> TeamMember:
        try:
            self._session.add(member)
            self._session.commit()
            self._session.refresh(member)
            return member
        except Exception:
            self._session.rollback()
            raise

    def remove_member(self, member_id: int) -> bool:
        db_obj = self._session.query(TeamMember).filter_by(id=member_id).first()
        if db_obj:
            self._session.delete(db_obj)
            self._session.commit()
            return True
        return False

    def get_members(self, team_id: int) -> List[TeamMember]:
        return self._session.query(TeamMember).filter_by(team_id=team_id).all()


class PostgresKnowledgeAreaRepository(
    GenericSqlRepository[KnowledgeArea], KnowledgeAreaRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), KnowledgeArea)


class PostgresRoleRepository(GenericSqlRepository[Role], RoleRepositoryInterface):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Role)


class PostgresAdvisorshipRepository(
    GenericSqlRepository[Advisorship], AdvisorshipRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Advisorship)


class PostgresFellowshipRepository(
    GenericSqlRepository[Fellowship], FellowshipRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Fellowship)


class PostgresAcademicEducationRepository(
    GenericSqlRepository[AcademicEducation], AcademicEducationRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), AcademicEducation)


class PostgresArticleRepository(
    GenericSqlRepository[Article], ArticleRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Article)


class PostgresEducationTypeRepository(
    GenericSqlRepository[EducationType], EducationTypeRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), EducationType)


class PostgresProductionTypeRepository(
    GenericSqlRepository[ProductionType], ProductionTypeRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), ProductionType)


class PostgresResearchProductionRepository(
    GenericSqlRepository[ResearchProduction], ResearchProductionRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), ResearchProduction)
