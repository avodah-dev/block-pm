# Requirements Analysis Methodology

## Project Context: Sourcing Window Evolution

### History
- **SW 1.0**: Block built the original Sourcing Window as an internal tool, then attempted to market it to other companies
- **SW 2.0**: Block hired Legendary to rebuild on Salesforce 360, but the result was suboptimal
- **Current Project**: Block has hired us (Avodah) to build a modern Sourcing Window with proper architectural separation

### Architectural Mandate
Block requires clear separation between:
- **Product Layer**: Clean, vendor-agnostic marketplace platform usable by any company
- **Business Logic Layer**: Block-specific features, integrations, and competitive advantages

This ensures Block can both use the platform internally AND potentially offer it to other companies without exposing their proprietary business logic.

## Overview
This document describes the actual process used to develop the Sourcing Window epics, features, and stories from Block's requirements through discovery sessions to implementation planning. This methodology was executed September 2025 and resulted in the current draft analysis.

## Process Timeline

### Phase 1: Requirements Import and Validation
**Problem**: Initial requirements import was misaligned with Block's actual RFP documents
**Solution**: Complete rebuild of client-anchor-docs from Block's original CSV sources

#### Steps Taken:
1. Identified discrepancies in original CAD (Client Anchor Document) imports from Block's RFP
2. Rebuilt CAD-001 (buyer requirements) and CAD-002 (vendor requirements) from Block's source CSVs
3. Validated all 118 requirements (61 buyer, 57 vendor) from Block's RFP
4. Archived incorrect versions to prevent confusion
5. Updated all requirement IDs to match Block's source documents

**Key Learning**: Always validate imports against source documents before building dependencies

### Phase 2: Discovery Sessions and Domain Language Extraction
**Duration**: 3 days (September 8-10, 2025)
**Purpose**: Understand actual user workflows and pain points beyond written requirements

#### Discovery Inputs:
1. **Day 1**: Buyer workflows and pain points
   - Screen recordings of current Excel-based processes
   - Voice narrations explaining decision logic
   - Pain points around manual data entry

2. **Day 2**: Vendor perspectives
   - Demonstrations of multi-portal management
   - Communication gap examples
   - Order fulfillment challenges

3. **Day 3**: Integrated vendor workflows (Block's proprietary business model)
   - Block acts as middleman/integrated vendor
   - Auto-sourcing capabilities (Block's competitive advantage)
   - API integration requirements for Block's partners
   - Pass-through fulfillment models (Block's innovation)

#### Domain Language Capture:
- Extracted terminology from transcripts to build `project_dictionary.md`
- Ensured customer's language preserved in all documentation
- Key terms: Sourcing Window (SW), Sourcing Window Platform (SWP), EMA, integrated vendor
- Avoided generic tech terms in favor of domain-specific language

### Phase 3: Workflow Documentation
**Output**: 9 comprehensive workflows (W01-W09)
**Method**: Synthesis of discovery materials into structured user journeys

#### Workflow Categories Identified:
1. **Standard Workflows (W01-W05)**: Direct implementation of client requirements
   - W01: Buyer parts request
   - W02: Review and select vendor
   - W03: Vendor submit quote
   - W04: Messaging capability (cross-cutting)
   - W05: Vendor confirmation and shipping

2. **Integrated Vendor Workflows (W06-W09)**: Block's proprietary business model
   - W06: Integrated vendor with SW buyer
   - W07: Integrated vendor with non-SW buyer
   - W08: Auto-sourcing capability
   - W09: Fulfillment pass-through

#### Documentation Approach:
- Each workflow includes narrative from voice transcripts
- Step-by-step breakdown with system interactions
- Requirements mapping (initially flawed, later corrected)
- Persona identification and goals

### Phase 4: Requirements Rebuild and Workflow Correction
**Problem**: Workflows W06-W09 referenced non-existent requirements (SW-M-44 through SW-M-67)
**Root Cause**: Requirements only go up to SWP-M-46 and SW-M-43

#### Correction Process:
1. Removed all invalid requirement references from W06-W09
2. Recognized W06-W09 as business innovations, not requirement implementations
3. Updated workflow JSON files with correct structure
4. Validated all requirement mappings against actual CADs

**Key Insight**: Block's integrated vendor workflows (W06-W09) are their proprietary business innovations, not part of the base product requirements. These belong in the Business Logic Layer, not the Product Layer

### Phase 5: Epic/Feature/Story Generation
**Method**: Used LLM-assisted analysis with human validation
**Tool**: `generate_epics_task.md` agent task

#### Generation Process:
1. **Preparation**:
   - Created `workflow_analysis_summary.md` consolidating all workflows
   - Included architecture layers to maintain proper boundaries
   - Incorporated pain points from discovery

2. **LLM Analysis**:
   - Fed consolidated workflows to LLM
   - Generated 7 main epics with features and stories
   - Ensured coverage of all workflows and personas
   - Used domain language from project dictionary

3. **Structure Created**:
   - E01-E04: Direct requirement implementations
   - E05: Integration and messaging platform
   - E06-E07: Block's innovations (clearly marked)
   - E08-E10: Gap filling (admin, reporting, operations)

### Phase 6: Coverage Validation
**Purpose**: Ensure 100% requirement coverage and identify gaps

#### Validation Steps:
1. Created requirements traceability matrix
2. Mapped every requirement to features
3. Identified covered vs. uncovered requirements
4. Documented gaps requiring new features
5. Validated persona coverage across all epics

#### Results:
- 100% requirement coverage achieved (with clear architectural separation)
- Base product requirements: Addressed in E01-E04 (Product Layer)
- Block's business innovations: Contained in E06-E07 (Business Logic Layer)
- Platform gaps: Filled by E08-E10 (Product Layer enhancements)

## Current State (September 2025)

### Completed Artifacts:
1. ✅ Corrected client-anchor-docs with valid requirements
2. ✅ 9 workflows documented with proper requirement mapping
3. ✅ Project dictionary with domain language
4. ✅ Draft epics/features/stories (in `/epics-features-stories/draft/`)
5. ✅ Requirements traceability matrix
6. ✅ Gap analysis

### Ready for Review:
- `EPICS-FEATURES-STORIES-SUMMARY.md`: Complete breakdown
- `REQUIREMENTS-TRACEABILITY-MATRIX.md`: Coverage validation
- `REVIEW-GUIDE.md`: Stakeholder review instructions

## Next Steps

### Immediate (Current Phase):
1. Block stakeholder review of draft epics/features/stories
2. Validate MVP scope for Block's February launch
3. Prioritize features based on Block's business value
4. Finalize requirement mappings to Block's RFP

### Future Phases:
1. **Story Elaboration**:
   - Expand stories with acceptance criteria
   - Add technical requirements
   - Include UI/UX specifications

2. **Project Management Integration**:
   - Potential Linear API integration
   - Story point estimation
   - Sprint planning and backlog management

3. **Implementation Tracking**:
   - Move from draft to active folders
   - Track implementation progress
   - Maintain requirement traceability

## Lessons Learned

1. **Validate Early**: Always verify source documents before building dependencies
2. **Preserve Domain Language**: Use customer terminology throughout
3. **Separate Innovation**: Clearly distinguish base product requirements from Block's proprietary business innovations
4. **Document Process**: Capture methodology for repeatability
5. **Maintain Traceability**: Every feature must trace to requirement or identified gap

## Tools and Documents Used

### Source Documents:
- `/client-anchor-docs/`: Block's original RFP requirements
- `/transcripts/`: Discovery session materials with Block's team
- `/reference/project_dictionary.md`: Block's domain terminology

### Process Documents:
- `/processes/agent-tasks/generate_epics_task.md`: LLM generation instructions
- `/processes/agent-tasks/workflow_analysis_summary.md`: Consolidated analysis input

### Output Documents:
- `/epics-features-stories/draft/`: Generated artifacts
- `/analysis/requirements-traceability-matrix.json`: Coverage tracking

## Success Metrics

1. **Requirement Coverage**: 100% of 118 requirements mapped
2. **Workflow Support**: All 9 workflows have implementing features
3. **Persona Coverage**: All 3 personas plus admin addressed
4. **Gap Identification**: 5 major gap areas identified and addressed
5. **Domain Alignment**: Consistent use of customer terminology

## Methodology Validation

This methodology successfully:
- Transformed raw requirements into implementable stories
- Incorporated real user feedback from discovery
- Maintained clear separation of requirements vs. innovations
- Provided full traceability from requirement to implementation
- Created foundation for phased development approach

---

*Document Created*: September 26, 2025
*Last Updated*: September 26, 2025
*Status*: Describes completed analysis process