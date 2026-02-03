from datetime import date
from typing import List, Optional

from eo_lib.domain.entities import Role, TeamMember
from libbase.controllers.generic_controller import GenericController

from research_domain.domain.entities.academic_education import (
    AcademicEducation, EducationType)
from research_domain.domain.entities.article import Article, ArticleType
from research_domain.domain.entities.researcher import Researcher
from research_domain.domain.entities import (Advisorship, Campus, Fellowship,
                                             KnowledgeArea,
                                             ResearchGroup, University)
from research_domain.factories import ServiceFactory


class ResearcherController(GenericController[Researcher]):
    def __init__(self):
        service = ServiceFactory.create_researcher_service()
        super().__init__(service)

    def create_researcher(
        self,
        name: str,
        emails: List[str] = None,
        identification_id: str = None,
        birthday: date = None,
    ) -> Researcher:
        return self._service.create_with_details(
            name, emails, identification_id, birthday
        )


class UniversityController(GenericController[University]):
    def __init__(self):
        service = ServiceFactory.create_university_service()
        super().__init__(service)

    def create_university(
        self,
        name: str,
        description: str = None,
        short_name: str = None,
    ) -> University:
        university = University(
            name=name, description=description, short_name=short_name
        )
        self.create(university)
        return university


class CampusController(GenericController[Campus]):
    def __init__(self):
        service = ServiceFactory.create_campus_service()
        super().__init__(service)

    def create_campus(
        self,
        name: str,
        organization_id: int,
        description: str = None,
        short_name: str = None,
    ) -> Campus:
        campus = Campus(
            name=name,
            organization_id=organization_id,
            description=description,
            short_name=short_name,
        )
        self.create(campus)
        return campus


class KnowledgeAreaController(GenericController[KnowledgeArea]):
    def __init__(self):
        service = ServiceFactory.create_knowledge_area_service()
        super().__init__(service)

    def create_knowledge_area(self, name: str) -> KnowledgeArea:
        area = KnowledgeArea(name=name)
        self.create(area)
        return area


class RoleController(GenericController[Role]):
    def __init__(self):
        service = ServiceFactory.create_role_service()
        super().__init__(service)

    def create_role(self, name: str, description: str = None) -> Role:
        role = Role(name=name, description=description)
        self.create(role)
        return role

    def get_or_create_leader_role(self) -> Role:
        return self._service.get_or_create_leader_role()


class ResearchGroupController(GenericController[ResearchGroup]):
    def __init__(self):
        service = ServiceFactory.create_research_group_service()
        super().__init__(service)
        self._area_service = ServiceFactory.create_knowledge_area_service()
        self._role_service = ServiceFactory.create_role_service()

    def create_research_group(
        self,
        name: str,
        campus_id: int,
        organization_id: int = None,
        description: str = None,
        short_name: str = None,
        cnpq_url: str = None,
        site: str = None,
        knowledge_area_ids: List[int] = None,
    ) -> ResearchGroup:
        areas = []
        if knowledge_area_ids:
            for aid in knowledge_area_ids:
                area = self._area_service.get_by_id(aid)
                if area:
                    areas.append(area)

        return self._service.create_research_group(
            name=name,
            campus_id=campus_id,
            organization_id=organization_id,
            description=description,
            short_name=short_name,
            cnpq_url=cnpq_url,
            site=site,
            knowledge_areas=areas,
        )

    def add_leader(
        self,
        team_id: int,
        person_id: int,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> TeamMember:
        leader_role = self._role_service.get_or_create_leader_role()
        return self._service.add_leader(
            team_id=team_id,
            person_id=person_id,
            role_id=leader_role.id,
            start_date=start_date,
            end_date=end_date,
        )

    def get_leaders(self, team_id: int) -> List[TeamMember]:
        members = self._service.get_members(team_id)
        leader_role = self._role_service.get_or_create_leader_role()
        return [m for m in members if m.role_id == leader_role.id]


class AdvisorshipController(GenericController[Advisorship]):
    def __init__(self):
        service = ServiceFactory.create_advisorship_service()
        super().__init__(service)

    def create_advisorship(
        self,
        name: str,
        student_id: Optional[int] = None,
        supervisor_id: Optional[int] = None,
        fellowship_id: Optional[int] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        description: Optional[str] = None,
        status: str = "active",
        cancelled: bool = False,
        cancellation_date: Optional[date] = None,
    ) -> Advisorship:
        advisorship = Advisorship(
            name=name,
            student_id=student_id,
            supervisor_id=supervisor_id,
            fellowship_id=fellowship_id,
            start_date=start_date,
            end_date=end_date,
            description=description,
            status=status,
            cancelled=cancelled,
            cancellation_date=cancellation_date,
        )
        self.create(advisorship)
        return advisorship

    def cancel_advisorship(
        self, advisorship_id: int, cancellation_date: Optional[date] = None
    ) -> Optional[Advisorship]:
        if not cancellation_date:
            cancellation_date = date.today()
        return self._service.cancel_advisorship(advisorship_id, cancellation_date)


class FellowshipController(GenericController[Fellowship]):
    def __init__(self):
        service = ServiceFactory.create_fellowship_service()
        super().__init__(service)

    def create_fellowship(
        self,
        name: str,
        value: float,
        description: Optional[str] = None,
        sponsor_id: Optional[int] = None,
    ) -> Fellowship:
        fellowship = Fellowship(
            name=name,
            value=value,
            description=description,
            sponsor_id=sponsor_id,
        )
        self.create(fellowship)
        return fellowship


class AcademicEducationController(GenericController[AcademicEducation]):
    """
    Controller for Academic Education operations.
    """

    def __init__(self):
        service = ServiceFactory.create_academic_education_service()
        super().__init__(service)

    def create_academic_education(
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
        Adds a new education entry to a researcher's profile.
        """
        return self._service.create_education(
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

    def list_history(self, researcher_id: int) -> List[AcademicEducation]:
        """
        Lists academic history for a researcher.
        """
        return self._service.get_by_researcher(researcher_id)


class ArticleController(GenericController[Article]):
    """
    Controller for Article management.
    """

    def __init__(self):
        service = ServiceFactory.create_article_service()
        super().__init__(service)

    def create_article(
        self,
        title: str,
        year: int,
        type: str,  # String input from API/CLI parsed to Enum
        author_ids: Optional[List[int]] = None,
        **kwargs,
    ) -> Article:
        try:
            # Parse Enum from string if needed, or pass directly if internal call
            article_type = ArticleType(type) if isinstance(type, str) else type
            return self._service.create_article(
                title=title,
                year=year,
                type=article_type,
                author_ids=author_ids,
                **kwargs,
            )
        except ValueError:
            raise ValueError(f"Invalid ArticleType: {type}")

    def add_author(self, article_id: int, researcher_id: int) -> Optional[Article]:
        return self._service.add_author(article_id, researcher_id)


class EducationTypeController(GenericController[EducationType]):
    """
    Controller for Education Types.
    """

    def __init__(self):
        service = ServiceFactory.create_education_type_service()
        super().__init__(service)

    def create_education_type(self, name: str) -> EducationType:
        """
        Creates a new Education Type.
        """
        return self._service.create_education_type(name=name)

    def list_education_types(self) -> List[EducationType]:
        """
        Lists all Education Types.
        """
        return self.get_all()
