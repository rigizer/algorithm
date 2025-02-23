from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, board):
    queue = deque()
    visited = [[[False] * m for _ in range(n)] for _ in range(2)]

    queue.append((0, 0, 0, 1))
    visited[0][0][0] = True

    while queue:
        y, x, s, t = queue.popleft()

        if (y, x) == (n - 1, m - 1):
            return t

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 0 and visited[s][ny][nx] == False:
                    queue.append((ny, nx, s, t + 1))
                    visited[s][ny][nx] = True
                elif board[ny][nx] == 1 and visited[s][ny][nx] == False and s == 0:
                    queue.append((ny, nx, s + 1, t + 1))
                    visited[s][ny][nx] = True

    return -1

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

result = bfs(n, m, board)
print(result)