from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def find(board, queue, visited, n):
    for i in range(16):
        for j in range(16):
            if board[i][j] == n:
                return i, j

def bfs(board):
    queue = deque()
    visited = [[False] * 16 for _ in range(16)]

    sy, sx = find(board, queue, visited, 2)
    ey, ex = find(board, queue, visited, 3)

    queue.append((sy, sx))
    visited[sy][sx] = True

    while queue:
        ny, nx = queue.popleft()

        if (ny, nx) == (ey, ex):
            return 1

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < 16 and 0 <= x < 16 and board[y][x] != 1 and visited[y][x] == False:
                queue.append((y, x))
                visited[y][x] = True

    return 0

for _ in range(10):
    t = int(input())
    board = [list(int(i) for i in input()) for _ in range(16)]

    result = bfs(board)
    print('#{} {}'.format(t, result))