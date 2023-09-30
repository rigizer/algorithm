from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
global_visited = [[False] * m for _ in range(n)]
result = 0

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(i, j, n, m):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    queue.append((i, j))
    visited[i][j] = True

    while queue:
        ny, nx = queue.popleft()
        
        for d in range(8):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m:
                if board[y][x] > board[i][j]:
                    return False
                elif board[y][x] == board[i][j] and visited[y][x] == False:
                    queue.append((y, x))
                    visited[y][x] = True
    
    for a in range(n):
        for b in range(m):
            if visited[a][b] == True:
                global_visited[a][b] = True

    return True

for i in range(n):
    for j in range(m):
        if global_visited[i][j] == False:
            checked = bfs(i, j, n, m)

            if checked == True:
                result += 1

print(result)