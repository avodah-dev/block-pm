# Processes Folder Documentation

## Purpose
Contains reusable processes, agent task instructions, and operational scripts used throughout
the project lifecycle. These are the "how-to" documents and tools that support development,
analysis, and project management activities. Separating these from core documentation helps
distinguish operational tools from system design documents.

## Folder Structure

### /agent-tasks/
**Purpose**: LLM/Agent instructions for specific analysis and generation tasks
**Usage**: Reference when needing to regenerate or update project artifacts
**Contents**:
- `rebuild-efs-draft.md`: Rebuild entire epic/feature/story draft from workflows
- `epic-detail-generation.md`: Generate detailed epic documentation with user stories
- `csv-export-for-stickies.md`: Convert summaries to CSV for Excel/MIRO
- `story-enrichment.md`: Add full attributes and traceability to stories

### /scripts/
**Purpose**: Python scripts and utilities for data processing
**Contents**:
- `rebuild_workflows.py`: Regenerate workflow JSON from source data

### /completed/
**Purpose**: Archive of one-time tasks that have been executed
**Usage**: Historical reference, may be adapted for similar future tasks
**Status**: Currently empty - tasks move here after completion

## File Inventory

### Agent Task Documents
Each task document includes:
- **Header**: Purpose and last usage date
- **Context**: When and why to use
- **Instructions**: Step-by-step process
- **Expected Output**: What gets generated
- **Reusability**: Whether task is repeatable

### Current Agent Tasks

#### rebuild-efs-draft.md
- **Last Used**: September 26, 2025
- **Purpose**: Rebuild entire epic/feature/story structure from workflows
- **Output**: Complete draft of all epics, features, and stories
- **Reusable**: Yes, when workflows or requirements significantly change

#### epic-detail-generation.md
- **Last Used**: September 26, 2025
- **Purpose**: Generate comprehensive epic detail documents with full user stories
- **Output**: Detailed epic document with business context and stories in "As a..." format
- **Reusable**: Yes, for each epic requiring detailed documentation

#### csv-export-for-stickies.md
- **Last Used**: September 26, 2025
- **Purpose**: Convert epic/feature/story summaries to CSV format for tools
- **Output**: Three-column CSV optimized for Excel review and MIRO sticky notes
- **Reusable**: Yes, whenever updated summaries need export

#### story-enrichment.md
- **Last Used**: September 26, 2025
- **Purpose**: Add full attributes, acceptance criteria, and traceability to stories
- **Output**: Fully-specified stories with all development attributes
- **Reusable**: Yes, for any epic needing complete story specifications

## Usage Patterns

### For Regeneration Tasks
1. Identify which artifact needs updating
2. Find corresponding task in `/agent-tasks/`
3. Review and update instructions if needed
4. Execute task with current data
5. Move to `/completed/` if one-time use

### For New Processes
1. Create new document in appropriate subfolder
2. Use existing tasks as templates
3. Include clear header with purpose/usage
4. Document expected inputs and outputs
5. Note reusability status

### For Scripts
1. Document script purpose in file header
2. Include usage examples
3. Note dependencies and requirements
4. Keep related to data processing/generation

## Relationships to Other Folders

### Consumes From
- `/03-outputs/workflows/`: Source data for analysis
- `/01-sources/client-requirements/`: Requirements for generation
- `/03-outputs/personas/`: User context for tasks
- `/01-sources/transcripts/`: Discovery insights for process validation

### Generates For
- `/03-outputs/epics/`, `/03-outputs/features/`, `/03-outputs/stories/`: Development artifacts
- `/02-analysis/requirements/`: Coverage reports
- `/02-analysis/mappings/`: Relationship matrices
- `/03-outputs/drafts/`: Analysis and planning documents

## Maintenance Notes
- Review agent tasks before reuse for currency
- Archive completed one-time tasks
- Update task documents with lessons learned
- Keep scripts synchronized with data structures
- Document any manual steps in automated processes

## Task Status Tracking
Tasks should include status markers:
- **Active**: Currently usable and maintained
- **Archived**: Completed, kept for reference
- **Deprecated**: Outdated, do not use
- **Template**: Base for creating new tasks

## Quality Checklist for New Processes
- [ ] Clear purpose statement
- [ ] Usage context defined
- [ ] Input requirements specified
- [ ] Output format documented
- [ ] Reusability status noted
- [ ] Dependencies listed
- [ ] Last used date tracked

## Future Additions
Potential process documents to add:
- Gap analysis generation process
- Requirement extraction from transcripts
- Workflow validation checklist
- Release readiness assessment
- Documentation update procedures