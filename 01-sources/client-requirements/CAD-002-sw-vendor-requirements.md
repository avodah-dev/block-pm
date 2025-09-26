# CAD-002: Sourcing Window (Vendor) Requirements

## Document Information
- **Document ID**: CAD-002
- **Title**: Sourcing Window (Vendor) Requirements
- **Source**: SW-cleaned.csv (from original Excel export)
- **Extracted Date**: 2025-09-25T17:11:04.864954
- **Total Requirements**: 57

## Requirements Summary by Category
- **MUST HAVE**: 43 requirements
- **SHOULD HAVE**: 6 requirements
- **COULD HAVE**: 4 requirements
- **NOT DOING**: 4 requirements

## MUST HAVE Requirements

### SW-M-1
**Requirement**: Ability to full manage suppliers while still agnostic to Block

**Details**: Assigning vendors capabilities, tracking DOA rates, etc for Block Imaging

**Phase**: Phase 1 - Let's talk about it

**New Functionality**: Yes/No (currently exists in Block system, needs to integrate into new system)

---

### SW-M-2
**Requirement**: Ability for vendors to have multiple 'capabilities'

**Details**: These are buckets we put them in to route requests to

**Phase**: Phase 1

**Process**: Sourcing and Vendor Management

**New Functionality**: No

---

### SW-M-3
**Requirement**: Must be able to rank each vendor within a capability with a tier

**Details**: Tiers 1-3 (+) based on vendor KPI

**Phase**: Phase 2 - Internal - synced with SF?

**New Functionality**: No

---

### SW-M-4
**Requirement**: Must be able to manage Customer Concession Vendors

**Details**: If not approved, or actively listed as customer concession by Block, teams need to still have visablity into capabilities

**Phase**: Phase 2 - Internal - synced with SF?

**New Functionality**: No

---

### SW-M-5
**Requirement**: Must be able to record vendor warehouse locations and shipping cut off times on Vendor Account

**Details**: There may be multiple, differing, options per supplier

**Phase**: Phase 2 - Internal - synced with SF?

**New Functionality**: Yes

---

### SW-M-6
**Requirement**: On Capability record, we must be able to include 'notes' visable to internal (Block) users only

**Phase**: Phase 2 - Internal - synced with SF?

**New Functionality**: No

---

### SW-M-7
**Requirement**: Ability for vendors to be connected to multiple customers

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-8
**Requirement**: Must be able to have multiple users under 1 account

**Phase**: Phase 1

**Process**: Users

**New Functionality**: No

---

### SW-M-9
**Requirement**: User must be able to see who is logged in from homepage

**Phase**: Phase 1

**Process**: Homepage

**New Functionality**: No

---

### SW-M-10
**Requirement**: Homepage must default to Open Requests

**Details**: Requests that have not yet been responded to

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-11
**Requirement**: Requests must order by oldest on top

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-12
**Requirement**: Requests (SRCs) must display with Time Open, SRC #, Requesting Customer, Material, Qty Requested and any notes customer put in at time of submission

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-13
**Requirement**: When responding from homepage view, user must be able to press 'unavailable' button without drilling into SRC

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-14
**Requirement**: From homepage view, Vendor must be able to view their connected customers

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-15
**Requirement**: From homepage view, vendor must be able to see Roll up of Pending Fulfillments

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-16
**Requirement**: From homepage view, vendor must be able to see Pending Fulfilments, Request History and Order History

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-17
**Requirement**: Vendor must be able to 'search' each list view (Open Requests, Pending Fulfillments, Request History, Order History)

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-18
**Requirement**: Pending Fulfillments tab must display  PO#, Customer, Item Description, Total, Age Open (measured by time passed since PO record was created, until PO record confirmed), Confirmed. Button to click in to to view Purchase Records, or hyperlink PO#

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-19
**Requirement**: Request History View: Tiem Open (shows vendor response time), Sourcing Item #, Customer Name, Item Description, Qty, Status / Disposition (rename disposition 'condition'), Pricing (EX/OR). Ability to click into SRC to view record (or add'l button to click into to view).

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-20
**Requirement**: Vendor must see SRC#, Item Description, Customer Name, Created Date, Requested Qty adn Request Notes (what customer entered at time of request)

**Phase**: Phase 1

**Process**: Responding to SRC

**New Functionality**: No

---

### SW-M-21
**Requirement**: Vendor to be able to respond from email without logging into portal

**Details**: Ex: Virtus Imaging

**Phase**: Phase 1 - Buttons or reply to the email

**New Functionality**: Yes

---

### SW-M-22
**Requirement**: Vendor must be able to click 'no stock button'

**Details**: This should automatically update the status to 'No stock' and close the record out, taking vendor to homepage

**Phase**: Phase 1

**New Functionality**: Yes

---

### SW-M-23
**Requirement**: Buttons at bottom of SRC: Submit Quote, Clone, No Stock

**Phase**: Phase 1

**New Functionality**: Yes/No (these are new names)

---

### SW-M-24
**Requirement**: To submit quote, vendor must enter Exchange Price, Outright Price, Condition, Warranty Period, Warranty Type

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-25
**Requirement**: Optional fields on SRC: Alternative Part Number, Date of Manufacturer, Item Usage.

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-26
**Requirement**: Quantity' field on SRC should default to 1, and be renamed to 'Qty available'

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-27
**Requirement**: New Check Box: 'This Item is on Backorder'

**Details**: If vendor selects this, it must be visable to customer in SWP / Block Imaging as it means this is NOT in stock

**Phase**: Phase 1 - Discuss

**New Functionality**: Yes

---

### SW-M-28
**Requirement**: If vendor Submits Quote, it keeps them on SRC record with a 'submitted' notification and allows them to clone it for a second option (third, 4th)

**Details**: Developers: Please propose alt. way of user offering multiple options for one material

**Phase**: Phase 1 - Discuss

**New Functionality**: Yes/No (currently exists in Block system, needs to integrate into new system)

---

### SW-M-29
**Requirement**: Vendor must be able to view all connected cloned options in their history

**Phase**: Phase 1

**New Functionality**: Yes

---

### SW-M-30
**Requirement**: Vendor must be able to view customer user on the EMA and send messages, files, photos, etc

**Details**: EMA = Messsage app

**Phase**: Phase 1 - Important

**New Functionality**: Yes/No (currently exists in Block system, needs to integrate into new system)

---

### SW-M-31
**Requirement**: Vendor must be able to click into order from 'Pending Fulfilments' view and from link in email

**Phase**: Phase 1

**Process**: Processing Orders

**New Functionality**: No

---

### SW-M-32
**Requirement**: Vendor must see same view as customer here: Recap of purchase fields (Customer Name, PO#, Issued Date, Total USE

**Phase**: Phase 1

---

### SW-M-33
**Requirement**: Vendor must be able to click 'Confirm Order' Button

**Details**: Launches email notification to customer that order is en process, stops timer

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-34
**Requirement**: Vendor must be able to enter tracking, Serial Number, RMA number

**Details**: When submitted, customer gest email w/notification

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-35
**Requirement**: Vendor must be able to save all or one of the fields above. Notification only fires to customer when all 3 fields are entered

**Phase**: Phase 1

**New Functionality**: Yes

---

### SW-M-36
**Requirement**: Vendor must be able to send and receive messages on sourcing record (notifications firing for each)

**Phase**: Phase 1

**Process**: EMA

**New Functionality**: No

---

### SW-M-37
**Requirement**: Vendor must be able to send/recieve notifications on order record

**Details**: notifications firing for each

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-38
**Requirement**: Once a sourcing record has been purchased, vendor may still use EMA on that record but guided to PO record if messages are related to order itself

**Phase**: Phase 1

**New Functionality**: No

---

### SW-M-39
**Requirement**: Vendor must receive a notification to the email (on the capability) for a new request

**Phase**: Phase 1

**Process**: Notifications

---

### SW-M-40
**Requirement**: Vendor must receive a notification via email for a PO

**Phase**: Phase 1

---

### SW-M-41
**Requirement**: Vendor must receive a notificaiton via email for a chatter (EMA)

**Phase**: Phase 1

---

### SW-M-42
**Requirement**: Vendor must have ability to click into link on every email notification to be taken directly to that record

**Phase**: Phase 1

---

### SW-M-43
**Requirement**: Vendor must be able to receive orders for warranty replacement from customers

**Details**: Vendor must KNOW it's a warranty, know why, and be prompted to provide warranty RMA

**Phase**: Phase 1

**New Functionality**: YES

---

## SHOULD HAVE Requirements

### SW-S-1
**Requirement**: FAQ tab on SW Homepage

**Details**: A place where venders can access training videos, tips and tricks, release updates, etc

**Phase**: Phase 1

**New Functionality**: Yes

---

### SW-S-2
**Requirement**: Vendors should be able to view their shipping cut offs from portal view in SW

**Details**: On home page, so they can request edits as neede

**Phase**: Phase 1 - Discuss

**New Functionality**: Yes/No (currently exists in Block system, needs to integrate into new system)

---

### SW-S-3
**Requirement**: Ability for vendors to view all req items that are connected to a single Req

**Details**: This helps them understand bulk sales opportunities, hero kits, etc

**Phase**: Phase 1

**New Functionality**: Yes

---

### SW-S-4
**Requirement**: Legal agreements for buyers / vendors (some sort of T's&C's for using the portal)

**Details**: Not a dev. requirement*

**Phase**: Phase 2

**New Functionality**: Yes

---

### SW-S-5
**Requirement**: Vendor should be able to Cancel a PO if they can no longer fulfil it

**Details**: This would auto-close stages & status to 'Cancelled' and must issue notification to customer that order was cancelled.

**Phase**: Phase 1 - Discuss

**New Functionality**: Yes

---

### SW-S-6
**Requirement**: If vendor does not response to an SRC within 7 days, the record should automatically move to history as a 'No Response' status (ie: removed from homepage, timer stops)

**Phase**: Phase 1 - Discuss

**New Functionality**: Yes

---

## COULD HAVE Requirements

### SW-C-1
**Requirement**: Ability for Vendor to Export Views / Data from portal

**Phase**: Phase 2+

---

### SW-C-2
**Requirement**: Ability for internal Block teams to propose new suppliers

**Details**: This would trigger Vendor Quality team + SW team to vet and onboard new supplies

**Phase**: Phase 2+

**New Functionality**: Yes

---

### SW-C-3
**Requirement**: Ability for vendors to upload / view their Terms and Conditions

**Details**: At the very least this should live on account in Block SF

**Phase**: Phase 2+

**New Functionality**: Yes

---

### SW-C-4
**Requirement**: Ability for vendors to view their approval status in SW

**Details**: Auto alert from Sourcing Window when they are about to expire, and ability to fill out form and submit to re-new.

**Phase**: Phase 2+

**New Functionality**: Yes

---

## NOT DOING Requirements

### SW-N-1
**Requirement**: Any connection to Legendary - and fully agnostic to Block's SF org

**Phase**: Phase 1

---

### SW-N-2
**Requirement**: In SW, There will not be an editable 'status'

**Phase**: Phase 1

**Process**: On SRC Record

---

### SW-N-3
**Requirement**: In SW, there will not be a 'cancel' button

**Phase**: Phase 1

---

### SW-N-4
**Requirement**: in SW, there will not be a 'save' button

**Phase**: Phase 1

---
