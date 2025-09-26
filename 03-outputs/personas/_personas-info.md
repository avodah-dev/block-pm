# Personas Folder Documentation

## Purpose
Defines the user types who interact with the Sourcing Window platform. These personas
drive workflow design, feature prioritization, and user experience decisions. Each persona
represents a distinct role with specific goals, pain points, and system interactions.

## Core Files

### P01-buyer.json
- **Role**: Procurement Buyer
- **Primary Function**: Create parts requests and select vendors
- **Key Activities**: Request creation, quote review, vendor selection
- **Pain Points**: Manual processes, limited visibility, time-consuming tasks
- **System Goals**: Efficiency, transparency, automation

### P02-vendor.json
- **Role**: External Vendor/Supplier
- **Primary Function**: Respond to RFQs and fulfill orders
- **Key Activities**: Quote submission, order management, shipping updates
- **Pain Points**: Multiple platforms, unclear requirements, communication gaps
- **System Goals**: Clear requirements, streamlined submission, order tracking

### P03-integrated-vendor.json
- **Role**: Integrated Vendor (Special Partnership)
- **Primary Function**: Automated fulfillment and direct integration
- **Key Activities**: Auto-quoting, inventory sync, direct fulfillment
- **Special Features**: API integration, automated workflows, priority handling
- **System Goals**: Seamless integration, minimal manual intervention

### index.json
- **Purpose**: Catalog of all defined personas
- **Contents**: Persona IDs, names, descriptions, primary workflows
- **Usage**: Quick reference and navigation
- **Update**: When new personas are identified

### TEMPLATE-persona.md
- **Purpose**: Template for creating new personas
- **Structure**: Standard format for persona documentation
- **Sections**: Demographics, goals, pain points, workflows, success metrics
- **Usage**: Ensure consistency when adding personas

## Persona Structure

Each persona JSON follows this format:
```json
{
  "id": "P##",
  "name": "Persona Name",
  "role": "Business Role",
  "department": "Organizational Unit",
  "goals": ["Primary objectives"],
  "pain_points": ["Current challenges"],
  "workflows": ["W##", "W##"],
  "features_needed": ["Key capabilities"],
  "success_metrics": ["KPIs"]
}
```

## Relationships to Other Folders

### Influences
- `/03-outputs/workflows/`: Each workflow has a primary persona
- `/03-outputs/epics/`, `/03-outputs/features/`, `/03-outputs/stories/`: Features prioritized by persona needs
- `/01-sources/client-requirements/`: Requirements often persona-specific

### Informed By
- `/01-sources/transcripts/`: Discovery sessions revealed persona pain points and goals
- `/02-analysis/requirements/`: Requirements analysis identifies persona needs

### Referenced By
- All user stories in `/03-outputs/stories/` include persona context
- Workflow documents in `/03-outputs/workflows/` specify participating personas
- Feature specifications in `/03-outputs/features/` target persona goals

## Usage Patterns

### For Workflow Design
1. Identify persona for workflow
2. Review persona goals and pain points
3. Design workflow to address needs
4. Validate against success metrics

### For Feature Prioritization
1. Map features to persona benefits
2. Weight by persona importance
3. Consider multi-persona features
4. Prioritize based on impact

### For User Experience
1. Use persona context for UI decisions
2. Tailor messaging to persona language
3. Design flows for persona skill level
4. Optimize for persona workflows

## Persona Insights

### Buyer (P01)
- **Volume**: Primary platform users
- **Complexity**: Handles complex multi-vendor scenarios
- **Integration**: Internal systems (ERP, procurement)
- **Training**: Requires onboarding and support

### Vendor (P02)
- **Volume**: Large number of external users
- **Variability**: Wide range of technical capabilities
- **Access**: Limited to specific functions
- **Support**: Self-service focused

### Integrated Vendor (P03)
- **Volume**: Small number of strategic partners
- **Automation**: Highly automated interactions
- **Integration**: Deep API integration
- **Support**: Technical implementation support

## Discovery Insights
From discovery sessions, we learned:
- Buyers frustrated with current manual processes
- Vendors want clearer communication channels
- Integrated vendors need robust API capabilities
- All personas value real-time status updates

## Maintenance Notes
- Update personas based on user research
- Add new personas as user base expands
- Document persona evolution over time
- Keep pain points current with user feedback
- Validate assumptions through user testing

## Future Personas (Potential)
- **Administrator**: System configuration and user management
- **Analyst**: Reporting and spend analysis
- **Approver**: Purchase approval workflows
- **Auditor**: Compliance and audit trails

## Success Metrics by Persona
- **Buyer**: Time to complete request, vendor response rate
- **Vendor**: Quote win rate, response time
- **Integrated Vendor**: Automation rate, error rate

## Next Steps
1. Validate current personas with stakeholders
2. Develop detailed journey maps per persona
3. Create persona-specific test scenarios
4. Design persona-based training materials
5. Establish persona feedback channels