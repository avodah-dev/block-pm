# Sourcing Window Project Dictionary
## Comprehensive Domain Language Reference

*Compiled from Discovery Days 1-3 (September 8-10, 2025)*

---

## Core Platform Terms

### **Sourcing Window (SW)**
- **Definition**: The vendor-facing marketplace platform where external vendors receive RFQs and submit quotes
- **Context**: "Vendors use SW to respond to part requests"
- **Not to be confused with**: Sourcing Window Pro (buyer-facing)

### **Sourcing Window Pro (SWP)**
- **Definition**: The buyer-facing platform where external customers submit part requests and review quotes
- **Context**: "External buyers use SWP to request parts they need"
- **Key distinction**: Pro = buyers, non-Pro = vendors

### **Sourcing Window v3 / 3.0**
- **Definition**: The new unified platform being built to replace current fragmented systems
- **Context**: "MVP Plus" launch targeting February
- **Vision**: Standalone product that could eventually be sold separately

### **Salesforce 360 (SF360)**
- **Definition**: Block's primary business platform for inventory, customer management, and all operations
- **Context**: "Everything runs through Salesforce"
- **Current state**: Source of truth for business data

---

## User Roles & Personas

### **External Buyer**
- **Definition**: Customer from hospitals/healthcare systems using SWP to procure parts
- **Example**: "Sarah Daly from Common Spirit"
- **Workflow**: Creates requisitions, reviews quotes, selects vendors

### **Internal Buyer**
- **Definition**: Block procurement team members sourcing parts for inventory or service
- **Context**: "Erica's team doing 50+ orders per day manually"
- **Pain point**: No queue system, all manual distribution

### **External Vendor**
- **Definition**: Third-party suppliers responding to RFQs through Sourcing Window
- **Context**: "100+ vendors in our pool"
- **Workflow**: Receives RFQ, submits quote, fulfills orders

### **FSE (Field Service Engineer)**
- **Definition**: Technicians assigned to equipment performing on-site repairs at hospitals
- **Context**: "FSE is assigned to each piece of equipment"
- **Unique need**: Parts basket → requisition workflow
- **Pain point**: "I don't do Salesforce"

### **CSR (Customer Service Representative)**
- **Definition**: Block team members managing customer orders and vendor relationships
- **Context**: "10 CSRs on parts team trying to find and sell parts"
- **Reality**: "30 tabs open... cannot function with one more"

### **Biomed/Biomedical**
- **Definition**: Hospital staff responsible for medical equipment maintenance
- **Context**: Separate persona with unique sourcing requirements
- **Future consideration**: Not in Phase 1 scope

---

## Parts & Inventory Terms

### **Part / Material**
- **Definition**: Individual component or replacement part for medical equipment
- **Salesforce term**: "Material" (Block reluctantly uses this)
- **Context**: "We call it a material now... we don't want to"

### **Part Number (PN)**
- **Definition**: Identifier for parts, can contain letters and numbers despite the name
- **Format issue**: Block adds hyphens (4535-619-90892), others don't
- **Search method**: Primary way users find parts

### **Raw Part Number**
- **Definition**: Normalized part number with formatting removed
- **Formula**: "Super top secret" - removes dashes, trims leading zeros
- **Usage**: 85-90% of all searches use part number

### **Serial Number**
- **Definition**: Manufacturer's unique identifier for individual parts
- **Context**: Added during harvest, critical for tracking
- **FSE need**: Required for field service documentation

### **SKU (Stock Keeping Unit)**
- **Definition**: Unique identifier for inventory items
- **Context**: Used in inventory management systems
- **Relationship**: May differ from part number

### **Service Hold**
- **Definition**: Inventory status preventing sale of parts reserved for service contracts
- **Context**: "Parts on service hold can't be sold to regular customers"
- **Priority**: Service contracts take precedence

### **Finished Goods**
- **Definition**: Inventory status for parts ready for sale
- **Context**: After testing and refurbishment by component repair
- **Flow**: Harvest → Test → Finished Goods

### **Core/Core Return**
- **Definition**: Non-functioning part exchanged for credit or replacement
- **Context**: "$3,000 threshold between exchange and outright purchase"
- **Process**: Returns team processes credits

---

## Process & Workflow Terms

### **Requisition (Rec/Req)**
- **Definition**: Formal request for parts, header/wrapper for the order
- **Context**: "Everything gets a requisition"
- **Technical**: Object containing header information

### **Requisition Line Items**
- **Definition**: Individual part lines within a requisition
- **Context**: Contains part numbers and pricing
- **Relationship**: One requisition, multiple line items

### **RFQ (Request for Quote)**
- **Definition**: Request sent to vendors asking for pricing on specific parts
- **Context**: Automatically generated when parts not in Block inventory
- **Flow**: Requisition → RFQ → Vendor quotes

### **SR (Service Request)**
- **Definition**: Initial ticket created when equipment needs service
- **Context**: "Everything gets an SR" - created by call center
- **Starting point**: All service workflows begin here

### **SRV (Service Request Visit)**
- **Definition**: Work order created from SR when on-site visit needed
- **Context**: "SRV is created off the SR for that piece of equipment"
- **Assignment**: Links to specific FSE

### **Parts Basket**
- **Definition**: Temporary collection of parts before requisition creation
- **Context**: "Engineer puts parts in basket, then chatters us"
- **Pain point**: Manual process, notification breakdowns

### **Sourcing Items**
- **Definition**: Vendor quotes/responses for requisition line items
- **Context**: "One req item could be sourced from 4-5-6 vendors"
- **Selection**: Buyer picks winning sourcing item

### **Shopping Cart**
- **Definition**: Data structure managing vendor selection and PO creation
- **Technical**: "Ephemeral object - there then gone"
- **Function**: Connects sourcing items to purchase orders

### **PO (Purchase Order)**
- **Definition**: Formal authorization for vendor to ship parts
- **Context**: Can split into multiple POs for different vendors
- **Complexity**: Virtual vs real POs in Salesforce

### **TO (Technical Order)**
- **Definition**: Work order for component repair team
- **Context**: "Parts move into a TO for repair team"
- **Internal**: Block's repair process

---

## Technical & System Terms

### **API (Application Programming Interface)**
- **Definition**: Method for systems to communicate and exchange data
- **Context**: "API integration with Salesforce"
- **Strategy**: "API-first design" for future

### **Source of Truth**
- **Definition**: Authoritative data source when multiple systems exist
- **Decision point**: "Should Salesforce remain source of truth?"
- **Future**: Synchronization rather than single source

### **Bi-directional Sync**
- **Definition**: Two-way real-time data updates between systems
- **Context**: "Near real-time transcription both ways"
- **Challenge**: Conflict resolution required

### **Chatter**
- **Definition**: Salesforce's internal messaging/collaboration system
- **Context**: "Engineers should chatter us from the SRV"
- **Risk**: Can at-mention anyone in company

### **EMA (Enhanced Messaging Application)**
- **Definition**: Custom messaging system for buyer-vendor communication
- **Purpose**: "Bridge the gap" with controlled conversations
- **Advantage**: No security issues like Chatter

### **Legendary**
- **Definition**: Third-party inventory management suite built on Salesforce
- **Impact**: Creates vendor lock-in with customizations
- **Context**: "Legendary built current sourcing window"

### **BI Logistics**
- **Definition**: Block Imaging logistics app within Salesforce
- **Note**: BI = Block Imaging, NOT Business Intelligence
- **Function**: Warehouse management, inventory movement

### **Sandbox**
- **Definition**: Test environment separate from production
- **Context**: "All in Sandbox, not production"
- **Usage**: Testing before live deployment

### **Public Events / Streaming Events**
- **Definition**: Salesforce's real-time data change notifications
- **Usage**: "Push public event with rec ID"
- **Alternative**: To explicit API calls

---

## Business Terms

### **Service Contract**
- **Definition**: Agreement for Block to maintain hospital equipment
- **Priority**: Takes precedence over general sales
- **Example**: "Oklahoma University Health Siemens contract"

### **Harvest/Harvesting**
- **Definition**: Process of removing usable parts from decommissioned equipment
- **Context**: "Harvest team pulls parts and brings to inventory"
- **Flow**: Decommission → Harvest → Test → Stock

### **Component Repair**
- **Definition**: Internal team testing and refurbishing parts
- **Context**: "Handles all testing before finished goods"
- **Quality**: Ensures parts meet standards

### **Auto-sourcing**
- **Definition**: Automatic vendor selection based on tiering/rules
- **Status**: Excluded from Phase 1 scope
- **Future**: Admin feature for later phases

### **Tiering**
- **Definition**: Vendor ranking system for automatic selection
- **Context**: "Applies to Block sourcing, not SWP customers"
- **Deferred**: Part of auto-sourcing (Phase 2+)

### **Modality**
- **Definition**: Equipment type classification (CT, MRI, X-ray, etc.)
- **Context**: "Internally call modality"
- **Usage**: Tags materials/parts by equipment type

### **Compatibility**
- **Definition**: Part interchangeability relationships
- **Complexity**: "Doesn't always work in reverse"
- **Example**: Part A replaces B, but B may not replace A

---

## Pain Points & Issues

### **"Eternal Loop of Doom"**
- **Definition**: Password reset bug trapping users in endless cycle
- **Impact**: Major authentication pain point
- **Solution needed**: Fix authentication flow

### **"30 tabs open"**
- **Definition**: CSR workflow reality with multiple systems
- **Quote**: "Cannot function with one more tab"
- **Root cause**: System fragmentation

### **"Tribal Knowledge"**
- **Definition**: Critical information only known by specific individuals
- **Example**: "So much in Paul Beard's brain"
- **Risk**: Single point of failure

### **Duplicate Materials**
- **Definition**: Multiple database entries for same part
- **Cause**: "Search function sucks"
- **Impact**: Data quality degradation

### **"Past Trauma"**
- **Definition**: Negative experience from rushed January 2023 go-live
- **Context**: "No choice" - forced launch
- **Result**: Two years of unfinished processes

### **Virtual Company Confusion**
- **Definition**: Fake "Sourcing Window Company" for accounting workaround
- **Problem**: "Is it virtual or real?"
- **Quote**: "Virtual stuff is killing people"

---

## Strategic Terms

### **MVP Plus**
- **Definition**: Current capabilities plus key pain points addressed
- **Strategy**: "Lift and shift plus"
- **Target**: February launch for external users

### **Power Tools**
- **Definition**: Block-specific features vs general product features
- **Context**: "Specifically a Block enabler"
- **Decision**: What stays with Block vs product

### **Super-User/Super-Customer**
- **Definition**: Block's special status with enhanced integrations
- **Context**: "Block is super-user with automation"
- **Not**: Special case, but premium customer

### **External-First Launch**
- **Definition**: Releasing to external users before internal
- **Unusual**: Opposite of "eat your own dogfood"
- **Reason**: Avoid internal disruption

### **Hard Cut**
- **Definition**: Complete switchover vs parallel systems
- **Jeff's view**: "Head will explode" with parallel
- **Preference**: Clean transition

---

## Future Features

### **Voice Recognition**
- **Definition**: Speech-to-text for hands-free part ordering
- **Use case**: FSEs with hands busy under equipment
- **Vision**: "I need quotes on a C-WISP"

### **ConvoPro**
- **Definition**: Siemens-approved AI/chat platform
- **Purpose**: "Private AI cloud" for safe chat
- **Status**: "Disappointing implementation" currently

### **Fuzzy Matching**
- **Definition**: Search finding results despite typos/formatting
- **Need**: Handle hyphenation and spelling variations
- **Priority**: High for improving search

---

## Cultural Observations

### **"I don't do Salesforce"**
- **Speaker**: FSEs (Field Service Engineers)
- **Meaning**: Intentional system avoidance
- **Described as**: "Willing lack of understanding"

### **"If it's less clicks and better"**
- **Context**: Change acceptance criteria
- **Meaning**: Users will adopt if demonstrably improved
- **Key**: Must show clear value

### **"Fat Lego blocks" / "Duplo blocks"**
- **Definition**: Salesforce's large, inflexible components
- **Problem**: Limits granular customization
- **Impact**: Forces workarounds

---

## Vendor/Partner Terms

### **All Parts**
- **Definition**: Major third-party vendor with inventory API
- **Status**: "Plug and play" API available
- **Integration**: Phase 1 consideration

### **PartSource**
- **Definition**: Another major vendor partner
- **History**: Steve's former employer
- **API**: Established and ready

### **Common Spirit**
- **Definition**: Major healthcare customer using SWP
- **Example buyer**: Sarah Daly
- **Represents**: External buyer persona

---

*This dictionary represents the actual language used by Block Imaging stakeholders during discovery. It should be referenced to ensure all workflows, features, and documentation use terminology that resonates with users rather than generic technical terms.*

*Last Updated: September 10, 2025*