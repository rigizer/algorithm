def solve_one_case(n, k, grid):
    dp = [[[[0] * (k + 1) for _ in range(2)] for _ in range(n)] for _ in range(n)]

    if grid[0][1] == '.':
        dp[0][1][0][0] = 1
    if grid[1][0] == '.':
        dp[1][0][1][0] = 1

    for x in range(n):
        for y in range(n):
            for dir in range(2):
                for turns in range(k + 1):
                    val = dp[x][y][dir][turns]
                    if val == 0:
                        continue
                    if dir == 0:
                        nx, ny = x, y + 1
                    else:
                        nx, ny = x + 1, y

                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
                        dp[nx][ny][dir][turns] += val

                    if turns + 1 <= k:
                        ndir = 1 - dir
                        if ndir == 0:
                            nx, ny = x, y + 1
                        else:
                            nx, ny = x + 1, y
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
                            dp[nx][ny][ndir][turns + 1] += val

    total = 0
    for dir in range(2):
        for turns in range(k + 1):
            total += dp[n - 1][n - 1][dir][turns]
    return total

t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    grid = [input() for _ in range(n)]
    results.append(solve_one_case(n, k, grid))

for res in results:
    print(res)