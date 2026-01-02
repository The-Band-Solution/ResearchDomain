# ResearchDomain Library

**ResearchDomain** is a robust, strictly architectural Python library designed for managing **Researchers**, **Research Groups**, **Universities**, and **Campuses**. It serves as a domain-specific implementation leveraging **Clean Architecture**, **Spec-Driven Development**, **TDD**, and **DRY** principles, built on top of the generic core implementations `libbase` and `eo_lib`.

## 🌟 Features

*   **Strict Architecture**: Layered design with Controllers (Facade), Services (Logic), Repositories (Persistence), and Domain Models.
*   **Specialized Domain**: Tailored entities for academic environments, specializing generic enterprise ontology concepts.
*   **Multi-Storage Strategy**: Built-in support for PostgreSQL (Production) and In-Memory storage (Testing/Dev) with automatic strategy selection.
*   **DRY (Don't Repeat Yourself)**: Unified Domain Entities and ORM Models leveraging specialized SQLAlchemy Declarative patterns.
*   **CRUD+L & Membership**: Full support for entity management and specialized research group membership logic.
*   **Database Agnostic Wiring**: Built on SQLAlchemy and the Strategy Pattern.
*   **Fully Documented**: Comprehensive documentation as code and Google-style docstrings.
*   **Test Driven**: Verified with `pytest` and end-to-end demonstration scripts.

## 🛠️ Installation

### Prerequisites
- Python 3.10+
- PostgreSQL (Optional, defaults to Memory for dev)

### Direct Installation (Recommended)

You can install `research-domain` directly from official releases.

1.  **Install via pip**:
    Download and install the latest wheel (`.whl`) from our [GitHub Releases](https://github.com/The-Band-Solution/ResearchDomain/releases):

    ```bash
    # Install version v0.1.0
    pip install https://github.com/The-Band-Solution/ResearchDomain/releases/download/v0.1.0/research_domain-0.1.0-py3-none-any.whl
    ```

### Development Setup (Clone)

If you wish to contribute or run the internal demos, clone the repository:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/The-Band-Solution/ResearchDomain.git
    cd ResearchDomain
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install for development**:
    ```bash
    pip install -e .[dev]
    ```

## ⚙️ Configuration

The library uses `python-dotenv` for configuration. Create a `.env` file in the root directory:

```env
# Storage Strategy (memory, postgres, db)
STORAGE_TYPE=memory

# PostgreSQL (Required if STORAGE_TYPE=db or postgres)
# DATABASE_URL=postgresql://user:password@localhost:5432/research_db
```

## 🚀 Usage

The library exposes **Specialized Controllers** as the public API.

### 1. University & Campus Management
```python
from research_domain import UniversityController, CampusController

uni_ctrl = UniversityController()
campus_ctrl = CampusController()

# Create University
ufsc = uni_ctrl.create_university(name="UFSC", short_name="Federal University")

# Create Campus associated with the University
florianopolis = campus_ctrl.create_campus(
    name="Florianópolis Campus", 
    organization_id=ufsc.id
)
```

### 2. Researcher Management
```python
from research_domain import ResearcherController

ctrl = ResearcherController()

# Create Researcher with multiple contact emails
dr_joyce = ctrl.create_researcher(
    name="Dr. Joyce", 
    emails=["joyce@ufsc.br", "joyce.academic@gmail.com"]
)

# Get & List
researcher = ctrl.get_by_id(dr_joyce.id)
all_researchers = ctrl.get_all()
```

### 3. Research Group Management
```python
from research_domain import ResearchGroupController

ctrl = ResearchGroupController()

# Create Research Group within a Campus
ai_lab = ctrl.create_research_group(
    name="Artificial Intelligence Laboratory",
    campus_id=1,
    organization_id=1,
    short_name="LIA"
)

# Membership management (Inherited from Team patterns)
ctrl.add_member(team_id=ai_lab.id, person_id=dr_joyce.id)
```

## 🧪 Testing

### Running Unit Tests (TDD)
Run the domain and logic test suite with:
```bash
pytest
```

### Running the Verification Demo
A demonstration script is provided to verify database persistence and end-to-end flows:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python3 tests/demo.py
```

## 📚 Documentation
*   [Requirements](docs/requirements.md)
*   [Specifications](docs/specifications.md)
*   [SDD / UML](docs/sdd.md)
*   [Project Backlog](docs/backlog.md)
