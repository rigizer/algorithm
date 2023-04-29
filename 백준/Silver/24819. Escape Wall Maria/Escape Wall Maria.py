from collections import deque

# 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs_init(n, m, board, queue, visited):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                queue.append((i, j, 0))
                visited[i][j] = True

                return

def bfs(t, n, m, board):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    bfs_init(n, m, board, queue, visited)

    while queue:
        ny, nx, nt = queue.popleft()

        if nt > t:
            return 'NOT POSSIBLE'

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m:
                if board[y][x] != '1' and visited[y][x] == False:
                    if board[y][x] != '0':
                        if board[y][x] == 'U' and d != 2: continue
                        elif board[y][x] == 'R' and d != 3: continue
                        elif board[y][x] == 'D' and d != 0: continue
                        elif board[y][x] == 'L' and d != 1: continue
                    
                    queue.append((y, x, nt + 1))
                    visited[y][x] = True
            
            else:
                if nt <= t:
                    return nt

    return 'NOT POSSIBLE'

t, n, m = map(int, input().split())
board = [input() for _ in range(n)]

result = bfs(t, n, m, board)
print(result)