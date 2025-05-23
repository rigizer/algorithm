nums = [int(input()) for _ in range(int(input()))]

dp = [0 for _ in range(100001)]
dp[0] = dp[1] = 1
dp[2] = dp[3] = 2
dp[4] = dp[5] = 3

for i in range(6, 100001):
    dp[i] = (dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1_000_000_009
for num in nums:
    print(dp[num])