# W02: Review and Select Vendor Workflow

## Overview
- **Persona**: P01-buyer
- **Goal**: Review vendor quotes and purchase parts
- **Trigger**: "I need to review my quotes and buy a part"
- **Estimated Duration**: 10-20 minutes

## Workflow Steps

### 📊 Step-to-Requirements Matrix

| Step ID | Step Name | Requirements Addressed | Type |
|---------|-----------|----------------------|------|
| W02-S01 | Access Dashboard | SWP-M-19 | User Action |
| W02-S02 | Select Request | SWP-M-20 | User Action |
| W02-S03 | Access Vendor Response | SWP-M-21 | User Action |
| W02-S04 | View Request Details | SWP-M-22, SWP-M-23 | User Action |
| W02-S05 | Apply Filters (Optional) | SWP-M-24 | User Action |
| W02-S06 | Review Quote Details | SWP-M-23, SW-M-24 | User Action |
| W02-S07 | Add to Cart and Select | SWP-M-25, SWP-M-26 | User Action |
| W02-S08 | Handle Unfulfilled Items | SWP-M-27 | User Action |
| W02-S09 | Proceed to Checkout | SWP-M-28, SWP-M-29, SWP-M-30 | User Action |
| W02-S10 | Submit Purchase Order | SWP-M-31 | User Action |
| W02-S11 | Purchase Additional Quotes | SWP-M-32 | User Action |
| W02-S12 | Cancel Remaining Balance | SWP-M-33 | User Action |
| W02-S13 | Create Vendor Order | SW-M-7, SW-M-8 | System Process |
| W02-S14 | Await Confirmation | SWP-M-34 | End State |
| W02-S15 | Messaging (Parallel) | SWP-M-35 | User Action |

## Detailed Flow Description

### Main Path
1. **Dashboard Entry** → Select Request → Click vendor response link
2. **Review Phase**: View request overview with quotes and part details
3. **Selection Phase**: Review vendor quotes → Add to cart → Select conditions
4. **Checkout Phase**: Upload PO/Enter PO# → Submit PO
5. **Completion**: System creates vendor order → Email vendor → Confirmation

### Decision Points
- **W02-S10**: After submitting PO
  - Purchase more quotes → Return to W02-S06
  - Complete purchase → Continue to completion
- **W02-S08**: If unfulfilled quantities exist
  - Return to find other vendors

### Optional/Parallel Features
- **Filtering** (W02-S05): Apply "Applies to Apples" view
- **Messaging** (W02-S15): Available throughout workflow
- **Cancel Balance** (W02-S12): Cancel remaining unfulfilled quantities

## Key UI Components

### Legend Elements (from diagram)
- **Persona** (Purple)
- **Data Source** (Grey border)
- **User Screen/Focus** (Green)
- **User Action** (Yellow)
- **Automated Action** (Orange)
- **Input** (White)
- **Component** (Black)

## Requirements Coverage Analysis

### ✅ Fully Addressed (20 requirements)
- **Quote Review**: SWP-M-19 through SWP-M-24
- **Cart & Selection**: SWP-M-25 through SWP-M-27
- **Checkout Process**: SWP-M-28 through SWP-M-31
- **Order Management**: SWP-M-32 through SWP-M-35
- **Vendor Side**: SW-M-7, SW-M-8, SW-M-24

## Implementation Considerations

### Features Needed
1. **Dashboard & Request Management** (W02-S01, W02-S02)
2. **Quote Review Interface** (W02-S04, W02-S05, W02-S06)
3. **Shopping Cart** (W02-S07, W02-S08)
4. **Checkout & PO Management** (W02-S09, W02-S10)
5. **Order Processing** (W02-S13)
6. **Messaging System** (W02-S15)

### Data Flow
- Request Database → Quote Details → Cart → Purchase Order → Vendor Order
- Email notifications at vendor order creation
- Real-time messaging capability

### Validation Points
- PO Document OR PO Number required (not both)
- Quantity availability checks
- Condition selection validation

## Success Metrics
- Quote review to purchase time < 20 minutes
- Cart abandonment rate < 10%
- PO submission success rate > 95%
- Vendor notification time < 1 minute