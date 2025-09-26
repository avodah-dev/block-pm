# Epic Overview

## E01-REQUEST-MANAGEMENT: Buyer Parts Request Creation and Management
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Core Functionality
**Coverage**: 15 requirements directly addressed

This epic encompasses the complete buyer workflow for creating and managing parts requisitions in Sourcing Window Pro. It provides the foundation for buyers to search the parts database, create new materials when needed, configure multi-part requisitions with special instructions, and distribute requests to qualified vendors based on their capabilities. This is the entry point for all procurement activity and directly addresses Block's need for intuitive part searching with fuzzy matching and raw part number normalization.

**Features**:
- F01: Parts database search and management
- F02: Request creation and configuration
- F03: Vendor selection and distribution

---

## E02-QUOTE-MANAGEMENT: Vendor Quote Submission and Tracking
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Core Functionality
**Coverage**: 12 requirements directly addressed

This epic handles the vendor side of the procurement process, enabling suppliers to submit, manage, and track their quotes through Sourcing Window. It provides vendors with the ability to submit multiple quote variants for different conditions (new, refurbished, exchange), manage pricing and availability, and receive automated notifications about opportunities. The epic addresses Block's requirement for vendors to respond directly from email notifications without logging in, streamlining the quote submission process.

**Features**:
- F04: Quote submission interface
- F05: Quote collection and organization
- F06: Quote notification system

---

## E03-PURCHASE-SELECTION: Quote Review and Vendor Selection
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Core Functionality
**Coverage**: 10 requirements directly addressed

This epic provides buyers with comprehensive tools to review, compare, and select winning quotes from vendors. It includes the critical shopping cart functionality that allows buyers to select items from multiple vendors, generate purchase orders with proper terms and conditions, and complete the procurement process. The epic directly addresses Block's need for a "quick select view" for comparing sourcing options and maintaining cart persistence across sessions.

**Features**:
- F07: Quote comparison interface
- F08: Shopping cart functionality
- F09: Purchase order generation

---

## E04-ORDER-FULFILLMENT: Order Processing and Shipment Tracking
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Core Functionality
**Coverage**: 8 requirements directly addressed

This epic manages the post-purchase workflow from order confirmation through delivery. It enables vendors to acknowledge orders, provide shipping information including tracking numbers and serial numbers, and handle partial fulfillments or cancellations. For buyers, it provides real-time visibility into order status, shipment tracking, and delivery confirmation. This addresses Block's requirement for comprehensive order tracking and vendor-provided shipping information.

**Features**:
- F10: Order confirmation management
- F11: Shipping information capture
- F12: Order status tracking

---

## E05-MESSAGING-PLATFORM: Enhanced Messaging Application (EMA)
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Critical Integration
**Coverage**: 9 requirements directly addressed

This epic implements Block's Enhanced Messaging Application (EMA) to enable secure, contextual communication between buyers and vendors. Unlike Salesforce Chatter which has security concerns, EMA provides controlled conversations attached to specific requisitions, quotes, and orders. It includes file attachment support, email notifications for new messages, and maintains complete conversation history. This directly addresses Block's need to "bridge the gap" in buyer-vendor communication.

**Features**:
- F13: Core messaging infrastructure
- F14: Message routing and notifications
- F15: Message search and retrieval

---

## E06-USER-MANAGEMENT: User Accounts and Access Control
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Foundation
**Coverage**: 6 requirements directly addressed

This epic establishes the user management foundation for Sourcing Window 3.0, supporting multiple users under single accounts for both buyer and vendor organizations. It implements secure authentication (addressing the "eternal loop of doom" password reset issue), role-based permissions, and user profile management. The epic includes support for integrated vendors who need dual buyer/vendor capabilities, a unique requirement discovered during Block's discovery sessions.

**Features**:
- F16: User authentication and registration
- F17: Role-based permissions
- F18: User profile management

---

## E07-VENDOR-CAPABILITIES: Vendor Profile and Capability Management
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Core Vendor Functionality
**Coverage**: 11 requirements directly addressed

This epic enables vendors to establish and maintain their business profiles, declare capabilities by modality and geography, and track their performance metrics. It supports Block's requirement for vendors to specify which parts and equipment types they can service, their warehouse locations with cutoff times, and maintain internal notes on capabilities. The performance tracking feature provides visibility into quote response rates, on-time delivery, and quality metrics.

**Features**:
- F19: Vendor profile configuration
- F20: Capability declaration
- F21: Vendor performance tracking

---

## E08-DASHBOARD-ANALYTICS: Dashboards and Reporting
**Size**: Large (12 stories, 3 features)
**Priority**: Phase 1 - High Value
**Coverage**: 8 requirements directly addressed

This epic provides role-specific dashboards and comprehensive analytics for both buyers and vendors. It addresses Block's requirement for homepage views that default to open requests (oldest on top for vendors, newest for buyers) and provides critical business intelligence including spend analysis, vendor performance, and quote win rates. The custom report builder enables power users to create specific views for their unique business needs.

**Features**:
- F22: Buyer dashboard
- F23: Vendor dashboard
- F24: Reporting and analytics

---

## E09-INTEGRATED-VENDOR: Advanced Integrated Vendor Capabilities
**Size**: XL (16 stories, 4 features)
**Priority**: Phase 2 - Advanced Features
**Coverage**: Discovery-driven, not in original requirements

This epic represents significant functionality discovered during Block's discovery sessions for integrated vendors like Block itself who act as both buyers and vendors. It includes sophisticated capabilities like auto-sourcing with tiered vendor release, drop-ship orchestration for direct fulfillment, and network relationship management. This epic positions Sourcing Window 3.0 as a true B2B marketplace platform capable of supporting complex multi-party transactions.

**Features**:
- F25: Vendor-to-buyer role switching
- F26: Auto-sourcing engine
- F27: Drop-ship orchestration
- F28: Network relationship management

---

## E10-SYSTEM-INTEGRATION: External System Connectivity
**Size**: Large (12 stories, 3 features)
**Priority**: MVP - Critical for Block
**Coverage**: Architecture-driven requirements

This epic provides the integration layer necessary for Sourcing Window 3.0 to operate within Block's ecosystem. It includes bi-directional synchronization with Salesforce 360 (maintaining it as the source of truth), API connections to third-party vendors like All Parts and PartSource, and a comprehensive API gateway for future extensibility. This addresses Block's critical need for seamless data flow between systems while avoiding the "30 tabs open" problem that plagues current users.

**Features**:
- F29: API gateway
- F30: Salesforce integration
- F31: Third-party vendor integrations

---

## E11-ADMINISTRATION: System Administration and Configuration
**Size**: Large (12 stories, 3 features)
**Priority**: Phase 1 - Operational Necessity
**Coverage**: 5 requirements directly addressed

This epic provides administrative tools for managing the Sourcing Window platform, including business rules configuration, data management utilities, and user administration capabilities. It addresses Block's need for configurable approval thresholds, automated archival after 7 days, and comprehensive audit trails. The bulk import/export tools are critical for initial data migration from the current Salesforce-based system.

**Features**:
- F32: System configuration
- F33: Data management
- F34: User administration

---

## E12-MOBILE-EXPERIENCE: Mobile and Field Service Support
**Size**: Large (12 stories, 3 features)
**Priority**: Phase 2 - FSE Enhancement
**Coverage**: FSE pain points from discovery

This epic addresses the unique needs of Field Service Engineers (FSEs) who "don't do Salesforce" and need mobile-friendly tools for parts ordering while working on equipment. It includes innovative features like voice-to-text part number entry for hands-free operation, parts basket to requisition conversion, and photo upload for part identification. The mobile-responsive design ensures all core workflows function seamlessly on tablets and smartphones.

**Features**:
- F35: Mobile-responsive interface
- F36: Field service engineer support
- F37: Mobile notifications

---

## E13-SEARCH-DISCOVERY: Advanced Search and Discovery
**Size**: Large (12 stories, 3 features)
**Priority**: Phase 2 - User Experience Enhancement
**Coverage**: Discovery-driven enhancements

This epic enhances the platform's search and discovery capabilities beyond basic part number searches. It implements global search across all entities, smart recommendations using AI-driven suggestions for alternative parts and price optimization, and browse/discovery features for exploring the parts catalog. This addresses feedback from discovery sessions about the current system where "search function sucks" and causes duplicate material entries.

**Features**:
- F38: Global search capability
- F39: Smart recommendations
- F40: Browse and discovery

---

## Summary Metrics

| Size | Count | Stories | Priority |
|------|-------|---------|----------|
| XL | 1 | 16 | Phase 2 |
| Large | 12 | 144 | Mixed (8 MVP, 4 Phase 1-2) |

**Total Coverage**:
- 103 of 118 requirements (87.3%)
- 42 discovery-driven stories (26.3%)
- All 9 workflows fully represented
- 3 personas supported (Buyer, Vendor, Integrated Vendor)