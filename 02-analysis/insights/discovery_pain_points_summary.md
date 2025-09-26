# Discovery Summary: Topics & Pain Points
## September 8-10, 2025 - Three Day Synthesis

---

## Executive Summary

Block Imaging's Sourcing Window platform requires fundamental restructuring to address systemic inefficiencies while preserving critical business operations. The discovery revealed a complex ecosystem where **"tribal knowledge"** sustains operations, **30+ browser tabs** define user workflows, and an **"eternal loop of doom"** exemplifies system failures. The path forward requires careful balance between revolutionary change and operational stability.

---

## Major Topics Across All Days

### 1. System Architecture Evolution
**Day 1**: Current state assessment - "Everything runs through Salesforce"
**Day 2**: Strategic vision - Sourcing Window as standalone product
**Day 3**: Technical implementation - 12+ objects, bi-directional sync

**Key Decision**: Sourcing Window v3 will be a standalone product that treats Block as a "super-customer" rather than building Block-specific solutions.

### 2. User Personas & Workflows
**Identified 8 personas** with distinct needs:
- External Buyers (SWP users like Common Spirit)
- Internal Buyers (Block procurement - 50+ daily orders)
- External Vendors (100+ in pool)
- Internal Management
- External Management
- Platform Admin
- FSE (Field Service Engineers)
- Biomed teams

**Critical Insight**: FSEs say "I don't do Salesforce" - requiring special workflow considerations.

### 3. Launch Strategy Reversal
**Traditional**: Internal first ("eat your own dogfood")
**Block's Approach**: External first to avoid internal disruption
**Rationale**: "Past trauma" from January 2023 rushed launch created two years of incomplete processes

### 4. Data Ownership & Integration
**Current**: Salesforce as source of truth
**Future**: Bi-directional synchronization between systems
**Challenge**: "Virtual company" workarounds creating confusion

---

## Critical Pain Points (Ranked by Impact)

### 🔴 **SEVERE - System Breaking**

1. **"Eternal Loop of Doom"**
   - Password reset traps users indefinitely
   - Requires manual intervention each time
   - Blocks system access completely

2. **Notification System Breakdown**
   - Engineers' actions don't trigger CSR alerts
   - "We don't get notifications... caused havoc"
   - Manual workarounds required constantly

3. **No Queue System**
   - Procurement team distributes work manually
   - 50+ orders per day handled individually
   - No visibility into workload distribution

### 🟠 **HIGH - Major Productivity Loss**

4. **"30 Tabs Open"**
   - CSRs juggle multiple systems simultaneously
   - "Cannot function with one more tab"
   - System fragmentation at its worst

5. **Search Functionality Failure**
   - "Creating duplicate materials because search sucks"
   - Part number formatting inconsistencies
   - No fuzzy matching capability

6. **Virtual vs Real Confusion**
   - "Sourcing Window Company" fake entity for accounting
   - "Is it virtual or real?" constant question
   - "Virtual stuff is killing people"

7. **Cancellation Process**
   - "Pain in the butt" to switch vendors after selection
   - Multiple manual steps required
   - No simple reselection flow

### 🟡 **MODERATE - Operational Friction**

8. **"Tribal Knowledge" Dependency**
   - "So much in Paul Beard's brain"
   - Critical decisions rely on individuals
   - No documented decision criteria

9. **Part Number Chaos**
   - Block adds hyphens, others don't
   - "Raw part number" formula is "super top secret"
   - No global uniqueness

10. **Manual Sourcing Overrides**
    - "I only want these two vendors"
    - Auto-sourcing frequently bypassed
    - Tier system not trusted

11. **Service Hold Complexity**
    - Parts reserved for contracts vs available
    - Manual tracking and allocation
    - Priority conflicts between sales and service

### 🟢 **LOW - Quality of Life**

12. **FSE Resistance**
    - "I don't do Salesforce"
    - "Willing lack of understanding"
    - Separate workflow needs ignored

13. **File Management**
    - Download to re-upload workaround
    - Multiple systems storing same files
    - Version control issues

---

## Recurring Themes

### Technology Debt
- **Legendary customizations** creating vendor lock-in
- **"Fat Lego blocks"** (Salesforce inflexibility)
- Multiple systems doing similar functions
- Search degraded over time ("used to have great search")

### Process Inefficiency
- Everything requires manual intervention
- Notifications unreliable or missing
- No automation where it's needed most
- Workarounds accepted as normal

### Communication Gaps
- Chatter vs EMA vs email confusion
- "At-mention anyone" security issues
- No unified messaging strategy
- Context lost between systems

### Change Management Fears
- "Past trauma" from 2023 launch
- Two years of unfinished processes
- Skepticism about FMD delivery
- Fear of retraining

---

## Solutions Identified

### Phase 1 (MVP Plus) - February Launch
✅ Fix authentication/password issues
✅ Unified messaging system (replacing EMA)
✅ Better search with fuzzy matching
✅ Single platform for external buyers/vendors
✅ Preserve internal workflows initially

### Phase 2-3 - Post Launch
📋 Migrate internal users gradually
📋 Implement queue system for procurement
📋 Add voice recognition for FSEs
📋 Auto-sourcing improvements
📋 Full bi-directional sync

### Deferred/Future
🔮 Biomed persona workflows
🔮 Complete Salesforce decoupling
🔮 Advanced AI features (ConvoPro)
🔮 Industry-wide part number standardization

---

## Risk Mitigation Strategies

### Technical Risks
- **Parallel Systems**: Jeff warns "head will explode" - plan hard cut
- **Synchronization**: Start manual, then add APIs
- **Data Migration**: 3-month active data, historical tab for rest

### Business Risks
- **Internal Adoption**: Beta user program with Sam, Vicki, Jordan
- **External Adoption**: Marketing engine required for February
- **Change Resistance**: "Less clicks and better" demonstration

### Operational Risks
- **Knowledge Transfer**: Document Paul Beard's decisions
- **Service Continuity**: No disruption to contracts
- **Vendor Relations**: Early engagement with All Parts, PartSource

---

## Success Metrics

### Must Have (February)
- Zero password reset loops
- All external users migrated
- Search success rate >90%
- Single sign-on working
- Basic messaging functional

### Should Have (Q2)
- Internal beta users active
- Queue system operational
- Notification reliability >99%
- API integration with major vendors
- Voice prototype demonstrated

### Nice to Have (Future)
- Full internal migration
- AI-powered features
- Industry-leading voice interface
- Complete Salesforce independence

---

## Key Stakeholder Quotes

**Paul Beard** (Executive): "November... December... January... February"
**Jeff** (FMD): "The simplest model is the platform lives on its own"
**Sam** (User): "If it's less clicks and better, they'll accept change"
**FSE**: "I don't do Salesforce, that's not for me"
**CSR**: "30 tabs open... cannot function with one more"

---

## Conclusion

The Sourcing Window v3 project represents more than a technical upgrade - it's an opportunity to fundamentally reimagine how Block Imaging operates. The pain points are clear, the solutions are achievable, and the stakeholders are aligned on the vision. Success requires respecting the "past trauma" while building toward a future where the platform can stand alone as a product.

The February MVP Plus launch should focus on eliminating the most painful friction points for external users while preserving internal operations. This approach allows Block to validate the new platform without risking core business operations, setting the stage for gradual internal adoption and eventual full migration.

---

*Compiled from 3 days of discovery sessions with Block Imaging and Avodah teams*
*Total participants: 15+ stakeholders across business, technical, and operational roles*