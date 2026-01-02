# 🧪 ResearchDomain Library

[![CI](https://github.com/The-Band-Solution/ResearchDomain/actions/workflows/ci.yml/badge.svg)](https://github.com/The-Band-Solution/ResearchDomain/actions/workflows/ci.yml)
[![Version](https://img.shields.io/github/v/tag/The-Band-Solution/ResearchDomain?label=version)](https://github.com/The-Band-Solution/ResearchDomain/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A specialized library for managing academic research data, including research groups, campuses, universities, researchers, and scientific production. Built on top of [eo_lib](https://github.com/The-Band-Solution/eo_lib) and following Clean Architecture principles.

## 🏗️ Core Entities

The library specializes generic enterprise ontology concepts into the research domain:

- **University** (Organization): Higher education institutions.
- **Campus** (OrganizationalUnit): Physical locations or administrative divisions of a university.
- **Researcher** (Person): Academic staff and members of research groups.
- **ResearchGroup** (Team): Collaborative units focused on specific research lines.

## 🚀 Quick Start

### Installation

```bash
pip install research-domain
```

Or install from source:

```bash
git clone https://github.com/The-Band-Solution/ResearchDomain.git
cd ResearchDomain
pip install .
```

### Usage Example

```python
from research_domain import (
    UniversityController, 
    CampusController, 
    ResearcherController, 
    ResearchGroupController
)

# 1. Setup controllers
uni_ctrl = UniversityController()
campus_ctrl = CampusController()

# 2. Basic workflow
ufsc = uni_ctrl.create_university(name="UFSC", short_name="Federal University")
fln = campus_ctrl.create_campus(name="Florianópolis", organization_id=ufsc.id)

print(f"Created Campus: {fln.name} in University {ufsc.name}")
```

## ⚙️ Configuration

The library supports a multi-storage strategy configurable via environment variables in a `.env` file:

```env
# Available options: memory, postgres, db
STORAGE_TYPE=memory

# Required only if STORAGE_TYPE=postgres or db
DATABASE_URL=postgresql://user:password@localhost:5432/research_db
```

## 📚 Documentation

For detailed technical information, refer to the following documents:

- **[Requirements](docs/requirements.md)**: Functional and non-functional specifications.
- **[Software Design Description (SDD)](docs/sdd.md)**: Architecture diagrams and domain model.
- **[API Specifications](docs/specifications.md)**: Detailed controller and repository signatures.
- **[Project Backlog](docs/backlog.md)**: Current task status and iteration planning.

## 🛠️ Infrastructure

- **Automatic Backlog Sync**: GitHub Actions automatically keep the `backlog.md` in sync with GitHub Issues.
- **Database Migrations**: Integrated setup logic in `tests/demo.py` for easy PostgreSQL initialization.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
