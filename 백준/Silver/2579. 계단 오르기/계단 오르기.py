n = int(input())
s = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(s[1])
    exit()

dp = [0] * (n + 1)
dp[1] = s[1]
dp[2] = s[1] + s[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + s[i], dp[i - 3] + s[i - 1] + s[i])

print(dp[n])