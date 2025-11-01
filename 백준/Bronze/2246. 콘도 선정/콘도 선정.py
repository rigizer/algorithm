import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
condos = [tuple(map(int, input().split())) for _ in range(n)]
condos.sort()

min_cost = float('inf')
result = 0

for d, c in condos:
    if c < min_cost:
        result += 1
        min_cost = c

print(result)