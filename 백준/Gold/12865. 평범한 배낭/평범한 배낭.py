n, k = map(int, input().split())
wv_lst = [[0, 0]]
for _ in range(n):
    wv_lst.append(list(map(int, input().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = wv_lst[i][0]
        value = wv_lst[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])