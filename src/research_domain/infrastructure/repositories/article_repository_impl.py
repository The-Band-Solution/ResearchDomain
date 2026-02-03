from typing import List, Optional

from libbase.infrastructure.sql_repository import GenericSqlRepository
from research_domain.domain.entities.article import Article
from research_domain.domain.repositories.article_repository import IArticleRepository

class ArticleRepositoryImpl(GenericSqlRepository[Article], IArticleRepository):
    """
    SQLAlchemy implementation of the Article Repository.
    """
    def __init__(self, session):
        super().__init__(session, Article)

    def list_by_year(self, year: int) -> List[Article]:
        return self._session.query(Article).filter(Article.year == year).all()
        
    def find_by_doi(self, doi: str) -> Optional[Article]:
        return self._session.query(Article).filter(Article.doi == doi).first()
