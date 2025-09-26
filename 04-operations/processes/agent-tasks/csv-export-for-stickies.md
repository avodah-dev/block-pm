# CSV Export for Stickies Task

## Purpose
Convert epic/feature/story hierarchical documentation into CSV format optimized for Excel review and MIRO sticky note creation, with shortened names that maintain clarity while fitting space constraints.

## Input Requirements
1. **Source Document**: Path to epics-features-stories-summary.md or similar hierarchical listing
2. **Output Location**: /03-outputs/drafts/ directory
3. **Format Requirements**: Three-column CSV with hierarchy preserved through blank cells

## Output Specifications

### File Naming Convention
- Pattern: `epic-feature-story-stickies.csv`
- Location: /03-outputs/drafts/
- Format: UTF-8 encoded CSV

### CSV Structure
```csv
Epic,Feature,Story
E01: Epic Name,F01: Feature Name,S001: Story description
,,S002: Story description
,,S003: Story description
,F02: Feature Name,S004: Story description
,,S005: Story description
E02: Epic Name,F03: Feature Name,S006: Story description
```

### Column Specifications
1. **Epic Column**:
   - Only populated on first row of each epic group
   - Format: `E##: [Shortened Name]`
   - Target length: 15-20 words

2. **Feature Column**:
   - Only populated on first row of each feature group
   - Format: `F##: [Shortened Name]`
   - Target length: 15-25 words

3. **Story Column**:
   - One story per row
   - Format: `S###: [Shortened description]`
   - Target length: 20-25 words

## Processing Instructions

### Step 1: Parse Source Document
1. Read the markdown source file
2. Identify epic headers (## Epic E##-)
3. Identify feature headers (### Feature F##:)
4. Identify story items (- S###:)
5. Maintain hierarchical relationships

### Step 2: Name Shortening Rules

#### General Principles
- Remove articles (a, an, the) where possible
- Use "&" instead of "and"
- Use common abbreviations:
  - Management → Mgmt
  - Configuration → Config
  - Information → Info
  - Application → App
  - Administrator → Admin
  - Operations → Ops
  - Identification → ID

#### Epic Name Shortening
- Keep epic ID (E##)
- Extract core concept (2-3 words max)
- Examples:
  - "Buyer parts request creation and management" → "Request Management"
  - "Enhanced messaging application (EMA)" → "Messaging Platform (EMA)"

#### Feature Name Shortening
- Keep feature ID (F##)
- Focus on primary function
- Use action words where possible
- Examples:
  - "Parts database search and management" → "Parts Search & Management"
  - "Quote submission interface" → "Quote Submission Interface"

#### Story Description Shortening
- Keep story ID (S###)
- Focus on deliverable/action
- Remove implementation details
- Remove technical specifications
- Examples:
  - "Implement parts search with fuzzy matching and raw part number normalization"
    → "Parts search with fuzzy matching and raw part normalization"
  - "Create vendor selection interface with qualification filters"
    → "Vendor selection interface with filters"

### Step 3: CSV Generation
1. Create header row: `Epic,Feature,Story`
2. For each epic:
   - Write epic name in column 1 of first row only
   - Leave column 1 blank for subsequent rows
3. For each feature within epic:
   - Write feature name in column 2 of first row only
   - Leave column 2 blank for subsequent rows
4. For each story within feature:
   - Write story description in column 3
   - Each story gets its own row

### Step 4: Hierarchy Preservation
- Blank cells maintain visual hierarchy
- Never skip rows between items
- Maintain epic → feature → story nesting
- Preserve original ID numbers for traceability

## Quality Checks

### Length Validation
- Epic names: 15-20 words (≈80-120 characters)
- Feature names: 15-25 words (≈100-150 characters)
- Story descriptions: 20-25 words (≈120-180 characters)

### Readability Validation
- Each item must be understandable standalone
- Shortened names must preserve core meaning
- Technical terms kept where essential
- Business value still apparent

### Format Validation
- CSV properly escaped (quotes, commas)
- UTF-8 encoding for special characters
- No trailing commas
- Consistent ID formatting

## Use Case Optimization

### For Excel Review
- Hierarchical structure visible through blanks
- Can add columns for:
  - Priority
  - Size estimates
  - Phase assignment
  - Owner/assignee
  - Status tracking
- Sortable/filterable by epic or feature

### For MIRO Stickies
- Text length fits standard sticky note size
- Readable at zoom-out levels (board overview)
- Natural grouping through paste patterns
- IDs enable cross-referencing
- Shortened names work as sticky headers

## Example Transformations

### Input (Original)
```
## Epic E01-REQUEST-MANAGEMENT: Buyer parts request creation and management
### Feature F01: Parts database search and management
- S001: Implement parts search with fuzzy matching and raw part number normalization
```

### Output (CSV)
```
E01: Request Management,F01: Parts Search & Management,S001: Parts search with fuzzy matching and raw part normalization
```

## Special Considerations

### Domain Terms to Preserve
Always keep these Block-specific terms:
- EMA (Enhanced Messaging Application)
- PO (Purchase Order)
- RFQ (Request for Quote)
- FSE (Field Service Engineer)
- SWP/SW (Sourcing Window variants)

### Abbreviation Standards
Consistent abbreviations across export:
- Implementation → Impl (only if needed)
- System → Sys (only if needed)
- Management → Mgmt
- Administration → Admin
- Configuration → Config

## Validation Checklist
- [ ] All epics from source included
- [ ] All features from source included
- [ ] All stories from source included
- [ ] ID numbers preserved accurately
- [ ] Hierarchy maintained through blanks
- [ ] Names shortened appropriately
- [ ] CSV format valid
- [ ] File saved in correct location

## Notes for Agent
- This is a standalone task - read source file fresh
- Focus on clarity over brevity
- Maintain consistency in abbreviations
- Preserve technical accuracy
- Test CSV format validity
- Consider copy/paste behavior in target tools
- Ensure no data loss in transformation