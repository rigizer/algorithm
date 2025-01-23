n, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (t + 1) for _ in range(n)]

for i in range(0, n):
    for j in range(1, t + 1):
        w = data[i][0]
        v = data[i][1]
        
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n - 1][t])