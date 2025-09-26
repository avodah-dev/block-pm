# Discovery Day 2 - September 9, 2025
## Conversation Topics and Domain Keywords

---

## Major Conversation Topics

### 1. **Internal Workflows Deep Dive**
- Field Service Engineer (FSE) parts request process
- Service Request (SR) to Service Request Visit (SRV) flow
- Parts basket management and requisition creation
- Manual processes and notification breakdowns
- Procurement team's 50+ daily manual interventions

### 2. **Architecture & Integration Strategy**
- Sourcing Window as standalone product vs embedded tool
- Source of truth decisions (Salesforce vs Sourcing Window)
- Bi-directional synchronization requirements
- Power tools vs product features distinction
- Block as "super-user" customer model

### 3. **Leadership Strategic Alignment (Exec Lunch)**
- Phase 1: External users with minimal Salesforce changes
- Phase 2-3: Lower confidence intentionally for learning
- Materials master record ownership debate
- Data warehouse implications
- Past trauma from rushed January 2023 go-live

### 4. **User Experience & Change Management**
- "30 tabs open" workflow reality for CSRs
- Fixation on staying within Salesforce
- "If it's less clicks and better, they'll accept change"
- Two years of unfinished processes from rushed launch
- Beta user approach for internal adoption

### 5. **Vendor Management & Sourcing**
- Apples-to-apples comparison challenges
- Cancellation process pain points
- Multi-vendor quote management
- Shipping carrier complexity (FedEx/UPS/DHL)
- PO submission and confirmation workflow

---

## Domain Keywords & Definitions

### **Core Process Terms**

**SR (Service Request)**
- Definition: Initial ticket created when equipment needs service
- Usage: "Everything gets an SR" - created by call center for every customer call

**SRV (Service Request Visit)**
- Definition: Work order created from SR when on-site visit is needed
- Usage: "SRV is created off of the SR for that piece of equipment"

**Parts Basket**
- Definition: Temporary collection of parts before requisition creation
- Usage: "Engineer puts parts in basket, then chatters us to create requisition"

**Requisition (Rec/Req)**
- Definition: Formal parts request created from basket items
- Usage: "We submit the parts basket to create a requisition"

**Queue**
- Definition: Work distribution system (currently missing for procurement)
- Usage: "We don't have a queue yet... it's been working on"

### **User Roles & Teams**

**FSE (Field Service Engineer)**
- Definition: Technician assigned to specific equipment who performs on-site repairs
- Usage: "FSE is assigned to each piece of equipment"

**Procurement Team**
- Definition: Internal Block team handling parts sourcing (4 people)
- Usage: "Erica's team doing 50+ orders per day manually"

**Parts Team**
- Definition: CSRs managing parts sales and vendor relationships
- Usage: "10 CSRs on the parts team trying to find and sell parts"

**Call Center/Desk**
- Definition: Initial contact point for service requests
- Usage: "Call center creates a service request in Salesforce"

### **System & Integration Terms**

**Chatter**
- Definition: Salesforce's internal messaging system
- Usage: "Engineers should chatter us from the SRV"

**Source of Truth**
- Definition: Authoritative data source when multiple systems contain same data
- Usage: "Both systems will maintain same set of data... synchronization rather than single source"

**Power Tools**
- Definition: Block-specific features vs product features for all customers
- Usage: "Power tool is specifically a Block enabler" vs general product features

**Super-User/Super-Customer**
- Definition: Block's special status with enhanced integrations
- Usage: "Block is a super-user with automation... super premium"

**Sandbox**
- Definition: Test environment for trying features without affecting production
- Usage: "This is all in Sandbox, not production"

### **Workflow States & Actions**

**Do Not Auto-Source**
- Definition: Button that stops automatic vendor selection (currently broken)
- Usage: "If engineer clicks do not auto-source, we should get notifications"

**Parts Management**
- Definition: Section in SR/SRV where engineers add needed parts
- Usage: "They go to parts management and put the parts they need"

**Confirm Order**
- Definition: Vendor action acknowledging PO receipt
- Usage: "I would hit confirm order and email goes to buyer"

**Select/Add to Cart**
- Definition: Buyer choosing vendor and building purchase order
- Usage: "Select which vendor, add to cart, then enter PO information"

### **Business Process Terms**

**Tier/Tiering**
- Definition: Vendor ranking system for automatic selection (internal only)
- Usage: "Tiering applies to any sourcing for Block, not SWP customers"

**Capabilities**
- Definition: Vendor's ability to provide specific part types
- Usage: "Vendors with capabilities and alignments for those parts"

**PO (Purchase Order)**
- Definition: Formal document authorizing purchase
- Usage: "Upload PO, enter shipping information, submit"

**Exchange vs Outright**
- Definition: Core return for credit vs direct purchase
- Usage: "$3,000 threshold between exchange and outright purchase"

### **Pain Points & Workarounds**

**Manual Sourcing**
- Definition: CSR override of automatic vendor selection
- Usage: "I only want these two vendors because I know this guy has it"

**Notification Breakdowns**
- Definition: System failures to alert appropriate teams
- Usage: "We don't get notifications... that changed and caused havoc"

**Cancellation Complexity**
- Definition: Difficulty switching vendors after initial selection
- Usage: "To cancel and buy from different vendor is pain in the butt"

**Tab Overload**
- Definition: CSRs managing 30+ browser tabs simultaneously
- Usage: "They have 30 tabs open... absolutely cannot function with one more"

### **Technical Architecture Terms**

**Embedded vs Standalone**
- Definition: Tool within Salesforce vs separate application
- Usage: "Embedded inside Salesforce vs one tab Salesforce, one tab Sourcing Window"

**Bi-directional Sync**
- Definition: Two-way data updates between systems
- Usage: "Near real-time transcription Salesforce stuff... same thing other way"

**API Integration**
- Definition: System-to-system connection for data exchange
- Usage: "Strong APIs and infrastructures... the right way to do it"

**Data Warehouse**
- Definition: Centralized repository for analytics (being considered)
- Usage: "Mark wants direct poll from data warehouse"

### **Vendor-Specific Terms**

**Direct vs Indirect**
- Definition: Block-owned inventory vs third-party vendor inventory
- Usage: "Auto source to direct tier one if Block, otherwise no tier"

**Common Spirit**
- Definition: Major customer using SWP for procurement
- Usage: "Sarah Daly from Common Spirit" - example buyer persona

**Vendor Master**
- Definition: Central vendor database shared across systems
- Usage: "All vendor records live in vendor master"

**FedEx/UPS/DHL Accounts**
- Definition: Customer shipping preferences stored in system
- Usage: "We're one of only people doing all three carriers"

### **Cultural & Process Observations**

**"Past Trauma"**
- Definition: Negative experiences from rushed 2023 go-live
- Usage: "Past trauma from having to go live January... no choice"

**"Legendary Customizations"**
- Definition: Third-party modifications causing vendor lock-in
- Usage: "Legendary built current sourcing window... now no one owns it"

**"Willing Lack of Understanding"**
- Definition: Engineers refusing to learn Salesforce
- Usage: "I don't do Salesforce, that's not for me"

**"Duplo Blocks"**
- Definition: Metaphor for Salesforce's large, inflexible components
- Usage: "Fat Lego blocks" limiting granular customization

---

## Key Strategic Decisions

### Architecture Philosophy
- **Sourcing Window = Standalone Product**
- **Block = Premium Customer (not special case)**
- **Power Tools stay separate from product features**
- **Materials master lives in Sourcing Window**

### Integration Approach
- **Bi-directional sync with conflict resolution**
- **Embedded views for internal users initially**
- **Gradual migration from Salesforce processes**
- **API-first design for all integrations**

### Phase Strategy
- **Phase 1**: 90% confidence - External users, minimal change
- **Phase 2-3**: 25% confidence - Learn together, adjust based on Phase 1
- **Focus on user experience over system preferences**

---

## Notable Quotes

- "I don't do Salesforce, that's not for me" - FSE resistance
- "They have 30 tabs open... cannot function with one more" - CSR reality
- "If it's less clicks and better, you can make whatever change" - Change acceptance criteria
- "We're creating duplicate materials because search function sucks" - Ongoing from Day 1
- "Past trauma" - Referenced multiple times about 2023 launch
- "Block is the number one most important customer" - Strategic positioning
- "Fat Lego blocks" - Salesforce limitation metaphor

---

## Critical Issues Identified

1. **Notification System Broken** - Engineers' actions don't trigger CSR alerts
2. **No Queue System** - Manual work distribution for procurement team
3. **Cancellation Process** - Can't easily switch vendors after selection
4. **50+ Manual Interventions Daily** - Procurement team overwhelmed
5. **Two Years Unfinished** - Processes never completed from 2023 launch

---

## Action Items & Recommendations

- Map all object types needing synchronization
- Design conflict resolution for bi-directional sync
- Create beta user program for internal adoption
- Build notification queue for procurement team
- Implement easy cancellation/reselection flow
- Document Paul Beard's decision criteria (still pending from Day 1)

---

## Terminology Conflicts/Clarifications from Day 1

- **BI** = Block Imaging (not Business Intelligence) - Corrected in Day 1 doc
- **Material vs Part** - Consistent usage, Salesforce forces "material"
- **Service contracts** take priority - Confirmed multiple times
- **Tribal knowledge** problem persists - Paul Beard still critical bottleneck

---

*Document compiled from Day 2 Discovery transcripts (September 9, 2025)*
*Participants: Block team (Steve, Sam, Vicki, Allie, Jordan, Erica) and Avodah team*
*Executive session with Paul Beard provided strategic clarity*