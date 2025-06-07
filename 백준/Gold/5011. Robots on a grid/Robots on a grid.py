from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = int(input())
board = [list(input()) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

if board[0][0] == '.':
    dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            if i + 1 < n and board[i + 1][j] == '.':
                dp[i + 1][j] += dp[i][j]
            if j + 1 < n and board[i][j + 1] == '.':
                dp[i][j + 1] += dp[i][j]

if dp[n - 1][n - 1] != 0:
    print(dp[n - 1][n - 1] % (2 ** 31 - 1))
else:
    result = False

    queue = deque()
    visited = [[False] * n for _ in range(n)]

    if board[0][0] == '.':
        queue.append((0, 0))
        visited[0][0] = True

    while queue:
        y, x = queue.popleft()

        if (y, x) == (n - 1, n - 1):
            result = True
            break
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == '.' and visited[ny][nx] == False:
                queue.append((ny, nx))
                visited[ny][nx] = True

    if result == True:
        print('THE GAME IS A LIE')
    else:
        print('INCONCEIVABLE')