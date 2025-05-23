MOD = 1_000_000_009
MAX_N = 1000
MAX_M = 1000

dp = [[0] * (MAX_M + 1) for _ in range(MAX_N + 1)]
dp[0][0] = 1

for n in range(1, MAX_N + 1):
    for m in range(1, MAX_M + 1):
        for k in [1, 2, 3]:
            if n - k >= 0:
                dp[n][m] = (dp[n][m] + dp[n - k][m - 1]) % MOD

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(dp[n][m])