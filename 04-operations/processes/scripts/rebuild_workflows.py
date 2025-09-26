#!/usr/bin/env python3
"""
Rebuild all workflows with correct requirement references from new CAD files
"""

import json
import re
from pathlib import Path

# Requirement mappings based on new CAD files content
REQUIREMENT_MAPPINGS = {
    # W01 mappings (already done)

    # W02 mappings - Review and Select Vendor
    "W02": {
        "W02-S01": ["SWP-M-3", "SWP-M-7"],  # Dashboard access
        "W02-S02": ["SWP-M-7", "SWP-M-20"],  # Select request
        "W02-S03": [],  # Access vendor response (no direct requirement)
        "W02-S04": ["SWP-M-20", "SWP-M-21"],  # View request details & SRC options
        "W02-S05": ["SWP-M-5"],  # Apply filters
        "W02-S06": ["SWP-M-21"],  # Review quote details
        "W02-S07": ["SWP-M-30", "SWP-M-22", "SWP-M-23"],  # Add to cart
        "W02-S08": ["SWP-M-31"],  # Handle unfulfilled
        "W02-S09": ["SWP-M-32", "SWP-M-33", "SWP-M-34", "SWP-M-35", "SWP-M-36", "SWP-M-37", "SWP-M-38"],  # Checkout
        "W02-S10": ["SWP-M-39", "SWP-M-40", "SWP-M-41"],  # Submit PO
        "W02-S11": ["SWP-M-31"],  # Purchase additional
        "W02-S12": [],  # Cancel balance
        "W02-S13": ["SWP-M-41", "SW-M-40"],  # Create vendor order
        "W02-S14": ["SWP-M-42"],  # Await confirmation
        "W02-S15": ["SWP-M-24", "SWP-M-25", "SWP-M-26", "SWP-M-27", "SWP-M-28", "SWP-M-29"],  # Messaging
    },

    # W03 mappings - Vendor Submit Quote
    "W03": {
        "W03-S01": ["SW-M-10"],  # Access homepage
        "W03-S02": ["SW-M-10", "SW-M-11", "SW-M-12"],  # View open requests
        "W03-S03": ["SW-M-13"],  # Quick unavailable
        "W03-S04": ["SW-M-20"],  # Select request
        "W03-S05": ["SW-M-20"],  # View request details
        "W03-S06": ["SW-M-22"],  # No stock option
        "W03-S07": ["SW-M-24", "SW-M-25", "SW-M-26"],  # Submit quote
        "W03-S08": ["SW-M-27"],  # Backorder option
        "W03-S09": ["SW-M-23", "SW-M-28", "SW-M-29"],  # Submit and clone
        "W03-S10": ["SW-M-39"],  # System notification
        "W03-S11": ["SWP-M-17"],  # Customer notification
        "W03-S12": ["SW-M-19"],  # Update history
    },

    # W04 mappings - Messaging Capability (EMA)
    "W04": {
        "W04-S01": ["SWP-M-26", "SW-M-36"],  # Initiate message
        "W04-S02": ["SWP-M-29", "SW-M-30"],  # Access EMA
        "W04-S03": ["SWP-M-26", "SW-M-36"],  # Compose message
        "W04-S04": ["SWP-M-27"],  # Attach files
        "W04-S05": ["SWP-M-28"],  # Validate attachments
        "W04-S06": ["SWP-M-26", "SW-M-36"],  # Send message
        "W04-S07": ["SWP-M-24", "SW-M-41"],  # Send notification
        "W04-S08": ["SWP-M-25", "SW-M-30"],  # Display message
        "W04-S09": ["SW-M-38"],  # Guidance for PO messages
    },

    # W05 mappings - Vendor Confirmation & Shipping
    "W05": {
        "W05-S01": ["SW-M-31", "SW-M-40", "SW-M-42"],  # Receive PO notification
        "W05-S02": ["SW-M-15", "SW-M-18"],  # View pending fulfillments
        "W05-S03": ["SW-M-31", "SW-M-32"],  # Access PO details
        "W05-S04": ["SW-M-32"],  # View PO information
        "W05-S05": ["SW-M-33"],  # Confirm order
        "W05-S06": ["SW-M-34", "SW-M-35"],  # Enter shipping info
        "W05-S07": ["SW-M-35"],  # Save tracking
        "W05-S08": ["SWP-M-43", "SWP-M-44", "SWP-M-45"],  # Update order status
        "W05-S09": [],  # Send notification (covered in S08)
        "W05-S10": ["SW-M-37", "SWP-M-24"],  # Order messaging
    },

    # W06 mappings - Integrated Vendor SW Buyer Timeline
    "W06": {
        "W06-S01": [],  # Receive request (system)
        "W06-S02": [],  # Route to vendor (system)
        "W06-S03": [],  # Submit quote (system)
        "W06-S04": [],  # Buyer review (system)
        "W06-S05": [],  # Purchase decision (system)
        "W06-S06": [],  # Order processing (system)
        "W06-S07": [],  # Complete order (system)
    },

    # W07 mappings - Integrated Vendor Non-SW Buyer Timeline
    "W07": {
        "W07-S01": [],  # Receive request (system)
        "W07-S02": [],  # Route internal (system)
        "W07-S03": [],  # Manual quote (system)
        "W07-S04": [],  # Send quote (system)
        "W07-S05": [],  # Purchase decision (system)
        "W07-S06": [],  # Manual order (system)
        "W07-S07": [],  # Complete order (system)
    },

    # W08 mappings - Integrated Vendor Auto Sourcing
    "W08": {
        "W08-S01": [],  # Receive request (system)
        "W08-S02": [],  # Check inventory (system)
        "W08-S03": [],  # Check pricing (system)
        "W08-S04": [],  # Generate quote (system)
        "W08-S05": [],  # Submit quote (system)
        "W08-S06": [],  # Update status (system)
        "W08-S07": [],  # PO received (system)
        "W08-S08": [],  # Auto fulfill (system)
        "W08-S09": [],  # Complete order (system)
    },

    # W09 mappings - Integrated Vendor Fulfillment Passthrough
    "W09": {
        "W09-S01": [],  # Receive request (system)
        "W09-S02": [],  # Check capability (system)
        "W09-S03": [],  # Forward to vendor (system)
        "W09-S04": [],  # Vendor quote (system)
        "W09-S05": [],  # Submit to buyer (system)
        "W09-S06": [],  # PO received (system)
        "W09-S07": [],  # Forward PO (system)
        "W09-S08": [],  # Track fulfillment (system)
        "W09-S09": [],  # Complete order (system)
    }
}

def update_workflow(workflow_path, workflow_id):
    """Update a workflow JSON file with correct requirement mappings"""

    with open(workflow_path, 'r') as f:
        workflow = json.load(f)

    if workflow_id not in REQUIREMENT_MAPPINGS:
        print(f"  ⚠️ No mappings defined for {workflow_id}")
        return False

    mappings = REQUIREMENT_MAPPINGS[workflow_id]
    all_requirements = set()

    # Update each step
    for step in workflow.get('steps', []):
        step_id = step.get('step_id')
        if step_id in mappings:
            step['requirements_addressed'] = mappings[step_id]
            all_requirements.update(mappings[step_id])

    # Update requirements coverage
    if all_requirements:
        sorted_reqs = sorted(list(all_requirements))
        workflow['requirements_coverage'] = {
            'directly_addressed': sorted_reqs,
            'partially_addressed': [],
            'gaps': [],
            'notes': 'Requirements mapped to actual CAD-001 and CAD-002 content after CSV data cleanup'
        }

    # Write back
    with open(workflow_path, 'w') as f:
        json.dump(workflow, f, indent=2)

    print(f"  ✓ Updated {workflow_id} with {len(all_requirements)} unique requirements")
    return True

def main():
    """Update all workflows with correct requirement mappings"""

    workflows_dir = Path("/Users/andrewbailey/dev/block-sw-discovery/workflows")

    print("Updating workflows with correct requirement mappings...")
    print()

    # Skip W01 as it's already done
    workflow_files = [
        ("W02-review-select-vendor.json", "W02"),
        ("W03-vendor-submit-quote.json", "W03"),
        ("W04-messaging-capability.json", "W04"),
        ("W05-vendor-confirmation-shipping.json", "W05"),
        ("W06-integrated-vendor-sw-buyer-timeline.json", "W06"),
        ("W07-integrated-vendor-non-sw-buyer-timeline.json", "W07"),
        ("W08-integrated-vendor-auto-sourcing.json", "W08"),
        ("W09-integrated-vendor-fulfillment-passthrough.json", "W09"),
    ]

    for filename, workflow_id in workflow_files:
        workflow_path = workflows_dir / filename
        if workflow_path.exists():
            print(f"Processing {workflow_id}...")
            update_workflow(workflow_path, workflow_id)
        else:
            print(f"  ❌ File not found: {filename}")

    print()
    print("✅ All workflows updated!")

if __name__ == "__main__":
    main()