# Architecture Layers: Sourcing Window Ecosystem

## Overview
This document defines the three distinct architectural layers in the Sourcing Window implementation, clarifying what functionality belongs where and how they interact. This separation is critical for maintaining a clean, reusable product while supporting client-specific needs.

## The Three Layers

### 1. Product Layer: Sourcing Window 🏗️
**What it is**: The core, standalone marketplace platform

**Responsibilities**:
- **Marketplace Operations**
  - Parts request creation and distribution
  - Quote submission and management
  - Vendor selection and purchasing
  - Order fulfillment tracking
  - Network visibility controls

- **Core Features**
  - User authentication and authorization
  - Vendor/buyer role management
  - Integrated vendor dual-role switching
  - Messaging capability
  - Notification system
  - Dashboard and reporting

- **Data Management**
  - Part catalog
  - Vendor network relationships
  - Requisition hierarchy (parent/child)
  - Quote history
  - Order tracking

**Key Principles**:
- Must work for ANY customer, not just current client
- No client-specific business rules
- Clean APIs for integration
- Self-contained functionality
- Scalable and multi-tenant ready

**What it DOESN'T do**:
- Client-specific workflows
- Integration with specific business systems
- Custom approval chains
- Accounting/invoicing
- Inventory management (beyond availability)

### 2. Business Logic Layer 🔄
**What it is**: The client-specific integration and customization layer

**Responsibilities**:
- **System Integration**
  - Salesforce ↔ Sourcing Window data sync
  - Event handling between systems
  - API callbacks and webhooks
  - Status synchronization

- **Business Rules**
  - Client-specific approval workflows
  - Custom markup calculations
  - Vendor selection criteria
  - Budget constraints
  - Compliance requirements

- **Data Transformation**
  - Map Salesforce objects to SW entities
  - Convert between data formats
  - Aggregate reporting across systems
  - Handle currency/unit conversions

- **Automation**
  - Auto-create SW requests from Salesforce
  - Update Salesforce when SW quotes arrive
  - Trigger workflows based on thresholds
  - Schedule batch operations

**Implementation Options**:
- **Phase 1**: API integrations and batch jobs
- **Phase 2**: Real-time event streaming
- **Phase 3**: Custom UI components
- **Future**: Full middleware platform

**Key Principles**:
- Bridge between systems, don't replace them
- Maintain data consistency
- Handle edge cases gracefully
- Provide visibility into integration status
- Support phased rollout

### 3. Business System: Salesforce 360 💼
**What it is**: The client's system of record for business operations

**Current Responsibilities**:
- **Financial Management**
  - Accounting and invoicing
  - Purchase orders
  - Budget tracking
  - Payment processing

- **Customer Relationship**
  - Contact management
  - Account history
  - Contract management
  - SLAs and terms

- **Business Operations**
  - Opportunity pipeline
  - Sales forecasting
  - Internal approvals
  - Reporting and analytics

- **Inventory** (currently)
  - Stock levels
  - Warehouse management
  - Serial number tracking

**Migration Path**:
- Some functions may move to Sourcing Window over time
- Others may move to Business Logic Layer
- Core accounting likely stays in Salesforce

## Interaction Patterns

### Pattern 1: SW-Initiated Flow
```
Sourcing Window → Business Logic → Salesforce
Example: New quote arrives → Transform data → Update opportunity
```

### Pattern 2: Salesforce-Initiated Flow
```
Salesforce → Business Logic → Sourcing Window
Example: Phone order → Create request → Broadcast to network
```

### Pattern 3: Dual-System Coordination
```
Salesforce ← Business Logic → Sourcing Window
     ↓            ↓            ↓
  Business     Sync Layer    Marketplace
  Records      & Rules       Operations
```

## Decision Framework

### Where does this feature belong?

Ask these questions in order:

1. **Is it specific to one client?**
   - Yes → Business Logic Layer
   - No → Continue to #2

2. **Is it about marketplace operations?**
   - Yes → Sourcing Window Product
   - No → Continue to #3

3. **Is it about financial/accounting?**
   - Yes → Business System (Salesforce)
   - No → Continue to #4

4. **Does it require data from multiple systems?**
   - Yes → Business Logic Layer
   - No → Likely Product or Business System

## Examples by Feature

| Feature | Layer | Reasoning |
|---------|-------|-----------|
| Create parts request | Product | Core marketplace function |
| Submit quote | Product | Core marketplace function |
| Integrated vendor role switching | Product | Marketplace capability |
| Calculate client-specific markup | Business Logic | Client-specific rule |
| Sync quotes to Salesforce | Business Logic | Integration function |
| Generate invoice | Business System | Accounting function |
| Track inventory levels | Business System* | Currently in Salesforce |
| Send email notifications | Product | Core platform feature |
| Apply approval chain | Business Logic | Client-specific workflow |
| Vendor network visibility | Product | Marketplace feature |
| Custom report for CFO | Business Logic | Cross-system aggregation |

*May migrate to Product in future phases

## Implementation Priorities

### Phase 1: MVP (Current)
- **Product**: Basic marketplace functions
- **Business Logic**: Manual processes, minimal integration
- **Business System**: Continues current operations

### Phase 2: Integration
- **Product**: Enhanced features, APIs
- **Business Logic**: Automated sync, event handling
- **Business System**: Reduced manual entry

### Phase 3: Optimization
- **Product**: Advanced capabilities
- **Business Logic**: Full automation, custom UI
- **Business System**: Focus on core competencies

## Technical Considerations

### APIs and Integration Points
- **Product APIs**: RESTful, webhooks, real-time events
- **Business Logic**: Middleware, ETL, event bus
- **Salesforce**: SOAP/REST APIs, Apex triggers, Platform Events

### Data Ownership
- **Product**: Owns marketplace transactional data
- **Business Logic**: Owns mappings and transformations
- **Business System**: Owns business records and financial data

### Security Boundaries
- Each layer maintains its own security context
- Business Logic Layer manages cross-system authentication
- No direct database access between systems

## Key Takeaways

1. **Sourcing Window Product** must remain generic and reusable
2. **Business Logic Layer** handles ALL client-specific needs
3. **Salesforce** remains system of record during transition
4. **Clear boundaries** prevent feature creep and maintain scalability
5. **Phased approach** allows gradual migration and risk management

## Open Questions for Client

1. What functions MUST remain in Salesforce long-term?
2. Which integrations are Phase 1 vs Phase 2 priorities?
3. What level of real-time sync is required vs batch acceptable?
4. Who owns the Business Logic Layer development?
5. What's the timeline for reducing Salesforce dependency?

## Document Maintenance
This document should be updated as:
- New features are identified
- Integration patterns emerge
- Client priorities change
- Technology decisions are made