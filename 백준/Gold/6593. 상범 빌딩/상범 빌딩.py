from collections import deque

start, end = None, None

# 전, 후, 좌, 우, 상, 하
dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

def init_board(l, r, c):
    global start, end

    board = []
    for z in range(l):
        z_temp = []
        for y in range(r):
            y_temp = list(input())

            for x, val in enumerate(y_temp):
                if val == 'S':
                    start = (z, y, x)
                elif val == 'E':
                    end = (z, y, x)

            z_temp.append(y_temp)
        board.append(z_temp)
        input()

    return board

def bfs(l, r, c, board):
    global start, end

    queue = deque()
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]

    queue.append((start[0], start[1], start[2], 0))
    visited[start[0]][start[1]][start[2]] = True

    while queue:
        nz, ny, nx, nt = queue.popleft()

        if board[nz][ny][nx] == 'E':
            return 'Escaped in {} minute(s).'.format(nt)
        
        for d in range(6):
            z = nz + dz[d]
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= z < l and 0 <= y < r and 0 <= x < c and board[z][y][x] != '#' and visited[z][y][x] == False:
                queue.append((z, y, x, nt + 1))
                visited[z][y][x] = True
    
    return 'Trapped!'

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break

    board = init_board(l, r, c)

    result = bfs(l, r, c, board)
    print(result)