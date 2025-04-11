n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + a[i - 1]

m = int(input())
for x in range(m):
    i, j = map(int, input().split())
    result = dp[j] - dp[i - 1]
    print(result)