def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    
    for i in range(0, len(triangle) - 1):   # 세로 반복
        for j in range(len(triangle[i])):   # 가로 크기만큼 반복
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    return max(dp[-1])