def supply_report(supplies):
    report = {}
    for item in supplies:
        if item in report:
            report[item] += 1
        else:
            report[item] = 1
    return report


supplies = ["water", "food", "food", "medkit"]

result = supply_report(supplies)

print(result)