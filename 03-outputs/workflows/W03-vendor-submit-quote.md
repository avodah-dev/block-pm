# W03: Vendor Submit Quote Workflow

## Input Sources
- **Image**: vendor-submit-quote-diagram.png
- **Voice Narration**: Team discussion transcript
- **Created Date**: 2025-09-24

## Overview
- **Persona**: P02-vendor
- **Goal**: Submit competitive quotes for parts requests
- **Trigger**: "I have a request to submit pricing"
- **Estimated Duration**: 5-10 minutes

## Narrative Description

The vendor's day typically starts by checking their dashboard in Sourcing Window (not the Pro version - that's for buyers). They're looking for new opportunities to quote on parts they can supply. These opportunities come in two ways: they can see them directly in their dashboard's "Open Requests" view, or they receive email notifications about specific opportunities that match their capabilities.

When an email arrives, it's designed for quick action. The vendor can click directly through to the request, or - and this is crucial for efficiency - they could potentially click a "No Stock" button right from the email if they know they can't fulfill it. This saves everyone time by immediately removing them from consideration without requiring a full login.

Once they're viewing an open request (whether from the dashboard or email link), the first thing the system checks is whether this opportunity is still available. Sometimes a buyer has already purchased from another vendor, and there's no point in the vendor spending time creating a quote for something that's already been fulfilled. If that's the case, they see a clear message: "This opportunity is no longer available" or "This order has already been fulfilled."

If the opportunity is still open, the vendor can see the full request details and begin crafting their response. They enter their pricing, specify the condition of the part (new, refurbished, used, etc.), and define their warranty terms. This is where vendors differentiate themselves - same part, different conditions and warranties can mean different price points.

Here's where it gets interesting: vendors often have the same part in multiple conditions. They might have one that's new and another that's refurbished. Instead of choosing just one to quote, they can add multiple options. After entering the first quote (pricing, condition, warranty), they can choose to "Add another condition" and create a second quote variant. This gives buyers more options and increases the vendor's chances of winning the business.

Throughout this process, there's a messaging capability, though it's rarely used at this initial quoting stage. Vendors are typically just responding to the straightforward request.

Once they've added all their quote variants, they hit submit. This automatically triggers an email to the buyer, letting them know a new quote has arrived. The vendor's work is done - now they wait to see if they win the business.

There's an important technical consideration that came up: what happens when multiple people from the same vendor company try to work on the same quote? Unlike modern collaborative tools like Figma or Linear that show real-time updates, this system needs some form of collision detection or locking mechanism. For the first version, it might be as simple as showing a warning that someone else from their company is viewing or has already submitted pricing. This prevents duplicate work and confusion.

## Workflow Steps

### 📊 Step-to-Requirements Matrix

| Step ID | Step Name | Requirements Addressed | Type |
|---------|-----------|----------------------|------|
| W03-S01a | Access via Dashboard | SW-M-9 | User Action |
| W03-S01b | Access via Email Link | SW-M-10 | User Action |
| W03-S02 | Check Opportunity Status | SW-M-11 | System Check |
| W03-S03 | View Request Details | SW-M-12 | User Action |
| W03-S04a | Submit No Stock | SW-M-13 | User Action |
| W03-S04b | Enter Quote Details | SW-M-14, SW-M-24 | User Action |
| W03-S05 | Add Multiple Conditions | SW-M-15 | User Action |
| W03-S06 | Submit Quote | SW-M-16 | User Action |
| W03-S07 | Auto Email Buyer | SW-M-17 | System Process |

## Detailed Step Descriptions

### W03-S01a: Access via Dashboard
- **Actions**: Navigate to Dashboard → Open Requests View
- **UI Elements**: Dashboard, Open Requests section
- **Next**: W03-S02

### W03-S01b: Access via Email Link
- **Actions**: Click link in email notification
- **UI Elements**: Email with embedded link
- **Future Enhancement**: "No Stock" button in email
- **Next**: W03-S02

### W03-S02: Check Opportunity Status 🔍
- **Type**: System Automated Check
- **Business Rule**: If buyer already purchased → Show "closed/not won" message
- **Prevents**: Vendor wasting time on fulfilled requests
- **Decision Point**:
  - Still open → W03-S03
  - Already closed → End (show lost opportunity message)

### W03-S03: View Request Details 📋
- **Actions**: Review part requirements, quantities, specifications
- **UI Elements**: Request details panel
- **Data Displayed**: Part number, quantity needed, required date
- **Next**: W03-S04a or W03-S04b

### W03-S04a: Submit No Stock ❌
- **Actions**: Click "No Stock" button
- **Business Impact**: Removes vendor from consideration
- **Notification**: System notifies buyer of no availability
- **End State**: Workflow complete

### W03-S04b: Enter Quote Details 💰
- **Actions**: Enter pricing, select condition, specify warranty
- **Required Fields**:
  - Pricing (currency amount)
  - Condition (dropdown: New/Refurbished/Used)
  - Warranty (text or dropdown)
- **Optional**: Message to buyer
- **Next**: W03-S05

### W03-S05: Add Multiple Conditions (Decision) ➕
- **Actions**: Choose to add another price/condition variant
- **Business Value**: Offer multiple options to increase win probability
- **Decision Point**:
  - Add another → Return to W03-S04b
  - Done → W03-S06

### W03-S06: Submit Quote ✅
- **Actions**: Click "Submit Quote" button
- **Validations**: All required fields completed
- **Creates**: Quote record in system
- **Next**: W03-S07

### W03-S07: Auto Email Buyer 📧
- **Type**: System Automated
- **Actions**: Generate and send email notification to buyer
- **Content**: New quote available for review
- **End State**: Vendor sees confirmation, quote submitted

## Edge Cases & Considerations

### Multi-User Collision
- **Scenario**: Multiple vendor employees accessing same quote
- **Current Gap**: No real-time collaboration features
- **Proposed Solutions**:
  - Show warning: "Another user from your company is viewing this"
  - Lock mechanism: First user locks the quote
  - Refresh notifications: Alert when quote already submitted

### Lost Opportunities
- **Scenario**: Vendor clicks email link after buyer already purchased
- **Solution**: Clear messaging about opportunity status
- **User Experience**: Immediate feedback, no wasted effort

## Requirements Coverage

### ✅ Fully Addressed
- SW-M-9: Dashboard access to opportunities
- SW-M-10: Email notification with direct link
- SW-M-11: Opportunity status checking
- SW-M-12: View request details
- SW-M-13: No stock indication
- SW-M-14: Submit pricing
- SW-M-15: Multiple condition options
- SW-M-16: Quote submission
- SW-M-17: Buyer notification
- SW-M-24: Pricing, condition, warranty fields

### 🔄 Gaps Identified
- Multi-user collision handling (not in original requirements)
- Email-embedded "No Stock" button (future enhancement)
- Real-time updates for same-company users

## Success Metrics
- Quote submission time < 10 minutes
- Email notification sent < 30 seconds after submission
- Zero duplicate quotes from same company
- 100% buyer notification success rate