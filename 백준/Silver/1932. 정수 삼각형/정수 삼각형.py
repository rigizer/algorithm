n = int(input())
ns = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1e9] * n for _ in range(n)]

dp[0][0] = ns[0][0]
for i in range(n - 1):
    for j in range(i + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + ns[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + ns[i + 1][j + 1])

print(max(dp[n - 1]))