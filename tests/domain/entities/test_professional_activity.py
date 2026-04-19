from eo_lib.domain.entities import Organization

from research_domain.domain.entities.professional_activity import ProfessionalActivity
from research_domain.domain.entities.researcher import Researcher


class TestProfessionalActivity:
    def test_create_professional_activity(self):
        researcher = Researcher(name="Dr. Example", id=1)
        organization = Organization(name="Federal Institute", id=10)

        activity = ProfessionalActivity(
            researcher_id=researcher.id,
            organization_id=organization.id,
            institution="Instituto Federal do Espirito Santo, IFES, Brasil.",
            institution_name="Instituto Federal do Espirito Santo",
            institution_acronym="IFES",
            institution_country="Brasil",
            period="2012 - Atual",
            start_year=2012,
            current=True,
            bond="Servidor Publico",
            classification="Professor Efetivo",
            work_regime="Dedicacao exclusiva",
            activity_type="Atuacao profissional",
        )

        assert activity.researcher_id == 1
        assert activity.organization_id == 10
        assert activity.institution == "Instituto Federal do Espirito Santo, IFES, Brasil."
        assert activity.institution_name == "Instituto Federal do Espirito Santo"
        assert activity.institution_acronym == "IFES"
        assert activity.institution_country == "Brasil"
        assert activity.period == "2012 - Atual"
        assert activity.start_year == 2012
        assert activity.end_year is None
        assert activity.current is True
        assert activity.bond == "Servidor Publico"
        assert activity.classification == "Professor Efetivo"
        assert activity.work_regime == "Dedicacao exclusiva"
        assert activity.activity_type == "Atuacao profissional"

    def test_create_professional_activity_from_lattes_dict(self):
        payload = {
            "instituicao": "Instituto Federal do Espírito Santo, IFES, Brasil.",
            "instituicao_nome": "Instituto Federal do Espírito Santo",
            "instituicao_sigla": "IFES",
            "instituicao_pais": "Brasil",
            "periodo": "2012 - Atual",
            "ano_inicio": "2012",
            "ano_fim": "Atual",
            "vinculo": "Servidor Público",
            "enquadramento": "Professor Efetivo",
            "regime": "Dedicação exclusiva",
            "cargo_funcao": None,
            "tipo": "Atuação profissional",
        }

        activity = ProfessionalActivity.from_dict(researcher_id=1, data=payload)

        assert activity.researcher_id == 1
        assert activity.institution == payload["instituicao"]
        assert activity.institution_name == payload["instituicao_nome"]
        assert activity.institution_acronym == payload["instituicao_sigla"]
        assert activity.institution_country == payload["instituicao_pais"]
        assert activity.period == payload["periodo"]
        assert activity.start_year == 2012
        assert activity.end_year is None
        assert activity.current is True
        assert activity.bond == payload["vinculo"]
        assert activity.classification == payload["enquadramento"]
        assert activity.work_regime == payload["regime"]
        assert activity.role_function is None
        assert activity.activity_type == payload["tipo"]
