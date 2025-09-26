# Workflows Folder Documentation

## Purpose
Documents the end-to-end user journeys through the Sourcing Window platform. Workflows
represent the horizontal view of the system, showing how users accomplish their goals
by moving through multiple features and touchpoints. These are the practical implementations
of business processes that satisfy requirements.

## Core Workflow Files

### Standard Buyer-Vendor Workflows
- **W01-buyer-parts-request**: Buyer initiates procurement process
- **W02-review-select-vendor**: Buyer evaluates quotes and chooses vendor
- **W03-vendor-submit-quote**: Vendor responds to RFQ with pricing
- **W05-vendor-confirmation-shipping**: Vendor fulfills and ships order

### System Capabilities
- **W04-messaging-capability**: Cross-cutting communication system
  - Not a workflow but a capability used across all workflows
  - Enables buyer-vendor interaction throughout process

### Integrated Vendor Workflows
- **W06-integrated-vendor-sw-buyer-timeline**: SW buyer with integrated vendor
- **W07-integrated-vendor-non-sw-buyer-timeline**: Non-SW buyer with integrated vendor
- **W08-integrated-vendor-auto-sourcing**: Automated vendor selection
- **W09-integrated-vendor-fulfillment-passthrough**: Direct fulfillment integration

## Supporting Files

### index.json
- **Purpose**: Master catalog of all workflows
- **Contents**: Workflow metadata, status, personas, complexity
- **Structure**: JSON array with workflow summaries
- **Usage**: Navigation and workflow discovery

### workflow_analysis_summary.md
- **Purpose**: Comprehensive analysis of all workflows
- **Contents**: Workflow summaries, gaps, requirements coverage, epic suggestions
- **Format**: Markdown document with structured sections
- **Usage**: Context for generating epics, features, and stories

### TEMPLATE-workflow.md
- **Purpose**: Standard template for new workflows
- **Structure**: Sections for actors, steps, systems, requirements
- **Usage**: Create consistent workflow documentation

## Workflow File Structure

Each workflow contains:
```
1. Metadata (ID, version, status)
2. Actors (participating personas)
3. Trigger (what initiates the workflow)
4. Steps (sequential process flow)
5. Systems (platforms involved)
6. Data flows (information movement)
7. Decision points (branching logic)
8. Requirements fulfilled
9. Success metrics
```

## Workflow Categories

### Primary Workflows (W01-W03, W05)
- **Actors**: Standard buyers and vendors
- **Complexity**: Moderate
- **Automation**: Partial
- **Frequency**: High volume

### Integrated Workflows (W06-W09)
- **Actors**: Integrated vendors with special capabilities
- **Complexity**: High
- **Automation**: Extensive
- **Frequency**: Strategic partnerships

### System Capabilities (W04)
- **Type**: Infrastructure service
- **Usage**: Embedded in other workflows
- **Scope**: Platform-wide

## Relationships to Other Folders

### Sources From
- `/03-outputs/personas/`: Workflow actors and their goals
- `/01-sources/client-requirements/`: Requirements driving workflows
- `/01-sources/transcripts/`: Real process observations from discovery sessions

### Informs
- `/03-outputs/epics/`, `/03-outputs/features/`, `/03-outputs/stories/`: Features needed to enable workflows
- `/02-analysis/mappings/`: Workflow-to-requirement traceability
- `/02-analysis/requirements/`: Coverage and gap identification

### Referenced By
- `/03-outputs/drafts/`: Draft epics/features/stories use workflows for context

## Usage Patterns

### For Process Understanding
1. Select workflow by user goal
2. Review step-by-step process
3. Identify touchpoints and handoffs
4. Map to system features

### For Development Planning
1. Identify features needed per step
2. Determine integration points
3. Plan API requirements
4. Design user interfaces

### For Testing
1. Use workflows as test scenarios
2. Validate each step independently
3. Test end-to-end journeys
4. Verify requirement satisfaction

## Workflow Insights

### Coverage Statistics (Updated 2025-09-26)
- **Total Workflows**: 9 documented
- **Personas Covered**: All 3 (Buyer, Vendor, Integrated Vendor)
- **Requirements Mapped**: 103 of 118 requirements (87.3% coverage)
- **Discovery Validation**: All validated through sessions
- **Stories Generated**: 160 stories covering all workflows

### Complexity Analysis
- **Simplest**: W03 (Vendor submit quote) - 5 steps
- **Most Complex**: W08 (Auto-sourcing) - 12+ steps
- **Most Integrated**: W09 (Passthrough) - 3+ systems

### Common Patterns
- All workflows include messaging capability
- Most have approval/review steps
- Status visibility is critical throughout
- Exception handling needed at each step

## File Naming Convention
- Format: `W[NN]-[descriptive-name]`
- Numbers: Sequential, grouped by type
- Names: Kebab-case, action-oriented
- Extensions: .json (data), .md (documentation)

## Maintenance Requirements
- Update when requirements change
- Validate against user feedback
- Keep synchronized with features
- Document variations and exceptions
- Review after each sprint

## Workflow States
- **Draft**: Initial documentation
- **Reviewed**: Validated with stakeholders
- **Approved**: Ready for implementation
- **Implemented**: Built and tested
- **Deployed**: In production use

## Quality Checklist
- [ ] All steps clearly defined
- [ ] Actors identified for each step
- [ ] Requirements mapped
- [ ] Exception paths documented
- [ ] Success metrics defined
- [ ] Data flows specified
- [ ] Integration points identified

## Next Steps
1. Generate epics, features, and stories from workflows
2. Build requirement traceability matrix
3. Validate integrated vendor workflows with partners
4. Create detailed API specifications per workflow
5. Design workflow monitoring and metrics