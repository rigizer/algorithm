from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def check_start_end(r, c, board):
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                return i, j

def bfs(r, c, d, board):
    queue = deque()
    visited = [[[False] * c for _ in range(r)] for _ in range(d + 1)]

    sy, sx = check_start_end(r, c, board)

    queue.append((0, sy, sx, 0))
    visited[0][sy][sx] = True

    while queue:
        nz, ny, nx, nt = queue.popleft()

        for dir in range(4):
            y = ny + dy[dir]
            x = nx + dx[dir]

            if 0 <= y < r and 0 <= x < c and visited[nz][y][x] == False and board[y][x] != '#':
                if nz == d and board[y][x] == 'E':
                    return nt + 1
                elif board[y][x] != '.' and board[y][x] != 'S' and board[y][x] != 'E':
                    if int(board[y][x]) == nz + 1:
                        queue.append((nz + 1, y, x, nt + 1))
                        visited[nz + 1][y][x] = True
                        continue
                
                queue.append((nz, y, x, nt + 1))
                visited[nz][y][x] = True

for _ in range(int(input())):
    r, c, d = map(int, input().split())
    board = [list(input()) for _ in range(r)]

    result = bfs(r, c, d, board)
    print(result)