from collections import deque

dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]

def bfs(n, board):
    result = 0

    queue = deque()
    visited = [[[False] * n for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if board[i][j][k] == '*' and visited[i][j][k] == False:
                    result += 1
                    queue.append((i, j, k))
                    visited[i][j][k] = True

                    while queue:
                        nz, ny, nx = queue.popleft()

                        for d in range(6):
                            z = nz + dz[d]
                            y = ny + dy[d]
                            x = nx + dx[d]

                            if 0 <= z < n and 0 <= y < n and 0 <= x < n and board[z][y][x] == '*' and visited[z][y][x] == False:
                                queue.append((z, y, x))
                                visited[z][y][x] = True

    return result

n = int(input())
board = [[list(input()) for _ in range(n)] for _ in range(n)]

result = bfs(n, board)
print(result)