from collections import deque

def bfs(h, w, a, b, board):
    result = 0
    
    queue = deque()
    visited = [[False] * w for _ in range(h)]

    if board[a][b] == 'X':
        queue.append((a, b))
        visited[a][b] = True

    while queue:
        ny, nx = queue.popleft()

        for di, dy, dx in [(0, -1, 0), (1, -1, 1), (2, 0, 1), (3, 1, 1), (4, 1, 0), (5, 1, -1), (6, 0, -1), (7, -1, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < h and 0 <= x < w:
                if board[y][x] == '.' and di % 2 == 0:
                    result += 1
                elif board[y][x] == 'X' and visited[y][x] == False:
                    queue.append((y, x))
                    visited[y][x] = True
            else:
                if di % 2 == 0:
                    result += 1

    return result

while True:
    h, w, a, b = map(int, input().split())
    if (h, w, a, b) == (0, 0, 0, 0):
        break
    board = [list(input()) for _ in range(h)]

    result = bfs(h, w, a - 1, b - 1, board)
    print(result)