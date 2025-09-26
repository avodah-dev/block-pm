# W07: Integrated Vendor - Non-SW Buyer Timeline

## Input Sources
- **Image**: Non-SW Buyer Timeline diagram
- **Voice Narration**: Team discussion on phone/email order handling
- **Created Date**: 2025-09-25

## Overview
- **Persona**: P03-integrated-vendor
- **Goal**: Fulfill phone/email orders through SW network when lacking inventory
- **Trigger**: Phone call or email request from non-SW buyer
- **Context**: Business system (Salesforce) to Sourcing Window integration

## Narrative Description

This workflow captures a critical reality of the integrated vendor's world: not all buyers use Sourcing Window. Many orders still come in the old-fashioned way - a phone call from a long-time customer, an urgent email from a hospital needing a part immediately. The integrated vendor must bridge two worlds: their traditional business operations in Salesforce and the modern marketplace capabilities of Sourcing Window.

The journey begins when a buyer (let's say Detroit Medical) calls the integrated vendor directly. This isn't a Sourcing Window request - it's a traditional phone order. The integrated vendor's sales rep takes the call, enters the details into Salesforce (their system of record for accounting and order management), and the system automatically checks inventory.

Here's the inflection point: if they have stock, this stays entirely in their traditional flow - Salesforce handles everything, the part ships from their warehouse, and Sourcing Window never knows this transaction happened. But when they don't have stock, that's when the integration magic needs to happen.

The discussion between the team members revealed a fundamental tension here. There's a desire for automation - Salesforce firing off an event to Sourcing Window saying "I need this part" - but there's also the reality of human behavior and system boundaries. The pragmatic approach that emerged: when the integrated vendor doesn't have stock, they manually open Sourcing Window and create a buyer request for that part.

This is a crucial behavioral shift. Instead of making phone calls to their vendor network (the old way), they're now using Sourcing Window as their sourcing tool. They enter the part request in Sourcing Window, which then broadcasts it to their entire vendor network - all the vendors they're connected to as a buyer.

The vendors respond with quotes through Sourcing Window (following the standard W03 vendor quote workflow). The integrated vendor reviews these quotes in Sourcing Window, selects the best option, applies their markup, and then - here's where the systems converge again - they enter that marked-up price back into their Salesforce quote for the original customer.

An important operational detail emerged in the discussion: the challenge of team coordination. If you have a team of 10 people, how do you know who's working on what? The current state involves email notifications going to a shared inbox, with team members needing to coordinate ("Is Andy handling this one?"). This highlights a gap between the single-user mental model of Sourcing Window and the team-based reality of many vendor operations.

The workflow continues with the integrated vendor purchasing through Sourcing Window, then managing the drop-ship process. But there's a critical difference from W06: the shipping destination. Since this is their direct customer (not a Sourcing Window buyer), they need to ensure the third-party vendor ships to THEIR customer's address, not to them.

The architectural discussion revealed deeper questions about system boundaries. Should everything flow through Sourcing Window? Should there be automated synchronization between Salesforce and Sourcing Window? The answer isn't just technical - it's about business process and change management. As one team member noted, these vendors are used to seeing everything in "one view" in Salesforce. Asking them to monitor two systems is a behavioral change.

The consensus that emerged: Sourcing Window is a "power tool" for accessing the vendor network. Salesforce remains the system of record for the business. A business logic layer can bridge between them, handling callbacks, status updates, and data synchronization. But fundamentally, if you want to access the network of vendors, you use Sourcing Window. If you're managing your business operations, you use Salesforce.

## Workflow Steps

### 📊 Step-to-Requirements Matrix

| Step ID | Step Name | Requirements Addressed | System | Reference |
|---------|-----------|----------------------|---------|-----------|
| W07-S01 | Receive Phone/Email Order | SW-M-44 | External | New |
| W07-S02 | Enter in Business System | SW-M-45 | Salesforce | New |
| W07-S03 | Check Internal Inventory | SW-M-46 | Salesforce | New |
| W07-S04 | Create SW Buyer Request | SW-M-47 | Sourcing Window | Modified W01 |
| W07-S05 | Vendors Submit Quotes | - | Sourcing Window | Reuse W03 |
| W07-S06 | Review & Select Quote | SW-M-48 | Sourcing Window | Modified W02 |
| W07-S07 | Mark Up & Quote Customer | SW-M-49 | Salesforce | New |
| W07-S08 | Customer Accepts | SW-M-50 | External | New |
| W07-S09 | Purchase from Vendor | SW-M-51 | Sourcing Window | Reuse W02 |
| W07-S10 | Manage Drop-Ship | - | Both Systems | Reuse W05 |

## Detailed Step Descriptions

### W07-S01: Receive Phone/Email Order 📞
- **Channel**: Phone call or email (non-SW)
- **Actor**: Non-SW Buyer (e.g., Detroit Medical)
- **Creates**: Traditional order request
- **Next**: W07-S02

### W07-S02: Enter in Business System 💼
- **System**: Salesforce
- **Actor**: Integrated Vendor sales rep
- **Actions**:
  - Create opportunity/quote in Salesforce
  - Enter part details, quantity, customer info
- **Next**: W07-S03

### W07-S03: Check Internal Inventory 🔍
- **System**: Salesforce (automatic)
- **Decision Point**: Have stock?
  - Yes → Traditional Salesforce fulfillment (END - no SW involvement)
  - No → W07-S04
- **Business Rule**: Only involve SW when sourcing needed

### W07-S04: Create SW Buyer Request 🔄
- **System Transition**: Salesforce → Sourcing Window
- **Actor**: Integrated Vendor (as Buyer)
- **Key Difference from W01**:
  - Not initiated by SW buyer
  - Triggered by external demand
  - Must note actual delivery address (end customer)
- **Reuses**: Core W01 request creation process
- **Next**: W07-S05

### W07-S05: Vendors Submit Quotes 📨
- **System**: Sourcing Window
- **Completely Reuses**: W03-vendor-submit-quote workflow
- **No modifications needed**: Standard vendor response process
- **Next**: W07-S06

### W07-S06: Review & Select Quote 👀
- **System**: Sourcing Window
- **Actor**: Integrated Vendor
- **Partially Reuses**: W02-review-select-vendor
- **Key Difference**:
  - Not making final purchase yet
  - Gathering pricing for customer quote
- **Actions**: Review quotes, potentially negotiate
- **Next**: W07-S07

### W07-S07: Mark Up & Quote Customer 💰
- **System Transition**: Sourcing Window → Salesforce
- **Actor**: Integrated Vendor
- **Actions**:
  - Take selected SW quote price
  - Apply markup
  - Update Salesforce quote for original customer
  - Send quote to customer (email/phone)
- **Business Logic**: Markup strategy and margin management
- **Next**: W07-S08

### W07-S08: Customer Accepts 📝
- **Channel**: Phone/email confirmation
- **Actor**: Original customer
- **Creates**: Confirmed order in Salesforce
- **Next**: W07-S09

### W07-S09: Purchase from Vendor ✅
- **System**: Sourcing Window
- **Completely Reuses**: W02 selection and purchase steps
- **Actor**: Integrated Vendor (as Buyer)
- **Critical Note**: Specify customer's shipping address
- **Next**: W07-S10

### W07-S10: Manage Drop-Ship 📦
- **System**: Both (coordination required)
- **Completely Reuses**: W05-vendor-confirmation-shipping
- **Key Difference**:
  - Ship-to address is end customer
  - Updates may need to sync to Salesforce
- **End State**: Part delivered to end customer

## System Architecture & Integration Points

### Dual-System Reality
```
Phone/Email Order
    ↓
Salesforce (System of Record)
    ↓ [No Stock]
Manual Transition → Sourcing Window (Sourcing Tool)
    ↓
Network Sourcing
    ↓
Price Discovery → Back to Salesforce
    ↓
Customer Quote/Order
    ↓
Return to SW → Execute Purchase
    ↓
Drop-Ship Management (Both Systems)
```

### Business Logic Layer Opportunities

#### Current State (Manual)
- User opens two tabs
- Manually transfers information
- Monitors two inboxes
- Manual status synchronization

#### Future State (Automated)
- API callbacks for status updates
- Automatic quote synchronization
- Unified monitoring dashboard
- Event-driven updates between systems

### Key Integration Points
1. **Inventory Check**: Salesforce → Decision point
2. **Quote Transfer**: SW quote → Salesforce markup
3. **Order Execution**: Salesforce order → SW purchase
4. **Status Updates**: SW fulfillment → Salesforce visibility

## Operational Considerations

### Team Coordination Challenges
- **Multiple users**: Who's handling which request?
- **Shared inbox**: Email notification management
- **System visibility**: Need to check both systems
- **Current workaround**: Shared inbox + communication

### Change Management
- **From**: Everything in Salesforce
- **To**: Two-system workflow
- **Impact**: Training, process documentation, team coordination
- **Mitigation**: Clear boundaries between systems

### System Boundaries
- **Salesforce**:
  - Customer relationships
  - Accounting & invoicing
  - Internal inventory
  - Business reporting

- **Sourcing Window**:
  - Vendor network access
  - Price discovery
  - Network inventory
  - Drop-ship coordination

## Requirements Coverage

### ✅ New Requirements
- SW-M-44 through SW-M-51: Non-SW buyer integration flow
- System synchronization touch points
- Drop-ship to end customer addresses

### 🔄 Reused Workflows
- W01: Core request creation (modified for context)
- W02: Review and selection (used twice - review and purchase)
- W03: Vendor quoting (unchanged)
- W05: Fulfillment process (modified for end-customer delivery)

## Success Metrics
- Time from phone call to SW request
- Manual vs. automated step ratio
- System synchronization accuracy
- End-customer delivery success rate
- Team coordination efficiency

## Future Enhancements
- Salesforce-to-SW automatic request creation
- Bi-directional status synchronization
- Unified dashboard for both systems
- Team assignment automation
- Real-time inventory visibility across systems