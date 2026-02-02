from typing import List, Optional

from eo_lib.services.base_service import BaseService
from research_domain.domain.entities.article import Article, ArticleType
from research_domain.domain.repositories.article_repository import IArticleRepository
from research_domain.domain.repositories.researcher_repository import IResearcherRepository

class ArticleService(BaseService[Article]):
    """
    Service for managing Articles.
    """
    def __init__(
        self, 
        repository: IArticleRepository,
        researcher_repository: IResearcherRepository
    ):
        super().__init__(repository)
        self.article_repository = repository
        self.researcher_repository = researcher_repository

    def create_article(
        self, 
        title: str, 
        year: int, 
        type: ArticleType,
        author_ids: Optional[List[int]] = None,
        doi: Optional[str] = None,
        journal_conference: Optional[str] = None,
        **kwargs
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
            **kwargs
        )
        return self.repository.add(article)

    def add_author(self, article_id: int, researcher_id: int) -> Optional[Article]:
        """
        Add an author to an existing article.
        """
        article = self.repository.get(article_id)
        researcher = self.researcher_repository.get(researcher_id)
        
        if article and researcher:
            if researcher not in article.authors:
                article.authors.append(researcher)
                self.repository.update(article)
            return article
        return None
