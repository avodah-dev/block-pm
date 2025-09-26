# Discovery Day 1 - September 8, 2025
## Conversation Topics and Domain Keywords

---

## Major Conversation Topics

### 1. **System Architecture & Integration**
- Current reliance on Salesforce 360 as the core business platform
- Sourcing Window v2.0 built on top of Salesforce with "Legendary" customizations
- Discussion of whether to keep Salesforce as source of truth vs. migrate to new system
- API integration challenges and synchronization requirements
- Debate over replacing vs. rebuilding current functionality

### 2. **User Personas & Workflows**
- Identified 8 key personas:
  - External Buyer (SWP - Sourcing Window Pro users)
  - Internal Buyer (Block procurement teams)
  - External Vendor
  - Internal Management
  - External Management
  - Platform Admin
  - Field Service Engineer (FSE)
  - Biomedical (Biomed) teams

### 3. **Part Lifecycle & Management**
- Complete part journey from acquisition to customer delivery
- Inventory management challenges
- Service contract requirements vs. general inventory
- Manual decision-making processes (Paul Beard as key decision maker)

### 4. **Pain Points & Process Issues**
- Password reset "eternal loop of doom"
- Duplicate part creation due to poor search functionality
- Hyphenation and formatting inconsistencies in part numbers
- Manual workarounds and tribal knowledge dependencies

### 5. **Team Dynamics & Discovery Process**
- Working Genius assessment results showing strong "Tenacity" across Block team
- Discussion of discovery methodology and workflow mapping
- Avodah team debrief on approach and client engagement

---

## Domain Keywords & Definitions

### **Core Systems**

**Salesforce 360 (SF360)**
- Definition: Block's primary business platform for inventory, customer management, and operations
- Usage: "Everything runs through Salesforce" - central source of truth for all business data

**Sourcing Window (SW)**
- Definition: The vendor-facing marketplace where external vendors list and sell parts
- Usage: Platform where vendors receive RFQs and submit quotes

**Sourcing Window Pro (SWP)**
- Definition: The buyer-facing platform where external customers submit part requests
- Usage: "External buyers use SWP to request parts they need"

**Legendary**
- Definition: Third-party inventory management suite built on top of Salesforce
- Usage: Creates customizations that lock Block into specific workflows and processes

**BI Logistics**
- Definition: Block Imaging logistics application within Salesforce for warehouse management
- Usage: Handles inventory movement, allocation, and condition tracking

### **Part-Related Terms**

**Part Number (PN)**
- Definition: Unique identifier for a part, can contain letters and numbers despite the name
- Usage: Primary search method; Block adds hyphens (e.g., 4535-619-90892) while others don't

**Material**
- Definition: Salesforce's terminology for what Block calls a "part"
- Usage: "We call it a material now... we don't want to, but in Salesforce it's material"

**OEC WISP**
- Definition: Wireless relay component for C-arm medical equipment that helps connect to hospital networks
- Usage: Example part used throughout discovery discussions

**SKU**
- Definition: Stock Keeping Unit - unique identifier for inventory items
- Usage: Referenced when discussing inventory management and part identification

**Serial Number**
- Definition: Manufacturer's unique identifier for individual parts, used for tracking
- Usage: Added during harvest process, critical for part lifecycle tracking

### **Process Terms**

**Requisition (Rec/Req)**
- Definition: A formal request for parts created by buyers in the system
- Usage: "Create new requisition" - initiating a part request

**RFQ (Request for Quote)**
- Definition: Request sent to vendors asking for pricing on specific parts
- Usage: Automatically generated when parts aren't in Block inventory

**Harvest/Harvesting**
- Definition: Process of removing usable parts from decommissioned equipment
- Usage: "Harvest team pulls parts from systems and brings them into inventory"

**Service Hold**
- Definition: Inventory status preventing sale of parts reserved for service contracts
- Usage: "Parts on service hold can't be sold to regular customers"

**Component Repair**
- Definition: Internal team that tests, repairs, and refurbishes parts before stock
- Usage: "Component repair team handles all testing before parts go to finished goods"

### **User Types & Roles**

**CSR (Customer Service Representative)**
- Definition: Block team members who handle customer orders and vendor relationships
- Usage: "10 CSRs on the parts team trying to find and sell parts"

**FSE (Field Service Engineer)**
- Definition: Technicians who service equipment on-site at hospitals
- Usage: Different workflow needs than procurement teams

**Biomed/Biomedical**
- Definition: Hospital staff responsible for medical equipment maintenance
- Usage: Separate persona with unique sourcing requirements

**Platform Admin**
- Definition: Super-user role managing the overall Sourcing Window platform
- Usage: Handles system configuration, user management, and platform settings

### **Business Terms**

**Service Contract**
- Definition: Agreement for Block to maintain specific hospital equipment
- Usage: "Oklahoma University Health has a Siemens service contract"

**Finished Goods**
- Definition: Inventory status for parts ready for sale
- Usage: Parts move to "finished goods" after testing and refurbishment

**Core/Core Return**
- Definition: Non-functioning part exchanged for credit or replacement
- Usage: "When a core comes back, returns team processes the credit"

**Auto-sourcing**
- Definition: Automatic vendor selection based on tiering and business rules
- Usage: Feature being excluded from Phase 1 scope

### **Technical Terms**

**API (Application Programming Interface)**
- Definition: Method for different software systems to communicate
- Usage: "API integration with Salesforce for data synchronization"

**Source of Truth**
- Definition: The authoritative data source when multiple systems contain same information
- Usage: Key architectural decision - "Should Salesforce remain the source of truth?"

**Fuzzy Matching**
- Definition: Search capability that finds results despite typos or formatting differences
- Usage: Needed to handle hyphenation and spelling variations in part numbers

**Deep API Integration**
- Definition: Direct system-to-system connection bypassing manual login
- Usage: "Premium version would have deep API integration, no login required"

### **Workflow States**

**Open Request**
- Definition: Active requisition awaiting vendor responses
- Usage: Default view on buyer dashboard

**Pending Order**
- Definition: Request where vendor has been selected but shipment pending
- Usage: Tracked separately from open requests

**TO (Technical Order)**
- Definition: Work order for component repair team
- Usage: "Parts move into a TO for repair team to process"

### **Vendor-Specific Terms**

**Tiering**
- Definition: Vendor ranking system for automatic selection
- Usage: Part of auto-sourcing logic (deferred to later phase)

**Vendor Pool**
- Definition: Group of approved vendors for specific part categories
- Usage: "Sourcing from our vendor pool of 100+ suppliers"

**EMA (Vendor Messaging)**
- Definition: Communication system for vendor interactions
- Usage: "Returns team uses EMA for vendor negotiations"

### **Key Phrases & Pain Points**

**"Eternal Loop of Doom"**
- Definition: Password reset bug that traps users in endless reset cycle
- Usage: Major authentication pain point requiring manual intervention

**"Tribal Knowledge"**
- Definition: Critical information only known by specific individuals
- Usage: "So much tribal knowledge in Paul Beard's brain"

**"Within My Capabilities"**
- Definition: Vendor decision point about whether they can fulfill request
- Usage: Key workflow branch in vendor response process

**"Duplicate Materials"**
- Definition: Multiple database entries for same part due to search/entry issues
- Usage: "Creating duplicate materials because search function sucks"

---

## Cultural & Process Observations

### Communication Patterns
- Heavy reliance on individual expertise (Paul Beard mentioned repeatedly)
- Manual workarounds accepted as normal operations
- Strong internal collaboration but siloed knowledge

### Technology Debt
- "Legendary" system creating vendor lock-in
- Multiple systems doing similar functions (Salesforce apps)
- Search functionality degraded over time ("used to have great search")

### Business Priorities
- Service contracts take priority over general sales
- Speed to market crucial for field service
- Cost management for procurement vs. revenue generation for sales

### Change Management Concerns
- Fear of retraining on new systems
- Attachment to current workarounds
- Skepticism about FMD's delivery capabilities

---

## Key Decisions Pending

1. **Salesforce Integration**: Keep as source of truth or migrate?
2. **Scope Definition**: What's truly MVP vs. "MVP Plus"?
3. **Authentication Model**: How to solve password/login issues?
4. **Search Enhancement**: Fuzzy matching implementation priority?
5. **Admin Features**: When to address auto-sourcing and tiering?

---

## Notable Quotes

- "Everything runs through Salesforce" - System dependency
- "We call it a material now... we don't want to" - Forced terminology
- "Eternal loop of doom" - Password reset frustration
- "So much tribal knowledge in Paul Beard's brain" - Knowledge concentration
- "We're creating duplicate materials because search function sucks" - Data quality issue

---

## Action Items Identified

- Map complete object types and data ownership
- Define synchronization strategy for multi-system updates
- Document Paul Beard's decision criteria
- Design fuzzy matching for part number search
- Create authentication best practices implementation

---

*Document compiled from Day 1 Discovery transcripts (September 8, 2025)*
*Participants: Block team (Steve, Sam, Vicki, Allie, Jordan, Amy) and Avodah team*