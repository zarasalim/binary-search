import random

random.seed(42)
numbers = sorted(random.randint(1, 1000) for _ in range(100))

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

search_values = [50, 120, 450, 720, 999]

for val in search_values:
    idx = binary_search(numbers, val)
    if idx != -1:
        print(f"{val} найден по индексу {idx}")
    else:
        print(f"{val} не найден")