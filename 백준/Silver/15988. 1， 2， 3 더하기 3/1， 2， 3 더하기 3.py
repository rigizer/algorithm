MOD = 1_000_000_009

dp = [0] * 1_000_001
dp[0] = 1

for i in range(1, 1_000_001):
    if i - 1 >= 0:
        dp[i] = (dp[i] + dp[i - 1]) % MOD
    if i - 2 >= 0:
        dp[i] = (dp[i] + dp[i - 2]) % MOD
    if i - 3 >= 0:
        dp[i] = (dp[i] + dp[i - 3]) % MOD

for _ in range(int(input())):
    n = int(input())
    print(dp[n])