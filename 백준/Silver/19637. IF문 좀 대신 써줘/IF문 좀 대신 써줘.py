import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
title = []
limit = []

for _ in range(n):
    name, val = input().split()
    title.append(name)
    limit.append(int(val))

result = []
for _ in range(m):
    power = int(input())
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if power <= limit[mid]:
            right = mid
        else:
            left = mid + 1
    result.append(title[left])

print('\n'.join(result))