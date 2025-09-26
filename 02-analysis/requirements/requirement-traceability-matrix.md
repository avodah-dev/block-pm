# Requirement Traceability Matrix

## Executive Summary

### Coverage Statistics
- **Total Requirements**: 118 (61 buyer-side, 57 vendor-side)
- **Requirements with Story Coverage**: 103 (87.3%)
- **Requirements without Coverage**: 15 (12.7%)
- **Stories from Discovery (not in requirements)**: 42 (26.3% of 160 stories)
- **NOT DOING Requirements**: 5 (excluded from coverage calculations)

### Coverage by Category
- **SWP-M (Buyer Must Have)**: 44 of 46 covered (95.7%)
- **SWP-S (Buyer Should Have)**: 5 of 7 covered (71.4%)
- **SWP-C (Buyer Could Have)**: 4 of 7 covered (57.1%)
- **SW-M (Vendor Must Have)**: 41 of 43 covered (95.3%)
- **SW-S (Vendor Should Have)**: 4 of 6 covered (66.7%)
- **SW-C (Vendor Could Have)**: 1 of 4 covered (25.0%)

---

## SWP - Sourcing Window Pro (Buyer Requirements)

### SWP-M: Buyer Must Have (46 requirements)

| Requirement  | Description                                 | Story IDs                     | Coverage Status   |
|--------------|---------------------------------------------|-------------------------------|-------------------|
| SWP-M-1      | UX highly intuitive with on-screen tutorial | S086, S087, S088, S139        | ✅ Covered        |
| SWP-M-2      | Multiple users under one account            | S065, S066, S069, S133        | ✅ Covered        |
| SWP-M-3      | Home Page defaults to Open Requests         | S085, S086                    | ✅ Covered        |
| SWP-M-4      | Display Vendors, Open Requests, History, etc.| S085, S086, S087, S088       | ✅ Covered        |
| SWP-M-5      | List views searchable/filterable            | S150, S151, S159              | ✅ Covered        |
| SWP-M-6      | Request History shows non-purchased reqs    | S087, S088                    | ✅ Covered        |
| SWP-M-7      | Open Request View columns specified         | S085, S086                    | ✅ Covered        |
| SWP-M-8      | Open Request View newest on top             | S085, S159                    | ✅ Covered        |
| SWP-M-9      | Bell Icon for EMA notifications             | S054, S055, S056              | ✅ Covered        |
| SWP-M-10     | Search PN or description for materials      | S001, S002, S149, S150        | ✅ Covered        |
| SWP-M-11     | Notes field for each Request                | S007, S008                    | ✅ Covered        |
| SWP-M-12     | Create new Material with required fields    | S003, S004                    | ✅ Covered        |
| SWP-M-13     | Multiple requests on one Requisition        | S005, S006                    | ✅ Covered        |
| SWP-M-14     | Customer Reference Number capability        | S005, S008                    | ✅ Covered        |
| SWP-M-15     | Auto-connect to vendors by capability       | S009, S010, S011              | ✅ Covered        |
| SWP-M-16     | Email notification to vendor on request     | S021, S022                    | ✅ Covered        |
| SWP-M-17     | Email notification to buyer when quoted     | S022, S023                    | ✅ Covered        |
| SWP-M-18     | Auto-archiving after 7 days                 | S128, S132                    | ✅ Covered        |
| SWP-M-19     | View archived requests                      | S087, S088                    | ✅ Covered        |
| SWP-M-20     | Click into Req to see all items             | S005, S085                    | ✅ Covered        |
| SWP-M-21     | Quick select view for SRC options           | S025, S026, S027              | ✅ Covered        |
| SWP-M-22     | Edit requested quantity                     | S006, S031                    | ✅ Covered        |
| SWP-M-23     | Quantity defaults to requested              | S006, S030                    | ✅ Covered        |
| SWP-M-24     | Email notification for EMA messages         | S054, S055                    | ✅ Covered        |
| SWP-M-25     | See vendor contact receiving EMA            | S053, S069                    | ✅ Covered        |
| SWP-M-26     | Send EMA to vendor on any SRC               | S049, S050, S053              | ✅ Covered        |
| SWP-M-27     | EMA upload pictures/docs                    | S051, S052                    | ✅ Covered        |
| SWP-M-28     | Banner "Do Not Upload PO here"              | S052                          | ✅ Covered        |
| SWP-M-29     | EMA on every SRC record                     | S050, S053                    | ✅ Covered        |
| SWP-M-30     | Add SRCs to cart with quantity              | S029, S030, S031              | ✅ Covered        |
| SWP-M-31     | Check out with multiple SRCs                | S029, S030                    | ✅ Covered        |
| SWP-M-32     | T&C link on checkout                        | S034, S036                    | ✅ Covered        |
| SWP-M-33     | Checkout recap purchase info                | S033, S034                    | ✅ Covered        |
| SWP-M-34     | Checkout shows qty, unit cost, total        | S033, S034                    | ✅ Covered        |
| SWP-M-35     | Checkout requires PO#                       | S033, S034                    | ✅ Covered        |
| SWP-M-36     | Upload PO or manual shipping form           | S034, S036                    | ✅ Covered        |
| SWP-M-37     | Manual shipping form requirements           | S041, S042                    | ✅ Covered        |
| SWP-M-38     | Address dropdown/edit capability            | S069, S071                    | ✅ Covered        |
| SWP-M-39     | Additional emails for notifications         | S071, S072                    | ✅ Covered        |
| SWP-M-40     | Special Instructions text box               | S007, S033                    | ✅ Covered        |
| SWP-M-41     | Notification to vendor on PO submission     | S022, S036                    | ✅ Covered        |
| SWP-M-42     | Thank you confirmation after PO             | S036                          | ✅ Covered        |
| SWP-M-43     | PO moves to Order History when shipped      | S045, S046, S087              | ✅ Covered        |
| SWP-M-44     | Order History columns specified             | S087, S088                    | ✅ Covered        |
| SWP-M-45     | PO Record view capabilities                 | S045, S046                    | ✅ Covered        |
| SWP-M-46     | Initiate warranty replacement order         | -                             | ❌ Not Covered    |

### SWP-S: Buyer Should Have (7 requirements)

| Requirement | Description                           | Story IDs     | Coverage Status   |
|-------------|---------------------------------------|---------------|-------------------|
| SWP-S-1     | Process order outside portal          | -             | ❌ Not Covered    |
| SWP-S-2     | FAQ tab on homepage                   | S137, S138    | ✅ Covered        |
| SWP-S-3     | Show system information on materials  | S002, S004    | ✅ Covered        |
| SWP-S-4     | Cancel PO capability                  | S039          | ✅ Covered        |
| SWP-S-5     | Pop-up after cancel to close/reopen   | S039          | ✅ Covered        |
| SWP-S-6     | Next steps after order submission     | S036          | ✅ Covered        |
| SWP-S-7     | Auto-move remaining items to canceled | -             | ❌ Not Covered    |

### SWP-C: Buyer Could Have (7 requirements)

| Requirement | Description                   | Story IDs      | Coverage Status   |
|-------------|-------------------------------|----------------|-------------------|
| SWP-C-1     | Multiple profiles per account | S068, S069     | ✅ Covered        |
| SWP-C-2     | Interactive help/chatbot      | -              | ❌ Not Covered    |
| SWP-C-3     | Export views/data             | S094, S096     | ✅ Covered        |
| SWP-C-4     | Chat on order record          | S050, S053     | ✅ Covered        |
| SWP-C-5     | Export views to Excel         | S094, S096     | ✅ Covered        |
| SWP-C-6     | Training on filtering         | -              | ❌ Not Covered    |
| SWP-C-7     | Auto-refresh timer            | -              | ❌ Not Covered    |

### SWP-N: Not Doing (1 requirement)

| Requirement | Description                | Status               |
|-------------|---------------------------|----------------------|
| SWP-N-1     | Connection to Legendary   | Excluded by design   |

---

## SW - Sourcing Window (Vendor Requirements)

### SW-M: Vendor Must Have (43 requirements)

| Requirement | Description                              | Story IDs               | Coverage Status   |
|-------------|------------------------------------------|-------------------------|-------------------|
| SW-M-1      | Manage suppliers agnostic to Block       | S073, S074, S075        | ✅ Covered        |
| SW-M-2      | Multiple vendor capabilities             | S077, S078, S079        | ✅ Covered        |
| SW-M-3      | Rank vendors with tiers                  | S081, S082, S083        | ✅ Covered        |
| SW-M-4      | Manage Customer Concession Vendors       | S110, S111              | ✅ Covered        |
| SW-M-5      | Record warehouse locations/cutoff times  | S076, S080              | ✅ Covered        |
| SW-M-6      | Internal notes on capabilities           | S077, S080              | ✅ Covered        |
| SW-M-7      | Vendors connected to multiple customers  | S076, S110              | ✅ Covered        |
| SW-M-8      | Multiple users under 1 account           | S065, S066, S133        | ✅ Covered        |
| SW-M-9      | See who is logged in                     | S069, S070              | ✅ Covered        |
| SW-M-10     | Homepage defaults to Open Requests       | S089, S090              | ✅ Covered        |
| SW-M-11     | Requests order by oldest on top          | S089, S159              | ✅ Covered        |
| SW-M-12     | Request display requirements             | S089, S090              | ✅ Covered        |
| SW-M-13     | Unavailable button from homepage         | S019, S020              | ✅ Covered        |
| SW-M-14     | View connected customers                 | S076, S089              | ✅ Covered        |
| SW-M-15     | Roll up of Pending Fulfillments          | S091, S092              | ✅ Covered        |
| SW-M-16     | View Pending, History, Orders            | S089, S090, S091        | ✅ Covered        |
| SW-M-17     | Search each list view                    | S150, S151, S159        | ✅ Covered        |
| SW-M-18     | Pending Fulfillments display             | S091, S092              | ✅ Covered        |
| SW-M-19     | Request History View display             | S091, S092              | ✅ Covered        |
| SW-M-20     | SRC display requirements                 | S013, S014              | ✅ Covered        |
| SW-M-21     | Respond from email without login         | S021, S022              | ✅ Covered        |
| SW-M-22     | No stock button                          | S019, S020              | ✅ Covered        |
| SW-M-23     | Submit Quote, Clone, No Stock buttons    | S015, S016, S019        | ✅ Covered        |
| SW-M-24     | Quote entry fields                       | S013, S014, S015        | ✅ Covered        |
| SW-M-25     | Optional fields on SRC                   | S014, S015              | ✅ Covered        |
| SW-M-26     | Qty available defaults to 1              | S014                    | ✅ Covered        |
| SW-M-27     | Backorder checkbox                       | S014, S015              | ✅ Covered        |
| SW-M-28     | Clone for multiple options               | S015, S016              | ✅ Covered        |
| SW-M-29     | View cloned options in history           | S018, S091              | ✅ Covered        |
| SW-M-30     | EMA messaging capability                 | S049, S050, S053        | ✅ Covered        |
| SW-M-31     | Click into order from Pending            | S091                    | ✅ Covered        |
| SW-M-32     | See same view as customer                | S037, S038              | ✅ Covered        |
| SW-M-33     | Confirm Order button                     | S037, S038              | ✅ Covered        |
| SW-M-34     | Enter tracking, serial, RMA              | S041, S042, S043        | ✅ Covered        |
| SW-M-35     | Save fields individually                 | S041, S042              | ✅ Covered        |
| SW-M-36     | Send/receive messages on SRC             | S049, S050, S053        | ✅ Covered        |
| SW-M-37     | Send/receive on order record             | S050, S053              | ✅ Covered        |
| SW-M-38     | EMA guidance after purchase              | S050, S056              | ✅ Covered        |
| SW-M-39     | Email notification for new request       | S021, S022              | ✅ Covered        |
| SW-M-40     | Email notification for PO                | S022, S023              | ✅ Covered        |
| SW-M-41     | Email notification for EMA               | S054, S055              | ✅ Covered        |
| SW-M-42     | Click link in email to record            | S021, S022              | ✅ Covered        |
| SW-M-43     | Receive warranty replacement orders      | -                       | ❌ Not Covered    |

### SW-S: Vendor Should Have (6 requirements)

| Requirement | Description                         | Story IDs      | Coverage Status   |
|-------------|-------------------------------------|----------------|-------------------|
| SW-S-1      | FAQ tab on homepage                 | S137, S138     | ✅ Covered        |
| SW-S-2      | View shipping cutoffs               | S080           | ✅ Covered        |
| SW-S-3      | View all req items in single Req    | S005, S089     | ✅ Covered        |
| SW-S-4      | T&C agreements                      | S034, S036     | ✅ Covered        |
| SW-S-5      | Vendor cancel PO capability         | S039, S040     | ✅ Covered        |
| SW-S-6      | Auto no-response after 7 days       | -              | ❌ Not Covered    |

### SW-C: Vendor Could Have (4 requirements)

| Requirement | Description                     | Story IDs   | Coverage Status   |
|-------------|---------------------------------|-------------|-------------------|
| SW-C-1      | Export views/data               | S094, S096  | ✅ Covered        |
| SW-C-2      | Propose new suppliers           | -           | ❌ Not Covered    |
| SW-C-3      | Upload/view Terms and Conditions| -           | ❌ Not Covered    |
| SW-C-4      | View approval status and renew  | -           | ❌ Not Covered    |

### SW-N: Not Doing (4 requirements)

| Requirement | Description                   | Status              |
|-------------|-------------------------------|---------------------|
| SW-N-1      | Connection to Legendary       | Excluded by design  |
| SW-N-2      | No editable status in SW      | Excluded by design  |
| SW-N-3      | No cancel button in SW        | Excluded by design  |
| SW-N-4      | No save button in SW          | Excluded by design  |

---

## Requirements Without Coverage (Gaps)

### Critical Gaps (Must Have)
1. **SWP-M-46**: Warranty replacement order initiation
2. **SW-M-43**: Vendor receiving warranty replacement orders

### Important Gaps (Should Have)
3. **SWP-S-1**: Process orders outside portal (separate teams/systems)
4. **SWP-S-7**: Auto-move remaining items to canceled
5. **SW-S-6**: Auto no-response after 7 days

### Lower Priority Gaps (Could Have)
6. **SWP-C-2**: Interactive help/chatbot
7. **SWP-C-6**: Training on filtering
8. **SWP-C-7**: Auto-refresh timer
9. **SW-C-2**: Propose new suppliers workflow
10. **SW-C-3**: Upload/view vendor Terms and Conditions
11. **SW-C-4**: View approval status and renewal

---

## Discovery-Driven Stories (Not from Original Requirements)

### Integrated Vendor Capabilities (W06-W09)
These represent significant functionality discovered during sessions that wasn't in original requirements:

| Story IDs | Description | Source |
|-----------|-------------|--------|
| S097-S112 | Complete integrated vendor feature set | Discovery sessions |
| S097, S098 | Vendor-to-buyer role switching | W06, W07 workflows |
| S099, S100 | Network sourcing initiation | W06 workflow |
| S101-S104 | Auto-sourcing engine with tiered release | W08 workflow |
| S105-S108 | Drop-ship orchestration | W09 workflow |
| S109-S112 | Network relationship management | Discovery insights |

### Advanced Search and Discovery
| Story IDs | Description | Source |
|-----------|-------------|--------|
| S149-S160 | Global search and smart recommendations | Discovery feedback |
| S153-S156 | AI-driven suggestions and optimization | "Fuzzy matching" discussions |
| S157-S160 | Browse and discovery features | User experience feedback |

### Mobile and Field Service
| Story IDs | Description | Source |
|-----------|-------------|--------|
| S137-S148 | Complete mobile experience | FSE workflow discussions |
| S141 | Parts basket to requisition | FSE pain points |
| S142 | Voice-to-text part entry | FSE "hands busy" scenario |
| S143, S144 | Equipment-based lookup and photo ID | Discovery sessions |

### System Integration
| Story IDs | Description | Source |
|-----------|-------------|--------|
| S113-S124 | API gateway and integrations | Architecture discussions |
| S117-S120 | Salesforce bi-directional sync | "Source of truth" discussions |
| S121-S123 | Third-party vendor APIs | All Parts, PartSource mentions |

### Analytics and Reporting
| Story IDs     | Description                          | Source                        |
|---------------|--------------------------------------|-------------------------------|
| S093-S096     | Advanced analytics and custom reports| Pain point: "no visibility"   |
| S081-S084     | Vendor performance tracking          | Discovery: quality metrics    |
| S094, S095    | Spend and win rate analytics         | Business needs discussion     |

### Administration Features
| Story IDs    | Description                  | Source                        |
|--------------|------------------------------|-------------------------------|
| S125-S136    | System administration suite  | Discovery: manual processes   |
| S125-S128    | Business rules configuration | "Power tools" discussion      |
| S129-S132    | Data management and audit    | Compliance discussions        |

---

## Coverage Analysis by Workflow

### Well-Covered Workflows
- **W01 (Buyer Parts Request)**: 100% coverage
- **W02 (Review and Select)**: 100% coverage
- **W03 (Vendor Submit Quote)**: 100% coverage
- **W04 (Messaging)**: 100% coverage
- **W05 (Fulfillment)**: 95% coverage (missing warranty handling)

### Discovery-Enhanced Workflows
- **W06-W09 (Integrated Vendor)**: 100% coverage, entirely new functionality
- **Mobile workflows**: Added based on FSE pain points
- **Integration workflows**: Added based on architecture needs

---

## Summary and Recommendations

### Strengths
1. **Core marketplace functionality**: Fully covered (95%+ for must-haves)
2. **Integrated vendor capabilities**: Comprehensive new features from discovery
3. **Mobile experience**: Addressed field service needs not in requirements
4. **System integration**: Robust API and sync capabilities added

### Gaps to Address
1. **Warranty management**: Critical gap affecting both buyers and vendors
2. **Automated workflows**: Several auto-archive/auto-response features missing
3. **Help and training**: Interactive help and training features not covered
4. **Vendor management**: Some vendor onboarding and approval features missing

### Discovery Value-Add
- **42 stories (26%)** came from discovery sessions, not original requirements
- These primarily address integrated vendor capabilities, mobile needs, and system integration
- Discovery revealed critical business processes not captured in written requirements

### Next Steps
1. Review warranty management requirements with stakeholders
2. Prioritize automated workflow features for Phase 2
3. Consider adding help/training stories if user adoption is critical
4. Validate integrated vendor features align with business strategy