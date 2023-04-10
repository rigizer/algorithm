from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(m, board):
    queue = deque()
    visited = [[False] * m for _ in range(m)]

    queue.append((0, 0, 0))
    visited[0][0] = True

    while queue:
        ny, nx, nt = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < m and 0 <= x < m and board[y][x] != '*' and visited[y][x] == False:
                if (y, x) == (m - 1, m - 1):
                    return nt + 1

                queue.append((y, x, nt + 1))
                visited[y][x] = True
    
    return -1

n = int(input())
for _ in range(n):
    m = int(input())
    board = [list(input()) for _ in range(m)]

    result = bfs(m, board)
    print(result)