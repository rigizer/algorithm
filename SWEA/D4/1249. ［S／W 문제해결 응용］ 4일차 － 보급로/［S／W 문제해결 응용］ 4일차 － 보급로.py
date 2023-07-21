from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, board):
    queue = deque()
    visited = [[1e9] * n for _ in range(n)]

    queue.append((0, 0))
    visited[0][0] = 0

    while queue:
        ny, nx = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < n and visited[y][x] > visited[ny][nx] + board[y][x]:
                queue.append((y, x))
                visited[y][x] = visited[ny][nx] + board[y][x]

    return visited[n - 1][n - 1]

t = int(input())
for c in range(t):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    result = bfs(n, board)
    print(f'#{c + 1} {result}')