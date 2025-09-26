# Instructions for Epic/Feature/Story Generation

## Your Task
Generate a comprehensive set of Epics, Features, and Stories based on the documented workflows for the Sourcing Window platform. Start with a single document containing one-sentence summaries, then expand to full stories after approval.

## Input Materials
1. **WORKFLOW-SUMMARY-FOR-ANALYSIS.md** - Consolidated overview
2. **WORKFLOW-DEVELOPMENT-MODEL.md** - Conceptual framework
3. **ARCHITECTURE-LAYERS.md** - System architecture
4. **/03-outputs/workflows/** folder - Detailed workflow documentation (W01-W09)
5. **/01-sources/client-requirements/** - Original requirements
6. **/03-outputs/personas/** - User personas (P01-P03)

## Phase 1: One-Sentence Summary Document

Create: `EPICS-FEATURES-STORIES-SUMMARY.md`

### Structure:
```markdown
# Epics, Features, and Stories Summary

## Epic E01: [Epic Name]
*One sentence describing the epic's business value*

### Feature F01.1: [Feature Name]
*One sentence describing what this feature enables*

#### Stories:
- S01.1.1: As a [persona], I want to [action] so that [value]
- S01.1.2: As a [persona], I want to [action] so that [value]

### Feature F01.2: [Feature Name]
*One sentence describing what this feature enables*

#### Stories:
- S01.2.1: As a [persona], I want to [action] so that [value]
```

## Epic Categories to Generate

### Required Epics (from workflows):
1. **Core Buyer Operations** (from W01, W02)
2. **Vendor Response Management** (from W03, W05)
3. **Integrated Vendor Capabilities** (from W06-W09)
4. **Communication Platform** (from W04)
5. **System Integration** (from W07, architecture)

### Additional Epics (from gaps):
6. **Administration & Configuration**
7. **Analytics & Reporting**
8. **Vendor Onboarding & Management**
9. **Approval Workflows**
10. **Platform Operations**

## Story Generation Rules

### Story Format
- **MUST** follow: "As a [persona], I want to [action] so that [value]"
- **Personas**: Use P01-buyer, P02-vendor, P03-integrated-vendor, or Admin
- **Actions**: Be specific and implementable
- **Value**: Clear business or user benefit

### Story Sizing
- **1-2 points**: Simple CRUD, basic UI
- **3-5 points**: Workflow step, integration point
- **5-8 points**: Complex feature, multiple components
- **8-13 points**: System-wide capability

### Coverage Requirements
- Every workflow step should have at least one story
- Every requirement should trace to at least one story
- Every persona should have relevant stories

## Traceability Matrix

For each story, identify:
- **Source Workflow(s)**: W01-W09
- **Requirements**: SWP-M-X or SW-M-X
- **Architecture Layer**: Product, Business Logic, or Business System
- **Dependencies**: Other stories that must complete first

## Priority Tagging

Tag each story with:
- **Phase**: MVP, Enhancement, Advanced, Optimization
- **Priority**: P1 (Critical), P2 (Important), P3 (Nice to have)
- **Complexity**: Low, Medium, High, Very High

## Special Considerations

### Integrated Vendor Stories
- Clearly differentiate standard vs. integrated vendor paths
- Include role-switching stories
- Address information pass-through needs
- Consider premium feature flags

### System Integration Stories
- Separate Product from Business Logic Layer
- Include Salesforce sync requirements
- Address dual-system monitoring
- Consider API and webhook needs

### Technical Debt Stories
- Include stories for architecture setup
- Add stories for monitoring/logging
- Consider performance optimization
- Include security and compliance

## Output Requirements

### Phase 1 Deliverable
Single markdown file with:
- 8-10 Epics
- 3-5 Features per Epic
- 3-5 Stories per Feature
- Total: ~100-150 one-sentence stories

### Validation Checklist
- [ ] All workflows covered
- [ ] All personas represented
- [ ] Core requirements addressed
- [ ] Gaps identified and filled
- [ ] Dependencies noted
- [ ] Priorities assigned
- [ ] Architecture layers specified

## Phase 2: Full Story Expansion

After approval of Phase 1, expand each story to include:
- Detailed acceptance criteria
- Technical implementation notes
- UI/UX considerations
- Test scenarios
- Edge cases

## Remember
- Start with the one-sentence summary document
- Focus on business value
- Maintain traceability to workflows and requirements
- Consider the three-layer architecture
- Think about both MVP and future phases
- Include stories for identified gaps
- Keep integrated vendor complexity in mind

## Success Criteria
Your generated epics/features/stories should:
1. Cover 100% of documented workflows
2. Address 90%+ of requirements
3. Fill identified gaps
4. Provide clear implementation path
5. Support phased rollout
6. Maintain architectural boundaries