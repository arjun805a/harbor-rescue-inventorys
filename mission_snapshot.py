def mission_snapshot(supplies):
    return supplies.copy()


supplies = ["water", "food", "medkit"]

result = mission_snapshot(supplies)

print(result)