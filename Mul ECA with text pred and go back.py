# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:35:51 2025

@author: chad
"""

import difflib

# Example dataset with 100 unique entries (shortened here for brevity)
data = [
    {"Event": "Machine Breakdown", "Cause": "Overheating due to lack of lubrication", "Action Taken": "Applied lubricant and scheduled regular maintenance"},
    {"Event": "Machine Breakdown", "Cause": "Overheating due to lack of lubrication", "Action Taken": "Replaced worn-out parts and checked cooling systems"},
    {"Event": "Machine Breakdown", "Cause": "Electrical fault", "Action Taken": "Replaced faulty wiring and inspected circuit breakers"},
    {"Event": "Machine Breakdown", "Cause": "Electrical fault", "Action Taken": "Updated electrical components and reinforced insulation"},
    {"Event": "Machine Breakdown", "Cause": "Clogged filters", "Action Taken": "Cleaned filters and checked filtration efficiency"},
    {"Event": "Machine Breakdown", "Cause": "Clogged filters", "Action Taken": "Replaced filters with higher-capacity alternatives"},
    {"Event": "Product Defect", "Cause": "Operator error", "Action Taken": "Provided additional training to operators"},
    {"Event": "Product Defect", "Cause": "Operator error", "Action Taken": "Implemented error-proofing mechanisms in production lines"},
    {"Event": "Product Defect", "Cause": "Inconsistent raw material quality", "Action Taken": "Conducted material quality checks before use"},
    {"Event": "Product Defect", "Cause": "Inconsistent raw material quality", "Action Taken": "Developed contracts with reliable suppliers"},
    {"Event": "Material Shortage", "Cause": "Supplier delay", "Action Taken": "Contacted alternate vendors to meet shortfalls"},
    {"Event": "Material Shortage", "Cause": "Supplier delay", "Action Taken": "Revised lead time expectations with primary suppliers"},
    {"Event": "Material Shortage", "Cause": "Inventory mismanagement", "Action Taken": "Implemented a real-time inventory tracking system"},
    {"Event": "Material Shortage", "Cause": "Inventory mismanagement", "Action Taken": "Trained staff to use the updated inventory system"},
    {"Event": "Frequent Downtime", "Cause": "Software glitches in the control system", "Action Taken": "Updated software and performed regular system checks"},
    {"Event": "Frequent Downtime", "Cause": "Software glitches in the control system", "Action Taken": "Engaged software vendor for permanent fixes"},
    {"Event": "Frequent Downtime", "Cause": "Operator error", "Action Taken": "Provided additional training for operators"},
    {"Event": "Frequent Downtime", "Cause": "Operator error", "Action Taken": "Implemented real-time monitoring to catch errors early"},
    {"Event": "Delayed Production", "Cause": "Labor shortage", "Action Taken": "Optimized staff scheduling and hired temporary workers"},
    {"Event": "Delayed Production", "Cause": "Labor shortage", "Action Taken": "Automated processes to reduce reliance on labor-intensive tasks"},
    {"Event": "Delayed Production", "Cause": "Equipment failure", "Action Taken": "Repaired equipment and implemented predictive maintenance"},
    {"Event": "Delayed Production", "Cause": "Equipment failure", "Action Taken": "Replaced outdated machinery with modern alternatives"},
    {"Event": "Operator Injury", "Cause": "Improper use of safety gear", "Action Taken": "Conducted safety workshops for all staff"},
    {"Event": "Operator Injury", "Cause": "Improper use of safety gear", "Action Taken": "Enforced strict safety policies with regular inspections"},
    {"Event": "Operator Injury", "Cause": "Faulty machinery", "Action Taken": "Repaired or replaced faulty equipment"},
    {"Event": "Operator Injury", "Cause": "Faulty machinery", "Action Taken": "Installed machine guards to prevent accidental contact"},
    {"Event": "Product Damage", "Cause": "Improper handling during transport", "Action Taken": "Improved packaging to minimize transport damage"},
    {"Event": "Product Damage", "Cause": "Improper handling during transport", "Action Taken": "Trained logistics team on proper handling techniques"},
    {"Event": "System Failure", "Cause": "Outdated software", "Action Taken": "Updated to the latest version and tested compatibility"},
    {"Event": "System Failure", "Cause": "Outdated software", "Action Taken": "Conducted user training for the updated system"},
    {"Event": "System Failure", "Cause": "Data corruption", "Action Taken": "Restored backups and enhanced database integrity checks"},
    {"Event": "System Failure", "Cause": "Data corruption", "Action Taken": "Installed real-time data monitoring tools"},
    {"Event": "Power Outage", "Cause": "Grid failure", "Action Taken": "Installed backup generators to ensure continuity"},
    {"Event": "Power Outage", "Cause": "Grid failure", "Action Taken": "Negotiated with utility providers for stable power supply"},
    {"Event": "Quality Complaints", "Cause": "Inadequate testing procedures", "Action Taken": "Enhanced testing procedures at each production stage"},
    {"Event": "Quality Complaints", "Cause": "Inadequate testing procedures", "Action Taken": "Added automated quality control checkpoints"},
    {"Event": "High Scrap Rate", "Cause": "Defective tools", "Action Taken": "Replaced worn-out tools and implemented checks for wear"},
    {"Event": "High Scrap Rate", "Cause": "Defective tools", "Action Taken": "Introduced predictive maintenance for tooling equipment"},
    {"Event": "Workplace Hazard", "Cause": "Obstructed pathways", "Action Taken": "Cleared all obstructions and enforced cleaning protocols"},
    {"Event": "Workplace Hazard", "Cause": "Obstructed pathways", "Action Taken": "Marked hazard zones and implemented regular audits"},
    {"Event": "Noise Pollution", "Cause": "Old machinery", "Action Taken": "Replaced outdated machines with quieter models"},
    {"Event": "Noise Pollution", "Cause": "Old machinery", "Action Taken": "Installed noise-dampening materials in production areas"},
    {"Event": "Product Recall", "Cause": "Defective components", "Action Taken": "Identified faulty batches and replaced components"},
    {"Event": "Product Recall", "Cause": "Defective components", "Action Taken": "Enhanced supplier quality audits to prevent recurrence"},
    {"Event": "Late Shipment", "Cause": "Incorrect documentation", "Action Taken": "Revised and automated documentation processes"},
    {"Event": "Late Shipment", "Cause": "Incorrect documentation", "Action Taken": "Trained staff in proper documentation practices"},
    {"Event": "Frequent Machine Restart", "Cause": "Heat sensor malfunction", "Action Taken": "Replaced sensors and conducted calibration checks"},
    {"Event": "Frequent Machine Restart", "Cause": "Heat sensor malfunction", "Action Taken": "Installed backup temperature monitoring systems"},
    {"Event": "Frequent Machine Restart", "Cause": "Obsolete hardware", "Action Taken": "Replaced outdated hardware components"},
    {"Event": "Frequent Machine Restart", "Cause": "Obsolete hardware", "Action Taken": "Planned phased hardware upgrades across facilities"},
    {"Event": "Delayed Production", "Cause": "Unrealistic production targets", "Action Taken": "Revised production schedules to realistic levels"},
    {"Event": "Delayed Production", "Cause": "Unrealistic production targets", "Action Taken": "Implemented project management tools to streamline processes"},
]


# Extract all unique events
unique_events = sorted(set(entry["Event"] for entry in data))

def select_event():
    """Allows the user to select an event by number or keyword."""
    while True:
        print("\nSelect an event by number or type a keyword (e.g., 'Prod' for Product-related events):")
        for idx, event in enumerate(unique_events, start=1):
            print(f"{idx}. {event}")
        
        user_input = input("\nEnter event number, keyword, or 'B' to go back: ").strip()
        
        # Check if the user wants to go back
        if user_input.lower() == 'b':
            return None
        
        # Check if the input is a number
        if user_input.isdigit():
            event_index = int(user_input) - 1
            if 0 <= event_index < len(unique_events):
                return unique_events[event_index]
            else:
                print("Invalid number. Please try again.")
        else:
            # Perform substring matching for text input
            matching_events = [event for event in unique_events if user_input.lower() in event.lower()]
            if matching_events:
                print("\nDid you mean one of these?")
                for idx, match in enumerate(matching_events, start=1):
                    print(f"{idx}. {match}")
                match_input = input("\nSelect by number or 'B' to go back: ").strip()
                if match_input.lower() == 'b':
                    continue
                elif match_input.isdigit():
                    match_index = int(match_input) - 1
                    if 0 <= match_index < len(matching_events):
                        return matching_events[match_index]
                    else:
                        print("Invalid number. Please try again.")
            else:
                print("No matching events found. Please try again.")

def select_cause(selected_event):
    """Allows the user to select a cause for the chosen event."""
    causes = sorted(set(entry["Cause"] for entry in data if entry["Event"] == selected_event))
    while True:
        print(f"\nPossible causes for '{selected_event}':")
        for idx, cause in enumerate(causes, start=1):
            print(f"{idx}. {cause}")
        
        user_input = input("\nEnter cause number or 'B' to go back: ").strip()
        
        if user_input.lower() == 'b':
            return None
        
        if user_input.isdigit():
            cause_index = int(user_input) - 1
            if 0 <= cause_index < len(causes):
                return causes[cause_index]
            else:
                print("Invalid number. Please try again.")
        else:
            print("Invalid input. Please try again.")

def display_actions(selected_event, selected_cause):
    """Displays actions for the selected event and cause."""
    actions = [entry["Action Taken"] for entry in data if entry["Event"] == selected_event and entry["Cause"] == selected_cause]
    print(f"\nActions for '{selected_event}' caused by '{selected_cause}':")
    for idx, action in enumerate(actions, start=1):
        print(f"{idx}. {action}")

def main():
    while True:
        selected_event = select_event()
        if not selected_event:
            print("\nExiting. Thank you!")
            break
        
        while True:
            selected_cause = select_cause(selected_event)
            if not selected_cause:
                break
            
            display_actions(selected_event, selected_cause)
            input("\nPress Enter to continue...")
            break  # Go back to event selection if needed

if __name__ == "__main__":
    main()
