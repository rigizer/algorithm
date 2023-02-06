from collections import deque

def bfs(n, m, board):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    queue.append((0, 0, 0))
    visited[0][0] = True

    while queue:
        ny, nx, nt = queue.popleft()

        if (n - 1, m - 1) == (ny, nx):
            return nt
        
        value = board[ny][nx]
        for dy, dx in [(-value, 0), (0, value), (value, 0), (0, -value)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < n and 0 <= x < m and visited[y][x] == False:
                queue.append((y, x, nt + 1))
                visited[y][x] = True
    
    return 'IMPOSSIBLE'

n, m = map(int, input().split())
board = [[int(j) for j in input()] for _ in range(n)]

result = bfs(n, m, board)
print(result)