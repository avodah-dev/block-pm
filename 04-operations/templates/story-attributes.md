# Story Attributes Definition

## Purpose
This document defines the required and optional attributes for all user stories in the Sourcing Window project. These attributes ensure consistency, enable proper categorization, and support various views and reports.

## Required Attributes

### 1. Story ID
- **Format**: S###-[EPIC] (e.g., S001-CORE, S045-VENDOR)
- **Purpose**: Unique identifier for tracking and reference

### 2. Title
- **Format**: Clear, action-oriented statement
- **Example**: "Enable vendor to submit quote with line items"

### 3. Persona
- **Options**:
  - P01-Buyer (Procurement buyer)
  - P02-Vendor (External supplier)
  - P03-Integrated-Vendor (Dual-role vendor)
  - P04-Admin (System administrator)
  - P05-Internal (Block internal user)
- **Purpose**: Identifies primary user affected

### 4. Architecture Layer
- **Options**:
  - `sw-frontend` - Sourcing Window Frontend (Product UI)
  - `sw-backend` - Sourcing Window Backend (Product API)
  - `bl-frontend` - Business Logic Frontend (Custom UI)
  - `bl-backend` - Business Logic Backend (Integration/Middleware)
  - `salesforce` - Salesforce/Business System
  - `infrastructure` - DevOps/Infrastructure
  - `data` - Database/Data Layer
  - `external` - Third-party Integrations
  - `cross-layer` - Spans multiple layers
- **Purpose**: Identifies where work will be performed

### 5. Epic
- **Format**: E##-[NAME] (e.g., E01-CORE-MARKETPLACE)
- **Purpose**: Groups related stories into major deliverables

### 6. Priority
- **Options**: P0 (Critical), P1 (High), P2 (Medium), P3 (Low)
- **Purpose**: Determines implementation order

### 7. Phase
- **Options**:
  - `Phase1` - Initial launch with core marketplace functionality
  - `Phase2` - Agile/Kanban delivery of enhancements and remaining features
- **Purpose**: Maps to delivery approach and contract phases

### 8. Story Points
- **Options**: 1, 2, 3, 5, 8, 13, 21
- **Purpose**: Effort estimation using Fibonacci scale

### 9. Acceptance Criteria
- **Format**: Bulleted list of testable conditions
- **Purpose**: Defines "done" for the story

### 10. Traceability
- **Format**: Object with two arrays
  ```json
  {
    "requirements": ["SW-M-1", "SW-V-5"],
    "workflows": ["W01", "W03"]
  }
  ```
- **Purpose**: Maintains full traceability to both requirements and workflows
- **Note**: Either array can be empty if not applicable

## Optional Attributes

### 11. Feature
- **Format**: F##-[NAME] (e.g., F03-QUOTE-SUBMISSION)
- **Purpose**: Mid-level grouping between Epic and Story

### 12. Dependencies
- **Format**: Array of Story IDs (e.g., ["S001-CORE", "S002-CORE"])
- **Purpose**: Identifies prerequisite stories

### 13. Source Information
- **Format**: Object with references to source documents
  ```json
  {
    "transcript": "20250908-discovery-day01/session-2.md",
    "timestamp": "1:23:45",
    "context": "User described need for bulk quote submission"
  }
  ```
- **Purpose**: Links to discovery sessions, meetings, or other source material
- **Use Case**: When story originates from discovery rather than formal requirements

### 14. Technical Notes
- **Format**: Free text
- **Purpose**: Implementation guidance, constraints, or considerations

### 15. Business Value
- **Format**: Brief statement
- **Purpose**: Explains why this story matters to the business

### 16. Risk Level
- **Options**: Low, Medium, High
- **Purpose**: Identifies implementation risk

### 17. Tags
- **Format**: Array of strings
- **Options**:
  - `api` - Requires API development
  - `ui` - User interface work
  - `integration` - System integration
  - `migration` - Data migration
  - `security` - Security-related
  - `performance` - Performance optimization
  - `compliance` - Regulatory/compliance
  - `analytics` - Reporting/analytics
- **Purpose**: Cross-cutting concerns and searchability

## Story Template

```json
{
  "id": "S###-EPIC",
  "title": "As a [persona], I want to [action] so that [value]",
  "persona": "P##-NAME",
  "architectureLayer": "layer-code",
  "epic": "E##-NAME",
  "feature": "F##-NAME",
  "priority": "P#",
  "phase": "Phase1|Phase2",
  "storyPoints": 0,
  "acceptanceCriteria": [
    "Given..., When..., Then...",
    "System shall..."
  ],
  "traceability": {
    "requirements": ["REQ-ID"],
    "workflows": ["W##"]
  },
  "sourceInformation": {
    "transcript": "path/to/transcript.md",
    "timestamp": "HH:MM:SS",
    "context": "Brief description"
  },
  "dependencies": ["S###-EPIC"],
  "technicalNotes": "",
  "businessValue": "",
  "riskLevel": "Low|Medium|High",
  "tags": []
}
```

## Usage Guidelines

### When Creating Stories
1. **Always** include all required attributes
2. Use the architecture layer to determine team assignment
3. Ensure traceability to requirements AND/OR workflows
4. Be specific in acceptance criteria
5. Include source information when story comes from discovery sessions

### Architecture Layer Selection
- Choose the PRIMARY layer where work occurs
- Use `cross-layer` only when truly spans multiple layers equally
- Infrastructure stories include CI/CD, deployment, monitoring
- Data stories include schema changes, migrations, ETL

### Phase Assignment
- **Phase1**: Core marketplace features for initial launch
  - Focus on MVP functionality
  - Fixed scope for initial contract
  - Structured sprint delivery
- **Phase2**: Enhanced features and continuous improvements
  - Kanban-style delivery
  - Feature enhancements
  - User feedback incorporation
  - Remaining contract deliverables

### Traceability Guidelines
- **Requirements**: Link to formal Block requirements (SW-M-*, SW-V-*)
- **Workflows**: Link to user workflows (W01-W09)
- **Both can be empty**: For pure technical debt or infrastructure stories
- **Source Information**: Use when story originates from discovery sessions

### Story Point Guidelines
- **1 point**: Trivial change, < 2 hours
- **2 points**: Simple story, < 1 day
- **3 points**: Standard story, 1-2 days
- **5 points**: Complex story, 2-3 days
- **8 points**: Very complex, 3-5 days
- **13 points**: Should probably be split
- **21 points**: Definitely should be split

## Validation Rules

1. Every story MUST have all required attributes
2. Story IDs must be unique across the system
3. Architecture layer must be from the defined list
4. Personas must reference existing persona definitions
5. At least one acceptance criterion required
6. Traceability must include at least requirements OR workflows (can have both, can have neither for technical stories)
7. Phase must be either Phase1 or Phase2

## Reporting Views

These attributes enable the following views:
- **By Architecture**: See all frontend vs backend work
- **By Persona**: Understand user impact
- **By Phase**: Phase1 launch vs Phase2 enhancements
- **By Epic/Feature**: Development hierarchy
- **By Priority**: Focus on critical path
- **By Dependencies**: Identify blockers
- **By Tags**: Find cross-cutting concerns
- **By Workflow**: See all stories supporting a user journey
- **By Requirement**: Track requirement implementation
- **By Source**: Trace back to discovery sessions

## Maintenance

This document should be updated when:
- New personas are identified
- Architecture layers change
- New tags become common
- Validation rules need adjustment
- New reporting needs emerge
- Phase definitions evolve