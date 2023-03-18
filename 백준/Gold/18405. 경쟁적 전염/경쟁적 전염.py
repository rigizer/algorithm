from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs_init(n, board, visited):
    virus = []

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                virus.append((board[i][j], i, j, 0))
                visited[i][j] = True
    
    virus.sort()
    return deque(virus)

def bfs(n, k, board, s, x, y):
    visited = [[False] * n for _ in range(n)]
    queue = bfs_init(n, board, visited)

    queue_break = False
    while queue:
        nv, ny, nx, nt = queue.popleft()

        for d in range(4):
            ty = ny + dy[d]
            tx = nx + dx[d]

            if 0 <= ty < n and 0 <= tx < n and board[ty][tx] == 0 and visited[ty][tx] == False:
                if nt + 1 > s:
                    queue_break = True
                    break
                
                board[ty][tx] = board[ny][nx]

                queue.append((board[ty][tx], ty, tx, nt + 1))
                visited[ty][tx] = True
            
            if queue_break == True:
                break
    
    if board[x - 1][y - 1] != 0:
        return board[x - 1][y - 1]

    return 0

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

result = bfs(n, k, board, s, x, y)
print(result)