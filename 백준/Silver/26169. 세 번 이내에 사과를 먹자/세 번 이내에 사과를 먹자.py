from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
result = 0

visited = [[False] * 5 for _ in range(5)]
visited[r][c] = True

def dfs(y, x, t, a):
    if t <= 3:
        if a >= 2:
            print(1)
            exit()
        if t == 3:
            return

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < 5 and 0 <= nx < 5:
            if board[ny][nx] != -1:
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    dfs(ny, nx, t + 1, a + board[ny][nx])
                    visited[ny][nx] = False

dfs(r, c, 0, 0)
print(0)