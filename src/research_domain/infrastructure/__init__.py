from .database import PostgresClient
from .repositories import (InMemoryCampusRepository,
                           InMemoryResearcherRepository,
                           InMemoryResearchGroupRepository,
                           InMemoryUniversityRepository,
                           PostgresCampusRepository,
                           PostgresResearcherRepository,
                           PostgresResearchGroupRepository,
                           PostgresUniversityRepository)

__all__ = [
    "PostgresResearcherRepository",
    "PostgresUniversityRepository",
    "PostgresCampusRepository",
    "PostgresResearchGroupRepository",
    "InMemoryResearcherRepository",
    "InMemoryUniversityRepository",
    "InMemoryCampusRepository",
    "InMemoryResearchGroupRepository",
    "PostgresClient",
]
