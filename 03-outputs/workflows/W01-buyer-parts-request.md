# W01: Buyer Parts Request Workflow

## Overview
- **Persona**: P01-buyer
- **Goal**: Request parts/materials from qualified vendors
- **Trigger**: "I Need A Part"
- **Estimated Duration**: 5-10 minutes

## Workflow Steps

### 📊 Step-to-Requirements Matrix

| Step ID | Step Name | Requirements Addressed | Type |
|---------|-----------|----------------------|------|
| W01-S01 | Initiate Request | - | User Action |
| W01-S02 | Search for Part | SWP-M-10 | User Action |
| W01-S02a | Create New Part (Alternative) | SWP-M-12 | User Action |
| W01-S03 | Select Part | - | User Action |
| W01-S04 | Finalize Request Details | SWP-M-11, SWP-M-13, SWP-M-14 | User Action |
| W01-S05 | Submit Request | SWP-M-15 | User Action |
| W01-S06 | Validate Vendor Capabilities | SWP-M-15, SW-M-1, SW-M-2 | System Process |
| W01-S07 | Check Modality & Manufacturer | SW-M-3, SW-M-4 | System Process |
| W01-S08 | Send Vendor Notifications | SWP-M-16, SW-M-39 | System Process |
| W01-S09 | Complete Workflow | - | End State |

## Detailed Step Descriptions

### W01-S01: Initiate Request
- **Actions**: Click 'Select Create' button
- **Next**: W01-S02

### W01-S02: Search for Part 🔍
- **Actions**: Enter search criteria, view results
- **Resources**: Parts/Material List database
- **Decision Point**:
  - Part found → W01-S03
  - Part not found → W01-S02a

### W01-S02a: Create New Part ➕
- **Data Inputs**:
  - Modality (required)
  - Manufacturer (required)
  - Part number (required)
  - Description (required)
  - System (optional)
- **Resources**: Parts/Material List database
- **Next**: W01-S03

### W01-S03: Select Part ✓
- **Actions**: Click part from list, confirm selection
- **Next**: W01-S04

### W01-S04: Finalize Request Details 📝
- **Data Inputs**:
  - Quantity (required)
  - Note (optional)
  - Customer reference number (optional)
- **Next**: W01-S05

### W01-S05: Submit Request 🚀
- **Validations**: Required fields, quantity > 0
- **Next**: W01-S06

### W01-S06: Validate Vendor Capabilities 🔄
- **Type**: System Automated
- **Resources**:
  - Vendor Capability database
  - User vendor list
- **Next**: W01-S07

### W01-S07: Check Modality & Manufacturer 🔍
- **Type**: System Automated
- **Checks**: Modality match, manufacturer authorization
- **Resources**: Vendor Capability database
- **Next**: W01-S08

### W01-S08: Send Vendor Notifications 📧
- **Type**: System Automated (Parallel)
- **Actions**:
  - Generate vendor opportunity records
  - Send email notifications
- **Resources**: Email system, Vendor Opportunity records
- **Next**: W01-S09

### W01-S09: Complete Workflow ✅
- **Actions**: Display confirmation, provide tracking number
- **End State**: Request submitted successfully

## Requirements Coverage Analysis

### ✅ Fully Addressed (12)
- **Part Search**: SWP-M-10 (Search PN or description)
- **Part Creation**: SWP-M-12 (Create new Material)
- **Request Details**: SWP-M-11 (Notes), SWP-M-13 (Multiple req items), SWP-M-14 (Customer ref number)
- **Vendor Connection**: SWP-M-15 (Auto-connect to vendors), SWP-M-16 (Email notification to vendor)
- **Vendor Management**: SW-M-1 (Manage suppliers), SW-M-2 (Vendor capabilities)
- **Vendor Matching**: SW-M-3 (Vendor tiers), SW-M-4 (Customer concession vendors)
- **Vendor Notification**: SW-M-39 (Email notification for new request)

### 📝 Notes
- Requirements updated after CAD file regeneration from cleaned CSV data
- Some UI/display requirements (e.g., homepage layouts) don't map to workflow steps
- System requirements for vendor management are referenced but full implementation is in other workflows

## Resources Used

### Databases
- **Parts/Material List**: Part search and creation
- **Vendor Capability**: Vendor matching and qualification

### Systems
- **Email System**: Vendor notifications
- **Vendor Opportunity**: Tracking vendor opportunities

## Implementation Considerations

### Features Needed
1. **Part Search & Management** (W01-S02, W01-S02a, W01-S03)
2. **Request Builder** (W01-S04, W01-S05)
3. **Vendor Matching Engine** (W01-S06, W01-S07)
4. **Notification System** (W01-S08)
5. **Request Tracking** (W01-S09)

### Potential Gaps
- Error handling for no qualified vendors
- Approval workflow integration (if budget thresholds apply)
- Vendor response tracking (post-notification)

## Success Metrics
- Request creation time < 10 minutes
- Vendor notification time < 1 minute after submission
- Zero missed qualified vendors
- 100% tracking number generation