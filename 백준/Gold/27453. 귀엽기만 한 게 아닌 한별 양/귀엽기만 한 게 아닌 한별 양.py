from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init(n, m, k, board, queue, visited):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                queue.append((i, j, [-1, -1], 0, 0, 0))
                board[i][j] = 1e8
            elif board[i][j] == 'X':
                board[i][j] = 1e8
            elif board[i][j] == 'H':
                board[i][j] = -1
            else:
                board[i][j] = int(board[i][j])

def bfs(n, m, k, board):
    queue = deque()
    visited = [[[False] * m for _ in range(n)] for _ in range(4)]
    init(n, m, k, board, queue, visited)

    while queue:
        ny, nx, before, v1, v2, nt = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m and board[y][x] != 1e8 and (y, x) != (before[0], before[1]):
                v0 = board[y][x]
                vs = v0 + v1 + v2

                if board[y][x] == -1:
                    return nt + 1
                
                if visited[d][y][x] == True:
                    continue
                
                if vs <= k:
                    queue.append((y, x, [ny, nx], v0, v1, nt + 1))
                    visited[d][y][x] = True

    return -1

n, m, k = map(int, input().split())
board = [[i for i in input()] for _ in range(n)]

result = bfs(n, m, k, board)
print(result)