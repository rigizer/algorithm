from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(r, c, board):
    i, j, k = map(int, input().split())
    origin = board[i][j]

    queue = deque()
    visited = [[False] * c for _ in range(r)]

    queue.append((i, j))
    visited[i][j] = True
    board[i][j] = k

    while queue:
        ny, nx = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < r and 0 <= x < c and visited[y][x] == False and board[y][x] == origin:
                queue.append((y, x))
                visited[y][x] = True
                board[y][x] = k

r, c = map(int, input().split())
board = [[int(i) for i in input()] for _ in range(r)]

bfs(r, c, board)
print('\n'.join(''.join([str(j) for j in i]) for i in board))