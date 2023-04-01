from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(sy, sx, depth):
    global n, m

    while stack:
        ny, nx = stack.pop()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m and board[sy][sx] == board[y][x]:
                if depth >= 4 and visited[y][x] == True and y == sy and x == sx:
                    print("Yes")
                    exit()
                elif visited[y][x] == False:
                    stack.append((y, x))
                    visited[y][x] = True
                    dfs(sy, sx, depth + 1)
                    visited[y][x] = False

    return False

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

stack = deque()
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        stack.append((i, j))
        visited[i][j] = True
        dfs(i, j, 1)
        visited[i][j] = False

print('No')