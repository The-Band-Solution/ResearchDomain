from datetime import date
from typing import List, Optional

from eo_lib.domain.entities import Role, TeamMember
from eo_lib.services import (OrganizationalUnitService, OrganizationService,
                             PersonService, TeamService)
from libbase.services.generic_service import GenericService

from research_domain.domain.entities.academic_education import (
    AcademicEducation, EducationType)
from research_domain.domain.entities.article import Article, ArticleType
from research_domain.domain.entities import (Advisorship, AdvisorshipRole, Campus, Fellowship,
                                             KnowledgeArea, Researcher,
                                             ResearchGroup, University)
from research_domain.domain.repositories import (
    AcademicEducationRepositoryInterface, AdvisorshipRepositoryInterface,
    ArticleRepositoryInterface, CampusRepositoryInterface,
    EducationTypeRepositoryInterface, FellowshipRepositoryInterface,
    KnowledgeAreaRepositoryInterface, ResearcherRepositoryInterface,
    ResearchGroupRepositoryInterface, RoleRepositoryInterface,
    UniversityRepositoryInterface)


class RoleService(GenericService[Role]):
    def __init__(self, repo: RoleRepositoryInterface):
        super().__init__(repo)
        self.repo = repo

    def get_or_create_leader_role(self) -> Role:
        """Finds or creates the 'Leader' role."""
        roles = self.get_all()
        for r in roles:
            if r.name.lower() == "leader":
                return r

        leader_role = Role(name="Leader", description="Research Group Leader")
        self.create(leader_role)
        return leader_role


class KnowledgeAreaService(GenericService[KnowledgeArea]):
    def __init__(self, repo: KnowledgeAreaRepositoryInterface):
        super().__init__(repo)


class ResearcherService(PersonService):
    def __init__(self, repo: ResearcherRepositoryInterface):
        super().__init__(repo)


class UniversityService(OrganizationService):
    def __init__(self, repo: UniversityRepositoryInterface):
        super().__init__(repo)


class CampusService(OrganizationalUnitService):
    def __init__(self, repo: CampusRepositoryInterface):
        super().__init__(repo)


class ResearchGroupService(TeamService):
    def __init__(self, repo: ResearchGroupRepositoryInterface):
        super().__init__(repo)
        self.repo = repo

    def create_research_group(
        self,
        name: str,
        campus_id: int,
        organization_id: int = None,
        description: str = None,
        short_name: str = None,
        cnpq_url: str = None,
        site: str = None,
        knowledge_areas: List[KnowledgeArea] = None,
    ) -> ResearchGroup:
        group = ResearchGroup(
            name=name,
            campus_id=campus_id,
            organization_id=organization_id,
            description=description,
            short_name=short_name,
            cnpq_url=cnpq_url,
            site=site,
            knowledge_areas=knowledge_areas,
        )
        self.create(group)
        return group

    def add_leader(
        self,
        team_id: int,
        person_id: int,
        role_id: int,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> TeamMember:
        """Adds a leader to the group."""
        if not start_date:
            start_date = date.today()

        return self.add_member(
            team_id=team_id,
            person_id=person_id,
            role_id=role_id,
            start_date=start_date,
            end_date=end_date,
        )


class AdvisorshipService(GenericService[Advisorship]):
    def __init__(
        self,
        repo: AdvisorshipRepositoryInterface,
        researcher_repo: ResearcherRepositoryInterface,
        role_repo: RoleRepositoryInterface,
    ):
        super().__init__(repo)
        self.researcher_repo = researcher_repo
        self.role_repo = role_repo

    def create_advisorship(
        self,
        name: str,
        student_id: Optional[int] = None,
        supervisor_id: Optional[int] = None,
        fellowship_id: Optional[int] = None,
        institution_id: Optional[int] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        description: Optional[str] = None,
        status: str = "active",
        cancelled: bool = False,
        cancellation_date: Optional[date] = None,
        type: Optional[str] = None, # Assuming type might be passed
    ) -> Advisorship:
        """
        Creates an Advisorship and assigns Student/Supervisor roles.
        """
        advisorship = Advisorship(
            name=name,
            fellowship_id=fellowship_id,
            institution_id=institution_id,
            start_date=start_date,
            end_date=end_date,
            description=description,
            status=status,
            cancelled=cancelled,
            cancellation_date=cancellation_date,
            # Type handling omitted for brevity/compatibility with existing call signature, can add if needed
        )
        
        # Add Student
        if student_id:
            student = self.researcher_repo.get(student_id)
            if student:
                # We need to find or create the Role object. 
                # Ideally we fetch by name.
                # Since RoleRepo is generic, we might iterate or assuming we can create if not exists.
                # For simplicity here, we assume we can filter or just create for now. 
                # Actually, role_repo should ideally have find_by_name. But GenericRepository usually has get_all.
                # Let's iterate for safety as we did in RoleService.
                all_roles = self.role_repo.get_all()
                role_student = next((r for r in all_roles if r.name == AdvisorshipRole.STUDENT.value), None)
                if not role_student:
                    role_student = Role(name=AdvisorshipRole.STUDENT.value)
                    self.role_repo.create(role_student)
                
                advisorship.add_member(person=student, role=role_student, start_date=start_date)

        # Add Supervisor
        if supervisor_id:
            supervisor = self.researcher_repo.get(supervisor_id)
            if supervisor:
                all_roles = self.role_repo.get_all()
                role_supervisor = next((r for r in all_roles if r.name == AdvisorshipRole.SUPERVISOR.value), None)
                if not role_supervisor:
                    role_supervisor = Role(name=AdvisorshipRole.SUPERVISOR.value)
                    self.role_repo.create(role_supervisor)

                advisorship.add_member(person=supervisor, role=role_supervisor, start_date=start_date)

        self.create(advisorship)
        return advisorship

    def cancel_advisorship(
        self, advisorship_id: int, cancellation_date: date
    ) -> Optional[Advisorship]:
        """Marks an advisorship as cancelled."""
        advisorship = self.get_by_id(advisorship_id)
        if advisorship:
            advisorship.cancelled = True
            advisorship.cancellation_date = cancellation_date
            # The generic service should have an update method or we can call repository directly
            self.update(advisorship)
            return advisorship
        return None


class FellowshipService(GenericService[Fellowship]):
    def __init__(self, repo: FellowshipRepositoryInterface):
        super().__init__(repo)


class AcademicEducationService(GenericService[AcademicEducation]):
    """
    Service for managing Academic Education history.
    """

    def __init__(self, repository: AcademicEducationRepositoryInterface):
        super().__init__(repository)

    def create_education(
        self,
        researcher_id: int,
        education_type_id: int,
        title: str,
        institution_id: int,
        start_year: int,
        end_year: Optional[int] = None,
        thesis_title: Optional[str] = None,
        advisor_id: Optional[int] = None,
        co_advisor_id: Optional[int] = None,
        knowledge_areas: list = None,
    ) -> AcademicEducation:
        """
        Creates and persists a new academic education record.
        """
        education = AcademicEducation(
            researcher_id=researcher_id,
            education_type_id=education_type_id,
            title=title,
            institution_id=institution_id,
            start_year=start_year,
            end_year=end_year,
            thesis_title=thesis_title,
            advisor_id=advisor_id,
            co_advisor_id=co_advisor_id,
            knowledge_areas=knowledge_areas,
        )

        self.create(education)
        return education

    def get_by_researcher(self, researcher_id: int) -> List[AcademicEducation]:
        """
        Retrieves all education records for a researcher.
        """
        return self._repository.list_by_researcher(researcher_id)

    def delete_education(self, education_id: int) -> bool:
        """
        Deletes an education record.
        """
        return self.delete(education_id)


class ArticleService(GenericService[Article]):
    """
    Service for managing Articles.
    """

    def __init__(
        self,
        repository: ArticleRepositoryInterface,
        researcher_repository: ResearcherRepositoryInterface,
    ):
        super().__init__(repository)
        self.researcher_repository = researcher_repository

    def create_article(
        self,
        title: str,
        year: int,
        type: ArticleType,
        author_ids: Optional[List[int]] = None,
        doi: Optional[str] = None,
        journal_conference: Optional[str] = None,
        **kwargs,
    ) -> Article:
        """
        Create a new article and associate authors.
        """
        authors = []
        if author_ids:
            for rid in author_ids:
                author = self.researcher_repository.get(rid)
                if author:
                    authors.append(author)

        article = Article(
            title=title,
            year=year,
            type=type,
            authors=authors,
            doi=doi,
            journal_conference=journal_conference,
            **kwargs,
        )
        self.create(article)
        return article

    def add_author(self, article_id: int, researcher_id: int) -> Optional[Article]:
        """
        Add an author to an existing article.
        """
        article = self.get_by_id(article_id)
        researcher = self.researcher_repository.get(researcher_id)

        if article and researcher:
            if researcher not in article.authors:
                article.authors.append(researcher)
                self.update(article)
            return article
        return None


class EducationTypeService(GenericService[EducationType]):
    """
    Service for managing Education Types.
    """

    def __init__(self, repository: EducationTypeRepositoryInterface):
        super().__init__(repository)

    def create_education_type(self, name: str) -> EducationType:
        """
        Creates a new Education Type.
        """
        education_type = EducationType(name=name)
        self.create(education_type)
        return education_type

    def get_by_name(self, name: str) -> Optional[EducationType]:
        """
        Retrieves an Education Type by name.
        """
        all_types = self.get_all()
        for et in all_types:
            if et.name == name:
                return et
        return None
