def scs(a, b):
    n, m = len(a), len(b)
    dp = [[''] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + a[i - 1]
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + b[j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + a[i - 1]
            else:
                if len(dp[i - 1][j] + a[i - 1]) < len(dp[i][j - 1] + b[j - 1]):
                    dp[i][j] = dp[i - 1][j] + a[i - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + b[j - 1]

    return dp[n][m]

try:
    while True:
        line = input()
        if not line:
            break
        a, b = line.split()
        print(scs(a, b))
except EOFError:
    pass