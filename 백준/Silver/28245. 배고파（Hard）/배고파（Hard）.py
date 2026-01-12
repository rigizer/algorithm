import sys
input = lambda: sys.stdin.readline().rstrip()

pairs = []
values = []

max_exp = 61
for x in range(max_exp):
    for y in range(x, max_exp):
        val = (1 << x) + (1 << y)
        if val > 10**18 + 10**6:
            break
        pairs.append((val, x, y))
        values.append(val)

pairs.sort()
values.sort()

import bisect

n = int(input())
result = []

for _ in range(n):
    m = int(input())
    idx = bisect.bisect_left(values, m)

    candidates = []
    if idx < len(values):
        candidates.append(pairs[idx])
    if idx > 0:
        candidates.append(pairs[idx - 1])

    best_val, best_x, best_y = candidates[0]
    best_diff = abs(best_val - m)

    for val, x, y in candidates[1:]:
        diff = abs(val - m)
        if diff < best_diff or (diff == best_diff and val < best_val):
            best_val, best_x, best_y = val, x, y
            best_diff = diff

    result.append(f'{best_x} {best_y}')

print('\n'.join(result))