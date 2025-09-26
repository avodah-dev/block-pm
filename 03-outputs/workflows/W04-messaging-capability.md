# W04: Messaging Capability (Cross-Cutting Feature)

## Input Sources
- **Image**: messaging-system-diagram.png
- **Voice Narration**: Team discussion on messaging architecture
- **Created Date**: 2025-09-24
- **Type**: SYSTEM CAPABILITY (not a traditional workflow)

## Overview
- **Personas**: All (P01-buyer, P02-vendor, future personas)
- **Goal**: Enable contextual communication throughout the platform
- **Nature**: Cross-cutting feature that enhances all workflows
- **Estimated Setup**: Embedded in multiple touchpoints

## Narrative Description

The messaging capability represents a fundamental shift in how communication works within the platform. Currently, messaging exists but it's fragmented - attached to specific objects like part requests or purchase orders, making it difficult to find past conversations. The team envisions messaging as a "first-class experience" that needs to be elevated and made more accessible.

The core insight is that "every message is just text sent with a context." This simple concept has profound implications. Unlike traditional messaging systems, every message here carries rich metadata - it knows what part it's about, which organizations are involved, what type of request it relates to, and who the participants are. This context makes messages not just searchable by text content (like finding the word "MRI") but also filterable by these business dimensions.

The current pain point is clear: "Oh, I know I had that conversation with some vendor at some point on some part or PO. I now need to go find that." Users waste time hunting through different objects trying to find a specific conversation. The solution is a unified Messages Page that serves as a command center for all communication.

From this Messages Page, users can:
1. Search by keyword across all messages
2. Filter by vendor to see all conversations with a specific company
3. Navigate by context (all messages about a specific part request)
4. Start new conversations with appropriate context

The power of this approach becomes apparent when considering the AI implications. Because messages are well-organized with rich context, an AI agent can instantly access relevant conversation history when a new request comes in. As discussed: "When a new request happens, we can give an agent really meaningful context immediately based on history... conversation references and data point references."

The system recognizes that messages can be attached to multiple object types:
- **Unique Part Requests**: Discussions about specifications, availability
- **Purchase Orders**: Negotiations about delivery, terms
- **Vendors**: General relationship conversations
- **Future Objects**: System is extensible for new contexts

Topics that commonly arise include warranty negotiations, price discussions, shipping timelines, and technical specifications. While the team considered pre-defining topic categories, they recognize the need for flexibility.

The technical challenge of message organization is similar to email threading. You don't want messages displayed purely chronologically (like "an inbox without conversations enabled" in Outlook), but rather grouped by conversation thread. Multiple threads can be active simultaneously about different aspects of the same part or with the same vendor.

What makes this special is that it's not just a messaging system - it's a knowledge capture system. Every conversation becomes part of the institutional memory, accessible and searchable, providing context for future decisions. The team sees this as foundational for future AI capabilities, where the system can suggest "here's what I think should happen next based on what I've seen."

## System Architecture (Not Linear Steps)

### Core Components

#### C01: Message Object
- **Properties**:
  - Text content
  - Sender/Recipient
  - Timestamp
  - Context Object (Part Request ID, PO ID, Vendor ID)
  - Thread ID
  - Topic tags (optional)
- **Requirements**: SW-M-18, SWP-M-35

#### C02: Messages Page (New Dashboard Section)
- **Functions**:
  - Global search across all messages
  - Filter by vendor
  - Filter by context type
  - Thread view
  - New conversation initiation
- **Requirements**: SWP-M-36, SW-M-19

#### C03: Context Attachment Points
- **Unique Part Request**: Message thread capability
- **Purchase Order**: Message thread capability
- **Vendor Relationship**: Direct messaging
- **Future Objects**: Extensible architecture
- **Requirements**: SWP-M-35, SW-M-20

#### C04: Search & Discovery
- **Capabilities**:
  - Full-text search
  - Metadata filtering (vendor, date, part)
  - Thread reconstruction
  - Context preservation
- **Requirements**: SWP-M-37

#### C05: Notification System
- **Triggers**:
  - New message received
  - Mention in conversation
  - Status change in related object
- **Delivery**: Email, in-app
- **Requirements**: SW-M-21

## Integration Points with Other Workflows

### W01 (Buyer Parts Request)
- Messaging available after request creation
- Vendors can ask clarifying questions
- Buyer can broadcast updates

### W02 (Review and Select Vendor)
- Negotiate terms before selection
- Discuss warranty/pricing
- Clarify specifications

### W03 (Vendor Submit Quote)
- Pre-quote clarifications
- Post-quote negotiations
- No-stock explanations

### Future Workflows
- All workflows gain messaging capability
- Context automatically attached
- History preserved across workflow transitions

## Data Access Rules

### Visibility Hierarchy
1. **Organization Level**: See all messages within your org
2. **Participation Level**: See threads you're part of
3. **Object Level**: See messages on objects you have access to
4. **Vendor-Buyer Relationship**: Maintained across contexts

## Technical Considerations

### Threading Logic
- Messages grouped by context + participants
- Similar to email conversation view
- Multiple simultaneous threads supported
- Chronological within threads

### Search Architecture
- Elasticsearch or similar for full-text
- Indexed on multiple dimensions
- Real-time updates
- Historical data preserved

### Scalability
- Messages as separate service
- Async processing for notifications
- Caching for frequent searches
- Archive strategy for old messages

## AI/ML Opportunities

### Immediate (Phase 1)
- Smart search suggestions
- Auto-categorization of topics
- Thread summarization

### Future (Phase 2+)
- Context-aware response suggestions
- Pattern recognition for common issues
- Predictive alerts based on conversation sentiment
- Automated knowledge base creation

## Success Metrics
- Message search time < 2 seconds
- 90% of historical conversations findable
- Zero lost message threads
- 100% context preservation

## Requirements Coverage
- **Direct**: SWP-M-35, SWP-M-36, SWP-M-37, SW-M-18, SW-M-19, SW-M-20, SW-M-21
- **Enhanced**: Goes beyond requirements to create unified communication platform

## Critical Design Decisions
1. **Messages as First-Class Objects**: Not just attachments but searchable, filterable entities
2. **Context Preservation**: Every message knows its business context
3. **Unified Access Point**: Single Messages Page for all communication
4. **Extensible Architecture**: New object types can gain messaging without redesign
5. **AI-Ready Structure**: Organized for future intelligence layer