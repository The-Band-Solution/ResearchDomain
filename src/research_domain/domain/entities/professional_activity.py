from typing import Any, Mapping, Optional

from eo_lib.domain.base import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from research_domain.domain.mixins import SerializableMixin


class ProfessionalActivity(Base, SerializableMixin):
    """
    Professional Activity Entity.
    Represents a researcher's professional work history.
    The structure is based on Lattes-like "atuacao_profissional" payloads.
    """

    __tablename__ = "professional_activities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    researcher_id = Column(Integer, ForeignKey("researchers.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)

    institution = Column(String(500), nullable=False)
    institution_name = Column(String(255), nullable=True)
    institution_acronym = Column(String(100), nullable=True)
    institution_country = Column(String(100), nullable=True)
    period = Column(String(100), nullable=True)
    start_year = Column(Integer, nullable=True)
    end_year = Column(Integer, nullable=True)
    bond = Column(String(100), nullable=True)
    classification = Column(String(255), nullable=True)
    work_regime = Column(String(100), nullable=True)
    role_function = Column(String(255), nullable=True)
    activity_type = Column(String(100), nullable=True)
    current = Column(Boolean, nullable=False, default=False)

    researcher = relationship("Researcher", back_populates="professional_activities")
    organization = relationship("Organization")

    def __init__(
        self,
        researcher_id: int,
        institution: str,
        organization_id: Optional[int] = None,
        institution_name: Optional[str] = None,
        institution_acronym: Optional[str] = None,
        institution_country: Optional[str] = None,
        period: Optional[str] = None,
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
        bond: Optional[str] = None,
        classification: Optional[str] = None,
        work_regime: Optional[str] = None,
        role_function: Optional[str] = None,
        activity_type: Optional[str] = None,
        current: bool = False,
        id: Optional[int] = None,
        **kwargs,
    ):
        self.id = id
        self.researcher_id = researcher_id
        self.organization_id = organization_id
        self.institution = institution
        self.institution_name = institution_name
        self.institution_acronym = institution_acronym
        self.institution_country = institution_country
        self.period = period
        self.start_year = start_year
        self.end_year = end_year
        self.bond = bond
        self.classification = classification
        self.work_regime = work_regime
        self.role_function = role_function
        self.activity_type = activity_type
        self.current = current

    @classmethod
    def from_dict(
        cls,
        researcher_id: int,
        data: Mapping[str, Any],
        organization_id: Optional[int] = None,
        id: Optional[int] = None,
    ) -> "ProfessionalActivity":
        raw_end_year = data.get("ano_fim")
        current = isinstance(raw_end_year, str) and raw_end_year.strip().lower() == "atual"

        return cls(
            id=id,
            researcher_id=researcher_id,
            organization_id=organization_id,
            institution=str(data.get("instituicao") or ""),
            institution_name=data.get("instituicao_nome"),
            institution_acronym=data.get("instituicao_sigla"),
            institution_country=data.get("instituicao_pais"),
            period=data.get("periodo"),
            start_year=cls._parse_year(data.get("ano_inicio")),
            end_year=None if current else cls._parse_year(raw_end_year),
            bond=data.get("vinculo"),
            classification=data.get("enquadramento"),
            work_regime=data.get("regime"),
            role_function=data.get("cargo_funcao"),
            activity_type=data.get("tipo"),
            current=current,
        )

    @staticmethod
    def _parse_year(value: Any) -> Optional[int]:
        if value in (None, "", "Atual"):
            return None
        try:
            return int(value)
        except (TypeError, ValueError):
            return None
