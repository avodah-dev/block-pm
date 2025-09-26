# Block Sourcing Window - Team Onboarding Guide

## Welcome to the Project!

This guide will get you oriented in 5 minutes.

## What We're Building

**Project**: Sourcing Window - A modern B2B marketplace platform for Block (formerly Square)
**Our Role**: Avodah is replacing Block's problematic Salesforce implementation (SW 2.0) with a clean, modern platform

## Project Structure - Follow the Numbers

The project is organized into four numbered folders that follow the natural information flow:

### 1️⃣ `/01-sources/` - What Block Gave Us
Start here to understand the requirements:
- **`client-requirements/`** - Block's original RFP requirements (118 total)
- **`rfp-responses/`** - Our initial responses pre-discovery
- **`transcripts/`** - 3 days of discovery session recordings

### 2️⃣ `/02-analysis/` - How We Understand It
Our analysis and insights:
- **`requirements/`** - Requirement tracking, gap analysis (43.2% coverage)
- **`mappings/`** - How everything connects
- **`insights/`** - Key findings from discovery

### 3️⃣ `/03-outputs/` - What We're Creating
All deliverables with unique IDs:
- **`personas/`** - User types (P01-P03)
- **`workflows/`** - User journeys (W01-W09)
- **`epics/`**, **`features/`**, **`stories/`** - Development breakdown
- **`drafts/`** - Work in progress

### 4️⃣ `/04-operations/` - How We Work
Project infrastructure:
- **`processes/`** - Procedures and automation
- **`architecture/`** - System design decisions
- **`templates/`** - Document templates

## Key Concepts

### ID System
Every major deliverable has a unique ID:
- **CAD-###** - Client Anchor Documents (requirements)
- **RRD-###** - RFP Response Documents
- **P##** - Personas
- **W##** - Workflows
- **E##** - Epics
- **F##** - Features
- **S##** - Stories

### Navigation Tips
1. **Start with CLAUDE.md** for the complete project overview
2. **Each folder has a `_foldername-info.md`** file explaining its contents
3. **Use the numbered folders** to understand the flow: Sources → Analysis → Outputs → Operations

## Quick Start Tasks

### For Product Managers
1. Review `/01-sources/client-requirements/` to understand Block's needs
2. Check `/02-analysis/requirements/gap-analysis.md` for coverage status
3. Explore `/03-outputs/workflows/` for user journey definitions

### For Developers
1. Start with `/04-operations/architecture/architecture_layers.md` for system design
2. Review `/03-outputs/drafts/EPICS-FEATURES-STORIES-SUMMARY.md` for development breakdown
3. Check `/03-outputs/workflows/` to understand user flows

### For Business Analysts
1. Begin with `/01-sources/transcripts/` for discovery insights
2. Review `/03-outputs/personas/` for user types
3. Examine `/02-analysis/mappings/` for requirement traceability

## Key Files to Review

1. **CLAUDE.md** - Complete project navigation and context
2. **roadmap.md** - Development timeline and phases
3. **`/02-analysis/requirements/gap-analysis.md`** - What's covered vs. missing
4. **`/04-operations/architecture/project_dictionary.md`** - Key terms and concepts

## Working with AI Agents

This project is optimized for AI-assisted development:
- **Research Mode**: Ask questions without modifying files
- **Add Mode**: Incorporate new information into the system
- Start requests with "Research:" or "Add:" for explicit mode selection

## Current Status

- ✅ Requirements documented (118 total)
- ✅ Discovery sessions completed (3 days)
- ✅ Personas defined (3 types)
- ✅ Workflows documented (9 complete)
- 🔄 Draft epics/features/stories generated
- 📊 43.2% of requirements addressed in initial RFP

## Next Steps

1. Review the gap analysis to understand what needs addressing
2. Finalize epics/features/stories from drafts
3. Map all development items back to requirements
4. Continue workflow documentation (7-10 more expected)

## Questions?

- **Project Structure**: Start with CLAUDE.md
- **Specific Areas**: Check the `_info.md` file in that folder
- **Requirements**: Look in `/01-sources/client-requirements/`
- **Development Plans**: Check `/03-outputs/drafts/`

Welcome aboard! The clear folder structure (Sources → Analysis → Outputs → Operations) makes it easy to find exactly what you need.