import pytest
from unittest.mock import MagicMock
from research_domain.services.article_service import ArticleService
from research_domain.controllers.article_controller import ArticleController
from research_domain.domain.entities.article import Article, ArticleType
from research_domain.domain.entities.researcher import Researcher
from research_domain.domain.repositories.article_repository import IArticleRepository
from research_domain.domain.repositories.repositories import ResearcherRepositoryInterface

class TestArticleLayers:
    @pytest.fixture
    def mock_article_repo(self):
        return MagicMock()

    @pytest.fixture
    def mock_researcher_repo(self):
        return MagicMock()

    @pytest.fixture
    def service(self, mock_article_repo, mock_researcher_repo):
        return ArticleService(mock_article_repo, mock_researcher_repo)

    @pytest.fixture
    def controller(self, service):
        return ArticleController(service)

    def test_service_create_article(self, service, mock_article_repo, mock_researcher_repo):
        # Setup
        r1 = Researcher(name="Author 1", id=1)
        mock_researcher_repo.get.return_value = r1
        
        # Action
        service.create_article(
            title="Service Test",
            year=2024,
            type=ArticleType.JOURNAL,
            author_ids=[1]
        )
        
        # Verify
        mock_article_repo.add.assert_called_once()
        call_args = mock_article_repo.add.call_args[0][0]
        assert isinstance(call_args, Article)
        assert call_args.title == "Service Test"
        assert len(call_args.authors) == 1
        assert call_args.authors[0].id == 1

    def test_controller_create_article_enum_parsing(self, controller, service):
        # Setup (mock service method explicitly if needed, but it's already linked)
        # We want to check enum parsing logic in controller
        service.create_article = MagicMock()
        
        # Action
        controller.create_article(title="Ctrl Test", year=2024, type="Journal")
        
        # Verify
        service.create_article.assert_called_once()
        call_kwargs = service.create_article.call_args[1]
        assert call_kwargs['type'] == ArticleType.JOURNAL

    def test_service_add_author(self, service, mock_article_repo, mock_researcher_repo):
        article = Article(title="Existing", year=2020, type=ArticleType.CONFERENCE_EVENT, id=10)
        researcher = Researcher(name="New Author", id=5)
        
        mock_article_repo.get_by_id.return_value = article
        mock_researcher_repo.get.return_value = researcher
        
        service.add_author(10, 5)
        
        assert len(article.authors) == 1
        assert article.authors[0] == researcher
        mock_article_repo.update.assert_called_once_with(article)
