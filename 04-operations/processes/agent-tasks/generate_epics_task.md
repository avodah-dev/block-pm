# Agent Task: Generate Epics, Features, and Stories

## Context
You are analyzing a B2B marketplace platform called Sourcing Window that connects buyers who need medical equipment parts with vendors who supply them. The system includes sophisticated integrated vendors who can act as both buyers and vendors.

## Your Mission
Generate a comprehensive set of Epics, Features, and Stories based on 9 documented workflows and identified gaps. Create a single summary document with one-sentence descriptions first.

## Resources to Review
1. Read `workflow_analysis_summary.md` for complete context (in this folder)
2. Read `llm_epic_generation_instructions.md` for detailed instructions (in this folder)
3. Review `/04-operations/architecture/architecture_layers.md` to understand system boundaries
4. Scan `/03-outputs/workflows/` folder for detailed workflow documentation
5. Check `/01-sources/client-requirements/` for original requirements

## Deliverable
Create `EPICS-FEATURES-STORIES-SUMMARY.md` containing:
- 8-10 Epics (one sentence each)
- 3-5 Features per Epic (one sentence each)
- 3-5 Stories per Feature (standard user story format)
- Total: ~100-150 stories

## Key Principles
1. **Cover all workflows**: W01-W09 must be fully represented
2. **Address gaps**: Include admin, reporting, and onboarding features
3. **Maintain architecture**: Clearly separate Product vs Business Logic Layer
4. **Support personas**: P01-buyer, P02-vendor, P03-integrated-vendor, Admin
5. **Enable phasing**: Tag as MVP, Enhancement, Advanced, or Optimization

## Epic Structure Required
1. Core Buyer Operations (W01, W02)
2. Vendor Response Management (W03, W05)
3. Integrated Vendor Capabilities (W06-W09)
4. Communication Platform (W04)
5. System Integration (Business Logic Layer)
6. Administration & Configuration (Gap)
7. Analytics & Reporting (Gap)
8. Vendor Onboarding (Gap)
9. Approval Workflows (Gap)
10. Platform Operations (Gap)

## Story Format
Every story MUST follow: "As a [persona], I want to [action] so that [value]"

## Validation
Ensure:
- ✓ All 9 workflows have stories
- ✓ All 3 personas are served
- ✓ 118 documented requirements are covered (61 buyer, 57 vendor)
- ✓ Integrated vendor complexity is addressed
- ✓ Gaps are filled with new stories
- ✓ Dependencies are noted

## Start Now
Begin by reading the summary document and generating the one-sentence epic/feature/story document. Focus on business value and implementability.