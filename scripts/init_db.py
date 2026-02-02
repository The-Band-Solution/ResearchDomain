
import os
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from eo_lib.domain.base import Base
from eo_lib.infrastructure.database.postgres_client import PostgresClient
from sqlalchemy import text

# Import generic entities to register them
from eo_lib.domain.entities import (Organization, OrganizationalUnit, Person,
                                    PersonEmail, Role, Team, TeamMember)

# Import domain entities to register them
from research_domain.domain.entities.academic_education import (
    AcademicEducation, EducationType)
from research_domain.domain.entities.advisorship import Advisorship
from research_domain.domain.entities.campus import Campus
from research_domain.domain.entities.fellowship import Fellowship
from research_domain.domain.entities.knowledge_area import KnowledgeArea
from research_domain.domain.entities.researcher import Researcher
from research_domain.domain.entities.research_group import ResearchGroup
from research_domain.domain.entities.university import University

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def init_db():
    print("Initialize Database Tool")
    
    # Check if we are pointing to a real database
    # For safety, we print the connection info or just the type
    # PostgresClient typically reads from env
    
    client = PostgresClient()
    engine = client._engine
    
    print(f"Target DB URL: {engine.url}")
    confirm = input("This will DROP SCHEMA public CASCADE and recreate it. Are you sure? (y/N): ")
    if confirm.lower() != 'y':
        print("Aborted.")
        return

    try:
        with engine.connect() as conn:
            print("Dropping schema public...")
            conn.execute(text("DROP SCHEMA public CASCADE"))
            conn.execute(text("CREATE SCHEMA public"))
            conn.execute(text("GRANT ALL ON SCHEMA public TO public"))
            # conn.execute(text("GRANT ALL ON SCHEMA public TO postgres")) # Optional/Specific
            conn.commit()
            print("Schema public dropped and recreated.")
    except Exception as e:
        print(f"Error during drop: {e}")
        return

    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    init_db()
