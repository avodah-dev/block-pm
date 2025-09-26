# Drafts Folder Documentation

## Purpose
Contains AI-generated analysis and draft development planning that bridges requirements with implementation. This folder serves as the staging area for transforming requirements and workflows into structured epic/feature/story breakdowns before final review and approval.

## Current Structure

### /draft/
- **Purpose**: Contains AI-generated analysis and proposals
- **Status**: Active - Contains completed first-pass analysis
- **Key Files**:
  - `EPICS-FEATURES-STORIES-SUMMARY.md`: Comprehensive breakdown of all epics/features
  - `REQUIREMENTS-TRACEABILITY-MATRIX.md`: Maps features to original requirements
  - `REVIEW-GUIDE.md`: Instructions for reviewing and finalizing drafts

## Related Final Folders

### /03-outputs/epics/
- **Purpose**: High-level business value deliverables
- **Status**: Contains template only (TEMPLATE-epic.md)
- **Future**: Will contain finalized epic documents moved from drafts (E01-XXX.md)
- **Scope**: Each epic delivers major user value

### /03-outputs/features/
- **Purpose**: Functional capabilities within epics
- **Status**: Contains template only (TEMPLATE-feature.md)
- **Future**: Will contain finalized feature documents moved from drafts (F01-XXX.md)
- **Scope**: User-facing functionality

### /03-outputs/stories/
- **Purpose**: Implementable development tasks
- **Status**: Contains template only (TEMPLATE-story.md)
- **Future**: Will contain finalized story documents moved from drafts (S01-XXX.md)
- **Scope**: 1-3 day development tasks

## Development Hierarchy

```
Epic (Business Value)
├── Feature 1 (User Capability)
│   ├── Story 1.1 (Implementation Task)
│   ├── Story 1.2 (Implementation Task)
│   └── Story 1.3 (Implementation Task)
├── Feature 2 (User Capability)
│   └── Stories...
└── Feature N...
```

## Draft Analysis Results

### Current Epics Identified
1. **E01**: Buyer Parts Request Management
2. **E02**: Vendor Quoting System
3. **E03**: Quote Review & Selection
4. **E04**: Order Processing & Fulfillment
5. **E05**: Communication Platform
6. **E06**: User Management & Permissions
7. **E07**: Analytics & Reporting

### Coverage Statistics (from draft)
- **Total Features**: 35+ identified
- **Requirements Mapped**: Comprehensive traceability
- **Personas Covered**: Buyer, Vendor, Integrated Vendor
- **Workflows Supported**: All 9 documented workflows

## Relationships to Other Folders

### Sources From
- `/01-sources/client-requirements/`: Original requirements
- `/03-outputs/workflows/`: User journey definitions
- `/03-outputs/personas/`: User type definitions
- `/01-sources/transcripts/`: Discovery session insights
- `/02-analysis/requirements/`: Requirement traceability and gap analysis

### Outputs To
- `/03-outputs/epics/`, `/03-outputs/features/`, `/03-outputs/stories/`: Final development documents
- Development backlog and sprint planning
- `/02-analysis/requirements/`: Implementation coverage tracking
- Technical architecture and design documents in `/04-operations/architecture/`

## Usage Patterns

### For Development Planning
1. Review draft analysis in /draft/ folder
2. Select epics/features for current phase
3. Break features into implementable stories
4. Move finalized items to respective folders
5. Track implementation against requirements

### For Traceability
1. Start with requirement ID from `/01-sources/client-requirements/`
2. Find mapping in `REQUIREMENTS-TRACEABILITY-MATRIX.md`
3. Locate feature in `EPICS-FEATURES-STORIES-SUMMARY.md`
4. Review implementation approach
5. Verify workflow coverage in `/03-outputs/workflows/`

## File Naming Conventions
- **Epics**: E[NN]-[descriptive-name].md (e.g., E01-buyer-request-mgmt.md)
- **Features**: F[NN]-[epic]-[name].md (e.g., F01-E01-parts-request-creation.md)
- **Stories**: S[NNN]-[feature]-[name].md (e.g., S001-F01-request-form-ui.md)

## Template Structure
Each document type has a template defining:
- Required metadata fields
- Traceability links (requirements, workflows)
- Acceptance criteria format
- Dependencies and relationships
- Estimation guidelines

## Migration Process (Draft to Final)
1. Review draft analysis with stakeholders
2. Validate requirement mappings
3. Adjust scope based on priorities
4. Create individual epic/feature/story files
5. Move from draft to active folders
6. Update indices and traceability

## Maintenance Notes
- Keep draft folder for historical reference
- Update traceability matrix as implementation proceeds
- Document any scope changes or variations
- Maintain bidirectional links to requirements
- Regular review of unimplemented features

## Next Steps
1. Stakeholder review of draft analysis
2. Prioritization of epics for Phase 1
3. Detailed story writing for prioritized features
4. Technical design for complex features
5. Sprint planning based on story points