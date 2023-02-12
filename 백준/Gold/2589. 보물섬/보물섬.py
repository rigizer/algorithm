from collections import deque

r, c = map(int, input().split())
board = [[j for j in input()] for _ in range(r)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(i, j, r, c, board):
    result = 0

    queue = deque()
    visited = [[False] * c for _ in range(r)]

    queue.append((i, j, 0))
    visited[i][j] = True

    while queue:
        ny, nx, nt = queue.popleft()
        result = max(result, nt)

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < r and 0 <= x < c and board[y][x] == 'L' and visited[y][x] == False:
                queue.append((y, x, nt + 1))
                visited[y][x] = True

    return result

result = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            result = max(result, bfs(i, j, r, c, board))

print(result)