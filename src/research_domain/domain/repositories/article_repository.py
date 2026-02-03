from abc import ABC, abstractmethod
from typing import List, Optional

from libbase.infrastructure.interface import IRepository
from research_domain.domain.entities.article import Article

class IArticleRepository(IRepository[Article], ABC):
    """
    Interface for Article Repository.
    """
    
    @abstractmethod
    def list_by_year(self, year: int) -> List[Article]:
        """
        List all articles published in a specific year.
        """
        pass
    
    @abstractmethod
    def find_by_doi(self, doi: str) -> Optional[Article]:
        """
        Find an article by its DOI.
        """
        pass
