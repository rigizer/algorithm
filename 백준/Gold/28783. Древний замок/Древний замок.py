from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init(n, m, board, queue, visited):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                queue.append((i, j, 0, 0))
                visited[0][i][j] = True

                return

def bfs(n, m, k, board, stone):
    queue = deque()
    visited = [[[False] * m for _ in range(n)] for _ in range(k + 1)]

    init(n, m, board, queue, visited)

    while queue:
        y, x, z, t = queue.popleft()

        if z == k:
            if board[y][x] == 'F':
                return t
        else:
            check = False
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == '#' and [ny + 1, nx + 1] == stone[z] and visited[z + 1][y][x] == False:
                    queue.append((y, x, z + 1, t))
                    visited[z + 1][y][x] = True

                    check = True
                    break
            
            if check == True:
                continue
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != '#' and visited[z][ny][nx] == False:
                queue.append((ny, nx, z, t + 1))
                visited[z][ny][nx] = True

    return -1

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
stone = [list(map(int, input().split())) for _ in range(k)]

result = bfs(n, m, k, board, stone)
print(result)