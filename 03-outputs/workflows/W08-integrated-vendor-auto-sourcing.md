# W08: Integrated Vendor Request Response with Auto-Sourcing

## Input Sources
- **Image**: Integrated vendor auto-sourcing workflow diagram
- **Voice Narration**: Detailed explanation of tiered vendor sourcing
- **Created Date**: 2025-09-25

## Overview
- **Persona**: P03-integrated-vendor
- **Goal**: Respond to requests using intelligent auto-sourcing when lacking inventory
- **Trigger**: Receiving request to submit pricing
- **Key Feature**: Tiered vendor release system for optimized sourcing

## Narrative Description

This workflow represents the sophisticated decision-making and sourcing capabilities that make integrated vendors so powerful in the Sourcing Window ecosystem. When an integrated vendor receives a request to submit pricing, they face a critical decision point that determines their entire response strategy.

The journey begins simply enough - a request arrives asking for pricing on a part. If the integrated vendor has stock, they follow the standard vendor workflow: enter their pricing, specify conditions, warranty terms, and submit. Business as usual. But it's when they DON'T have stock that the real power of being an integrated vendor reveals itself.

Instead of simply marking "no stock" and losing the opportunity, the integrated vendor can transform into a buyer and create a request for that exact part from their network of connected vendors. But here's the crucial constraint: they can only request from vendors who aren't already part of the original buyer's request. This prevents duplicate quotes and maintains clean competitive boundaries.

The integrated vendor now faces a choice: manually select vendors or use the powerful "auto-sourcing" feature. Auto-sourcing is what we might call a "premium user feature" or "power tool" - it's the difference between calling ten vendors individually and having an intelligent system orchestrate your entire sourcing strategy.

Here's how auto-sourcing works: An integrated vendor might be connected to 50+ vendors, but they know from experience that not all vendors are created equal. They have their top tier - maybe 10 vendors who consistently deliver quality parts quickly. Then they have their second tier - another 10 who are reliable but maybe slower or more expensive. And then a third tier for specialized or backup suppliers.

The tiered release system is elegant in its simplicity but powerful in its effect. When the integrated vendor triggers auto-sourcing, the system first releases the request ONLY to Tier 1 vendors. These preferred vendors get first shot at the business. After a configured time period (maybe 10 minutes, maybe an hour - this would be configurable), if sufficient quotes haven't been received, the system automatically releases to Tier 2 vendors. And if needed, after another delay, to Tier 3.

This tiered approach serves multiple purposes:
- It rewards vendor relationships and performance
- It prevents overwhelming the integrated vendor with too many quotes at once
- It allows for quick responses from preferred vendors before opening to broader market
- It maintains competitive dynamics while managing complexity

The architectural question here is interesting: Where does the tier configuration live? In the discussion, several options emerged:
- Could be in the business system (Salesforce) with an API providing tier lists
- Could be in the business logic layer for client-specific tiering rules
- Could be a Product feature with configurable tiers per integrated vendor

Regardless of where the configuration lives, the Product must support the tiered release mechanism - this is core functionality that enables sophisticated sourcing strategies.

As quotes come in from the tiered vendors (following the standard vendor quote submission process), the integrated vendor reviews them. They might receive 4 quotes from 2 tiers of vendors. They evaluate based on price, warranty, condition, and their knowledge of vendor reliability. They might select one option, or strategically, they might select two options to give their buyer choice.

Here's where the markup feature becomes critical. The integrated vendor takes the selected quote(s) and marks up the pricing. This isn't just adding a random percentage - it's their value-add for:
- Orchestrating the sourcing process
- Taking responsibility for the transaction
- Managing vendor relationships
- Handling any issues that arise
- Providing a single point of contact

The markup feature could be simple (user manually adjusts price) or sophisticated (automatic percentage markup, tiered markup based on value, dynamic markup based on competition). For now, we'll treat it as a feature that allows price adjustment with potential for enhancement.

The integrated vendor then submits their marked-up quote to the original buyer. Importantly, they pass through all the original warranty terms and conditions - they're transparent about everything except the price markup. The buyer sees what appears to be a standard vendor quote, unaware of the complex sourcing that happened behind the scenes.

If the buyer selects the integrated vendor's quote and purchases, only the integrated vendor gets notified initially. They then must cascade that purchase down to their selected vendor, initiating the fulfillment process. This creates a clean communication chain: buyer → integrated vendor → selected vendor.

The beauty of this system is its recursive nature. In theory, the selected vendor could themselves be an integrated vendor, creating multi-tier sourcing chains. The system handles this elegantly through the parent/child requisition ID structure.

## Workflow Steps

### 📊 Step-to-Requirements Matrix

| Step ID | Step Name | Requirements | Layer | Notes |
|---------|-----------|--------------|-------|-------|
| W08-S01 | Receive Request | - | Product | Standard vendor receipt |
| W08-S02 | Check Stock Decision | SW-M-52 | Product | Branch point |
| W08-S03a | Submit Standard Quote | - | Product | Reuse W03 if stock available |
| W08-S03b | Initiate Auto-Sourcing | SW-M-53, SW-M-54 | Product | Unique to integrated vendor |
| W08-S04 | Configure Tiers | SW-M-55 | Product/BLL | Tier selection |
| W08-S05 | Release Tier 1 | SW-M-56 | Product | First vendor group |
| W08-S06 | Wait Period | SW-M-57 | Product | Configurable delay |
| W08-S07 | Release Tier 2 | SW-M-58 | Product | Second vendor group |
| W08-S08 | Collect Quotes | - | Product | Standard quote collection |
| W08-S09 | Review & Select | SW-M-59 | Product | Choose best option(s) |
| W08-S10 | Apply Markup | SW-M-60 | Product/BLL | Price adjustment |
| W08-S11 | Submit to Buyer | SW-M-61 | Product | Marked quote submission |
| W08-S12 | Await Selection | - | Product | Standard wait |
| W08-S13 | Cascade Purchase | SW-M-62 | Product | If selected |

## Detailed Step Descriptions

### W08-S01: Receive Request 📨
- **Completely Reuses**: W03 initial steps
- **Actor**: Integrated Vendor
- **Context**: Part of original buyer's vendor list
- **Next**: W08-S02

### W08-S02: Check Stock Decision 🔍
- **Actor**: Integrated Vendor
- **Type**: Decision Point
- **Branches**:
  - Has Stock → W08-S03a (standard flow)
  - No Stock → W08-S03b (auto-sourcing)
- **Layer**: Product (decision), potentially BLL (inventory check)

### W08-S03a: Submit Standard Quote (Stock Path) ✅
- **Completely Reuses**: W03-vendor-submit-quote
- **Actor**: Integrated Vendor (as standard vendor)
- **Result**: Quote submitted, workflow ends
- **Layer**: Product

### W08-S03b: Initiate Auto-Sourcing (No Stock Path) 🚀
- **NEW FEATURE - Premium Capability**
- **Actor**: Integrated Vendor (transform to buyer)
- **Actions**:
  - Create new request for same part
  - Exclude vendors from original request
  - Link to parent requisition
- **Layer**: Product
- **Next**: W08-S04

### W08-S04: Configure Tiers 📊
- **Actor**: System with Integrated Vendor config
- **Options for Tier Data Source**:
  - Product: Stored tier configurations
  - BLL: API call to business system
  - Business System: Real-time tier calculation
- **Example Configuration**:
  - Tier 1: Top 10 vendors (immediate)
  - Tier 2: Next 10 vendors (after 10 min)
  - Tier 3: Next 10 vendors (after 30 min)
- **Next**: W08-S05

### W08-S05: Release Tier 1 🥇
- **Type**: System Automated
- **Actions**:
  - Send request to Tier 1 vendors only
  - Start wait timer
- **Layer**: Product
- **Next**: W08-S06

### W08-S06: Wait Period ⏱️
- **Type**: System Timer
- **Duration**: Configurable (e.g., 10 minutes)
- **Decision**:
  - Sufficient quotes received → W08-S08
  - Timer expires → W08-S07
- **Layer**: Product

### W08-S07: Release Tier 2 🥈
- **Type**: System Automated
- **Condition**: Insufficient Tier 1 responses
- **Actions**:
  - Send request to Tier 2 vendors
  - Potentially repeat for Tier 3
- **Layer**: Product
- **Next**: W08-S08

### W08-S08: Collect Quotes 📥
- **Reuses**: W03 vendor response collection
- **Actor**: Multiple vendors
- **Result**: Pool of quotes from various tiers
- **Layer**: Product
- **Next**: W08-S09

### W08-S09: Review & Select 👀
- **Partially Reuses**: W02 review functionality
- **Actor**: Integrated Vendor (as buyer)
- **Actions**:
  - Compare quotes (price, warranty, condition)
  - Select one or multiple options
- **Strategic Choice**: May select multiple to offer buyer options
- **Layer**: Product
- **Next**: W08-S10

### W08-S10: Apply Markup 💰
- **NEW FEATURE - Critical for Integrated Vendor**
- **Actor**: Integrated Vendor
- **Implementation Options**:
  - Simple: Manual price adjustment
  - Advanced: Percentage markup
  - Future: Dynamic/tiered markup rules
- **Layer Decision**:
  - Product: Basic markup capability
  - BLL: Client-specific markup rules
- **Next**: W08-S11

### W08-S11: Submit to Buyer 📤
- **Partially Reuses**: W03 quote submission
- **Actor**: Integrated Vendor (as vendor)
- **Key Details**:
  - Price: Marked up
  - Warranty/Condition: Pass-through from selected vendor
  - Appearance: Standard vendor quote
- **Layer**: Product
- **Next**: W08-S12

### W08-S12: Await Selection ⏳
- **Standard Process**: Buyer reviews all quotes
- **Reference**: W02 buyer selection process
- **Next**: W08-S13 (if selected)

### W08-S13: Cascade Purchase 🔄
- **Actor**: Integrated Vendor
- **Actions**:
  - Receive purchase from buyer
  - Create purchase to selected vendor
  - Initiate drop-ship process
- **Reference**: W06 purchase cascade
- **Layer**: Product
- **Leads to**: W09 (fulfillment workflow)

## Architecture & Layer Decisions

### Product Layer (Sourcing Window)
- **Core Auto-Sourcing Engine**: Tiered release mechanism
- **Timer Management**: Configurable wait periods
- **Vendor Exclusion Logic**: Prevent duplicate requests
- **Basic Markup Feature**: Price adjustment capability
- **Quote Aggregation**: Collect from multiple tiers

### Business Logic Layer Options
- **Tier Configuration API**: Retrieve vendor tiers from business system
- **Markup Rules Engine**: Client-specific markup calculations
- **Auto-Sourcing Triggers**: Inventory-based automation
- **Performance Analytics**: Track tier effectiveness

### Business System Integration Points
- **Inventory Check**: Real-time stock verification
- **Vendor Performance Data**: Inform tier assignments
- **Pricing History**: Guide markup decisions
- **Approval Workflows**: For high-value auto-sourcing

## Edge Cases & Considerations

### No Quotes from Any Tier
- **Scenario**: All tiers exhausted, no quotes received
- **Options**:
  - Submit "no stock" to original buyer
  - Manually reach out to specialty vendors
  - Escalate to procurement team

### Tier 1 Provides Sufficient Quotes
- **Optimization**: Cancel Tier 2/3 if not needed
- **Benefit**: Reduces vendor fatigue
- **Implementation**: Configurable quote threshold

### Conflicting Tier Responses
- **Scenario**: Tier 2 quote better than Tier 1
- **Decision**: Business choice vs. relationship management
- **Solution**: Integrated vendor discretion

## Requirements Coverage

### ✅ New Requirements
- SW-M-52 through SW-M-62: Auto-sourcing capabilities
- Tiered vendor management
- Configurable release delays
- Markup management
- Quote aggregation from multiple sources

### 🔄 Reuses Existing Workflows
- W03: Standard quote submission (when stock available)
- W02: Review and selection process
- W01: Creating requests (modified for exclusions)

## Success Metrics
- Tier 1 response rate vs. Tier 2/3
- Time to sufficient quotes
- Markup optimization
- Win rate with auto-sourced quotes
- Vendor tier performance validation

## Configuration Requirements
- Tier assignment interface
- Delay timer settings
- Markup rules configuration
- Vendor exclusion logic
- Quote threshold settings

## Future Enhancements
- AI-driven tier optimization
- Dynamic delay adjustment based on urgency
- Predictive markup based on competition
- Multi-currency handling
- Automated tier rebalancing based on performance