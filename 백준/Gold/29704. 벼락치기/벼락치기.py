n, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

total_penalty = sum(row[1] for row in data)

dp = [0] * (t + 1)

for d, m in data:
    for j in range(t, d - 1, -1):
        dp[j] = max(dp[j], dp[j - d] + m)

print(total_penalty - dp[t])