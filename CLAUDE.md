# Requirements Management System

## Project Overview

### Client Context
**Client**: Block Imaging
**Project**: Sourcing Window - Modern B2B marketplace platform
**Our Role**: Avodah is building a clean, modern replacement for SW 2.0

### Platform Evolution
- **SW 1.0**: Block's internal tool, built on Salesforce and then shared with other medical parts sales and procurement teams.
- **SW 2.0**: Legendary's Salesforce 360 implementation (suboptimal)
- **SW 3.0**: The vision is for SW 3.0 to be a modern platform with proper architectural separation

### Key Architectural Principle
Clear separation between:
- **Product Layer**: Clean, vendor and buyer agnostic marketplace (any company could use)
- **Business Logic Layer**: Block's proprietary features and competitive advantages
  - Other companies could build their own business logic layer and use the SW API to maximize the produts utility.

This project organizes and tracks the relationship between Block's requirements, our RFP responses, and product development for the Sourcing Window platform. It maintains traceability from Block's original requests through our responses to actual implementation.

## Root Files
- **CLAUDE.md** (this file): Project overview and navigation guide
- **roadmap.md**: Development phases for this project management project
- **transition_prompt.md**: Session handoff document (see Session Handoff Procedure below)

## Root Directory Structure

### 📋 Core System Files (Root)
- See Root Files

### 📁 Organized Project Structure

#### `/01-sources/` — Input Materials
Everything we receive from Block and discovery sessions
- **`client-requirements/`**: Original client RFP documents (was: client-anchor-docs)
  - See: `_client-requirements-info.md`
- **`rfp-responses/`**: Our original RFP responses (was: avodah-rfp-response)
  - See: `_rfp-responses-info.md`
- **`transcripts/`**: Discovery meeting recordings and notes
  - See: `_transcripts-info.md`

#### `/02-analysis/` — Understanding & Processing
How we analyze and understand the requirements
- **`requirements/`**: Requirements tracking and coverage (was: analysis)
  - See: `_requirements-info.md`
- **`mappings/`**: Cross-reference matrices between entities
- **`insights/`**: Discovery findings and pain points

#### `/03-outputs/` — What We Create
All deliverable outputs with unique IDs
- **`personas/`**: User types (P##)
  - See: `_personas-info.md`
- **`workflows/`**: User journeys (W##)
  - See: `_workflows-info.md`
- **`epics/`**: Epic specifications (E##)
- **`features/`**: Feature specifications (F##)
- **`stories/`**: User stories (S##)
- **`drafts/`**: Work in progress items
  - See: `_drafts-info.md`

#### `/04-operations/` — How We Work
Project infrastructure and processes
- **`processes/`**: Agent tasks, scripts, and procedures
  - See: `_processes-info.md`
- **`architecture/`**: Technical decisions and system design (was: reference)
  - See: `_architecture-info.md`
- **`templates/`**: Document templates for all entity types

## Operating Modes

### 🔍 Research Mode
**When to use**: During meetings, planning sessions, or when thinking through problems
**What it does**: Quickly queries and analyzes existing information without modifying data

**Example queries**:
- "What are the vendor management requirements?"
- "Which workflows involve vendor selection?"
- "Show me all Phase 1 requirements for buyers"
- "What did we commit to in our RFP response about reporting?"
- "Which requirements relate to EMA functionality?"
- "What personas use the approval workflow?"

**Response style**: Quick, focused answers based on existing data. No file modifications.

### ➕ Add Mode
**When to use**: When incorporating new information into the system
**What it does**: Processes and properly categorizes new content

**Types of additions**:
- **Transcripts**: "Add this meeting transcript about vendor workflows"
- **Documents**: "Add this requirements document as a client anchor doc"
- **Workflows**: "Add a workflow for vendor onboarding"
- **Epics/Features/Stories**: "Add these user stories from our planning session"
- **Updates**: "Update the RFP response for requirement SW-M-1"

**Process**:
1. Identify document type and appropriate location
2. Extract structured information
3. Update relevant indices and mappings
4. Maintain traceability links
5. Report what was added and any gaps identified

### Mode Indicators
Start your request with:
- **"Research:"** or **"Question:"** for research mode
- **"Add:"** or **"Document:"** for add mode
- Or just ask naturally - I'll infer from context

## Directory Structure & Current State

### 📁 `/01-sources/` — Input Materials ✅

#### `client-requirements/` (7 files)
- **CAD-001-swp-buyer-requirements** (.json/.md): 61 buyer-side requirements
- **CAD-002-sw-vendor-requirements** (.json/.md): 57 vendor-side requirements
- **index.json**: Catalog of all anchor documents
- **original-csvs/**: Source CSV files

#### `rfp-responses/` (4 files)
- **RRD-001-sw-vendor-response.json**: Response to vendor requirements
- **RRD-002-swp-buyer-response.json**: Response to buyer requirements
- **index.json**: Response document catalog

#### `transcripts/` (18+ files)
- **20250908-discovery-day01/**: Day 1 transcripts and notes
- **20250909-discovery-day02/**: Day 2 transcripts and notes
- **20250910-discovery-day03/**: Day 3 transcripts and notes

### 📁 `/02-analysis/` — Understanding & Processing ✅

#### `requirements/` (5 files)
- **requirements-matrix.json**: Initial requirement tracking
- **requirements-traceability-matrix.json**: Client requirements to RFP mapping
- **gap-analysis.md**: Coverage report (43.2% addressed in original RFP)
- **analysis_methodology.md**: How we analyze requirements

#### `mappings/` (Ready for population)
- Will contain cross-reference matrices between entities

#### `insights/` (1 file)
- **discovery_pain_points_summary.md**: Key findings from discovery sessions

### 📁 `/03-outputs/` — What We Create ✅

#### `personas/` (5 files)
- **P01-buyer.json**: Procurement buyer persona
- **P02-vendor.json**: Vendor/supplier persona
- **P03-integrated-vendor.json**: Integrated vendor persona
- **index.json**: Persona catalog

#### `workflows/` (20 files)
- **W01-W09**: Complete workflow definitions (JSON + MD)
- **workflow-inputs.json**: How workflows were created
- **index.json**: Workflow catalog

#### `drafts/` (1 file)
- **EPICS-FEATURES-STORIES-SUMMARY.md**: Complete draft analysis

#### `epics/`, `features/`, `stories/` (Empty - ready for finalized items)

### 📁 `/04-operations/` — How We Work ✅

#### `processes/` (Multiple files)
- **agent-tasks/**: LLM instructions and analysis tasks
- **completed/**: Finished process artifacts
- **scripts/**: Automation tools

#### `architecture/` (2 files)
- **architecture_layers.md**: System architecture decisions
- **project_dictionary.md**: Key terms and concepts

#### `templates/` (2 files)
- **TEMPLATE-persona.md**: Template for personas
- **TEMPLATE-workflow.md**: Template for workflows

## Document Formats

### Client Anchor Docs (CAD)
```markdown
# CAD-[ID]: [Title]

## Summary
Brief overview of this requirement document

## Requirements
- REQ-[ID]: Requirement description
  - Priority: [High/Medium/Low]
  - Category: [Functional/Non-functional/Technical]

## Related Documents
- Links to other CADs
- External references
```

### RFP Response Docs (RRD)
```markdown
# RRD-[ID]: [Title]

## Addresses
- CAD-[ID]: How we address this anchor doc
- REQ-[ID]: Specific requirement responses

## Our Approach
Detailed response content

## Commitments
What we've committed to deliver

## Variations
Where our approach differs from the request
```

### Epics/Features/Stories
```markdown
# [E/F/S][ID]: [Title]

## Description
What we're building and why

## Traces To
- CAD-[ID]: Original client requirement
- RRD-[ID]: Our response commitment
- REQ-[ID]: Specific requirements fulfilled

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Notes
Additional context, changes from original vision
```

## Tracking Indices

### requirements-matrix.json
```json
{
  "requirements": [
    {
      "id": "REQ-001",
      "source": "CAD-001",
      "status": "addressed|partial|not-addressed|deferred",
      "response": "RRD-001",
      "implementation": ["E01", "F01", "S01"],
      "notes": "Any variations or explanations"
    }
  ]
}
```

### Gap Analysis Process
1. Extract all requirements from Client Anchor Docs
2. Map responses from RFP Response Docs
3. Connect implementation (Epics/Features/Stories)
4. Identify:
   - Unaddressed requirements
   - Partial implementations
   - Over-delivery (things we're doing beyond request)
   - Deprecated requirements (no longer relevant)

## Conceptual Model: Workflows ↔ Development

### Key Relationships
1. **Workflows** = User journeys that cross multiple features
2. **Features** = Functional capabilities that enable user actions
3. **Stories** = Implementable units that build features
4. **Epics** = Collections of features delivering major value

### Connection Rules
- Every **Story** has: Persona + Feature + Epic
- Every **Feature** appears in: One or more Workflows
- Every **Workflow** serves: One primary Persona
- Everything traces back to: Original Requirements

### The Power of Dual Views
- **Horizontal (Workflows)**: Shows complete user journeys
- **Vertical (Epics→Features→Stories)**: Shows implementation hierarchy
- **Intersection**: Features bridge workflows and development

For detailed model documentation, see `WORKFLOW-DEVELOPMENT-MODEL.md`

## Workflow

### Adding New Documents
1. **Client Requirements (CAD)**:
   - Add to `01-sources/client-requirements/`
   - Update `01-sources/client-requirements/index.json`
   - Extract requirements to `02-analysis/requirements/requirements-matrix.json`

2. **RFP Response**:
   - Add to `01-sources/rfp-responses/`
   - Link to relevant CADs
   - Update cross-reference indices in `02-analysis/mappings/`

3. **Development Items**:
   - Create in `03-outputs/drafts/` first
   - Move to `03-outputs/[epics|features|stories]/` when finalized
   - Always trace back to source requirements
   - Note any deviations or enhancements

### Regular Reviews
- Run gap analysis to find unaddressed requirements
- Update coverage reports
- Review transcripts for requirement changes
- Adjust implementation priorities

## Mode-Specific Behaviors

### In Research Mode
- **Fast responses** from existing data
- **No file changes** unless explicitly requested
- **Cross-references** between requirements, responses, and development items
- **Gap identification** without creating new documents
- **Summary views** of complex relationships

### In Add Mode
- **Structured extraction** from unstructured content
- **Proper categorization** using established naming conventions
- **Automatic indexing** in relevant JSON files
- **Relationship mapping** to existing documents
- **Gap analysis** comparing new content to existing
- **Confirmation** of what was added and where

## Current Project Status

### 📊 Progress Metrics
- **Requirements Documented**: 118 total (61 buyer, 57 vendor)
- **RFP Coverage**: 43.2% of requirements addressed in original response
- **Workflows Documented**: 9 total (includes integrated vendor workflows)
- **Personas Created**: 3 (Buyer, Vendor, Integrated Vendor)
- **Discovery Sessions**: 3 days of transcripts captured
- **Epics/Features/Stories**: Draft analysis complete with traceability matrix
- **Project Reorganization**: ✅ Complete - Clear separation of sources, analysis, outputs, and operations

### 🎯 Next Steps
1. Complete remaining workflows (7-10 more expected)
2. Run LLM analysis to generate Epics/Features/Stories
3. Map generated items back to requirements
4. Identify complete coverage and remaining gaps

## Queries This System Supports
1. "What client requirements haven't been addressed?"
2. "Which workflows cover requirement X?"
3. "What did we commit to in our RFP response?"
4. "Where does our implementation differ from the original request?"
5. "What are we building that wasn't originally requested?"
6. "Show the workflow relationships and dependencies"

## Session Handoff Procedure

### Purpose
The `transition_prompt.md` file facilitates clean handoffs between work sessions, preventing stale instructions from causing confusion.

### Procedure
1. **Start of Session**:
   - Check `transition_prompt.md` for any active handoff notes
   - Act on instructions if present
   - Clear the content or mark as "REVIEWED [date]"

2. **End of Session**:
   - Only populate if specific handoff needed
   - Include context, next steps, and any blockers
   - Keep instructions current and actionable

3. **Maintenance**:
   - Never leave old/completed tasks in the file
   - Use for active transitions only
   - Archive important completions elsewhere if needed

## Documentation Scaffolding

### Purpose
The documentation scaffolding provides a lightweight navigation layer that helps both humans and agents understand the project structure with minimal context. Every folder contains a `_foldername-info.md` file that serves as a local guide.

### Structure
- **Naming Convention**: `_foldername-info.md` (underscore ensures it appears at bottom)
- **Length**: 50-75 lines per file
- **Location**: One in each active folder (except root, which uses CLAUDE.md)

### Contents of Each _info.md File
1. **Purpose Statement**: Clear explanation of folder's role
2. **File Inventory**: List of key files with brief descriptions
3. **Relationships**: Links to related folders and dependencies
4. **Conventions**: Patterns, naming schemes, and standards used
5. **Usage Notes**: When and how to interact with these files
6. **Maintenance**: Update requirements and frequencies

### Maintenance Requirements
**IMPORTANT**: When making changes to the project:
1. **Adding Files**: Update the relevant `_foldername-info.md` file
2. **Creating Folders**: Create corresponding `_foldername-info.md` file
3. **Completing Sessions**: Review and update affected info files
4. **Major Refactors**: Ensure all info files reflect new structure

### Navigation Flow
1. Start at `CLAUDE.md` for project overview
2. Use numbered folders to understand information flow:
   - `01-sources/` → What we received
   - `02-analysis/` → How we understand it
   - `03-outputs/` → What we're creating
   - `04-operations/` → How we work
3. Navigate to folder's `_foldername-info.md` for detailed guidance
4. Access specific files as needed

This scaffolding enables efficient project navigation without loading full file contents, reducing context usage while maintaining comprehensive understanding.

## Best Practices
- Every Epic/Feature/Story should trace to at least one requirement OR explicitly note it's an enhancement
- Document why requirements are not being addressed
- Keep indices updated as documents are added
- Use consistent ID formats for easy searching
- Maintain both human-readable docs and machine-parseable indices
- **Update documentation scaffolding** when adding files or completing sessions

## Tools and Scripts
Future automation opportunities:
- Auto-generate gap analysis from indices
- Extract requirements from new documents
- Generate traceability reports
- Validate cross-references
- Search across all documents for keywords