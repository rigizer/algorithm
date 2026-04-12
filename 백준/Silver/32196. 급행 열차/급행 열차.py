import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, k, x, y = map(int, input().split())

vals = []
for _ in range(n):
    a, b = map(int, input().split())
    vals.append(a * x - b * y)

vals.sort()

result = k * (x + y) + sum(vals[:m])
print(result)