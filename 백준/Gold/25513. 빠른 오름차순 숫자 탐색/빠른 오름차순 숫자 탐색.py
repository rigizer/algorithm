from collections import deque

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def bfs(board, visited, r, c):
    queue = deque()
    queue.append((0, r, c, 0))
    visited[0][r][c] = True

    while queue:
        nz, ny, nx, nt = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < 5 and 0 <= x < 5 and board[y][x] != -1:
                if visited[nz][y][x] == False:
                    if board[y][x] == nz + 1:
                        if board[y][x] == 6:
                            return nt + 1
                        
                        queue.append((nz + 1, y, x, nt + 1))
                        visited[nz + 1][y][x] = True

                    else:
                        queue.append((nz, y, x, nt + 1))
                        visited[nz][y][x] = True

    return -1

board = [list(map(int, input().split())) for _ in range(5)]
visited = [[[False] * 5 for _ in range(5)] for _ in range(6)]
r, c = map(int, input().split())

result = bfs(board, visited, r, c)
print(result)