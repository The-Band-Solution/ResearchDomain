# ResearchDomain API Reference

Automated documentation for LLM ingestion.


## File: `config.py`

### Class `Config`

- **Method** `get_database_url(cls) -> str`

- **Method** `get_storage_type(cls) -> str`

- **Method** `get_json_dir(cls) -> str`


---

## File: `controllers/controllers.py`

### Class `ResearcherController`

*Inherits from:* `GenericController[Researcher]`

- **Method** `__init__(self)`

- **Method** `create_researcher(self, name: str, emails: List[str], identification_id: str, birthday: date, resume: str) -> Researcher`


---

### Class `UniversityController`

*Inherits from:* `GenericController[University]`

- **Method** `__init__(self)`

- **Method** `create_university(self, name: str, description: str, short_name: str) -> University`


---

### Class `CampusController`

*Inherits from:* `GenericController[Campus]`

- **Method** `__init__(self)`

- **Method** `create_campus(self, name: str, organization_id: int, description: str, short_name: str) -> Campus`


---

### Class `KnowledgeAreaController`

*Inherits from:* `GenericController[KnowledgeArea]`

- **Method** `__init__(self)`

- **Method** `create_knowledge_area(self, name: str) -> KnowledgeArea`


---

### Class `RoleController`

*Inherits from:* `GenericController[Role]`

- **Method** `__init__(self)`

- **Method** `create_role(self, name: str, description: str) -> Role`

- **Method** `get_or_create_leader_role(self) -> Role`


---

### Class `ResearchGroupController`

*Inherits from:* `GenericController[ResearchGroup]`

- **Method** `__init__(self)`

- **Method** `create_research_group(self, name: str, campus_id: int, organization_id: int, description: str, short_name: str, cnpq_url: str, site: str, knowledge_area_ids: List[int]) -> ResearchGroup`

- **Method** `add_leader(self, team_id: int, person_id: int, start_date: Optional[date], end_date: Optional[date]) -> TeamMember`

- **Method** `get_leaders(self, team_id: int) -> List[TeamMember]`


---

### Class `AdvisorshipController`

*Inherits from:* `GenericController[Advisorship]`

- **Method** `__init__(self)`

- **Method** `create_advisorship(self, name: str, student_id: Optional[int], supervisor_id: Optional[int], fellowship_id: Optional[int], start_date: Optional[date], end_date: Optional[date], description: Optional[str], status: str, cancelled: bool, cancellation_date: Optional[date]) -> Advisorship`

- **Method** `cancel_advisorship(self, advisorship_id: int, cancellation_date: Optional[date]) -> Optional[Advisorship]`


---

### Class `FellowshipController`

*Inherits from:* `GenericController[Fellowship]`

- **Method** `__init__(self)`

- **Method** `create_fellowship(self, name: str, value: float, description: Optional[str], sponsor_id: Optional[int]) -> Fellowship`


---

### Class `AcademicEducationController`

  > Controller for Academic Education operations.

*Inherits from:* `GenericController[AcademicEducation]`

- **Method** `__init__(self)`

- **Method** `create_academic_education(self, researcher_id: int, education_type_id: int, title: str, institution_id: int, start_year: int, end_year: Optional[int], thesis_title: Optional[str], advisor_id: Optional[int], co_advisor_id: Optional[int], knowledge_areas: list) -> AcademicEducation`

  > Adds a new education entry to a researcher's profile.

- **Method** `list_history(self, researcher_id: int) -> List[AcademicEducation]`

  > Lists academic history for a researcher.


---

### Class `ArticleController`

  > Controller for Article management.

*Inherits from:* `GenericController[Article]`

- **Method** `__init__(self)`

- **Method** `create_article(self, title: str, year: int, type: str, author_ids: Optional[List[int]], **kwargs) -> Article`

- **Method** `add_author(self, article_id: int, researcher_id: int) -> Optional[Article]`


---

### Class `EducationTypeController`

  > Controller for Education Types.

*Inherits from:* `GenericController[EducationType]`

- **Method** `__init__(self)`

- **Method** `create_education_type(self, name: str) -> EducationType`

  > Creates a new Education Type.

- **Method** `list_education_types(self) -> List[EducationType]`

  > Lists all Education Types.


---

### Class `ProductionTypeController`

  > Controller for Production Types.

*Inherits from:* `GenericController[ProductionType]`

- **Method** `__init__(self)`

- **Method** `create_production_type(self, name: str) -> ProductionType`

  > Creates a new Production Type.


---

### Class `ResearchProductionController`

  > Controller for Research Productions.

*Inherits from:* `GenericController[ResearchProduction]`

- **Method** `__init__(self)`

- **Method** `create_production(self, title: str, year: int, production_type_id: int, author_ids: Optional[List[int]], publisher: Optional[str], isbn: Optional[str], edition: Optional[str], book_title: Optional[str], pages: Optional[str], version: Optional[str], platform: Optional[str], link: Optional[str], **kwargs) -> ResearchProduction`

  > Creates a new research production and associates authors.

- **Method** `add_author(self, production_id: int, researcher_id: int) -> Optional[ResearchProduction]`

  > Add an author to an existing production.


---

## File: `domain/base.py`

## File: `domain/entities/academic_education.py`

### Class `EducationType`

  > Education Type Model (e.g., Graduation, Master, Doctorate).

*Inherits from:* `Base, SerializableMixin`

- **Method** `__init__(self, name: str, id: Optional[int], **kwargs)`

- **Method** `__eq__(self, other)`


---

### Class `AcademicEducation`

  > Academic Education History Model.
  > Represents a degree or certification held by a researcher.

*Inherits from:* `Base, SerializableMixin`

- **Method** `__init__(self, researcher_id: int, education_type_id: int, title: str, institution_id: int, start_year: int, end_year: Optional[int], thesis_title: Optional[str], advisor_id: Optional[int], co_advisor_id: Optional[int], id: Optional[int], **kwargs)`


---

## File: `domain/entities/advisorship.py`

### Class `AdvisorshipType`

*Inherits from:* `enum.Enum`


---

### Class `AdvisorshipRole`

*Inherits from:* `enum.Enum`


---

### Class `AdvisorshipMember`

*Inherits from:* `Base, SerializableMixin`


---

### Class `Advisorship`

  > Advisorship Model.
  > 
  > A specialized Initiative that links a Student and a Supervisor (both represented as Person).
  > An Advisorship has a team composed of a student, supervisor, and board members.
  > Uses Joined Table Inheritance from initiatives.

*Inherits from:* `Initiative, SerializableMixin`

- **Method** `student(self) -> Optional[Person]`

  > Returns the person with Student role.

- **Method** `supervisor(self) -> Optional[Person]`

  > Returns the person with Supervisor role.

- **Method** `board_members(self) -> List[Person]`

  > Returns list of persons with Board Member role.

- **Method** `is_volunteer(self) -> bool`

  > Returns True if the advisorship is voluntary (no fellowship).

- **Method** `add_member(self, person: Person, role: Role, start_date: Optional[date])`

  > Adds a member to the advisorship.

- **Method** `__init__(self, name: str, fellowship_id: Optional[int], institution_id: Optional[int], type: Optional[AdvisorshipType], program: Optional[str], defense_date: Optional[date], fellowship: Optional[object], institution: Optional[object], start_date: Optional[date], end_date: Optional[date], cancelled: bool, cancellation_date: Optional[date], description: Optional[str], status: str, id: Optional[int], **kwargs)`


---

## File: `domain/entities/article.py`

### Class `ArticleType`

*Inherits from:* `enum.Enum`


---

### Class `Article`

  > Scientific Article Entity.
  > Represents a scientific publication with multiple authors.

*Inherits from:* `Base, SerializableMixin`

- **Method** `__init__(self, title: str, year: int, type: ArticleType, authors: Optional[List], doi: Optional[str], journal_conference: Optional[str], volume: Optional[str], pages: Optional[str], id: Optional[int], **kwargs)`


---

## File: `domain/entities/award.py`

### Class `Award`

  > Award Entity.
  > Represents an award or title received by a researcher.

*Inherits from:* `Base, SerializableMixin`

- **Method** `__init__(self, researcher_id: int, title: str, year: Optional[int], id: Optional[int], **kwargs)`


---

## File: `domain/entities/external_research_group.py`

### Class `ExternalResearchGroup`

  > ExternalResearchGroup Model.
  > 
  > Represents a research group from an external institution associated
  > with an initiative. Inherits from Team.

*Inherits from:* `Team`

- **Method** `__init__(self, name: str, contact_email: Optional[str], description: Optional[str], short_name: Optional[str], organization_id: Optional[int], id: Optional[int])`


---

## File: `domain/entities/fellowship.py`

### Class `Fellowship`

  > Fellowship Model.
  > 
  > Represents a scholarship or funding for a student in an advisorship.
  > A fellowship can have a sponsor organization that provides the funding.

*Inherits from:* `Base, SerializableMixin`

- **Method** `__init__(self, name: str, value: float, description: Optional[str], sponsor_id: Optional[int], sponsor: Optional[object], id: Optional[int], **kwargs)`

  > Initializes a new Fellowship instance.
  > 
  > Args:
  >     name: Name of the fellowship
  >     value: Monetary value of the fellowship
  >     description: Optional description
  >     sponsor_id: Optional ID of the sponsoring organization
  >     sponsor: Optional sponsor Organization object
  >     id: Optional fellowship ID


---

## File: `domain/entities/production_type.py`

### Class `ProductionType`

  > Production Type Entity.
  > Categorizes different types of research production (e.g., BOOK, SOFTWARE).

*Inherits from:* `Base`

- **Method** `__init__(self, name: str, id: Optional[int], **kwargs)`


---

## File: `domain/entities/research_production.py`

### Class `ResearchProduction`

  > Research Production Entity.
  > Represents academic outputs like Books, Chapters, and Software.

*Inherits from:* `Base, SerializableMixin`

- **Method** `__init__(self, title: str, year: int, production_type: Optional[object], production_type_id: Optional[int], authors: Optional[List], publisher: Optional[str], isbn: Optional[str], edition: Optional[str], book_title: Optional[str], pages: Optional[str], version: Optional[str], platform: Optional[str], link: Optional[str], id: Optional[int], **kwargs)`


---

## File: `domain/entities/initiative_demandante.py`

## File: `domain/entities/knowledge_area.py`

### Class `KnowledgeArea`

  > KnowledgeArea Model.
  > 
  > Represents a thematic area or field of study for research groups.

*Inherits from:* `Base`

- **Method** `__init__(self, name: str, id: Optional[int])`

  > Initializes a new KnowledgeArea instance.
  > 
  > Args:
  >     name (str): Unique name of the knowledge area.
  >     id (int, optional): Database ID for existing records.


---

## File: `domain/entities/language.py`

### Class `Language`

  > Language Catalog Entity.

*Inherits from:* `Base, SerializableMixin`

- **Method** `__init__(self, name: str, id: Optional[int], **kwargs)`


---

## File: `domain/entities/proficiency.py`

### Class `ProficiencyLevel`

*Inherits from:* `enum.Enum`


---

### Class `Proficiency`

  > Language Proficiency Entity.
  > Links a Researcher to a Language with specific skill levels.

*Inherits from:* `Base, SerializableMixin`

- **Method** `__init__(self, researcher_id: int, language_id: int, comprehension: Optional[ProficiencyLevel], speaking: Optional[ProficiencyLevel], reading: Optional[ProficiencyLevel], writing: Optional[ProficiencyLevel], id: Optional[int], **kwargs)`


---

## File: `domain/entities/research_group.py`

### Class `ResearchGroup`

  > ResearchGroup Model.
  > 
  > A ResearchGroup is a team associated with a campus, extending eo_lib Team.
  > It includes research-specific metadata like CNPq links and Knowledge Areas.

*Inherits from:* `Team, SerializableMixin`

- **Method** `__init__(self, name: str, campus_id: Optional[int], description: Optional[str], short_name: Optional[str], organization_id: Optional[int], cnpq_url: Optional[str], site: Optional[str], knowledge_areas: Optional[List], id: Optional[int])`

  > Initializes a new ResearchGroup instance.


---

## File: `domain/entities/researcher.py`

### Class `Researcher`

  > Researcher Model.
  > 
  > A Researcher represents a person in the research domain, extending eo_lib Person.
  > It includes academic metadata like CNPq and Google Scholar links.

*Inherits from:* `Person, SerializableMixin`

- **Method** `__init__(self, name: str, cnpq_url: Optional[str], google_scholar_url: Optional[str], resume: Optional[str], citation_names: Optional[str], knowledge_areas: Optional[List], articles: Optional[List], id: Optional[int], **kwargs)`

  > Initializes a new Researcher instance.


---

## File: `domain/entities/university.py`

### Class `University`

  > A University is an organization, extending eo_lib Organization.

*Inherits from:* `Organization`


---

### Class `Campus`

  > A Campus is an organizational unit within a university, extending eo_lib OrganizationalUnit.

*Inherits from:* `OrganizationalUnit`


---

## File: `domain/mixins.py`

### Class `SerializableMixin`

  > Mixin that adds serialization capabilities to SQLAlchemy models.

- **Method** `to_dict(self)`

  > Returns a dictionary representation of the model, including all columns
  > from the current class and any parent classes (if using Joined Table Inheritance).


---

## File: `domain/repositories/repositories.py`

### Class `ResearcherRepositoryInterface`

  > Interface for Researcher Repository.

*Inherits from:* `PersonRepositoryInterface`


---

### Class `UniversityRepositoryInterface`

  > Interface for University Repository.

*Inherits from:* `OrganizationRepositoryInterface`


---

### Class `CampusRepositoryInterface`

  > Interface for Campus Repository.

*Inherits from:* `OrganizationalUnitRepositoryInterface`


---

### Class `ResearchGroupRepositoryInterface`

  > Interface for ResearchGroup Repository.

*Inherits from:* `TeamRepositoryInterface`


---

### Class `KnowledgeAreaRepositoryInterface`

  > Interface for KnowledgeArea Repository.

*Inherits from:* `GenericRepositoryInterface`


---

### Class `RoleRepositoryInterface`

  > Interface for Role Repository.

*Inherits from:* `GenericRepositoryInterface`


---

### Class `AdvisorshipRepositoryInterface`

  > Interface for Advisorship Repository.

*Inherits from:* `GenericRepositoryInterface`


---

### Class `FellowshipRepositoryInterface`

  > Interface for Fellowship Repository.

*Inherits from:* `GenericRepositoryInterface`


---

### Class `AcademicEducationRepositoryInterface`

  > Interface for Academic Education Repository.

*Inherits from:* `GenericRepositoryInterface`

- **Method** `list_by_researcher(self, researcher_id: int) -> List[AcademicEducation]`

  > Lists all education records for a researcher.


---

### Class `ArticleRepositoryInterface`

  > Interface for Article Repository.

*Inherits from:* `GenericRepositoryInterface`

- **Method** `list_by_year(self, year: int) -> List[Article]`

  > List all articles published in a specific year.

- **Method** `find_by_doi(self, doi: str) -> Optional[Article]`

  > Find an article by its DOI.


---

### Class `EducationTypeRepositoryInterface`

  > Interface for EducationType Repository.

*Inherits from:* `GenericRepositoryInterface`


---

### Class `ProductionTypeRepositoryInterface`

  > Interface for ProductionType Repository.

*Inherits from:* `GenericRepositoryInterface`


---

### Class `ResearchProductionRepositoryInterface`

  > Interface for ResearchProduction Repository.

*Inherits from:* `GenericRepositoryInterface`


---

## File: `factories.py`

### Class `ServiceFactory`

  > Factory for creating Service instances with the appropriate Repository Strategy.

- **Method** `_get_strategies()`

- **Method** `create_researcher_service() -> ResearcherService`

- **Method** `create_university_service() -> UniversityService`

- **Method** `create_campus_service() -> CampusService`

- **Method** `create_research_group_service() -> ResearchGroupService`

- **Method** `create_knowledge_area_service() -> KnowledgeAreaService`

- **Method** `create_role_service() -> RoleService`

- **Method** `create_advisorship_service() -> AdvisorshipService`

- **Method** `create_fellowship_service() -> FellowshipService`

- **Method** `create_academic_education_service() -> AcademicEducationService`

- **Method** `create_article_service() -> ArticleService`

- **Method** `create_education_type_service() -> EducationTypeService`

- **Method** `create_production_type_service() -> ProductionTypeService`

- **Method** `create_research_production_service() -> ResearchProductionService`


---

## File: `infrastructure/database/postgres_client.py`

### Class `PostgresClient`

  > Singleton Database Client for PostgreSQL.
  > 
  > Manages the SQLAlchemy Engine and SessionFactory (SessionLocal) to provide
  > thread-safe database access throughout the application.

- **Method** `__new__(cls)`

  > Ensures only one instance of PostgresClient exists.
  > 
  > Returns:
  >     PostgresClient: The singleton instance.

- **Method** `_initialize(self)`

  > Initializes the SQLAlchemy engine and session factory.
  > Uses configuration from the Config class.

- **Method** `get_session(self) -> Session`

  > Creates and returns a new SQLAlchemy Session.
  > 
  > Returns:
  >     Session: A new database session instance.

- **Method** `create_tables(self)`

  > Utility method to create all database tables defined in the ORM models.
  > Useful for development and testing environments.


---

## File: `infrastructure/repositories/academic_education_repository_impl.py`

### Class `AcademicEducationRepository`

  > SQLAlchemy implementation of AcademicEducationRepository.
  > Inherits generic CRUD from BaseRepository.

*Inherits from:* `BaseRepository[AcademicEducation], IAcademicEducationRepository`

- **Method** `__init__(self, session: Session)`

- **Method** `add(self, education: AcademicEducation) -> AcademicEducation`

- **Method** `list_by_researcher(self, researcher_id: int) -> List[AcademicEducation]`


---

## File: `infrastructure/repositories/article_repository_impl.py`

### Class `ArticleRepositoryImpl`

  > SQLAlchemy implementation of the Article Repository.

*Inherits from:* `GenericSqlRepository[Article], IArticleRepository`

- **Method** `__init__(self, session)`

- **Method** `list_by_year(self, year: int) -> List[Article]`

- **Method** `find_by_doi(self, doi: str) -> Optional[Article]`


---

## File: `infrastructure/repositories/education_type_repository_impl.py`

### Class `EducationTypeRepositoryImpl`

  > SQLAlchemy implementation of EducationType Repository.

*Inherits from:* `GenericSqlRepository[EducationType], IEducationTypeRepository`

- **Method** `__init__(self, session: Session)`


---

## File: `infrastructure/repositories/memory_repositories.py`

### Class `BaseInMemoryRepository`

*Inherits from:* `GenericMemoryRepository`

- **Method** `__init__(self)`

- **Method** `add(self, entity: Any) -> Any`


---

### Class `InMemoryResearcherRepository`

*Inherits from:* `BaseInMemoryRepository, ResearcherRepositoryInterface`


---

### Class `InMemoryUniversityRepository`

*Inherits from:* `BaseInMemoryRepository, UniversityRepositoryInterface`


---

### Class `InMemoryCampusRepository`

*Inherits from:* `BaseInMemoryRepository, CampusRepositoryInterface`


---

### Class `InMemoryResearchGroupRepository`

*Inherits from:* `BaseInMemoryRepository, ResearchGroupRepositoryInterface`

- **Method** `__init__(self)`

- **Method** `add_member(self, member: TeamMember) -> TeamMember`

- **Method** `remove_member(self, member_id: int) -> bool`

- **Method** `get_members(self, team_id: int) -> List[TeamMember]`


---

### Class `InMemoryKnowledgeAreaRepository`

*Inherits from:* `BaseInMemoryRepository, KnowledgeAreaRepositoryInterface`


---

### Class `InMemoryRoleRepository`

*Inherits from:* `BaseInMemoryRepository, RoleRepositoryInterface`


---

### Class `InMemoryAdvisorshipRepository`

*Inherits from:* `BaseInMemoryRepository, AdvisorshipRepositoryInterface`


---

### Class `InMemoryFellowshipRepository`

*Inherits from:* `BaseInMemoryRepository, FellowshipRepositoryInterface`


---

### Class `InMemoryAcademicEducationRepository`

*Inherits from:* `BaseInMemoryRepository, AcademicEducationRepositoryInterface`


---

### Class `InMemoryArticleRepository`

*Inherits from:* `BaseInMemoryRepository, ArticleRepositoryInterface`


---

### Class `InMemoryEducationTypeRepository`

*Inherits from:* `BaseInMemoryRepository, EducationTypeRepositoryInterface`


---

### Class `InMemoryProductionTypeRepository`

*Inherits from:* `BaseInMemoryRepository, ProductionTypeRepositoryInterface`


---

### Class `InMemoryResearchProductionRepository`

*Inherits from:* `BaseInMemoryRepository, ResearchProductionRepositoryInterface`


---

## File: `infrastructure/repositories/sql_repositories.py`

### Class `PostgresResearcherRepository`

*Inherits from:* `GenericSqlRepository[Researcher], ResearcherRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresEducationTypeRepository`

*Inherits from:* `GenericSqlRepository[EducationType], EducationTypeRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresProductionTypeRepository`

*Inherits from:* `GenericSqlRepository[ProductionType], ProductionTypeRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresResearchProductionRepository`

*Inherits from:* `GenericSqlRepository[ResearchProduction], ResearchProductionRepositoryInterface`

- **Method** `__init__(self)`

### Class `PostgresUniversityRepository`

*Inherits from:* `GenericSqlRepository[University], UniversityRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresCampusRepository`

*Inherits from:* `GenericSqlRepository[Campus], CampusRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresResearchGroupRepository`

*Inherits from:* `GenericSqlRepository[ResearchGroup], ResearchGroupRepositoryInterface`

- **Method** `__init__(self)`

- **Method** `add_member(self, member: TeamMember) -> TeamMember`

- **Method** `remove_member(self, member_id: int) -> bool`

- **Method** `get_members(self, team_id: int) -> List[TeamMember]`


---

### Class `PostgresKnowledgeAreaRepository`

*Inherits from:* `GenericSqlRepository[KnowledgeArea], KnowledgeAreaRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresRoleRepository`

*Inherits from:* `GenericSqlRepository[Role], RoleRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresAdvisorshipRepository`

*Inherits from:* `GenericSqlRepository[Advisorship], AdvisorshipRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresFellowshipRepository`

*Inherits from:* `GenericSqlRepository[Fellowship], FellowshipRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresAcademicEducationRepository`

*Inherits from:* `GenericSqlRepository[AcademicEducation], AcademicEducationRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresArticleRepository`

*Inherits from:* `GenericSqlRepository[Article], ArticleRepositoryInterface`

- **Method** `__init__(self)`


---

### Class `PostgresEducationTypeRepository`

*Inherits from:* `GenericSqlRepository[EducationType], EducationTypeRepositoryInterface`

- **Method** `__init__(self)`


---

## File: `services/services.py`

### Class `RoleService`

*Inherits from:* `GenericService[Role]`

- **Method** `__init__(self, repo: RoleRepositoryInterface)`

- **Method** `get_or_create_leader_role(self) -> Role`

  > Finds or creates the 'Leader' role.


---

### Class `KnowledgeAreaService`

*Inherits from:* `GenericService[KnowledgeArea]`

- **Method** `__init__(self, repo: KnowledgeAreaRepositoryInterface)`


---

### Class `ResearcherService`

*Inherits from:* `PersonService`

- **Method** `__init__(self, repo: ResearcherRepositoryInterface)`


---

### Class `UniversityService`

*Inherits from:* `OrganizationService`

- **Method** `__init__(self, repo: UniversityRepositoryInterface)`


---

### Class `CampusService`

*Inherits from:* `OrganizationalUnitService`

- **Method** `__init__(self, repo: CampusRepositoryInterface)`


---

### Class `ResearchGroupService`

*Inherits from:* `TeamService`

- **Method** `__init__(self, repo: ResearchGroupRepositoryInterface)`

- **Method** `create_research_group(self, name: str, campus_id: int, organization_id: int, description: str, short_name: str, cnpq_url: str, site: str, knowledge_areas: List[KnowledgeArea]) -> ResearchGroup`

- **Method** `add_leader(self, team_id: int, person_id: int, role_id: int, start_date: Optional[date], end_date: Optional[date]) -> TeamMember`

  > Adds a leader to the group.


---

### Class `AdvisorshipService`

*Inherits from:* `GenericService[Advisorship]`

- **Method** `__init__(self, repo: AdvisorshipRepositoryInterface, researcher_repo: ResearcherRepositoryInterface, role_repo: RoleRepositoryInterface)`

- **Method** `create_advisorship(self, name: str, student_id: Optional[int], supervisor_id: Optional[int], fellowship_id: Optional[int], institution_id: Optional[int], start_date: Optional[date], end_date: Optional[date], description: Optional[str], status: str, cancelled: bool, cancellation_date: Optional[date], type: Optional[str]) -> Advisorship`

  > Creates an Advisorship and assigns Student/Supervisor roles.

- **Method** `cancel_advisorship(self, advisorship_id: int, cancellation_date: date) -> Optional[Advisorship]`

  > Marks an advisorship as cancelled.


---

### Class `FellowshipService`

*Inherits from:* `GenericService[Fellowship]`

- **Method** `__init__(self, repo: FellowshipRepositoryInterface)`


---

### Class `AcademicEducationService`

  > Service for managing Academic Education history.

*Inherits from:* `GenericService[AcademicEducation]`

- **Method** `__init__(self, repository: AcademicEducationRepositoryInterface)`

- **Method** `create_education(self, researcher_id: int, education_type_id: int, title: str, institution_id: int, start_year: int, end_year: Optional[int], thesis_title: Optional[str], advisor_id: Optional[int], co_advisor_id: Optional[int], knowledge_areas: list) -> AcademicEducation`

  > Creates and persists a new academic education record.

- **Method** `get_by_researcher(self, researcher_id: int) -> List[AcademicEducation]`

  > Retrieves all education records for a researcher.

- **Method** `delete_education(self, education_id: int) -> bool`

  > Deletes an education record.


---

### Class `ArticleService`

  > Service for managing Articles.

*Inherits from:* `GenericService[Article]`

- **Method** `__init__(self, repository: ArticleRepositoryInterface, researcher_repository: ResearcherRepositoryInterface)`

- **Method** `create_article(self, title: str, year: int, type: ArticleType, author_ids: Optional[List[int]], doi: Optional[str], journal_conference: Optional[str], **kwargs) -> Article`

  > Create a new article and associate authors.

- **Method** `add_author(self, article_id: int, researcher_id: int) -> Optional[Article]`

  > Add an author to an existing article.


---

### Class `EducationTypeService`

  > Service for managing Education Types.

*Inherits from:* `GenericService[EducationType]`

- **Method** `__init__(self, repository: EducationTypeRepositoryInterface)`

- **Method** `create_education_type(self, name: str) -> EducationType`

  > Creates a new Education Type.

- **Method** `get_by_name(self, name: str) -> Optional[EducationType]`

  > Retrieves an Education Type by name.


---

### Class `ProductionTypeService`

  > Service for managing Production Types.

*Inherits from:* `GenericService[ProductionType]`

- **Method** `__init__(self, repository: ProductionTypeRepositoryInterface)`

- **Method** `create_production_type(self, name: str) -> ProductionType`

  > Creates a new Production Type.

- **Method** `get_by_name(self, name: str) -> Optional[ProductionType]`

  > Retrieves a Production Type by name.


---

### Class `ResearchProductionService`

  > Service for managing Research Productions.

*Inherits from:* `GenericService[ResearchProduction]`

- **Method** `__init__(self, repository: ResearchProductionRepositoryInterface, researcher_repository: ResearcherRepositoryInterface)`

- **Method** `create_production(self, title: str, year: int, production_type_id: int, author_ids: Optional[List[int]], publisher: Optional[str], isbn: Optional[str], edition: Optional[str], book_title: Optional[str], pages: Optional[str], version: Optional[str], platform: Optional[str], link: Optional[str], **kwargs) -> ResearchProduction`

  > Creates a new research production and associates authors.

- **Method** `add_author(self, production_id: int, researcher_id: int) -> Optional[ResearchProduction]`

  > Add an author to an existing production.
