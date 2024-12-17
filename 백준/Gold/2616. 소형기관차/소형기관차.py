n = int(input())
train = list(map(int, input().split()))
limit = int(input())

s = [0]
value = 0
for t in train:
    value += t
    s.append(value)

dp = [[0] * (n + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * limit, n + 1):
        if i == 1:
            dp[i][j] = max(dp[i][j - 1], s[j] - s[j - limit])

        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - limit] + s[j] - s[j - limit])

print(dp[3][n])