from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, k, board):
    result = 0

    queue = deque()
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                result += 1
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    y, x = queue.popleft()
                    
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if 0 <= ny < n and 0 <= nx < m:
                            if board[y][x] - k <= board[ny][nx] <= board[y][x] + k:
                                if visited[ny][nx] == False:
                                    queue.append((ny, nx))
                                    visited[ny][nx] = True
    
    return result

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = bfs(n, m, k, board)
print(result)