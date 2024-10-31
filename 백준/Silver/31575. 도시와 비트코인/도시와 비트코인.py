from collections import deque

dy = [0, 1]
dx = [1, 0]

def bfs(n, m, board):
    queue = deque()
    visited = [[False] * n for _ in range(m)]

    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        y, x = queue.popleft()

        if (y, x) == (m - 1, n - 1):
            return 'Yes'
        
        for d in range(2):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append((ny, nx))
                visited[ny][nx] = True

    return 'No'

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

result = bfs(n, m, board)
print(result)