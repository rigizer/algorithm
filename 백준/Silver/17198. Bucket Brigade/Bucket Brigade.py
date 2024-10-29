from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init(board, queue, visited):
    for i in range(10):
        for j in range(10):
            if board[i][j] == 'L':
                queue.append((i, j, 0))
                visited[i][j] = True
                return

def bfs(board):
    queue = deque()
    visited = [[False] * 10 for _ in range(10)]

    init(board, queue, visited)

    while queue:
        y, x, t = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < 10 and 0 <= nx < 10 and board[ny][nx] != 'R' and visited[ny][nx] == False:
                if board[ny][nx] == 'B':
                    return t
                
                queue.append((ny, nx, t + 1))
                visited[ny][nx] = True

board = [list(input()) for _ in range(10)]
result = bfs(board)

print(result)