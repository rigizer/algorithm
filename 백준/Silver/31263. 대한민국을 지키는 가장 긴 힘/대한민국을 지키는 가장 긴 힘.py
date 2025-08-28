import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = input()

INF = 10 ** 9
dp = [INF] * (n + 1)
dp[0] = 0

for i in range(n):
    if dp[i] == INF:
        continue
    for length in range(1, 4):
        if i + length <= n:
            num_str = s[i:i+length]
            if num_str[0] == '0':
                continue
            num = int(num_str)
            if 1 <= num <= 641:
                if dp[i] + 1 < dp[i + length]:
                    dp[i+length] = dp[i] + 1

print(dp[n])