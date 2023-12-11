from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def find_word(n, board, word):
    for i in range(n):
        for j in range(n):
            if board[i][j] == word:
                return i, j

def bfs(n, board):
    ay, ax = find_word(n, board, 'A')
    by, bx = find_word(n, board, 'B')

    queue = deque()
    visited = [[1e9] * n for _ in range(n)]

    queue.append((ay, ax, 0, 0))
    visited[ay][ax] = 0

    ny, nx, nt, nd = queue.popleft()

    for d in range(4):
        y = ny + dy[d]
        x = nx + dx[d]

        if 0 <= y < n and 0 <= x < n and board[y][x] != 'x' and visited[y][x] == 1e9:
            queue.append((y, x, 0, d))
            visited[y][x] = 0
    
    while queue:
        ny, nx, nt, nd = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < n and board[y][x] != 'x':
                # 왔던 길로 다시 돌아가는 것을 방지
                if nd % 2 == d % 2 and nd != d:
                    continue

                if (nd % 2 == 0 and d % 2 == 1) or (nd % 2 == 1 and d % 2 == 0):
                    if visited[y][x] >= nt + 1:
                        queue.append((y, x, nt + 1, d))
                        visited[y][x] = nt + 1
                else:
                    if visited[y][x] >= nt:
                        queue.append((y, x, nt, d))
                        visited[y][x] = nt

    return visited[by][bx]

n = int(input())
board = [list(input()) for _ in range(n)]

result = bfs(n, board)
print(result)