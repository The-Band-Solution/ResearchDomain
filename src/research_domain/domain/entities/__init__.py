from .advisorship import Advisorship, AdvisorshipRole, AdvisorshipMember
from .external_research_group import ExternalResearchGroup
from .fellowship import Fellowship
from .initiative_demandante import initiative_demandantes
from .knowledge_area import KnowledgeArea
from .research_group import ResearchGroup
from .researcher import Researcher
from .university import Campus, University
from .production_type import ProductionType
from .research_production import ResearchProduction

__all__ = [
    "Researcher",
    "University",
    "Campus",
    "ResearchGroup",
    "KnowledgeArea",
    "ExternalResearchGroup",
    "initiative_demandantes",
    "Advisorship",
    "AdvisorshipRole",
    "AdvisorshipMember",
    "Fellowship",
    "ProductionType",
    "ResearchProduction",
]
