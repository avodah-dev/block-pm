# Discovery Day 3 - September 10, 2025
## Conversation Topics and Domain Keywords

---

## Major Conversation Topics

### 1. **Technical Architecture Deep Dive with FMD**
- Salesforce object model walkthrough (12+ core objects)
- Data synchronization strategies (streaming events vs APIs)
- Migration approach from Sourcing Window 2.0 to 3.0
- Source of truth discussions for materials/parts data
- Virtual vs real purchase orders in Salesforce

### 2. **MVP Plus Scope Definition**
- February launch target for external buyers/vendors
- Internal Block users phase 2/3 with lower confidence
- "Lift and shift plus" strategy - current capabilities plus pain points
- Debate over parallel systems vs hard cutover
- Beta user approach for soft launch

### 3. **Integration Complexity**
- Bi-directional sync requirements between systems
- Notification system ownership (who sends what)
- Shopping cart complexity for multi-vendor purchases
- API-first design vs manual touchpoints initially
- Conflict resolution for data synchronization

### 4. **Part Number Management**
- Raw part number formula ("super top secret")
- Compatibility tables and one-directional relationships
- Aliases and fuzzy matching requirements
- Manufacturer vs service vs commercial part numbers
- Global non-uniqueness of part numbers

### 5. **Voice Recognition Feature**
- FSE use case for hands-free part ordering
- Marketing differentiator potential
- Text-to-speech integration options
- WhatsApp-style voice messaging model
- Call-in AI agent possibilities

---

## Domain Keywords & Definitions

### **Technical Architecture Terms**

**Public Events**
- Definition: Salesforce's event streaming mechanism for data changes
- Usage: "Push a public event with rec ID, then fetch the latest data"

**Streaming Events**
- Definition: Real-time notification when Salesforce objects change
- Usage: Alternative to explicit API calls for synchronization

**Raw Part Number**
- Definition: Normalized part number with dashes removed and leading zeros trimmed
- Usage: "Super top secret formula" - primary search method (85-90% of searches)

**Content Links**
- Definition: Salesforce file security mechanism linking files to records
- Usage: "File inherits permissions from the record it's linked to"

**Ephemeral Object**
- Definition: Temporary data structure that exists during a process
- Usage: Shopping cart described as "ephemeral - there then gone"

### **Object Model Terms**

**Requisition**
- Definition: Header/wrapper for a parts request or sales order
- Usage: "The requisition drives off auto-sourcing"

**Requisition Line Items**
- Definition: Individual part lines within a requisition
- Usage: "Contains part numbers and ultimately the pricing quoted"

**Sourcing Items**
- Definition: Vendor quotes for requisition line items
- Usage: "One requisition item could be sourced from 4-5-6 different vendors"

**Shopping Cart (Object)**
- Definition: Data structure managing vendor selection and PO creation
- Usage: "Ephemeral object" that connects sourcing items to purchase orders

**Purchase Order (PO)**
- Definition: Formal authorization for vendor to ship parts
- Usage: "Could turn into two different POs to different vendors"

**Shipping Note**
- Definition: Internal Block object for tracking shipments
- Usage: "Not exposed in SW 2.0 but powers the tracking number"

**Sourcing Window Company**
- Definition: Fake company tag to keep virtual transactions out of financials
- Usage: "Keeps it out of the financial pool so customers can buy/sell without corrupting finances"

### **Integration & Sync Terms**

**Bi-directional Sync**
- Definition: Two-way data updates between Sourcing Window and Salesforce
- Usage: "Near real-time transcription both ways"

**Source of Truth**
- Definition: Authoritative system for specific data types
- Usage: "Materials will probably still live in Salesforce but synchronized"

**Historical Sourcing Tab**
- Definition: Legacy data view from previous system migrations
- Usage: "Took it from 1.0 to 2.0... satisfactory for users"

**Native Salesforce API**
- Definition: Direct access to Salesforce objects vs custom APIs
- Usage: "Opens up the complete object to you"

### **Product Strategy Terms**

**MVP Plus**
- Definition: Current capabilities reproduced plus pain points addressed
- Usage: "Lift and shift plus with minimal disruption to internal teams"

**Power Tools**
- Definition: Block-specific features vs general product features
- Usage: "Distinction between what stays with Block vs product features"

**External-First Launch**
- Definition: Strategy to launch with external users before internal
- Usage: Opposite of typical "eat your own dogfood" approach

**Sandbox to Production**
- Definition: Testing environment before live deployment
- Usage: "This is all in Sandbox, not production"

### **Vendor Management Terms**

**Modality**
- Definition: Equipment type classification (CT, MRI, etc.)
- Usage: "Internally call modality... from a CT"

**Manufacturer**
- Definition: OEM information linked to materials
- Usage: "They're not generating manufacturers... those are defined"

**Compatibility**
- Definition: Part interchangeability relationships
- Usage: "This part is interchangeable with this part but not always reversible"

**All Parts / PartSource**
- Definition: Major third-party vendors with inventory APIs
- Usage: "All Parts and PartSource have established API that's plug and play"

**Third-Party Stock**
- Definition: External vendor inventory managed in Salesforce
- Usage: "Manage as third-party stock initially"

### **Process Flow Terms**

**Auto-Sourcing**
- Definition: Automatic vendor selection based on rules
- Usage: "Requisition drives off things like auto-sourcing"

**Manual Sourcing**
- Definition: CSR override of automatic vendor selection
- Usage: "Whether someone manually sourced it or used auto-sourcing"

**Check Out**
- Definition: Final step converting shopping cart to purchase orders
- Usage: "Quote unquote check out... creates purchase orders"

**Cross-Company Purchases**
- Definition: Buying from multiple vendors in one transaction
- Usage: "Shopping cart fosters cross-company purchases"

### **Migration & Launch Terms**

**Hard Cut**
- Definition: Complete switchover from old to new system
- Usage: "If you try to split environment instead of hard cut, my head will explode"

**Three-Month Migration**
- Definition: Active data migration period for cutover
- Usage: "Migrated three months of data... full data intact"

**Beta User Program**
- Definition: Early access for select internal users
- Usage: "Internal beta users... your buddies at PartSource"

**Parallel Systems**
- Definition: Running old and new systems simultaneously
- Usage: Risk of "synchronizing between two live systems"

### **User Experience Terms**

**Bell Icon**
- Definition: Salesforce notification indicator
- Usage: "Little bell icon in top right... click here to go to it"

**Chatter**
- Definition: Salesforce's internal social collaboration tool
- Usage: "Chatter requires it be associated with a record"

**EMA (Enhanced Messaging Application)**
- Definition: Custom messaging between buyers and vendors
- Usage: "EMA bridged the gap... controlled conversation"

**At-Mention**
- Definition: Tagging users in chatter (security concern)
- Usage: "Can literally at-mention anyone in the company"

### **Voice Feature Terms**

**Voice Recognition**
- Definition: Speech-to-text for part ordering
- Usage: "I need quotes on a C-WISP" hands-free

**WhatsApp Model**
- Definition: Voice message paradigm popular in Latin America
- Usage: "Nobody texts. They send voice messages"

**AI Agent**
- Definition: Conversational interface for ordering
- Usage: "Call on the phone and talk to an AI"

**Whisper Flow**
- Definition: Enhanced voice-to-text tool
- Usage: "Better Siri for text-to-speech"

### **ConvoPro Terms**

**ConvoPro**
- Definition: Siemens-approved AI/chat platform
- Usage: "Private AI cloud... chat that's safe"

**Marketing Differentiator**
- Definition: Unique feature for competitive advantage
- Usage: Voice as "first major distributor in HTM market"

---

## Critical Technical Decisions

### Object Ownership
- **Materials/Parts**: Stays in Salesforce initially
- **Requisitions**: New system for external, Salesforce for internal (Phase 1)
- **Purchase Orders**: Complex dual system with virtual vs real
- **Notifications**: New system to absorb all external communications

### Integration Architecture
- **Day 1**: Manual touchpoints, no API
- **Future**: API-driven with streaming events
- **Synchronization**: Bi-directional with conflict resolution
- **File Security**: Inherit from record permissions

### Migration Strategy
- **Three months active data** for immediate operations
- **Historical sourcing tab** for legacy viewing
- **JSON dump access** for detailed history if needed
- **Hard cut preferred** over parallel systems

---

## Notable Quotes

- "Super top secret formula" - Raw part number conversion
- "My head will explode" - Jeff on parallel system complexity
- "Ephemeral object... there then gone" - Shopping cart nature
- "Virtual stuff is killing people" - Fake company workaround pain
- "85-90% is just part number search" - Search behavior insight
- "Can literally at-mention anyone" - Chatter security issue
- "Fat Lego blocks" - Salesforce limitations (from Day 2)
- "February with 100% home run" - Success criteria

---

## Pain Points Revealed

1. **Virtual Company Confusion** - Fake "Sourcing Window Company" for accounting
2. **Part Number Chaos** - No global uniqueness, multiple formats
3. **Compatibility Complexity** - One-directional relationships
4. **Object Proliferation** - 12+ objects for basic flow
5. **Notification Ownership** - Unclear who sends what when
6. **File Management** - Download to re-upload workaround
7. **Search Limitations** - Creating duplicate materials

---

## Risk Factors Identified

- **Synchronization complexity** between live systems
- **Salesforce API limitations** and rate limits
- **Data migration scope** - what to bring vs leave
- **Internal adoption** without "eating own dogfood"
- **ConvoPro maturity** - "disappointing implementation"
- **Voice feature** - Siemens compliance concerns

---

## Strategic Alignment

### Jeff's Perspective (FMD)
- **Agrees**: Flow not that complicated with right tech stack
- **Recommends**: Manual first, then API
- **Warns**: Parallel systems = complexity explosion
- **Supports**: Standalone product architecture

### Leadership Direction
- **February target** with marketing engine
- **External first** to avoid internal disruption
- **Beta program** for early internal adoption
- **"Black box" treatment** from Salesforce perspective

---

*Document compiled from Day 3 Discovery transcripts (September 10, 2025)*
*Technical session with FMD (Jeff, Carlos) and wrap-up with Steve*
*Focus on architecture, integration, and launch strategy*