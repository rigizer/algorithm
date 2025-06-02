n, k = map(int, input().split())
dp = [[1] * (n + 1) for _ in range(n + 1)]

for i in range(3, n + 1):
    for j in range(2, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][k])