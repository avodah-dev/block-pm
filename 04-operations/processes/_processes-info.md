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
- `generate_epics_task.md`: Instructions for epic/feature/story generation
- `llm_epic_generation_instructions.md`: Detailed prompts for LLM analysis
- `workflow_analysis_summary.md`: Workflow summarization for analysis

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

#### generate_epics_task.md
- **Last Used**: September 2025
- **Purpose**: Generate epics/features/stories from workflows
- **Output**: Draft development breakdown
- **Reusable**: Yes, when workflows significantly change

#### llm_epic_generation_instructions.md
- **Last Used**: September 2025
- **Purpose**: Detailed LLM prompts for analysis
- **Output**: Structured epic/feature/story documents
- **Reusable**: Yes, as template for similar analysis

#### workflow_analysis_summary.md
- **Last Used**: September 2025
- **Purpose**: Prepare workflows for LLM analysis
- **Output**: Consolidated workflow summary
- **Reusable**: Yes, when new workflows added

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