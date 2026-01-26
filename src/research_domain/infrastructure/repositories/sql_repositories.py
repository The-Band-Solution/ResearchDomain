from typing import List

from eo_lib.domain.entities import Role, TeamMember
from eo_lib.infrastructure.database.postgres_client import PostgresClient
from libbase.infrastructure.sql_repository import GenericSqlRepository

from research_domain.domain.entities import (Advisorship, Campus,
                                             ExternalResearchGroup, Fellowship,
                                             KnowledgeArea, Researcher,
                                             ResearchGroup, University)
from research_domain.domain.repositories import (
    AdvisorshipRepositoryInterface, CampusRepositoryInterface,
    ExternalResearchGroupRepositoryInterface, FellowshipRepositoryInterface,
    KnowledgeAreaRepositoryInterface, ResearcherRepositoryInterface,
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


class PostgresFellowshipRepository(
    GenericSqlRepository[Fellowship], FellowshipRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Fellowship)


class PostgresExternalResearchGroupRepository(
    PostgresResearchGroupRepository, ExternalResearchGroupRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        # Use GenericSqlRepository's init directly to set the session and model
        GenericSqlRepository.__init__(self, client.get_session(), ExternalResearchGroup)


class PostgresAdvisorshipRepository(
    GenericSqlRepository[Advisorship], AdvisorshipRepositoryInterface
):
    def __init__(self):
        client = PostgresClient()
        super().__init__(client.get_session(), Advisorship)
