from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, board):
    queue = deque()
    visited = [[1e9] * n for _ in range(n)]

    queue.append((0, 0, 0))
    visited[0][0] = 0

    while queue:
        ny, nx, nc = queue.popleft()
        
        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < n:
                if board[y][x] == 1 and nc < visited[y][x]:
                    queue.append((y, x, nc))
                    visited[y][x] = nc
                elif board[y][x] == 0 and nc + 1 < visited[y][x]:
                    queue.append((y, x, nc + 1))
                    visited[y][x] = nc + 1
    
    return visited[n - 1][n - 1]

n = int(input())
board = [[int(j) for j in input()] for _ in range(n)]

result = bfs(n, board)
print(result)