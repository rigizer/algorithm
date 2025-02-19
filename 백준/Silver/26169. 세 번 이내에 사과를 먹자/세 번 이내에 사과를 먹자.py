from collections import deque

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

def bfs(r, c):
    queue = deque()
    queue.append((r, c, 0, 0, -1, -1))

    while queue:
        y, x, t, a, by, bx = queue.popleft()

        if t <= 3:
            if a >= 2:
                return 1
            if t == 3:
                continue
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < 5 and 0 <= nx < 5:
                if board[ny][nx] != -1:
                    if (ny, nx) != (by, bx):
                        if board[ny][nx] == 0:
                            queue.append((ny, nx, t + 1, a, y, x))
                        elif board[ny][nx] == 1:
                            queue.append((ny, nx, t + 1, a + 1, y, x))

    return 0

result = bfs(r, c)
print(result)