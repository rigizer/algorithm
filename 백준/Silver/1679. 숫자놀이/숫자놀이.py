n = int(input())
arr = list(map(int, input().split()))
k = int(input())

m = max(arr) * k
dp = [100_001] * (m + 1)
dp[0] = 0

for i in range(m + 1):
    for j in arr:
        if i + j <= m:
            dp[i + j] = min(dp[i] + 1, dp[i + j])

for i in range(1, m + 1):
    if dp[i] > k:
        if i % 2 == 0:
            print(f'holsoon win at {i}')
        else:
            print(f'jjaksoon win at {i}')
        break