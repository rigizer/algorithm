n = int(input())
cases = [int(input()) for _ in range(n)]
dp = [[0 for _ in range(2)] for _ in range(100_001)]
dp[1][1] = dp[2][0] = dp[2][1] = 1
dp[3][0] = dp[3][1] = 2

for i in range(4, 100_001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 2][1] + dp[i - 3][1]) % 1_000_000_009
    dp[i][1] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 3][0]) % 1_000_000_009

for c in cases:
    print(str(dp[c][1]) + ' ' + str(dp[c][0]))