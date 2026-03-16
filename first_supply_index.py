def first_supply_index(supplies, target):
    for i in range(len(supplies)):
        if supplies[i] == target:
            return i
    return -1


supplies = ["water", "food", "medkit", "food"]

result = first_supply_index(supplies, "food")

print(result)