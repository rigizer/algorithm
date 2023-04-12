from collections import deque

dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs_init(n, m, board, queue, visited):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'K':
                queue.append((i, j, 0))
                visited[i][j] = True
                return

def bfs(n, m, board):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    bfs_init(n, m, board, queue, visited)

    while queue:
        ny, nx, nt = queue.popleft()

        for d in range(8):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m and board[y][x] != '#' and visited[y][x] == False:
                if board[y][x] == 'X':
                    return nt + 1
                
                queue.append((y, x, nt + 1))
                visited[y][x] = True
    
    return -1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

result = bfs(n, m, board)
print(result)