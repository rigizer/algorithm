import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
v = list(map(int, input().split()))

v.sort(reverse=True)

total = sum(v)
target = (total + 1) // 2

current = 0
k = 0

for i in range(n):
    current += v[i]
    k += 1
    if current >= target:
        break

result = m // (k + 1)
print(result)