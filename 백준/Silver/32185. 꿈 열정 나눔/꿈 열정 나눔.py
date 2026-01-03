import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
v0, p0, s0 = map(int, input().split())
base = v0 + p0 + s0

candidates = []

for i in range(1, n + 1):
    v, p, s = map(int, input().split())
    total = v + p + s
    if total <= base:
        candidates.append((total, i))

candidates.sort(reverse=True)

selected = candidates[:m - 1]

result = [0]
for _, idx in selected:
    result.append(idx)

print(*result)