from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(m, n, board):
    queue = deque()
    visited = [[1e9] * m for _ in range(n)]

    queue.append((0, 0, 0))
    visited[0][0] = 0

    while queue:
        ny, nx, nt = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m:
                if board[y][x] == 0 and nt < visited[y][x]:
                    queue.append((y, x, nt))
                    visited[y][x] = nt
                elif board[y][x] == 1 and nt + 1 < visited[y][x]:
                    queue.append((y, x, nt + 1))
                    visited[y][x] = nt + 1

    return visited[n - 1][m - 1]

n, m = map(int, input().split())
board = [[int(j) for j in input()] for _ in range(m)]

result = bfs(n, m, board)
print(result)