def linear_search(a: list, ele: int) -> str:
    for i in range(len(a)):
        if a[i] == ele:
            return f"Element found at position {i}"
    return "Element NOT found"

print(linear_search([2, 85, 63, 45, 32, 9], 63))

print(linear_search([85, 52, 63, 85, 96, 32, 17], 17))
