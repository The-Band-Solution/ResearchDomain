# Project Backlog - ResearchDomain

This document is automatically synchronized with GitHub Issues. Last updated: 2026-01-27 01:18:19

## 📋 Master Issue List
Overview of all demands, their states and executors.

| # | Status | Title | Executor | Sprint | Milestone |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [# 20](https://github.com/The-Band-Solution/ResearchDomain/issues/20) | 🟢 | Feat: Implement Services and Improve Factories | @paulossjunior | - | Issue Base |
| [# 17](https://github.com/The-Band-Solution/ResearchDomain/issues/17) | 🟢 | Feat: Associate Initiative to Demandante (Organization) | @paulossjunior | - | - |
| [# 15](https://github.com/The-Band-Solution/ResearchDomain/issues/15) | 🟢 | Feat: Associate Initiative to External Research Group | @paulossjunior | - | - |
| [# 13](https://github.com/The-Band-Solution/ResearchDomain/issues/13) | 🟢 | Feat: Associate Knowledge Area to Initiatives | @paulossjunior | - | - |
| [# 9](https://github.com/The-Band-Solution/ResearchDomain/issues/9) | ✅ | [US] Researcher Academic Metadata & Knowledge Areas | - | - | Issue Base |
| [# 6](https://github.com/The-Band-Solution/ResearchDomain/issues/6) | ✅ | [TASK] Implementation of Role-based Leadership and Many-to-Many Areas | - | - | Issue Base |
| [# 5](https://github.com/The-Band-Solution/ResearchDomain/issues/5) | ✅ | [US] ResearchGroup Categorization & Leadership Recognition | - | - | Issue Base |
| [# 4](https://github.com/The-Band-Solution/ResearchDomain/issues/4) | ✅ | [EPIC] ResearchGroup Metadata & Advanced Membership | - | - | Issue Base |
| [# 1](https://github.com/The-Band-Solution/ResearchDomain/issues/1) | ✅ | Implement ResearchGroup Feature (Entities, Repositories, Controllers) | - | - | Issue Base |

---

## 📂 Workflow States

### 🟢 In Progress / Todo
- [#20](https://github.com/The-Band-Solution/ResearchDomain/issues/20) **Feat: Implement Services and Improve Factories**
- [#17](https://github.com/The-Band-Solution/ResearchDomain/issues/17) **Feat: Associate Initiative to Demandante (Organization)**
- [#15](https://github.com/The-Band-Solution/ResearchDomain/issues/15) **Feat: Associate Initiative to External Research Group**
- [#13](https://github.com/The-Band-Solution/ResearchDomain/issues/13) **Feat: Associate Knowledge Area to Initiatives**

### ✅ Done / Released
- [#9](https://github.com/The-Band-Solution/ResearchDomain/issues/9) **[US] Researcher Academic Metadata & Knowledge Areas**
- [#6](https://github.com/The-Band-Solution/ResearchDomain/issues/6) **[TASK] Implementation of Role-based Leadership and Many-to-Many Areas**
- [#5](https://github.com/The-Band-Solution/ResearchDomain/issues/5) **[US] ResearchGroup Categorization & Leadership Recognition**
- [#4](https://github.com/The-Band-Solution/ResearchDomain/issues/4) **[EPIC] ResearchGroup Metadata & Advanced Membership**
- [#1](https://github.com/The-Band-Solution/ResearchDomain/issues/1) **Implement ResearchGroup Feature (Entities, Repositories, Controllers)**

---

## 📝 Detailed Backlog

### [OPEN] [#20](https://github.com/The-Band-Solution/ResearchDomain/issues/20) Feat: Implement Services and Improve Factories
- **Executor**: paulossjunior
- **Labels**: feature, task
- **Milestone**: Issue Base

**Description**:
Implement the service layer for the recently added domain entities and refactor ServiceFactory for better maintainability.\n\nRef: docs/requirements.md (FR-05-C, FR-05-E, FR-05-G)

---

### [OPEN] [#17](https://github.com/The-Band-Solution/ResearchDomain/issues/17) Feat: Associate Initiative to Demandante (Organization)
- **Executor**: paulossjunior
- **Labels**: epic
- **Milestone**: -

**Description**:
Implement Many-to-One relationship between Initiative and Organization (Demandante).\n\nRef: docs/requirements.md (FR-05-D)

---

### [OPEN] [#15](https://github.com/The-Band-Solution/ResearchDomain/issues/15) Feat: Associate Initiative to External Research Group
- **Executor**: paulossjunior
- **Labels**: epic
- **Milestone**: -

**Description**:
Implement ExternalResearchGroup entity and many-to-many relationship with Initiative.\n\nRef: docs/requirements.md (FR-05-C)

---

### [OPEN] [#13](https://github.com/The-Band-Solution/ResearchDomain/issues/13) Feat: Associate Knowledge Area to Initiatives
- **Executor**: paulossjunior
- **Labels**: epic
- **Milestone**: -

**Description**:
Implement Many-to-Many relationship between KnowledgeArea and Initiative entities.\n\nRef: docs/requirements.md (FR-05-B)

---

### [CLOSED] [#9](https://github.com/The-Band-Solution/ResearchDomain/issues/9) [US] Researcher Academic Metadata & Knowledge Areas
- **Executor**: -
- **Labels**: feature, us
- **Milestone**: Issue Base

**Description**:
## Description
As a researcher, I want my profile to include my academic links (CNPq, Google Scholar) and my specialized knowledge areas so that I can be correctly identified within the research domain.

## Acceptance Criteria
- Researcher entity supports `cnpq_url` (optional string).
- Researcher entity supports `google_scholar_url` (optional string).
- Researcher can be associated with multiple `KnowledgeAreas` (Many-to-Many).
- Code must follow TDD (Tests First).
- Documentation updated (`requirements.md`, `sdd.md`).

## Technical Metadata
- **Documentation**: Updated in `docs/requirements.md` (FR-01-C, FR-01-D).
- **Architecture**: Domain Layer update.

---

### [CLOSED] [#6](https://github.com/The-Band-Solution/ResearchDomain/issues/6) [TASK] Implementation of Role-based Leadership and Many-to-Many Areas
- **Executor**: -
- **Labels**: feature, task
- **Milestone**: Issue Base

**Description**:
## Description
Implement the technical changes for Role integration, Many-to-Many KnowledgeAreas, and Temporal Membership.

## Associated US
Associated with #5

## Technical Tasks
- [ ] Integrate `Role` entity and create default roles ("Leader", "Researcher").
- [ ] Implement `KnowledgeArea` and `group_knowledge_areas` association table.
- [ ] Update `ResearchGroup` and `TeamMember` (from `eo_lib`) schemas.
- [ ] Implement membership/leadership temporal logic (`start_date`, `end_date`).
- [ ] Update Controllers and Factories.
- [ ] Verify with unit tests and demo script.

## Definition of Done
- Code passes all tests.
- Documentation updated.
- Pull Request created targeting `developing`.

---

### [CLOSED] [#5](https://github.com/The-Band-Solution/ResearchDomain/issues/5) [US] ResearchGroup Categorization & Leadership Recognition
- **Executor**: -
- **Labels**: feature, us
- **Milestone**: Issue Base

**Description**:
## Description
As a researcher, I want my research group to be correctly categorized with multiple Knowledge Areas and linked to external directories (CNPq) so it can be correctly found and its leadership recognized.

## Parent Epic
Associated with #4

## Acceptance Criteria
- Researchers can assign multiple Knowledge Areas to a group.
- Researchers can set the group's web page and CNPq link.
- Leadership status is clearly defined by role and duration.

---

### [CLOSED] [#4](https://github.com/The-Band-Solution/ResearchDomain/issues/4) [EPIC] ResearchGroup Metadata & Advanced Membership
- **Executor**: -
- **Labels**: feature, epic
- **Milestone**: Issue Base

**Description**:
## Description
Implement metadata enhancements for ResearchGroups, including CNPq integration, site links, multiple knowledge areas (Many-to-Many), and Role-based temporal membership management (Leadership).

## References
Detailed in:
- [docs/requirements.md](https://github.com/The-Band-Solution/ResearchDomain/blob/main/docs/requirements.md)
- [docs/sdd.md](https://github.com/The-Band-Solution/ResearchDomain/blob/main/docs/sdd.md)
- [docs/specifications.md](https://github.com/The-Band-Solution/ResearchDomain/blob/main/docs/specifications.md)

## Acceptance Criteria
- ResearchGroup supports `cnpq_url` and `site`.
- ResearchGroup can be associated with multiple `KnowledgeAreas`.
- `TeamMember` uses `Role` (specifically "Leader" for leadership roles).
- `TeamMember` tracks `start_date` and `end_date`.
- All layers (Domain, Infrastructure, Service, Controller) updated.

---

### [CLOSED] [#1](https://github.com/The-Band-Solution/ResearchDomain/issues/1) Implement ResearchGroup Feature (Entities, Repositories, Controllers)
- **Executor**: -
- **Labels**: enhancement, feature
- **Milestone**: Issue Base

**Description**:
## Context
Implement the core entities for the `ResearchDomain` library as specified in the updated documentation.

## Requirements
- A `ResearchGroup` is a `Team`.
- A `ResearchGroup` must have at least one `Researcher`.
- A `ResearchGroup` is present in a `Campus`.
- A `Campus` is in a `University`.

## Proposed Changes
- Implement `University` (Organization), `Campus` (OrganizationalUnit), `ResearchGroup` (Team), and `Researcher` (Person).
- Implement specialized repository interfaces and SQLAlchemy strategies.
- Implement specialized controllers.

## References
Detailed in `docs/requirements.md`, `docs/sdd.md`, and `docs/specifications.md`.

---
