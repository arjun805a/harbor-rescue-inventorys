# Harbor Rescue Inventory

# 1. mission_snapshot
# Returns a copy of the list of supplies
def mission_snapshot(supplies):
    return supplies.copy()


# 2. cargo_window
# Returns a slice of the list starting at 'start' with length 'size'
def cargo_window(supplies, start, size):
    if size <= 0:
        return []
    return supplies[start:start + size]


# 3. first_supply_index
# Returns the index of the first occurrence of target
# If not found, return -1
def first_supply_index(supplies, target):
    for i in range(len(supplies)):
        if supplies[i] == target:
            return i
    return -1


# 4. supply_report
# Counts how many times each item appears
def supply_report(supplies):
    report = {}
    for item in supplies:
        if item in report:
            report[item] += 1
        else:
            report[item] = 1
    return report


# 5. priority_load (stretch)
# Returns a new list with priority items first
# Original list must not change
def priority_load(supplies, priority_item):
    priority_items = []
    other_items = []

    for item in supplies:
        if item == priority_item:
            priority_items.append(item)
        else:
            other_items.append(item)

    return priority_items + other_items


# -----------------------------
# Test section (to see results)
# -----------------------------
if __name__ == "__main__":

    supplies = ["water", "food", "medkit", "food", "rope"]

    print("Mission Snapshot:")
    print(mission_snapshot(supplies))

    print("\nCargo Window (start=1, size=3):")
    print(cargo_window(supplies, 1, 3))

    print("\nFirst Supply Index of 'food':")
    print(first_supply_index(supplies, "food"))

    print("\nSupply Report:")
    print(supply_report(supplies))

    print("\nPriority Load (medkit first):")
    print(priority_load(supplies, "medkit"))

    print("\nOriginal List (should not change):")
    print(supplies)