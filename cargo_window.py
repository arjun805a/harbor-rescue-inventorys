def cargo_window(supplies, start, size):
    if size <= 0:
        return []
    return supplies[start:start + size]


supplies = ["water", "food", "medkit", "rope", "blanket"]

result = cargo_window(supplies, 1, 3)

print(result)