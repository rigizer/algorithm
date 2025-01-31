n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(k)]
dp = [[0] * (n + 1) for _ in range(k)]

for i in range(k):
    for j in range(1, n + 1):
        w = data[i][1]
        v = data[i][0]
        
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[k - 1][n])