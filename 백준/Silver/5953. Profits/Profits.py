import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
result = -10**18
current = 0

for _ in range(n):
    x = int(input())
    current = max(x, current + x)
    result = max(result, current)

print(result)