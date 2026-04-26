import sys
input = lambda: sys.stdin.readline().rstrip()

r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

neg = -10**9
dp = [[neg] * c for _ in range(r)]

dp[0][0] = a[0][0]

for j in range(1, c):
    for i in range(r):
        best = neg
        if dp[i][j - 1] != neg:
            best = max(best, dp[i][j - 1])
        if i > 0 and dp[i - 1][j - 1] != neg:
            best = max(best, dp[i - 1][j - 1])
        if i < r - 1 and dp[i + 1][j - 1] != neg:
            best = max(best, dp[i + 1][j - 1])
        if best != neg:
            dp[i][j] = best + a[i][j]

print(dp[r - 1][c - 1])