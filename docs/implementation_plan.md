# Implementation Plan: New Services and Factory Improvements

Implement services for `Fellowship`, `ExternalResearchGroup`, and `Advisorship`, and refactor `ServiceFactory` for better maintainability.

## User Review Required

> [!IMPORTANT]
> **Refactoring ServiceFactory**: I will change the internal implementation of `ServiceFactory` to use a mapping-based strategy instead of index-based tuple unpacking. This will make it much easier to add new services in the future.

## Proposed Changes

### Domain Repositories

#### [MODIFY] [repositories.py](file:///home/paulossjunior/projects/ResearchDomain/src/research_domain/domain/repositories/repositories.py)
- Add `FellowshipRepositoryInterface`
- Add `ExternalResearchGroupRepositoryInterface`
- Add `AdvisorshipRepositoryInterface`

### Services

#### [MODIFY] [services.py](file:///home/paulossjunior/projects/ResearchDomain/src/research_domain/services/services.py)
- Implement `FellowshipService(GenericService[Fellowship])`
- Implement `ExternalResearchGroupService(TeamService)`
- Implement `AdvisorshipService(GenericService[Advisorship])`

### Factories

#### [MODIFY] [factories.py](file:///home/paulossjunior/projects/ResearchDomain/src/research_domain/factories.py)
- Refactor `ServiceFactory._get_strategies()` to return a dictionary or a structured object.
- Update existing `create_*` methods to use the new strategy structure.
- Register `create_fellowship_service`, `create_external_research_group_service`, and `create_advisorship_service`.

### Controllers

#### [MODIFY] [controllers.py](file:///home/paulossjunior/projects/ResearchDomain/src/research_domain/controllers/controllers.py)
- Implement `FellowshipController`
- Implement `ExternalResearchGroupController`
- Implement `AdvisorshipController`

## Verification Plan

### Automated Tests
- Create `tests/test_services_extended.py` to test the new services and the refactored factory.
- Verify that `ServiceFactory` correctly returns instances for all services.
- Verify CRUD operations for `Fellowship`, `ExternalResearchGroup`, and `Advisorship`.

### Manual Verification
- Run a demo script to ensure all services are correctly wired.
