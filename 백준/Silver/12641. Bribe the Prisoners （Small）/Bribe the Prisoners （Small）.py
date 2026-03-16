import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for tc in range(1, t + 1):
    p, q = map(int, input().split())
    arr = list(map(int, input().split()))

    pos = [0] + arr + [p + 1]
    m = q + 2

    dp = [[0] * m for _ in range(m)]

    for length in range(2, m):
        for l in range(m - length):
            r = l + length
            dp[l][r] = 10**18
            for k in range(l + 1, r):
                cost = dp[l][k] + dp[k][r] + (pos[r] - pos[l] - 2)
                if cost < dp[l][r]:
                    dp[l][r] = cost
            if dp[l][r] == 10**18:
                dp[l][r] = 0

    print(f'Case #{tc}: {dp[0][m - 1]}')