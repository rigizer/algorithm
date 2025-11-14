def solution(info, n, m):
    INF = 10**9

    dp = [INF] * n
    dp[0] = 0

    for a_trace, b_trace in info:
        next_dp = [INF] * n

        for a in range(n):
            if dp[a] == INF:
                continue

            new_a = a + a_trace
            if new_a < n:
                if dp[a] < next_dp[new_a]:
                    next_dp[new_a] = dp[a]

            new_b = dp[a] + b_trace
            if new_b < m:
                if new_b < next_dp[a]:
                    next_dp[a] = new_b

        dp = next_dp

    result = -1
    for a in range(n):
        if dp[a] < m:
            result = a
            break

    return result