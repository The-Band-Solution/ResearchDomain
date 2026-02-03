from typing import List, Optional, Any

from libbase.controllers.generic_controller import GenericController
from research_domain.services.article_service import ArticleService
from research_domain.domain.entities.article import Article, ArticleType

class ArticleController(GenericController[Article]):
    """
    Controller for Article management.
    """
    def __init__(self, service: ArticleService):
        super().__init__(service)

    def create_article(
        self, 
        title: str, 
        year: int, 
        type: str, # String input from API/CLI parsed to Enum
        author_ids: Optional[List[int]] = None,
        **kwargs
    ) -> Any:
        try:
            # Parse Enum from string if needed, or pass directly if internal call
            article_type = ArticleType(type) if isinstance(type, str) else type
            return self._service.create_article(
                title=title,
                year=year,
                type=article_type,
                author_ids=author_ids,
                **kwargs
            )
        except ValueError:
            raise ValueError(f"Invalid ArticleType: {type}")

    def add_author(self, article_id: int, researcher_id: int) -> Any:
        return self._service.add_author(article_id, researcher_id)
