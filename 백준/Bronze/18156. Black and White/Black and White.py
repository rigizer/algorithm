import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
grid = [input() for _ in range(n)]
half = n // 2

for row in grid:
    if row.count('B') != half or row.count('W') != half:
        print(0)
        sys.exit(0)
    for i in range(n - 2):
        if row[i] == row[i + 1] == row[i + 2]:
            print(0)
            sys.exit(0)

for col in range(n):
    b = w = 0
    for row in range(n):
        if grid[row][col] == 'B':
            b += 1
        else:
            w += 1
    if b != half or w != half:
        print(0)
        sys.exit(0)
    for row in range(n - 2):
        if grid[row][col] == grid[row + 1][col] == grid[row + 2][col]:
            print(0)
            sys.exit(0)

print(1)