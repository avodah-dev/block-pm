# Rebuild Epic-Feature-Story Draft

## Purpose
Create a repeatable process for generating a draft of epics, features, and stories from our documented workflows and source information. This is a two-part process that first generates the EFS structure from workflows, then validates coverage through a traceability matrix.

## Process 1: Generate Epics, Features, and Stories from Workflows

### Mission
Build a comprehensive draft of epics, features, and stories that:
1. Covers all documented workflows
2. Uses client domain language from the project dictionary
3. Creates logical groupings of functionality
4. Provides one-line descriptions suitable for review
5. IS a foundation for expanding to full Epics / Features / Stories

### Required Inputs
1. **Workflows**: All workflows in `/03-outputs/workflows/` (currently W01-W09)
   - Use `index.json` for the complete workflow list
   - Read individual W##-*.json and W##-*.md files for detailed steps
   - Review `workflow_analysis_summary.md` for gaps and context
2. **Project Dictionary**: `/04-operations/architecture/project_dictionary.md` for domain language
3. **Personas**: `/03-outputs/personas/` for user context
4. **Architecture**: `/04-operations/architecture/architecture_layers.md` for system boundaries

**Note on Context**: Use as much context as necessary to build comprehensive epics, features, and stories. While being efficient, it's important to fully understand the workflows, requirements, and business needs to create meaningful development items.

### Output File
`/03-outputs/drafts/epics-features-stories-summary.md`

### Output Format
```markdown
# Epics, Features, and Stories Summary

## Epic E01-[NAME]: [One-line description]

### Feature F01: [One-line description]
- S001: [One-line story description]
- S002: [One-line story description]
- S003: [One-line story description]

### Feature F02: [One-line description]
- S004: [One-line story description]
- S005: [One-line story description]

## Epic E02-[NAME]: [One-line description]

### Feature F03: [One-line description]
- S006: [One-line story description]
- S007: [One-line story description]
```

### Generation Guidelines
- **Epics**: 8-12 total, representing major functional areas
- **Features**: 2-6 per epic, representing capability groupings
- **Stories**: Multiple per feature, representing implementable units
- **Language**: Use terminology from the project dictionary
- **Coverage**: Every workflow step should be represented by at least one story
- **Format**: One-line descriptions only (no attributes, phases, or points)

## Process 2: Build Requirement Traceability Matrix

### Mission
Create a visual table showing the relationship between requirements, workflow steps, and stories to identify coverage gaps.

### Required Inputs
1. **Requirements**: `/01-sources/client-requirements/` (118 total requirements)
2. **Workflows**: The workflow documents referenced above
3. **Generated EFS**: The output from Process 1

### Output File
`/03-outputs/drafts/requirement-traceability-matrix.md`

### Output Format
```markdown
# Requirement Traceability Matrix

## Coverage Summary
- Total Requirements: 118
- Requirements with Stories: X
- Requirements without Stories: Y
- Workflows without Requirements: Z

## Traceability Table

| Requirement | Description | Workflow(s) | Story IDs |
|------------|-------------|-------------|-----------|
| SW-M-1 | Create requisition | W01 | S001, S002, S003 |
| SW-M-2 | Set quantity | W01 | S004 |
| SW-M-3 | Vendor selection | W02 | S015, S016 |
| SW-V-1 | Submit quote | W03 | S025, S026 |
| SW-V-2 | View requests | - | - |

## Workflows Not Traced to Requirements
| Workflow | Description | Story IDs | Note |
|----------|-------------|-----------|------|
| W04-Step-3 | Internal messaging | S045, S046 | Enhancement beyond requirements |

## Requirements Without Coverage
| Requirement | Description | Reason |
|------------|-------------|---------|
| SW-V-2 | View requests | Gap - needs story |
```

### Analysis Goals
1. Identify requirements without story coverage
2. Identify workflows/stories beyond original requirements (enhancements)
3. Validate that core requirements are addressed
4. Provide visual confirmation of comprehensive coverage

## Process Steps

### Step 1: Generate EFS from Workflows
1. Read all workflow documents
2. Read project dictionary for terminology
3. Group related workflow steps into features
4. Group related features into epics
5. Write one-line descriptions for each level
6. Output as structured markdown
7. Confirm with user before continuing

### Step 2: Build Traceability Matrix
1. List all 118 requirements with IDs and descriptions
2. Map requirements to workflow steps
3. Map workflow steps to story IDs from Step 1
4. Identify gaps in both directions
5. Output as table format for easy review
6. Report to user for next steps. 

There will be a seperate process for handling updates, this is a focus on full regeneration.

## Key Principles
1. **Simplicity**: One-line descriptions only in this draft phase
2. **Traceability**: Clear line from requirement → workflow → story
3. **Domain Language**: Use client terminology consistently
4. **Completeness**: Every workflow step should have a story
5. **Visibility**: Gaps should be clearly identified

## What This Process Does NOT Include
- Story attributes (personas, layers, phases, points)
- Detailed acceptance criteria
- Technical implementation details
- Priority or sequencing
- Final story format

These elements will be added in subsequent phases after stakeholder review of this initial draft.

## Success Criteria
- All workflows have been converted to stories
- Requirements coverage is >90% or gaps are documented
- Document is readable by both humans and agents
- Structure supports CSV export for feedback collection
- Traceability matrix clearly shows coverage and gaps