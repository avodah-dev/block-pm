# Client Requirements Folder Documentation

## Purpose
Contains the original requirements from Block's RFP that serve as the authoritative source for all development work. These client anchor documents (CAD) define what was initially requested and form the foundation for gap analysis, traceability, and implementation planning within the new project structure.

## Core Files

### CAD-001-swp-buyer-requirements.json/.md
- **Purpose**: Buyer-side platform requirements
- **Total Requirements**: 61 requirements
- **Categories**: Must Have (38), Should Have (15), Could Have (8)
- **Key Areas**: Parts requests, vendor selection, order management, reporting
- **Format**: Both JSON (structured) and MD (readable) versions

### CAD-002-sw-vendor-requirements.json/.md
- **Purpose**: Vendor-side platform requirements
- **Total Requirements**: 57 requirements
- **Categories**: Must Have (35), Should Have (12), Could Have (10)
- **Key Areas**: Quote submission, catalog management, order fulfillment, messaging
- **Format**: Both JSON (structured) and MD (readable) versions

### index.json
- **Purpose**: Master catalog of all client anchor documents
- **Contents**: Document IDs, titles, requirement counts, categories
- **Usage**: Quick navigation and requirement summary
- **Update**: When new anchor documents are added

### rebuild_workflows.py
- **Purpose**: Utility script for workflow regeneration
- **Function**: Rebuilds workflow JSON from source data
- **Usage**: Run when workflow structures need updating
- **Dependencies**: Reads from original-csvs folder

## Subdirectories

### /original-csvs/
- **Purpose**: Raw source data from client
- **Contents**: Original CSV exports of requirements
- **Format**: Unprocessed client data
- **Usage**: Source of truth for requirement extraction

## Document Format

### JSON Structure
```json
{
  "id": "CAD-XXX",
  "title": "Requirement Set Name",
  "requirements": [
    {
      "id": "REQ-XXX",
      "description": "What needs to be built",
      "priority": "Must Have|Should Have|Could Have",
      "category": "Functional|Technical|Non-functional"
    }
  ]
}
```

### Markdown Format
- Human-readable version of JSON content
- Includes additional context and notes
- Used for reviews and discussions

## Relationships to Other Folders

### Feeds Into
- `/01-sources/rfp-responses/`: Original RFP responses address these requirements
- `/02-analysis/requirements/`: Gap analysis and traceability based on these requirements
- `/03-outputs/workflows/`: User workflows implement these requirements
- `/03-outputs/epics/`, `/03-outputs/features/`, `/03-outputs/stories/`: Development work traces to requirements

### Referenced By
- All development and planning documents in `/03-outputs/`
- Traceability matrices in `/02-analysis/mappings/`
- Gap analysis reports in `/02-analysis/requirements/`

## Usage Patterns

### For Requirement Lookup
1. Check index.json for requirement summary
2. Open specific CAD file for details
3. Use requirement ID for cross-referencing
4. Check both JSON and MD versions

### For Coverage Analysis
1. Extract all requirement IDs from CAD files
2. Compare against RFP responses
3. Map to implementation plans
4. Identify gaps and overlaps

## Requirement ID Convention
- Format: `[PREFIX]-[CATEGORY]-[NUMBER]`
- Example: `SW-M-1` (Sourcing Window - Must Have - #1)
- Prefixes: SW (Vendor), SWP (Buyer Platform)
- Categories: M (Must), S (Should), C (Could)

## Maintenance Notes
- These are source documents - rarely modified
- Any clarifications go in separate files
- Keep JSON and MD versions synchronized
- Document requirement interpretations elsewhere
- Preserve original formatting and IDs

## Current Statistics
- **Total Requirements**: 118
- **Must Have**: 73 (61.9%)
- **Should Have**: 27 (22.9%)
- **Could Have**: 18 (15.2%)
- **Source Date**: Original RFP submission