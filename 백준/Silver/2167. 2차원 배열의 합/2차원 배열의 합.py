n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
do = [list(map(int, input().split())) for _ in range(k)]

dp = [[0 for i in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + arr[i - 1][j - 1] - dp[i - 1][j - 1]
for _, line in enumerate(do):
    i, j, x, y = line
    print(dp[x][y] - (dp[x][j - 1] + dp[i - 1][y]) + dp[i - 1][j - 1])