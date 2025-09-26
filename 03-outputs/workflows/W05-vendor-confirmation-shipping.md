# W05: Vendor Confirmation & Shipping Workflow

## Input Sources
- **Image**: vendor-confirmation-shipping-diagram.png
- **Voice Narration**: Team discussion on vendor fulfillment process
- **Created Date**: 2025-09-24

## Overview
- **Persona**: P02-vendor
- **Goal**: Confirm orders and ship parts to buyers
- **Trigger**: "I won, now I need to ship!"
- **Estimated Duration**: 5-15 minutes (excluding physical fulfillment)

## Narrative Description

The vendor has just received great news - their quote was selected! Now comes the critical part: actually fulfilling the order. This workflow represents the vendor's journey from winning a bid to successfully shipping the part.

The vendor typically learns about their win through two channels: an email notification (the fastest way) or by checking their dashboard's "Pending Fulfillment" section, which shows all orders where buyers selected them. Speed matters here - buyers are waiting for confirmation that their order is in good hands.

The first decision point is whether to immediately confirm the order. This confirmation serves as a handshake - "Yes, we got it, we're on it." It immediately updates the system to show the transaction has been acknowledged by both parties and triggers an email to the buyer. This simple step reduces buyer anxiety and establishes trust.

But here's where it gets interesting: not all vendors work the same way. Some vendors have parts readily available and can pull and pack quickly. Others might need to order from their suppliers or have longer processing times. The system accommodates both approaches:

**Path 1 - Quick Fulfillment**: For vendors with readily available inventory, they can skip the separate confirmation step and jump straight to fulfillment. When they complete the fulfillment details (tracking, serial, RMA), the system automatically confirms the order AND marks it as shipped in one action, sending a single comprehensive email to the buyer.

**Path 2 - Two-Step Process**: For vendors needing more time, they first confirm the order (buyer gets a "we're working on it" email), then download the PO, physically pull and pack the part in their warehouse, and return later to complete the fulfillment details.

There's also a critical **Path 3 - Cancellation**: Sometimes things go wrong. The vendor discovers they don't actually have the part they thought they had, or it's damaged, or there's another issue. Currently, vendors have to message buyers asking them to cancel - a friction point. The new system adds a "Cancel Order" button, allowing vendors to proactively cancel with an explanation, automatically notifying the buyer to select their second choice. This is new functionality that significantly improves the experience for both parties.

The fulfillment process itself requires specific information:
- **Tracking Number** (always required): For shipment tracking
- **Serial Number** (sometimes required): For certain types of parts
- **RMA Number** (always required, possibly multiple): For returns processing

Once all information is entered and the vendor clicks "Finish Order," the system sends a comprehensive "Part Shipped" email to the buyer with all tracking information. The order moves to shipped status, and the vendor's obligation is complete.

An important design consideration emerged during discussion: the flexibility in the confirmation flow. As Jake explained, "You don't have to confirm an order" separately - the system is smart enough to handle both workflows. If a vendor goes straight to fulfillment without confirming first, the system performs both actions but only sends one email to avoid notification fatigue.

This workflow directly impacts buyer satisfaction. Quick confirmations reduce anxiety, cancellation capabilities prevent delays, and accurate shipping information ensures smooth delivery. The vendor's efficiency here directly affects their reputation and likelihood of winning future bids.

## Workflow Steps

### 📊 Step-to-Requirements Matrix

| Step ID | Step Name | Requirements Addressed | Type |
|---------|-----------|----------------------|------|
| W05-S01a | Access via Dashboard | SW-M-22 | User Action |
| W05-S01b | Access via Email | SW-M-23 | User Action |
| W05-S02 | View Pending Orders | SW-M-24 | User Action |
| W05-S03 | Confirm Order (Optional) | SW-M-25 | User Action |
| W05-S04 | Download PO | SW-M-26 | User Action |
| W05-S05 | Pull & Pack (External) | - | External Process |
| W05-S06 | Enter Fulfillment Details | SW-M-27, SW-M-28 | User Action |
| W05-S07 | Complete Order | SW-M-29 | User Action |
| W05-S08 | Send Shipping Email | SW-M-30 | System Process |
| W05-S09 | Cancel Order (Alternative) | SW-M-31 | User Action |

## Detailed Step Descriptions

### W05-S01a: Access via Dashboard
- **Actions**: Navigate to Dashboard → Pending Fulfillment section
- **UI Elements**: Dashboard with pending orders list
- **Next**: W05-S02

### W05-S01b: Access via Email
- **Actions**: Click link in order won notification
- **UI Elements**: Email with direct link
- **Next**: W05-S02

### W05-S02: View Pending Orders
- **Description**: See list of orders where this vendor was selected
- **Data Displayed**: Order details, buyer info, part requirements
- **Decision Point**:
  - Confirm first → W05-S03
  - Straight to fulfill → W05-S04
  - Can't fulfill → W05-S09

### W05-S03: Confirm Order (Optional)
- **Actions**: Click "Confirm Order" button
- **Impact**: Updates status to "confirmed by vendor"
- **Automated**: Email sent to buyer "Order Confirmed"
- **Business Value**: Reduces buyer anxiety, shows responsiveness
- **Next**: W05-S04

### W05-S04: Download PO
- **Actions**: Download purchase order document
- **Purpose**: Get official order details for warehouse
- **Next**: W05-S05

### W05-S05: Pull & Pack Part (External)
- **Description**: Physical warehouse activities
- **Not in System**: Happens in vendor's facility
- **Duration**: Variable (minutes to days)
- **Next**: W05-S06

### W05-S06: Enter Fulfillment Details 📦
- **Actions**: Enter shipping information
- **Required Fields**:
  - Tracking Number (always)
  - Serial Number (conditional)
  - RMA Number (always, may be multiple)
- **Optional**: Message to buyer
- **Validation**: All required fields must be filled
- **Next**: W05-S07

### W05-S07: Complete Order ✅
- **Actions**: Click "Finish Order" button
- **System Actions**:
  - If not confirmed: Confirms order automatically
  - Marks as shipped
  - Updates all statuses
- **Next**: W05-S08

### W05-S08: Send Shipping Email 📧
- **Type**: System Automated
- **Content**: Part shipped notification with:
  - Tracking information
  - Serial numbers
  - RMA numbers
  - Expected delivery
- **End State**: Order complete, vendor obligation fulfilled

### W05-S09: Cancel Order (Alternative Path) ❌
- **NEW FUNCTIONALITY**: Not in current system
- **Actions**: Click "Cancel Order" button
- **Required**: Cancellation reason
- **Impact**:
  - Order marked as cancelled
  - Email sent to buyer
  - Buyer prompted to select alternative
- **Business Value**: Prevents delays, improves communication
- **End State**: Order cancelled

## Decision Flow Logic

```
Start → View Orders → Decision:
├─ Can fulfill quickly? → Skip confirm → Fulfill → Ship
├─ Need time? → Confirm → Download PO → Pack → Fulfill → Ship
└─ Can't fulfill? → Cancel → Notify buyer
```

## Key Business Rules

1. **Confirmation is Optional**: System handles single or two-step process
2. **Email Consolidation**: If skipping confirmation, only one email sent
3. **Cancellation Authority**: NEW - Vendors can now cancel directly
4. **Required Information**: Tracking always, Serial conditional, RMA always

## Requirements Coverage

### ✅ Fully Addressed
- SW-M-22 through SW-M-31: Complete fulfillment process

### 🆕 New Functionality
- Vendor-initiated cancellation (not in original requirements)
- Flexible confirmation flow
- Consolidated email option

## Success Metrics
- Confirmation time < 2 hours from order won
- Shipping information accuracy 100%
- Cancellation communication < 30 minutes
- Email delivery success > 99%

## Integration Points
- **W02**: Orders come from buyer selection
- **W04**: Messaging available throughout
- **Future**: Shipping provider integrations