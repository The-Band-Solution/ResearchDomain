import pytest
from research_domain.domain.entities.researcher import Researcher

def test_create_researcher_with_resume():
    resume_text = "Experienced researcher in AI and Software Engineering."
    researcher = Researcher(
        name="Dr. Smith",
        resume=resume_text
    )
    assert researcher.name == "Dr. Smith"
    assert researcher.resume == resume_text

def test_researcher_resume_none_by_default():
    researcher = Researcher(name="Dr. No Resume")
    assert researcher.resume is None

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from eo_lib.domain.base import Base
from libbase.infrastructure.sql_repository import GenericSqlRepository

def test_persist_researcher_with_resume():
    engine = create_engine("sqlite:///:memory:")
    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    resume_text = "Proficient in Python and Domain-Driven Design."
    researcher = Researcher(name="Persisted Dr.", resume=resume_text)
    
    repo = GenericSqlRepository(session, Researcher)
    repo.add(researcher)
    session.commit()
    researcher_id = researcher.id
    
    session.close()
    session = SessionLocal()
    
    retrieved = session.query(Researcher).filter_by(id=researcher_id).first()
    assert retrieved.resume == resume_text
    
    session.close()
