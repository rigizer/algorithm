import sys
input = lambda: sys.stdin.readline().rstrip()

from bisect import bisect_left, bisect_right

MAX_B = 2_000_000_000

cubes = []
i = 1
while True:
    c = i * i * i
    if c > MAX_B:
        break
    cubes.append(c)
    i += 1

t = int(input())
results = []

for case in range(1, t + 1):
    a, b = map(int, input().split())
    left = bisect_left(cubes, a)
    right = bisect_right(cubes, b)
    count = right - left
    results.append(f'Case #{case}: {count}')

print('\n'.join(results))