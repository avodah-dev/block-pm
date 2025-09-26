# Transcript Epic-Feature Indexing Task

## Purpose
Systematically analyze discovery transcript files to create an index mapping conversation segments to specific epics and features, while identifying potential gaps in the current epic/feature structure. This index enables targeted transcript review during epic refinement and ensures no valuable insights are lost.

## Input Requirements
1. **Transcript Source**: Path to day folder (e.g., /01-sources/transcripts/20250908-discovery-day01/)
2. **Epic-Feature Reference**: /03-outputs/drafts/epics-features-reference.json
3. **Project Dictionary**: /04-operations/architecture/project_dictionary.md
4. **Output Location**: /02-analysis/transcripts/ (create if needed)

## Output Specifications

### Primary Output: Index File
- **Filename Pattern**: `transcript-index-[YYYYMMDD]-day##.json`
- **Location**: /02-analysis/transcripts/
- **Format**: JSON with both machine-readable structure and human-friendly organization

### Secondary Output: Summary Report
- **Filename Pattern**: `transcript-index-[YYYYMMDD]-day##-summary.md`
- **Location**: /02-analysis/transcripts/
- **Format**: Markdown summary of findings and recommendations

## Processing Instructions

### Step 1: Preparation
1. **Load Reference Data**:
   - Read epics-features-reference.json
   - Load project dictionary for domain terms
   - Create keyword mapping from epic/feature names

2. **Prepare Analysis Framework**:
   ```json
   {
     "transcript_day": "20250908-discovery-day01",
     "epics_features": {}, // Will be populated
     "uncategorized_insights": [],
     "potential_gaps": [],
     "key_quotes": []
   }
   ```

### Step 2: Transcript-by-Transcript Analysis
For each .srt file in the day folder:

#### 2.1 Initial Pass - Segment Identification
1. Read transcript file (handle .srt format)
2. Break into logical segments (5-10 minute chunks or topic shifts)
3. For each segment:
   - Extract key phrases and domain terms
   - Identify speakers and roles
   - Note timestamp ranges

#### 2.2 Epic/Feature Mapping
For each segment:
1. **Direct Matching**:
   - Search for epic/feature keywords
   - Match domain terminology to specific features
   - Consider context (buyer vs vendor discussion)

2. **Contextual Matching**:
   - "parts search" → E01/F01
   - "vendor selection" → E01/F03
   - "quote comparison" → E03/F07
   - "messaging" or "EMA" → E05
   - "dashboard" or "reporting" → E08
   - "mobile" or "FSE" → E12

3. **Confidence Scoring**:
   - High: Direct mention of functionality
   - Medium: Related discussion with context
   - Low: Tangential reference

#### 2.3 Gap Identification
Look for discussions about:
- Features not in current structure
- Pain points without solutions
- "Would be nice" or "We need" statements
- Process descriptions without matching features
- Integration requirements not covered

### Step 3: Index Structure Creation

#### JSON Index Format
```json
{
  "metadata": {
    "transcript_day": "20250908-discovery-day01",
    "processed_date": "2025-09-27",
    "total_files": 6,
    "total_duration": "5:23:45"
  },
  "indexed_content": {
    "E01": {
      "epic_name": "Request Management",
      "references": [
        {
          "file": "09-08 - 3 - Discovery Day 1, External Buyers & Sellers, Part 1.srt",
          "timestamp_start": "00:12:34",
          "timestamp_end": "00:15:45",
          "feature": "F01",
          "feature_name": "Parts Search & Management",
          "confidence": "high",
          "context": "Discussion about part number normalization challenges",
          "key_quote": "The search function sucks... we need fuzzy matching",
          "speakers": ["Sarah (Buyer)", "Jeff (Product)"]
        }
      ]
    }
  },
  "uncategorized_insights": [
    {
      "file": "09-08 - 4 - Discovery Day 1, External Buyers & Sellers, Part 2.srt",
      "timestamp": "00:45:23",
      "insight": "Voice-to-text for FSEs in the field",
      "potential_epic": "E12 (Mobile) or New Epic",
      "priority": "medium",
      "quote": "FSEs have their hands under equipment, can't type"
    }
  ],
  "potential_gaps": [
    {
      "description": "Warranty management workflow",
      "mentioned_in": ["file1.srt", "file3.srt"],
      "frequency": "high",
      "suggested_epic": "New Epic or E04 extension",
      "business_impact": "Critical for service contracts"
    }
  ],
  "statistics": {
    "total_segments": 145,
    "mapped_segments": 128,
    "unmapped_segments": 17,
    "epics_referenced": 11,
    "features_referenced": 28,
    "confidence_high": 89,
    "confidence_medium": 32,
    "confidence_low": 7
  }
}
```

### Step 4: Summary Report Generation

#### Markdown Summary Format
```markdown
# Transcript Index Summary - Discovery Day 01

## Coverage Statistics
- **Segments Analyzed**: 145
- **Successfully Mapped**: 88.3% (128/145)
- **Epics Referenced**: 11 of 13
- **Features Referenced**: 28 of 40

## Top Referenced Epics
1. E01 Request Management (32 references)
2. E05 Messaging Platform (28 references)
3. E03 Purchase Selection (24 references)

## Key Insights Not Covered
### High Priority
- Warranty management workflow (mentioned 5 times)
- Bulk import capabilities (mentioned 3 times)

### Medium Priority
- Voice-to-text for field service
- Automated escalation rules

## Recommended Actions
1. Review warranty management segments for potential new epic
2. Enhance E12 (Mobile) with voice capabilities
3. Consider bulk operations feature for E11 (Admin)

## Notable Quotes
- "The search function sucks" - Sarah (Buyer) [00:12:34]
- "We need to see all quotes side by side" - Tom (Buyer) [01:23:45]
```

## Analysis Guidelines

### Keyword Recognition Patterns
Use both exact matches and contextual understanding:
- **Parts/Search**: "part number", "PN", "material", "search", "fuzzy"
- **Vendors**: "supplier", "vendor", "capability", "qualification"
- **Quotes**: "RFQ", "quote", "pricing", "sourcing", "SRC"
- **Orders**: "PO", "purchase order", "fulfillment", "shipping"
- **Messaging**: "EMA", "chat", "message", "notification"
- **Integration**: "Salesforce", "API", "sync", "integration"

### Context Clues for Mapping
- **Speaker Role**: Buyers discuss E01, E03; Vendors discuss E02, E07
- **Process Phase**: Request → Quote → Order → Fulfillment
- **System Names**: "Sourcing Window Pro" = Buyer features, "Sourcing Window" = Vendor features
- **Pain Points**: Map to features that solve them

### Gap Detection Signals
Listen for:
- "We can't currently..."
- "It would be great if..."
- "The problem is..."
- "We have to manually..."
- "There's no way to..."
- Process descriptions with no system support

## Quality Checks

### Completeness Validation
- [ ] All .srt files in folder processed
- [ ] Every segment assigned or marked uncategorized
- [ ] Confidence levels assigned to all mappings
- [ ] Timestamps accurate and complete
- [ ] Speaker identification where possible

### Accuracy Validation
- [ ] Epic/Feature mappings make logical sense
- [ ] Confidence levels justified by context
- [ ] Gaps are genuinely not covered by existing structure
- [ ] Key quotes accurately represent discussion

### Output Validation
- [ ] JSON file is valid and well-formed
- [ ] Summary report is readable and actionable
- [ ] Statistics are accurate
- [ ] Recommendations are specific and justified

## Usage of Index

### For Epic Refinement
When refining a specific epic:
1. Query index for all references to that epic
2. Review high-confidence segments first
3. Check medium/low confidence for edge cases
4. Review uncategorized for missed stories

### For Gap Analysis
1. Review potential_gaps section
2. Check frequency and business impact
3. Validate against current epic structure
4. Propose new epics or features as needed

### For Validation
1. Use key quotes to verify understanding
2. Check speaker context for accuracy
3. Validate pain points are addressed
4. Ensure critical discussions aren't missed

## Special Considerations

### .srt File Handling
- Parse subtitle format correctly
- Maintain timestamp accuracy
- Handle speaker identification if present
- Deal with transcription errors gracefully

### Multi-Part Sessions
- Maintain context across file parts
- Note when discussions span files
- Track topic continuations
- Aggregate related segments

### Confidence Assignment
- **High**: Direct feature discussion, clear requirements
- **Medium**: Related context, indirect reference
- **Low**: Possible connection, needs validation

## Notes for Agent
- Process one day at a time for manageability
- Read files in chronological order to maintain context
- Don't force mappings - mark as uncategorized if unclear
- Capture exact quotes when they illustrate key points
- Note speaker roles when identifiable
- Flag any technical discussions that might impact architecture
- Identify patterns across multiple mentions
- Be conservative with gap identification - verify it's truly missing