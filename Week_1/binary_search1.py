def binary_search1(a: list, ele: int, low: int, high : int ) -> str:
    mid = (low + high) // 2
    if a[mid] > ele:
        return binary_search1(a, ele, low, high - 1)
    elif a[mid] < ele:
        return binary_search1(a, ele, low + 1, high)
    elif a[mid] == ele:
        return f"The element is found at position {mid}"

print(binary_search1([2, 3, 4, 5, 6, 7], 6, 0, 5))

print(binary_search1([21, 32, 44, 56, 63, 78, 95, 100], 100, 0, 7))
