from collections import deque

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(m, n, i, j, board, visited):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        ny, nx = queue.popleft()

        for d in range(8):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < m and 0 <= x < n and board[y][x] == 1 and visited[y][x] == False:
                queue.append((y, x))
                visited[y][x] = True

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

result = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 1 and visited[i][j] == False:
            result += 1
            bfs(m, n, i, j, board, visited)

print(result)