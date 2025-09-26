# CAD-001: Sourcing Window Pro (Buyer) Requirements

## Document Information
- **Document ID**: CAD-001
- **Title**: Sourcing Window Pro (Buyer) Requirements
- **Source**: SWP-cleaned.csv (from original Excel export)
- **Extracted Date**: 2025-09-25T17:15:53.553900
- **Total Requirements**: 61

## Requirements Summary by Category
- **MUST HAVE**: 46 requirements
- **SHOULD HAVE**: 7 requirements
- **COULD HAVE**: 7 requirements
- **NOT DOING**: 1 requirements

## MUST HAVE Requirements

### SWP-M-1
**Requirement**: UX must be highly intuitive (like amazon) and buyer must be able to be guided thorugh the process (on-screen tutorial)

**Phase**: Phase 1

**New Functionality**: Yes

**Notes**: tutorial? Popover?

---

### SWP-M-2
**Requirement**: Multiple users under one account

**Details**: Shared data for account

**Phase**: Phase 1 - Discuss (Mark)

**New Functionality**: No

**Notes**: Organization? Add users? Remove users? (any other rights?)

**Phase 1 Notes**: Org Admin + users (Email block for add/remove)

**Future Notes**: Manage org (add/remove, dashboard to see insights)

---

### SWP-M-3
**Requirement**: Home Page must default to Open Requests

**Phase**: Phase 1

**Process**: Home Page Access

**New Functionality**: No

---

### SWP-M-4
**Requirement**: Home Page must display their Vendors, Open Requests, Request History, Order History, SRC History and Pending Orders

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-5
**Requirement**: List views for each (Open Requests, Request History, Order History, SRC History, Pending ORders) must be searchable / filterable

**Phase**: Phase 1

---

### SWP-M-6
**Requirement**: Request History must show all created Reqs that were not purchased

**Details**: must also show status, which could be 'Cancelled, Not Needed, Archived'

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-7
**Requirement**: Open Request View must list: Req / Customer Ref #, Item Description, Sourcing Status, Created By and Created Date

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-8
**Requirement**: Open Request View must show newest on top

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-9
**Requirement**: Home page must list Bell Icon for EMA notifications

**Details**: Alerts user that they have a pending message

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-10
**Requirement**: Ability for user to search PN or description to see Material Options

**Phase**: Phase 1 - Discuss

**Process**: Creating Requisitions

**New Functionality**: No

**Notes**: exact/fuzzy matches only?
Assuming NOT including equivalent parts?
PARTS Question - who controls parts list? Block SF, each buyer/vendor, or SW3?

**Phase 1 Notes**: fuzzy search (part number) or description

**Future Notes**: Improved search (possible AI to help with suggestions)

---

### SWP-M-11
**Requirement**: Ability for SWP user to fill out 'notes' for each Request

**Details**: Notes must be visable to their connected vendors

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-12
**Requirement**: Ability for SWP user to create a new Material

**Details**: This must be guided with required fields for Classification, Modality, Manufacturer, Part Number and Description

**Phase**: Phase 1

**New Functionality**: No

**Notes**: Currently saved to SF?
Future maintained in SW3? How do we stop slop from being added? Is there an approval process?

**Phase 1 Notes**: User can add just like current

**Future Notes**: Process to help improve quality, AI help etc

---

### SWP-M-13
**Requirement**: Ability for user to create a Requisition with multiple requests (Req items) on it

**Details**: Req can have anywhere from 1-multiple items

**Phase**: Phase 1

**New Functionality**: No

**Notes**: Can we treat like amazon? Multiple parts, different vendors
Past orders show individual parts not orders
This allows a buyer to start a req with 5 parts but be able to checkout with just 4 parts when ready, or 2 parts from one vendor annd 3 parts from another

This is just a way to track a group of reqs

**Phase 1 Notes**: req can have multiple part requests on them

---

### SWP-M-14
**Requirement**: Ability for Buyer to Add a Customer Reference Number

**Details**: Doing so can help them identify which Reqs are related to a specific deal. In Legacy, it was hyperlinked, and if you selected the link it would show you ALL Reqs that refernece that Customer Refernce Number. We lost this ability in SF360

**Phase**: Phase 1

**New Functionality**: Yes/No

---

### SWP-M-15
**Requirement**: Ability for a Req Item to automatically connect to the connected vendors in the right 'bucket'

**Details**: based on vendor capabilities in Block org

**Phase**: Phase 1

**New Functionality**: No

**Notes**: how are vendors notified of a new "bucket" or update?

**Phase 1 Notes**: Assuming we use SF360 capabilities (duplicate for SW3)

**Future Notes**: Manage in SW3 (allow vendors to set their own)?

---

### SWP-M-16
**Requirement**: Notification launches via email to vendor when Req Item is created

**Details**: When customer submits a Req, email fires to connected vendors to alert them

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-17
**Requirement**: Email Notification to Customer when Vendor quotes

**Details**: Quoted

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-18
**Requirement**: Auto Archiving: Reqs open for 7 days or longer must automatically be archived

**Details**: This should involve updating Req Stage to 'archived / not needed, etc'

**Phase**: Phase 1

**New Functionality**: No

**Notes**: Personally I dont love "auto" doing things unless the user asks, opts in or can modify

---

### SWP-M-19
**Requirement**: Buyer must be able to view Archived Reqs (request history)

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-20
**Requirement**: Buyer must be able to click into Req and see all requested Req Items

**Details**: This let's them see 1+ parts on the order, with ability to drill down further to see purchasing options

**Phase**: Phase 1

**Process**: Req Item View

**New Functionality**: No

**Notes**: I would argue - a req with mult parts is just a fast way to multi req but post that initial they become individual. They can be grouped for checking out (like add to cart) but otherwise seperate. So that a missing item on the order doesnt hold up the process. Or you can checkout with different vendors, if you want 2 items from one vendor and 1 from the other - based on quotes

---

### SWP-M-21
**Requirement**: Under req item, Buyer must view all SRC options in one view to do a 'quick select' of their preferred choice

**Details**: SRC's live under Req Items, Req items live under Req. SRC's should have 5 columns: Supplier, Pricing (Ex/OR), Warranty, Status/Condition,Sourcing Quantity (Sam to check this)

**Phase**: Phase 1

---

### SWP-M-22
**Requirement**: Customer must have ability to edit originally requested quantity for a Req Item

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-23
**Requirement**: Quantity should default to quantity customer REQUESTED

**Phase**: Phase 1

**New Functionality**: Yes, currently defaults to qty vendor quotes

**Notes**: If vendor only has 1, I would assume the user should be able to buy the 1 and get the remainder from someone else

---

### SWP-M-24
**Requirement**: Email notification to Customer when vendor sends EMA message

**Phase**: Phase 1

**Process**: EMA (Messaging)

**New Functionality**: No

---

### SWP-M-25
**Requirement**: Ability for customer to see vendor that would be receiving EMA (vendor contact)

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-26
**Requirement**: Ability for customer to send an EMA to a vendor on any SRC

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-27
**Requirement**: EMA: Ability to upload pictures / docs

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-28
**Requirement**: EMA: Banner that says 'Do Not Upload PO here'

**Details**: This is a common user mistake, and curretnly breaks entire connection

**Phase**: Phase 1 - Discuss

**New Functionality**: Yes

---

### SWP-M-29
**Requirement**: EMA should live on every single SRC record

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-30
**Requirement**: From Req Item, buyer must be able to add SRCs to cart (in doing so, must confirm quantity and purchase type)

**Phase**: Phase 1

**Process**: Check Out / Purchase Process

**New Functionality**: No

---

### SWP-M-31
**Requirement**: Buyer must be able to check out with multiple SRCs if one doesn't meet requested qty

**Phase**: Phase 1

---

### SWP-M-32
**Requirement**: Check Out Page must list link to T&C's for purchasing parts through portal

**Phase**: Phase 1

**New Functionality**: Yes

---

### SWP-M-33
**Requirement**: Check out page must recap purchase info: Description of material, Vendor purchasing it from, Req #, Buyer Name, Total cost

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-34
**Requirement**: Check out page must include qty purchased, unit cost and total for each part (Req item)

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-35
**Requirement**: Check Out page must require a PO#

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-36
**Requirement**: Check Out page must require 1 of 2 options: Hard copy PO to be uploaded (default) or Manual Shipping form to be be completed

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-37
**Requirement**: Manual Shipping must require: Shipping Method Drop Down (Fedex shipping levels, UPS shipping levels, etc), Shipping Account number, Recipeint First and last names, Recipient phone,  Ship To Address

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-38
**Requirement**: Buyer should be able to select / edit from drop down of addresses, or be able to add another address (that will moving forward be on their drop down list)

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-39
**Requirement**: Check out page must give option for buyer to add additional emails for post-sale notifications

**Details**: This gives them the ability to have tracking automatically sent to engineer or other person

**Phase**: Phase 1

**New Functionality**: no

---

### SWP-M-40
**Requirement**: Check out page must contain a 'Special Instructions' text box. If text is entered here, it must display on the PO notification email received by the vendor AND on the PO view once the vendor clicks in

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-41
**Requirement**: Notification to vendor must fire when buyer presses 'Submit PO to Vendor' button.

**Details**: Notification will be the "Congratulations, you have a PO!" template

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-42
**Requirement**: After Customer submits their PO, Customer should see completed PO record with attachments and a 'Thank you for your order!' confirmation of some sort.  If they X out of this, they should be taken back to their home page.

**Phase**: Phase 1

**New Functionality**: No

---

### SWP-M-43
**Requirement**: Once Vendor Ships Order, PO moves to 'Order History' on SWP Buyer Homepage

**Phase**: Phase 1

---

### SWP-M-44
**Requirement**: Order History must list the following columns: PO#, Vednor, Description (material purchased), Quantity, Net Unit Amount, Serial #'s, Tracking Numeber, RMA #, Purchase Date, and ability to click into the PO record and view purchase details

**Phase**: Phase 1

---

### SWP-M-45
**Requirement**: PO Record must allow buyer to view hard copy PO, materials purchased, the ability to click and view the SRC and access EMA records and (post shipment) the Tracking, SN adn RMA #

**Phase**: Phase 1

---

### SWP-M-46
**Requirement**: Customer must be able to initiate a warranty replacement order off of the original Req

**Details**: Reqs are tied together for easy viewing / reporting. Impacts notifications and vendors

**Phase**: Phase 1 - Discuss

**New Functionality**: YES

---

## SHOULD HAVE Requirements

### SWP-S-1
**Requirement**: Ability for a Customer to Indicate what was purchased but process order outside of portal

**Details**: Currently customer has to add SRC to cart and check up, requiring them to upload a PO and submit. Many large hospitals have completely separate teams or automated systems that will generate the PO and send them. We need a solution to allow for us to still track purchasing information, but not require the sending of the PO through the portal

**Phase**: Phase 2?

**New Functionality**: Yes

**Notes**: We could have a specific inbox that could try to automate this? Require the PO to reference something or supplier of some kind

---

### SWP-S-2
**Requirement**: FAQ tab on SWP Homepage

**Details**: A place where buyers can access training videos, tips and tricks, release updates, etc

**Phase**: Phase 1 - Discuss

**New Functionality**: Yes

---

### SWP-S-3
**Requirement**: Materials should show customers and vendors System information

**Details**: Currently portal visability prevents them from seeing the system, it only shows description, modality and manufacturer.

**Phase**: Phase 1 - Discuss

**New Functionality**: Yes

**Notes**: what is "system" info

---

### SWP-S-4
**Requirement**: From the Pending Orders View, the Customer should be able to select 'Cancel PO'

**Details**: To cancel an order, it would need to update the status of the PO to 'Cancelled' , fire an email notification to vendor telling them the PO was cancelled, and move record into Order History with a visual or designator that it was cancelled. We should record and communicate WHY the order was cancelled

**Phase**: Phase 1

**New Functionality**: Yes

**Notes**: I would assume you can cancel up until the vendor marks the order "shipped" or something

---

### SWP-S-5
**Requirement**: If Order was cancelled, the customer should get a Pop up asking if they want to close out the Requisition as Not Needed or to purchase a different SRC (ie: They can add another option to the cart and check out again, as the record was re-opened once they cancelled their first PO)

**Phase**: Phase 1

**New Functionality**: Yes

---

### SWP-S-6
**Requirement**: After customer submits order and goes to PO Confirmaiton view, it should tell them next steps

**Details**: Next, your vendor should confirm your order and ship your part. To view status, please monitor your Pending Orders

**Phase**: Phase 1

**Process**: Check Out / Purchase Process

---

### SWP-S-7
**Requirement**: Once customer chooses Req Item(s) desired in Checkout Process, the remaining Req Item(s) should move to canceled or archived (pop up question or automatically)

**Phase**: Phase 1

**New Functionality**: Yes

**Notes**: I would like to think the remaining items COULD be sourced from a different vendor

---

## COULD HAVE Requirements

### SWP-C-1
**Requirement**: Ability for an account to have multiple profiles

**Details**: We have customers who want to be in SWP but have existing Service Window accounts and cannot currenlty have both

**Phase**: Phase 1 - Let's talk about it

**New Functionality**: Yes

---

### SWP-C-2
**Requirement**: Interactive Help features / chat bot

**Details**: If they get stuck currently, they don't have immediate info on who to contact / what to do

**Phase**: Phase 1 - Let's talk about it

---

### SWP-C-3
**Requirement**: Ability for Customer to Export Views / Data from portal

**Phase**: Phase 2

---

### SWP-C-4
**Requirement**: Customers should have the ability to chat on the order record in addition to the SRC record

**Details**: We don't love this feature currently and would be interested in seeing an alternative

**Phase**: Phase 1?

**New Functionality**: No

---

### SWP-C-5
**Requirement**: Customer could have the ability to export views from SWP into excel (ex: Order history view)

**Phase**: Phase 1 - Let's talk about it

**New Functionality**: Yes

---

### SWP-C-6
**Requirement**: Customer could have further prompts / training on how to filter through the veiws they have

**Details**: Currently they can filter but it is not intuitive or user friendly and no one does it

**Phase**: Phase 2

**New Functionality**: Yes

---

### SWP-C-7
**Requirement**: Refresh mode, to select a page refresh timer (1, 2, 5 minutes etc)

**Phase**: Phase 1 - Refresh / Realtime?

---

## NOT DOING Requirements

### SWP-N-1
**Requirement**: Any connection to Legendary - and fully agnostic to Block's SF org

**Phase**: Phase 1

---
