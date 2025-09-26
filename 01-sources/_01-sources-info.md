# 01-Sources Directory

## Purpose
This directory contains all source documents and materials that form the foundation of the Sourcing Window requirements management system. These are the original, unprocessed inputs from various stakeholders.

## Directory Structure
```
01-sources/
├── client-requirements/     # Original client RFP documents and requirements
├── rfp-responses/          # Avodah's original RFP response documents
└── transcripts/            # Discovery meeting recordings and notes
```

## Subdirectories

### client-requirements/
Contains the original requirements documents from Block's RFP process. These serve as the authoritative source for what the client initially requested.
- **Files**: CAD-001 (buyer requirements), CAD-002 (vendor requirements)
- **Format**: Both JSON and Markdown versions for each document
- **Status**: 118 total requirements documented (61 buyer, 57 vendor)

### rfp-responses/
Contains Avodah's original responses to the client RFP, created before the discovery process began.
- **Files**: RRD-001 (vendor response), RRD-002 (buyer response)
- **Coverage**: 43.2% of client requirements addressed in original responses
- **Purpose**: Baseline for understanding initial commitments vs. discovered needs

### transcripts/
Contains verbatim transcripts and analysis from discovery sessions with Block stakeholders.
- **Sessions**: 3 days of discovery meetings (Sept 8-10, 2025)
- **Format**: Raw transcripts, processed notes, and extracted insights
- **Value**: Real requirements vs. written requirements comparison

## Relationships
- **Feeds into**: `/02-analysis/requirements/` for gap analysis and traceability
- **Referenced by**: All development planning in `/03-outputs/`
- **Supports**: Architecture decisions in `/04-operations/architecture/`

## Data Flow
1. **Client Requirements** → Requirements extraction and analysis
2. **RFP Responses** → Commitment tracking and coverage analysis
3. **Transcripts** → Discovery insights and requirement refinements
4. **Combined** → Comprehensive requirement understanding in analysis phase

## Maintenance Notes
- Source documents should remain immutable (preserve original state)
- Updates should be made through analysis and outputs, not by modifying sources
- New discovery materials should be added to appropriate subdirectories
- Index files track all documents for easy navigation

## Access Patterns
- **Research Mode**: Query across all sources for comprehensive understanding
- **Add Mode**: Add new discovery materials or late-arriving source documents
- **Analysis**: Reference for traceability and coverage verification

## Key Files to Check
- `client-requirements/index.json` - Catalog of all client requirement documents
- `rfp-responses/index.json` - Catalog of all RFP response documents
- `transcripts/` - Individual session folders with structured content