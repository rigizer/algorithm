tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + data[i - 1]
        
    max_sum = 0
    min_sum = 1e9
    
    for i in range(n - m + 1):
        current_sum = dp[i + m] - dp[i]
        max_sum = max(max_sum, current_sum)
        min_sum = min(min_sum, current_sum)
        
    print(f'#{t} {max_sum - min_sum}')