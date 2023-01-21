from collections import deque

# 전, 후, 좌, 우, 상, 하
dz = [0, 0, 0, 0, 1, -1]
dy = [1, -1, 0, 0, 0, 0,]
dx = [0, 0, -1, 1, 0, 0]

def bfs(n, m, h, board):
    result = 0

    queue = deque()
    visited = [[[False] * n for _ in range(m)] for _ in range(h)]

    # 익은 토마토를 queue에 넣기
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if board[z][y][x] == 1:
                    queue.append((z, y, x, 0))
                    visited[z][y][x] = True

    # BFS 탐색
    while queue:
        nz, ny, nx, nt = queue.popleft()

        result = max(result, nt)

        for d in range(6):
            z = nz + dz[d]
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= z < h and 0 <= y < m and 0 <= x < n and board[z][y][x] == 0 and visited[z][y][x] == False:
                queue.append((z, y, x, nt + 1))
                visited[z][y][x] = True
                board[z][y][x] = 1

    # 익지 않은 토마토가 있는지 확인
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if board[z][y][x] == 0:
                    return -1
                
    return result

n, m, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]

result = bfs(n, m, h, board)
print(result)