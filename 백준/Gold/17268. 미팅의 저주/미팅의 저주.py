n = int(input())
if n % 2 != 0:
    print(0)
else:
    dp = [0] * (n // 2 + 1)
    dp[0] = 1

    for i in range(1, n // 2 + 1):
        for j in range(i):
            dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % 987654321
    print(dp[n // 2])