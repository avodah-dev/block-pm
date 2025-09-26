# E01-REQUEST-MANAGEMENT: Buyer Parts Request Creation and Management (Full Specification)

## Epic Overview
**Size**: Large (12 stories, 3 features)
**Priority**: P0 (Critical - Core Marketplace Foundation)
**Primary Persona**: P01-Buyer (Procurement Buyer)
**Phase**: Phase 1 - MVP Core Functionality
**Requirements Coverage**: SWP-M-10, SWP-M-11, SWP-M-12, SWP-M-13, SWP-M-14, SWP-M-15, SW-M-1, SW-M-2, SW-M-3, SW-M-4, SW-S-3, and discovery insights

This epic encompasses the complete buyer workflow for creating and managing parts requisitions in Sourcing Window Pro (SWP). It provides the foundation for buyers to search the parts/materials database, create new materials when needed, configure multi-part requisitions with special instructions, and distribute requests to qualified vendors based on their capabilities. This is the entry point for all procurement activity and directly addresses Block's need for intuitive part searching with fuzzy matching and raw part number normalization - critical since 85-90% of searches use part numbers.

The epic solves the current pain point where "search function sucks" leading to duplicate materials in the database. It implements Block's "super top secret" raw part number formula that removes dashes and trims leading zeros, allowing buyers to find parts regardless of formatting variations (e.g., 4535-619-90892 vs 453561990892).

---

## Feature F01: Parts Database Search and Management

### Feature Summary
This feature provides the core search and material management capabilities that buyers need to find and select parts for requisitions. It implements fuzzy matching to handle the various ways part numbers are formatted across different vendors and manufacturers, addressing Block's critical need where 85-90% of all searches are by part number. The feature also enables creation of new materials when parts aren't found in the existing database, with required fields for modality, manufacturer, part number, and description to maintain data quality.

The search functionality goes beyond simple text matching to include normalization algorithms that handle Block's hyphenated format versus other vendors' formats, preventing the duplicate material problem that plagues the current system. Users can view detailed part specifications including compatibility relationships (understanding that part A may replace B, but B might not replace A), modality tags, and images to ensure they're selecting the correct item.

### User Stories

---

#### S001: Implement parts search with fuzzy matching and raw part number normalization

**Story ID**: S001
**Persona**: P01-Buyer
**Architecture Layer**: sw-backend, sw-frontend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F01-Parts-Database-Search
**Priority**: P0 (Critical)
**Phase**: Phase 1
**Story Points**: 5

**Description**:
As a buyer, I want to search for parts using partial or differently formatted part numbers so that I can find what I need regardless of how vendors format their part numbers. The system should apply Block's raw part number normalization (removing dashes, trimming zeros) automatically and suggest close matches when exact matches aren't found.

**Acceptance Criteria**:
- Search accepts part numbers with or without hyphens, spaces, or leading zeros
- System automatically applies raw part number normalization algorithm
- Fuzzy matching returns results within 2-3 character variations
- Search results show match confidence percentage
- Results prioritize exact matches, then normalized matches, then fuzzy matches
- Search completes within 2 seconds for database of 100,000+ parts
- System logs all searches to identify patterns for future optimization

**Traceability**:

**Requirements**:
- **SWP-M-10**: "Material / Part search (Customer must be able to search for a PN or description and click 'Select' to add to a material Request List)"
  - This story directly implements the part number search capability requested

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S02 (Search for Part)

**Technical Notes**:
- Implement Levenshtein distance algorithm for fuzzy matching
- Create indexed normalized_part_number column for performance
- Consider caching frequent search results
- Raw part number formula: remove all non-alphanumeric, trim leading zeros, uppercase

---

#### S002: Create parts database with modality and part compatibility tracking

**Story ID**: S002
**Persona**: P01-Buyer
**Architecture Layer**: sw-backend, data
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F01-Parts-Database-Search
**Priority**: P0 (Critical)
**Phase**: Phase 1
**Story Points**: 8

**Description**:
As a buyer, I want to see which equipment types (modalities like CT, MRI, X-ray) a part works with and understand part compatibility relationships (which parts can replace other parts) so that I can ensure I'm ordering the correct replacement. The database should clearly show when part compatibility is directional (Part A replaces B, but B doesn't replace A).

**Acceptance Criteria**:
- Database schema includes modality tags (CT, MRI, X-ray, Ultrasound, etc.)
- Parts can be tagged with multiple modalities
- Compatibility relationships stored with directionality
- UI displays compatibility as "Can replace" and "Can be replaced by" separately
- System shows manufacturer-specific compatibility notes
- Database supports equipment model-specific compatibility
- Import capability for existing Block compatibility data

**Traceability**:

**Requirements**:
- **SW-M-2**: "Ability for vendors to have multiple 'capabilities' - These are buckets we put them in to route requests to"
  - While this is vendor-focused, the modality tracking enables proper vendor routing
- **SW-M-3**: "Must be able to rank each vendor within a capability with a tier - Tiers 1-3 (+) based on vendor KPI"
  - Modality data supports tiered vendor selection

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Steps W01-S06/S07 (Validate Vendor Capabilities)

**Technical Notes**:
- Consider graph database for complex part compatibility relationships
- Implement bidirectional part compatibility matrix
- Plan for bulk import of existing part compatibility data from Salesforce
- Note: Vendor compatibility is separate - managed through vendor configuration

---

#### S003: Build part creation form for new materials not in database

**Story ID**: S003
**Persona**: P01-Buyer
**Architecture Layer**: sw-frontend, sw-backend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F01-Parts-Database-Search
**Priority**: P1 (High)
**Phase**: Phase 1
**Story Points**: 3

**Description**:
As a buyer, I want to create new material entries when I can't find a part in the system so that I can still submit my requisition and build the database for future use. The form should require modality, manufacturer, part number, and description as mandatory fields while allowing optional fields like system information.

**Acceptance Criteria**:
- Form requires: Modality, Manufacturer, Part Number, Description
- Optional fields: System, Model, Category, Image URL
- Duplicate detection warns if similar part exists
- New parts flagged for admin review
- Auto-save draft capability
- Created parts immediately searchable by creator
- Audit trail tracks who created each part

**Traceability**:

**Requirements**:
- **SWP-M-12**: "Customer must be able to create new Material with the following required fields: Modality, Manufacturer, Part #, Description, Sytem (optional)"
  - This story directly implements the new material creation requirement

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S02a (Create New Part - Alternative)

**Technical Notes**:
- Implement duplicate detection using normalized part numbers
- Consider approval workflow for new parts to maintain data quality
- Auto-populate manufacturer dropdown from existing data

---

#### S004: Implement part details view with specifications and images

**Story ID**: S004
**Persona**: P01-Buyer
**Architecture Layer**: sw-frontend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F01-Parts-Database-Search
**Priority**: P2 (Medium)
**Phase**: Phase 1
**Story Points**: 2

**Description**:
As a buyer, I want to view comprehensive details about a part including specifications, images, compatibility information, and historical pricing so that I can verify I'm selecting the correct item before adding it to my requisition.

**Acceptance Criteria**:
- Details page shows: Part number, Description, Manufacturer, Modality
- Display part images when available
- Show compatibility relationships
- Display last 5 purchase prices and dates
- Show average lead time from past orders
- Include vendor availability indicators
- Link to manufacturer specifications if available

**Traceability**:

**Requirements**:
- **SW-S-3**: "Vendor should be able to view all items requested (materials + qty) in Requisition, IN A SINGLE REQ"
  - Part details support comprehensive requisition viewing

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S03 (Select Part)

**Technical Notes**:
- Lazy load images for performance
- Cache frequently viewed part details
- Consider CDN for part images

---

## Feature F02: Request Creation and Configuration

### Feature Summary
This feature enables buyers to build complex, multi-part requisitions with all the configuration options needed for effective procurement. It supports Block's requirement that "multiple requests on one Requisition" while maintaining individual line item tracking for each part. Buyers can specify quantities, urgency levels, and add special instructions that help vendors understand specific needs or requirements for the order.

The feature includes attachment capabilities for supporting documentation like specifications or drawings, and implements a customer reference number field that helps buyers track requisitions back to their internal systems or service requests. The validation logic ensures all required information is captured before submission, preventing incomplete requests that would delay the procurement process.

### User Stories

---

#### S005: Design multi-part request builder interface

**Story ID**: S005
**Persona**: P01-Buyer
**Architecture Layer**: sw-frontend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F02-Request-Creation
**Priority**: P0 (Critical)
**Phase**: Phase 1
**Story Points**: 5

**Description**:
As a buyer, I want to add multiple parts to a single requisition with individual quantity and configuration for each line item so that I can efficiently request everything needed for a job in one submission. The interface should show all items in the requisition with the ability to modify or remove individual lines.

**Acceptance Criteria**:
- Support unlimited line items per requisition
- Each line shows: Part number, Description, Quantity, Unit price estimate
- Drag-and-drop reordering of line items
- Bulk actions: Delete selected, Copy line item
- Running total displayed
- Auto-save every 30 seconds
- Visual indicator for unsaved changes

**Traceability**:

**Requirements**:
- **SWP-M-13**: "Multiple requests on one Requisition should be an easy task"
  - Core requirement for multi-part requisitions
- **SW-S-3**: "Vendor should be able to view all items requested (materials + qty) in Requisition, IN A SINGLE REQ"
  - Ensures vendors see complete requisition

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S04 (Finalize Request Details)

**Technical Notes**:
- Use virtualization for large line item lists
- Implement optimistic UI updates for responsiveness
- Store draft state in localStorage for recovery

---

#### S006: Implement quantity and urgency specification

**Story ID**: S006
**Persona**: P01-Buyer
**Architecture Layer**: sw-frontend, sw-backend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F02-Request-Creation
**Priority**: P1 (High)
**Phase**: Phase 1
**Story Points**: 2

**Description**:
As a buyer, I want to specify the quantity needed for each part and indicate the urgency level (routine, urgent, emergency) so that vendors understand my timeline requirements and can prioritize their responses accordingly.

**Acceptance Criteria**:
- Quantity field accepts 1-9999 with validation
- Urgency levels: Routine (7-10 days), Urgent (2-3 days), Emergency (24 hours)
- Urgency can be set per line item or for entire requisition
- Visual indicators (colors/icons) for urgency levels
- Quantity defaults to 1
- Decimal quantities supported for applicable parts
- Urgency affects vendor notification priority

**Traceability**:

**Requirements**:
- Direct support for requisition configuration needs

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S04 (Finalize Request Details)

**Technical Notes**:
- Store urgency levels as enum for consistency
- Consider SLA tracking based on urgency

---

#### S007: Create special instructions and attachment capability

**Story ID**: S007
**Persona**: P01-Buyer
**Architecture Layer**: sw-frontend, sw-backend, data
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F02-Request-Creation
**Priority**: P1 (High)
**Phase**: Phase 1
**Story Points**: 3

**Description**:
As a buyer, I want to add special instructions to my requisition and attach relevant documents (specifications, drawings, photos) so that vendors have all the context they need to provide accurate quotes. The system should support common file formats with reasonable size limits.

**Acceptance Criteria**:
- Special instructions field supports 2000 characters
- File upload supports: PDF, JPG, PNG, DOC, DOCX, XLS, XLSX
- Maximum 5 files per requisition
- Maximum 10MB per file
- Files scan for malware before storage
- Instructions can be per line item or for entire requisition
- Preview capability for uploaded files

**Traceability**:

**Requirements**:
- **SWP-M-11**: "Notes field for each Request (not just for the Requisition)"
  - Implements notes/special instructions capability

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S04 (Finalize Request Details)

**Technical Notes**:
- Use S3 or similar for file storage
- Implement virus scanning on upload
- Generate thumbnails for image attachments

---

#### S008: Build request validation and submission logic

**Story ID**: S008
**Persona**: P01-Buyer
**Architecture Layer**: sw-backend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F02-Request-Creation
**Priority**: P0 (Critical)
**Phase**: Phase 1
**Story Points**: 3

**Description**:
As a buyer, I want the system to validate my requisition for completeness and required fields before submission so that I don't accidentally send incomplete requests to vendors. The validation should check for required fields, valid quantities, and ensure at least one part is included.

**Acceptance Criteria**:
- Validate at least one line item exists
- Check all required fields completed
- Verify quantities are positive integers
- Ensure delivery address is specified
- Validate customer reference number format if provided
- Show validation errors inline
- Prevent submission until errors resolved
- Generate unique requisition ID on submission

**Traceability**:

**Requirements**:
- **SWP-M-14**: "Customers to enter a Customer Reference Number (free text field for customer to enter SR, Case or other # for their own reference)"
  - Supports reference number validation

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S05 (Submit Request)

**Technical Notes**:
- Implement both client and server-side validation
- Use transaction for requisition creation
- Generate requisition IDs with timestamp prefix for sorting

---

## Feature F03: Vendor Selection and Distribution

### Feature Summary
This feature implements the intelligent vendor matching and distribution system that ensures requisitions reach the right suppliers based on their declared capabilities. It uses vendor-declared modality support, geographic coverage, and specialty certifications to automatically identify qualified vendors for each requisition. This addresses Block's requirement for "auto-connect to vendors by capability" while maintaining flexibility for manual vendor management.

The system performs real-time validation against vendor capabilities, checking not just part availability but also modality expertise, manufacturer relationships, and service territories. Buyers retain control with the ability to manually add vendors they know can fulfill the request or remove vendors they don't want to work with, supporting both automated efficiency and buyer judgment.

### User Stories

---

#### S009: Implement vendor capability matching algorithm

**Story ID**: S009
**Persona**: P01-Buyer (System Process)
**Architecture Layer**: sw-backend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F03-Vendor-Selection
**Priority**: P0 (Critical)
**Phase**: Phase 1
**Story Points**: 8

**Description**:
As a buyer, I want the system to automatically identify vendors who have compatibility with the parts in my requisition (based on part type, modality, or brand alignment) so that I don't have to manually select vendors for every request. The algorithm should consider vendor compatibility settings that Block has manually configured, including whether vendors specialize in specific brands (GE, Phillips) or can supply all types (like AllParts).

**Acceptance Criteria**:
- Algorithm matches vendors based on vendor compatibility (part type, modality, brand)
- Check vendor-to-part compatibility as configured by Block admin
- Consider vendor tier rankings (1-3+) in selection
- Check vendor geographic coverage
- Validate vendor certifications if required
- Exclude vendors on customer concession lists
- Return ranked list of qualified vendors
- Process completes within 3 seconds
- Log matching decisions for audit

**Traceability**:

**Requirements**:
- **SWP-M-15**: "Must auto-connect request with Vendor suppliers that have been accepted for that category"
  - Core requirement for automatic vendor matching
- **SW-M-1**: "Ability to full manage suppliers while still agnostic to Block - Assigning vendors capabilities, tracking DOA rates, etc"
  - Vendor capability management foundation
- **SW-M-2**: "Ability for vendors to have multiple 'capabilities'"
  - Multiple capability matching
- **SW-M-3**: "Must be able to rank each vendor within a capability with a tier"
  - Tier-based selection
- **SW-M-4**: "Must be able to manage Customer Concession Vendors"
  - Concession vendor handling

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Steps W01-S06/S07 (Validate Vendor Capabilities)

**Technical Notes**:
- Use scoring algorithm for vendor ranking based on compatibility strength
- Implement caching for vendor compatibility configurations
- Vendor compatibility is manually maintained by Block admin (not auto-discovered)
- Consider different compatibility types: brand-specific (Phillips), modality-specific (MRI), universal (AllParts)
- Consider ML for improving matching over time based on win rates

---

#### S010: Create vendor selection interface with qualification filters

**Story ID**: S010
**Persona**: P01-Buyer
**Architecture Layer**: sw-frontend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F03-Vendor-Selection
**Priority**: P1 (High)
**Phase**: Phase 1
**Story Points**: 3

**Description**:
As a buyer, I want to see which vendors will receive my requisition and understand why they were selected (modality match, geographic coverage, past performance) so that I can have confidence in the distribution list. The interface should show vendor qualifications and allow filtering by various criteria.

**Acceptance Criteria**:
- Display selected vendors with match reasons
- Show vendor tier/ranking
- Display vendor response rate and on-time delivery metrics
- Filter by: Tier, Location, Certifications, Performance
- Sort by: Name, Tier, Match Score, Performance
- Show estimated number of vendors before submission
- Visual indicators for vendor status

**Traceability**:

**Requirements**:
- **SW-M-1**: "Ability to full manage suppliers while still agnostic to Block"
  - Vendor visibility and management

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S05 (Submit Request)

**Technical Notes**:
- Implement responsive grid for vendor display
- Use tooltips for detailed vendor information

---

#### S011: Build automatic distribution to qualified vendors

**Story ID**: S011
**Persona**: P01-Buyer (System Process)
**Architecture Layer**: sw-backend, external
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F03-Vendor-Selection
**Priority**: P0 (Critical)
**Phase**: Phase 1
**Story Points**: 5

**Description**:
As a buyer, I want my requisition automatically sent to all qualified vendors when I submit it so that I get maximum market coverage without manual effort. The system should send notifications immediately and track which vendors have received the request.

**Acceptance Criteria**:
- Send requisition to all selected vendors simultaneously
- Email notifications sent within 60 seconds
- Track delivery status per vendor
- Retry failed deliveries up to 3 times
- Log all distribution attempts
- Update requisition status to "Distributed"
- Show vendor count on requisition

**Traceability**:

**Requirements**:
- **SWP-M-15**: "Must auto-connect request with Vendor suppliers that have been accepted for that category"
  - Automatic distribution to qualified vendors

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S08 (Send Vendor Notifications)

**Technical Notes**:
- Use message queue for reliable delivery
- Implement batch processing for large vendor lists
- Track email open/click rates if possible

---

#### S012: Design manual vendor addition/removal capability

**Story ID**: S012
**Persona**: P01-Buyer
**Architecture Layer**: sw-frontend, sw-backend
**Epic**: E01-REQUEST-MANAGEMENT
**Feature**: F03-Vendor-Selection
**Priority**: P2 (Medium)
**Phase**: Phase 1
**Story Points**: 2

**Description**:
As a buyer, I want to manually add vendors I know can help or remove vendors I don't want to work with on a specific requisition so that I maintain control over my supplier relationships. These manual adjustments should be remembered for similar future requisitions.

**Acceptance Criteria**:
- Search and add vendors not auto-selected
- Remove auto-selected vendors with reason
- Save vendor preferences for future requisitions
- Override warnings for unqualified vendors
- Track manual adjustments for reporting
- Bulk select/deselect capabilities
- Remember last 10 manual adjustments

**Traceability**:

**Requirements**:
- Supports buyer control over vendor selection

**Workflows**:
- **W01**: Buyer Parts Request Workflow - Step W01-S05 (Submit Request)

**Technical Notes**:
- Store preferences at user and organization level
- Implement "vendor blacklist" capability
- Track reason codes for removals

---

## Implementation Roadmap

### Phase 1 Sprint Allocation
- **Sprint 1**: S001, S002 (Database and search foundation)
- **Sprint 2**: S003, S004, S005 (Part creation and request builder)
- **Sprint 3**: S006, S007, S008 (Request configuration and validation)
- **Sprint 4**: S009, S011 (Vendor matching and distribution)
- **Sprint 5**: S010, S012 (Vendor selection UI and manual controls)

### Technical Dependencies
- Parts database with fuzzy matching algorithms
- Raw part number normalization service
- Vendor capability matching engine
- Email notification system
- File attachment storage (S3 or equivalent)
- Message queue for reliable vendor notification

### Integration Points
- Salesforce 360 for existing material data import
- Email system for vendor notifications
- Third-party vendor APIs (All Parts, PartSource) for catalog enhancement
- EMA system for follow-up communications
- Virus scanning service for attachments

### Success Metrics
- Search success rate (target: >95% find correct part)
- Requisition creation time (target: <5 minutes)
- Vendor response rate (target: >80%)
- Duplicate material creation rate (target: <2%)
- Auto-vendor selection accuracy (target: >90%)
- System response time (target: <2 seconds for search)