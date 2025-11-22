import sys
input = lambda: sys.stdin.readline().rstrip()

k = int(input())
grid = [[1 for _ in range(10)] for _ in range(10)]

for _ in range(k):
    parts = list(map(int, input().split()))
    rows = parts[:3]
    cols = parts[3:]
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1
    for r in rows:
        for j in range(10):
            grid[r-1][j] = 1
    for c in cols:
        for i in range(10):
            grid[i][c-1] = 1

lines = [' '.join(str(grid[i][j]) for j in range(10)) for i in range(10)]
print('\n'.join(lines))