import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
arr = list(map(int, input().split()))

groups = {}
for a in arr:
    r = a % k
    if r not in groups:
        groups[r] = []
    groups[r].append(a)

for r in groups:
    groups[r].sort()

idx = {r: 0 for r in groups}

for v in range(1, n + 1):
    r = v % k
    if r not in groups:
        print(0)
        exit()
    i = idx[r]
    if i >= len(groups[r]) or groups[r][i] > v:
        print(0)
        exit()
    idx[r] += 1

print(1)