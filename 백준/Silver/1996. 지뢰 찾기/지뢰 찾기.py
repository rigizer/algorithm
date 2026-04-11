import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
grid = [input() for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

result = [['0'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] != '.':
            result[i][j] = '*'
            continue

        total = 0
        for d in range(8):
            ni = i + dx[d]
            nj = j + dy[d]

            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] != '.':
                    total += int(grid[ni][nj])

        if total >= 10:
            result[i][j] = 'M'
        else:
            result[i][j] = str(total)

for row in result:
    print(''.join(row))