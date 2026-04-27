from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init(n, board, queue, dist):
    door = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                door += 1
                if door == 2:
                    return i, j
                
                for d in range(4):
                    dist[i][j][d] = 0
                    queue.appendleft((i, j, 0, d))

def bfs(n, board):
    queue = deque()
    INF = 10 ** 9
    dist = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    ey, ex = init(n, board, queue, dist)

    while queue:
        y, x, t, dir = queue.popleft()

        if (y, x) == (ey, ex):
            return t

        ny = y + dy[dir]
        nx = x + dx[dir]

        if not (0 <= ny < n and 0 <= nx < n):
            continue
        if board[ny][nx] == '*':
            continue

        if dist[ny][nx][dir] > t:
            dist[ny][nx][dir] = t
            queue.appendleft((ny, nx, t, dir))

        if board[ny][nx] == '!':
            for nd in [(dir + 1) % 4, (dir + 3) % 4]:
                if dist[ny][nx][nd] > t + 1:
                    dist[ny][nx][nd] = t + 1
                    queue.append((ny, nx, t + 1, nd))

n = int(input())
board = [list(input()) for _ in range(n)]

result = bfs(n, board)
print(result)