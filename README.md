# 🧪 ResearchDomain Library

[![CI](https://github.com/The-Band-Solution/ResearchDomain/actions/workflows/ci.yml/badge.svg)](https://github.com/The-Band-Solution/ResearchDomain/actions/workflows/ci.yml)
[![Version](https://img.shields.io/github/v/tag/The-Band-Solution/ResearchDomain?label=version)](https://github.com/The-Band-Solution/ResearchDomain/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A specialized library for managing academic research data, including research groups, campuses, universities, researchers, and scientific production. Built on top of [eo_lib](https://github.com/The-Band-Solution/eo_lib) and following Clean Architecture principles.

## 🏗️ Library Architecture

Following the standard library template, ResearchDomain is structured into four key layers:

### 1. Domain
Contains the core business entities and repository interfaces:
- **Entities**: [University](src/research_domain/domain/entities/university.py), [Campus](src/research_domain/domain/entities/university.py), [Researcher](src/research_domain/domain/entities/researcher.py), [ResearchGroup](src/research_domain/domain/entities/research_group.py).
- **Repositories**: Interfaces defined in [repositories.py](src/research_domain/domain/repositories/repositories.py).

### 2. Infrastructure
Concrete implementations for data access:
- **SQL (PostgreSQL)**: Optimized SQLAlchemy strategies in [sql_repositories.py](src/research_domain/infrastructure/repositories/sql_repositories.py).
- **In-Memory**: Standardized memory repositories with auto-increment IDs in [memory_repositories.py](src/research_domain/infrastructure/repositories/memory_repositories.py).

### 3. Services
Business logic layer extending [libbase](https://github.com/The-Band-Solution/libbase) and [eo_lib](https://github.com/The-Band-Solution/eo_lib):
- Implementation found in [services.py](src/research_domain/services/services.py).

### 4. Wiring & Presentation
Integration and API exposure:
- **Factories**: [ServiceFactory](src/research_domain/factories.py) manages strategy selection (Memory vs DB).
- **Controllers**: Specialized APIs for all research entities in [controllers.py](src/research_domain/controllers/controllers.py).

## 🚀 Quick Start

### Installation

```bash
pip install research-domain
```

### Usage Example

```python
from research_domain import UniversityController

uni_ctrl = UniversityController()
ufsc = uni_ctrl.create_university(name="UFSC", short_name="Federal University")
print(f"Created: {ufsc.name}")
```

## ⚙️ Configuration

Set the storage strategy in your `.env` file:

```env
# Options: memory, postgres, db
STORAGE_TYPE=memory
DATABASE_URL=postgresql://user:password@localhost:5432/research_db
```

## 📚 Documentation

- **[Requirements](docs/requirements.md)**
- **[Software Design Description (SDD)](docs/sdd.md)**
- **[API Specifications](docs/specifications.md)**
- **[Project Backlog](docs/backlog.md)**

## 📄 License

MIT License.
