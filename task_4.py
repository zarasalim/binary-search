import timeit
import random

sizes = [10**i for i in range(1, 7)]
num_runs = 5
linear_times = []
binary_times = []

for n in sizes:
    data = sorted(random.sample(range(n * 2), n))
    target_present = data[n // 4]

    stmt_linear = f"{target_present} in data"
    setup_linear = "from __main__ import data, target_present"
    t_linear = min(timeit.repeat(stmt=stmt_linear, setup=setup_linear, globals=globals(), number=num_runs, repeat=3)) / num_runs

    def binary_search(arr, x):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    stmt_binary = "binary_search(data, target_present)"
    setup_binary = "from __main__ import data, target_present, binary_search"
    t_binary = min(timeit.repeat(stmt=stmt_binary, setup=setup_binary, globals=globals(), number=num_runs, repeat=3)) / num_runs

    linear_times.append(t_linear)
    binary_times.append(t_binary)

print("Размер | Линейный (сек) | Бинарный (сек)")
for size, lt, bt in zip(sizes, linear_times, binary_times):
    print(f"{size:>6} | {lt:.9f} | {bt:.9f}")