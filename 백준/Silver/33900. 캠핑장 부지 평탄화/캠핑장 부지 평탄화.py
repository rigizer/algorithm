import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
plan = [list(map(int, input().split())) for _ in range(r)]

result = 0

for i in range(n - r + 1):
    for j in range(m - c + 1):
        base = grid[i][j] - plan[0][0]
        ok = True
        for x in range(r):
            for y in range(c):
                if grid[i + x][j + y] - plan[x][y] != base:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            result += 1

print(result)