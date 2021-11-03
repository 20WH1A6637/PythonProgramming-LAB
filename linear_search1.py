def linear_search1(a: list, ele: int, i: int) -> str:
    if i > len(a):
        return "Element NOT found"
    if a[i] == ele:
        return f"Element found at position {i}"
    else:
        i += 1
        return linear_search1(a, ele, i)

print(linear_search1([2, 85, 63, 45, 32, 9], 63, 0))

print(linear_search1([85, 52, 63, 85, 96, 32, 17], 17, 0))
