def binary_search(a: list, ele: int) -> str:
    low = 0
    high = len(a) - 1
    while(high>=low):
        mid = (low + high) // 2
        if a[mid] > ele:
            high -= 1
        elif a[mid] < ele:
            low += 1
        elif a[mid] == ele:
            return f"The element is found at position {mid}"

print(binary_search([2, 3, 4, 5, 6, 7], 6))

print(binary_search([21, 32, 44, 56, 63, 78, 95, 100], 100))




