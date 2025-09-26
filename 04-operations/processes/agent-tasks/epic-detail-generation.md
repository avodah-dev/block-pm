# Epic Detail Generation Task

## Purpose
Generate comprehensive epic detail documents that expand on high-level epic/feature/story summaries with full business context, user stories in standard format, and internal review documentation.

## Input Requirements
1. **Epic Summary Source**: Path to epics-features-stories-summary.md or similar file
2. **Epic Selection**: Specific epic ID (E01-E13) to detail
3. **Project Dictionary**: Access to /04-operations/architecture/project_dictionary.md
4. **Requirements Source**: Access to /01-sources/client-requirements/ for traceability
5. **Workflows**: Access to /03-outputs/workflows/ for user journey context

## Output Specifications

### File Naming Convention
- Pattern: `e##-[epic-name].md` (e.g., e01-request-management.md)
- Location: /03-outputs/drafts/ for review, then /03-outputs/epics/ when finalized

### Document Structure

#### 1. Epic Overview Section
```markdown
# E##-[EPIC-NAME]: [Full Epic Title]

## Epic Overview
**Size**: [T-shirt size] ([X] stories, [Y] features)
**Priority**: [MVP/Phase 1/Phase 2]
**Primary Persona**: [P01-Buyer/P02-Vendor/P03-Integrated]
**Requirements Coverage**: [List requirement IDs]

[2-3 paragraph business context using Block domain language]
[Specific pain points being addressed]
```

#### 2. Feature Sections
For each feature in the epic:
```markdown
## Feature F##: [Feature Name]

### Feature Summary
[2-3 sentences describing the feature's purpose and business value]
[How it addresses specific Block requirements or pain points]
[Technical or operational context where relevant]

### User Stories
[List of stories with details - see story format below]
```

#### 3. Story Format
```markdown
#### S###: [Story Title]

As a [persona], I want [action] so that [benefit].
[1-2 additional sentences with context or examples]
```

## Processing Instructions

### Step 1: Context Gathering
1. Read the epic summary from source file
2. Load project dictionary for domain terminology
3. Identify relevant client requirements for the epic
4. Review associated workflows (if specified in epic)

### Step 2: Epic Overview Generation
1. Extract epic title and expand to full description
2. Count stories and features for sizing
3. Determine priority based on requirement criticality
4. Write 2-3 paragraphs of business context:
   - Use Block-specific terminology from dictionary
   - Reference actual pain points from discovery
   - Include specific examples (e.g., "4535-619-90892 vs 453561990892")
   - Explain why this epic matters to Block's business

### Step 3: Feature Expansion
For each feature:
1. Expand feature name to be descriptive but concise
2. Write 2-3 sentence summary that includes:
   - What capability is being delivered
   - Which requirements or pain points it addresses
   - How it fits into the larger epic context
3. Connect to Block's operational reality

### Step 4: Story Elaboration
For each story:
1. Convert brief description to "As a... I want... so that..." format
2. Add 1-2 sentences of context that might include:
   - Specific examples from Block's operations
   - Technical details that matter
   - Edge cases or special considerations
   - Connection to other stories or features

### Step 5: Quality Checks
- Verify all stories from summary are included
- Ensure consistent use of domain terminology
- Check that each story has clear value proposition
- Validate persona assignments match story context
- Confirm feature groupings make logical sense

## Domain Language Guidelines
Use Block-specific terms consistently:
- "requisition" not "request" (except in proper names like "Request Management")
- "material" when referring to Block's Salesforce terminology
- "part" when referring to general usage
- "modality" for equipment types (CT, MRI, X-ray)
- "raw part number" for normalized part numbers
- "EMA" for Enhanced Messaging Application
- "SWP" for Sourcing Window Pro (buyer-facing)
- "SW" for Sourcing Window (vendor-facing)

## Implementation Considerations Section
Add at the end of each epic:
```markdown
## Implementation Considerations

### Technical Dependencies
- [List key technical requirements]

### Integration Points
- [List system integrations needed]

### Success Metrics
- [List measurable outcomes with targets]
```

## Example References
- Input: `/03-outputs/drafts/epics-features-stories-summary.md`
- Output: `/03-outputs/drafts/e01-request-management.md`
- Enhanced: `/03-outputs/drafts/e01-request-management-full.md`

## Validation Criteria
1. Every story from summary appears in detail document
2. All features have business context
3. Stories use standard "As a..." format
4. Domain language is consistent
5. Document is self-contained and readable
6. Epic provides enough detail for stakeholder review

## Notes for Agent
- This is a standalone task - do not assume prior context
- Read all referenced files fresh each time
- Maintain consistent tone: professional but accessible
- Balance technical accuracy with business readability
- When in doubt, refer to project dictionary for terminology
- Include enough detail for developers to understand scope
- Keep descriptions concise enough for executive review