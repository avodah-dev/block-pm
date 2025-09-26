# E01-REQUEST-MANAGEMENT: Buyer Parts Request Creation and Management

## Epic Overview
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Core Functionality
**Primary Persona**: P01-Buyer (Procurement Buyer)
**Requirements Coverage**: SWP-M-10, SWP-M-11, SWP-M-12, SWP-M-13, SWP-M-14, SWP-M-15, SW-M-1, SW-M-2, SW-M-3, SW-M-4, SW-S-3, and discovery insights

This epic encompasses the complete buyer workflow for creating and managing parts requisitions in Sourcing Window Pro (SWP). It provides the foundation for buyers to search the parts/materials database, create new materials when needed, configure multi-part requisitions with special instructions, and distribute requests to qualified vendors based on their capabilities. This is the entry point for all procurement activity and directly addresses Block's need for intuitive part searching with fuzzy matching and raw part number normalization - critical since 85-90% of searches use part numbers.

The epic solves the current pain point where "search function sucks" leading to duplicate materials in the database. It implements Block's "super top secret" raw part number formula that removes dashes and trims leading zeros, allowing buyers to find parts regardless of formatting variations (e.g., 4535-619-90892 vs 453561990892).

---

## Feature F01: Parts Database Search and Management

### Feature Summary
This feature provides the core search and material management capabilities that buyers need to find and select parts for requisitions. It implements fuzzy matching to handle the various ways part numbers are formatted across different vendors and manufacturers, addressing Block's critical need where 85-90% of all searches are by part number. The feature also enables creation of new materials when parts aren't found in the existing database, with required fields for modality, manufacturer, part number, and description to maintain data quality.

The search functionality goes beyond simple text matching to include normalization algorithms that handle Block's hyphenated format versus other vendors' formats, preventing the duplicate material problem that plagues the current system. Users can view detailed part specifications including compatibility relationships (understanding that part A may replace B, but B might not replace A), modality tags, and images to ensure they're selecting the correct item.

### User Stories

#### S001: Implement parts search with fuzzy matching and raw part number normalization
As a buyer, I want to search for parts using partial or differently formatted part numbers so that I can find what I need regardless of how vendors format their part numbers. The system should apply Block's raw part number normalization (removing dashes, trimming zeros) automatically and suggest close matches when exact matches aren't found.

#### S002: Create parts database with modality and compatibility tracking
As a buyer, I want to see which equipment types (modalities like CT, MRI, X-ray) a part works with and understand compatibility relationships between parts so that I can ensure I'm ordering the correct replacement. The database should clearly show when compatibility is directional (Part A replaces B, but B doesn't replace A).

#### S003: Build part creation form for new materials not in database
As a buyer, I want to create new material entries when I can't find a part in the system so that I can still submit my requisition and build the database for future use. The form should require modality, manufacturer, part number, and description as mandatory fields while allowing optional fields like system information.

#### S004: Implement part details view with specifications and images
As a buyer, I want to view comprehensive details about a part including specifications, images, compatibility information, and historical pricing so that I can verify I'm selecting the correct item before adding it to my requisition.

---

## Feature F02: Request Creation and Configuration

### Feature Summary
This feature enables buyers to build complex, multi-part requisitions with all the configuration options needed for effective procurement. It supports Block's requirement that "multiple requests on one Requisition" while maintaining individual line item tracking for each part. Buyers can specify quantities, urgency levels, and add special instructions that help vendors understand specific needs or requirements for the order.

The feature includes attachment capabilities for supporting documentation like specifications or drawings, and implements a customer reference number field that helps buyers track requisitions back to their internal systems or service requests. The validation logic ensures all required information is captured before submission, preventing incomplete requests that would delay the procurement process.

### User Stories

#### S005: Design multi-part request builder interface
As a buyer, I want to add multiple parts to a single requisition with individual quantity and configuration for each line item so that I can efficiently request everything needed for a job in one submission. The interface should show all items in the requisition with the ability to modify or remove individual lines.

#### S006: Implement quantity and urgency specification
As a buyer, I want to specify the quantity needed for each part and indicate the urgency level (routine, urgent, emergency) so that vendors understand my timeline requirements and can prioritize their responses accordingly.

#### S007: Create special instructions and attachment capability
As a buyer, I want to add special instructions to my requisition and attach relevant documents (specifications, drawings, photos) so that vendors have all the context they need to provide accurate quotes. The system should support common file formats with reasonable size limits.

#### S008: Build request validation and submission logic
As a buyer, I want the system to validate my requisition for completeness and required fields before submission so that I don't accidentally send incomplete requests to vendors. The validation should check for required fields, valid quantities, and ensure at least one part is included.

---

## Feature F03: Vendor Selection and Distribution

### Feature Summary
This feature implements the intelligent vendor matching and distribution system that ensures requisitions reach the right suppliers based on their declared capabilities. It uses vendor-declared modality support, geographic coverage, and specialty certifications to automatically identify qualified vendors for each requisition. This addresses Block's requirement for "auto-connect to vendors by capability" while maintaining flexibility for manual vendor management.

The system performs real-time validation against vendor capabilities, checking not just part availability but also modality expertise, manufacturer relationships, and service territories. Buyers retain control with the ability to manually add vendors they know can fulfill the request or remove vendors they don't want to work with, supporting both automated efficiency and buyer judgment.

### User Stories

#### S009: Implement vendor capability matching algorithm
As a buyer, I want the system to automatically identify vendors who have declared capability for the parts and modalities in my requisition so that I don't have to manually select vendors for every request. The algorithm should consider part type, modality, manufacturer relationships, and any specialty requirements.

#### S010: Create vendor selection interface with qualification filters
As a buyer, I want to see which vendors will receive my requisition and understand why they were selected (modality match, geographic coverage, past performance) so that I can have confidence in the distribution list. The interface should show vendor qualifications and allow filtering by various criteria.

#### S011: Build automatic distribution to qualified vendors
As a buyer, I want my requisition automatically sent to all qualified vendors when I submit it so that I get maximum market coverage without manual effort. The system should send notifications immediately and track which vendors have received the request.

#### S012: Design manual vendor addition/removal capability
As a buyer, I want to manually add vendors I know can help or remove vendors I don't want to work with on a specific requisition so that I maintain control over my supplier relationships. These manual adjustments should be remembered for similar future requisitions.

---

## Implementation Considerations

### Technical Dependencies
- Parts database with fuzzy matching algorithms
- Raw part number normalization service
- Vendor capability matching engine
- Email notification system
- File attachment storage

### Integration Points
- Salesforce 360 for existing material data
- Email system for vendor notifications
- Third-party vendor APIs (All Parts, PartSource) for catalog data
- EMA system for follow-up communications

### Success Metrics
- Search success rate (target: >95% find correct part)
- Requisition creation time (target: <5 minutes)
- Vendor response rate (target: >80%)
- Duplicate material creation rate (target: <2%)