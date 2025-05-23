dp = [0] * 10_001
dp[0] = 1

for num in [1, 2, 3]:
    for i in range(num, 10_001):
        dp[i] += dp[i - num]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])