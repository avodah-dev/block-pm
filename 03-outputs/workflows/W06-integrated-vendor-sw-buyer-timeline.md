# W06: Integrated Vendor - SW Buyer Timeline

## Input Sources
- **Image**: SW Buyer Timeline diagram
- **Voice Narration**: Team discussion on integrated vendor workflows
- **Created Date**: 2025-09-25

## Overview
- **Persona**: P03-integrated-vendor
- **Goal**: Act as middleman to fulfill SW buyer requests when lacking inventory
- **Trigger**: Receiving part request without having stock
- **Context**: Vendor becomes buyer to source from network

## Narrative Description

This workflow represents a sophisticated evolution in the Sourcing Window ecosystem - the birth of the integrated vendor. When a regular Sourcing Window buyer sends out a request for parts, it reaches their connected vendors, including what we call an "integrated vendor." This integrated vendor has special capabilities that transform them from a simple supplier into a network orchestrator.

The journey begins when the buyer creates their parts request, following the standard workflow we've already documented. The request flows out to all their connected vendors, but here's where things get interesting: one of those vendors is an integrated vendor (like Block Imaging in our example), and they don't have stock. In a traditional system, they'd simply decline or mark "no stock" and that would be the end of their participation. But not here.

The integrated vendor, upon realizing they don't have stock, makes a pivotal decision - they transform into a buyer themselves. They look at the original request and think, "I don't have this, but I know the network does." They immediately pivot to requesting pricing from THEIR vendors - the ones that weren't already connected to the original buyer. This is crucial: they're only reaching out to vendors the original buyer doesn't have access to, avoiding duplicate quotes and confusion.

Meanwhile, the regular connected vendors (the non-integrated ones) are submitting their pricing directly to the original buyer, following the standard vendor quote submission process. But the integrated vendor is playing a different game - they're aggregating quotes from the extended network.

As quotes come in from these third-party vendors, the integrated vendor reviews them carefully. They might negotiate, they might compare multiple options, they might consider shipping times and reliability. Once they've selected the best option (or options), they apply their markup - this is their value-add for orchestrating the transaction and taking on the coordination responsibility.

The integrated vendor then submits their marked-up quote to the original buyer, who now sees quotes from both their direct vendors AND the integrated vendor (representing the broader network). To the buyer, this looks like any other quote - they don't necessarily know that the integrated vendor is actually sourcing from elsewhere.

If the buyer selects the integrated vendor's quote and places the order, that's when the real magic happens. The integrated vendor receives the order but can't simply fulfill it from their warehouse - they need to cascade the order down to their selected vendor. They upload a purchase order to the third-party vendor for drop-shipping directly to the original buyer.

The third-party vendor then confirms the order and provides shipping details (tracking numbers, serial numbers, RMA information). Here's the elegant part: all of these confirmations and updates flow through the integrated vendor, who forwards them to the original buyer as if they were handling the shipment themselves. The buyer gets all their expected notifications - order confirmed, shipment tracking - without ever knowing the complexity happening behind the scenes.

There's a fascinating technical detail that emerged from the discussion: all of these related requests share a parent requisition ID. Each vendor has their own unique request ID, but they're all connected through this parent ID. The integrated vendor can see ALL related requests (giving them the network view), while the original buyer only sees requests from vendors they're directly connected to. This visibility control is what enables the integrated vendor model to work without creating confusion or revealing competitive information.

## Workflow Steps

### 📊 Step-to-Requirements Matrix

| Step ID | Step Name | Requirements | Workflow Reference | Notes |
|---------|-----------|--------------|-------------------|-------|
| W06-S01 | Buyer Creates Request | - | Reuse W01 | Complete workflow |
| W06-S02 | Integrated Vendor Decision | SW-M-33 | New | Check stock decision |
| W06-S03 | Create Extended Network Request | SW-M-34, SW-M-35 | Modified W01 | As buyer role |
| W06-S04 | Network Vendors Quote | SW-M-36 | Reuse W03 | Standard process |
| W06-S05 | Review & Markup | SW-M-37, SW-M-38 | Modified W02 | Add markup step |
| W06-S06 | Submit to Original Buyer | SW-M-39 | Modified W03 | Submit marked quote |
| W06-S07 | Buyer Selection Process | - | Reuse W02 | Complete workflow |
| W06-S08 | Integrated Vendor Purchases | SW-M-40, SW-M-41 | Modified W02 | Create drop-ship PO |
| W06-S09 | Third-Party Fulfillment | SW-M-42 | Reuse W05 | Drop-ship variant |
| W06-S10 | Forward Updates | SW-M-43 | New | Pass-through comms |

## Detailed Step Descriptions

### W06-S01: Buyer Creates Request 🔄
- **Completely Reuses**: W01-buyer-parts-request
- **Key Output**: Parent requisition ID created
- **Integrated Vendor Role**: Receives as connected vendor
- **Next**: W06-S02

### W06-S02: Integrated Vendor Decision 🔍
- **NEW STEP - Unique to Integrated Vendor**
- **Actor**: Integrated Vendor
- **Decision**: Has stock?
  - Yes → Reuse W03-vendor-submit-quote (standard flow)
  - No → W06-S03 (become buyer)
- **Transformation**: Vendor role → Buyer role

### W06-S03: Create Extended Network Request 🌐
- **Partially Reuses**: W01-buyer-parts-request
- **Actor**: Integrated Vendor (as Buyer)
- **Key Differences**:
  - Request only to non-connected vendors
  - Child requisition linked to parent
  - Inherited part details from original request
- **Next**: W06-S04

### W06-S04: Network Vendors Quote 💰
- **Completely Reuses**: W03-vendor-submit-quote
- **No modifications**: Standard vendor response process
- **Quotes sent to**: Integrated Vendor (as buyer)
- **Next**: W06-S05

### W06-S05: Review & Markup 📊
- **Partially Reuses**: W02-review-select-vendor (review portion only)
- **Actor**: Integrated Vendor
- **Additional Steps**:
  - Calculate markup percentage
  - Prepare consolidated quote
- **Does NOT purchase yet**: Only price discovery
- **Next**: W06-S06

### W06-S06: Submit to Original Buyer 📨
- **Partially Reuses**: W03-vendor-submit-quote
- **Actor**: Integrated Vendor (back as Vendor)
- **Key Difference**: Price includes markup
- **Appearance**: Standard vendor quote to buyer
- **Next**: W06-S07

### W06-S07: Buyer Selection Process 👀
- **Completely Reuses**: W02-review-select-vendor
- **Actor**: Original Buyer
- **No modifications**: Standard selection process
- **Outcome**: May select integrated vendor
- **Next**: W06-S08 (if integrated vendor selected)

### W06-S08: Integrated Vendor Purchases ✅
- **Partially Reuses**: W02-review-select-vendor (purchase portion)
- **Actor**: Integrated Vendor (as Buyer)
- **Key Differences**:
  - Creates drop-ship PO
  - Specifies original buyer's address
  - Links to parent order
- **Next**: W06-S09

### W06-S09: Third-Party Fulfillment 📦
- **Completely Reuses**: W05-vendor-confirmation-shipping
- **Actor**: Third-Party Vendor
- **Key Difference**: Ships to original buyer address
- **All standard steps apply**: Confirmation, tracking, etc.
- **Next**: W06-S10

### W06-S10: Forward Updates 📧
- **NEW STEP - Unique to Integrated Vendor**
- **Actor**: Integrated Vendor
- **Type**: Pass-through relay
- **Actions**:
  - Receive updates from third-party vendor
  - Forward to original buyer unchanged
  - Maintain audit trail
- **End State**: Seamless experience for buyer

## System Architecture Considerations

### Visibility Model
```
Parent Requisition ID
├── Original Buyer (sees only connected vendors)
│   ├── Connected Vendor 1 Quote
│   ├── Connected Vendor 2 Quote
│   └── Integrated Vendor Quote (marked up)
└── Integrated Vendor View (sees all)
    ├── All connected vendor quotes
    └── Extended network quotes
```

### Data Relationships
- **Parent Requisition ID**: Links all related requests
- **Visibility Rules**:
  - Buyer: Only sees vendors with `connected_to_buyer: true`
  - Integrated Vendor: Sees entire parent requisition tree
  - Network Vendors: Only see their specific request

### Business Logic Layer
- **Sourcing Window**: Core marketplace functionality
- **Integration Layer**: Handles Salesforce synchronization
- **Key Functions**:
  - Vendor-to-buyer role switching
  - Quote markup calculation
  - Drop-ship orchestration
  - Update forwarding

## Edge Cases & Considerations

### Multiple Integrated Vendors
- **Scenario**: Multiple integrated vendors in same request
- **Solution**: Each operates independently with own network
- **Result**: Maximum network coverage for buyer

### Markup Transparency
- **Current**: Buyer doesn't see markup or source
- **Consideration**: Future transparency options?

### Drop-Ship Failures
- **Risk**: Third-party vendor fails to deliver
- **Mitigation**: Integrated vendor remains responsible
- **Communication**: All issues flow through integrated vendor

## Requirements Coverage

### ✅ New Requirements Introduced
- SW-M-33 through SW-M-43: Integrated vendor capabilities
- Parent/child requisition relationships
- Network visibility controls
- Markup and margin management
- Drop-ship orchestration

### 🔄 Integration Points
- Builds on W01 (buyer request)
- Builds on W02 (review quotes)
- Builds on W03 (vendor quote)
- Builds on W05 (fulfillment)

## Success Metrics
- Network utilization rate
- Markup optimization
- Drop-ship success rate
- End-to-end fulfillment time
- Buyer satisfaction with expanded options

## Future Enhancements
- Automated markup strategies
- Multi-tier integrated vendor chains
- Real-time inventory visibility
- Direct integration with logistics providers
- Transparency options for sophisticated buyers