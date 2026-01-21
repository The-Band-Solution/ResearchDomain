from .memory_repositories import (InMemoryCampusRepository,
                                  InMemoryKnowledgeAreaRepository,
                                  InMemoryResearcherRepository,
                                  InMemoryResearchGroupRepository,
                                  InMemoryRoleRepository,
                                  InMemoryUniversityRepository)
from .sql_repositories import (PostgresCampusRepository,
                               PostgresKnowledgeAreaRepository,
                               PostgresResearcherRepository,
                               PostgresResearchGroupRepository,
                               PostgresRoleRepository,
                               PostgresUniversityRepository)

__all__ = [
    "PostgresResearcherRepository",
    "PostgresUniversityRepository",
    "PostgresCampusRepository",
    "PostgresResearchGroupRepository",
    "PostgresKnowledgeAreaRepository",
    "PostgresRoleRepository",
    "InMemoryResearcherRepository",
    "InMemoryUniversityRepository",
    "InMemoryCampusRepository",
    "InMemoryResearchGroupRepository",
    "InMemoryKnowledgeAreaRepository",
    "InMemoryRoleRepository",
]
