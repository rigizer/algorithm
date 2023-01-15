from collections import deque

def init_queue(n, m, board, queue, visited):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'H':
                queue.append((i, j))
                visited[i][j] = True
                
                return

def bfs(n, m, board):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    init_queue(n, m, board, queue, visited)

    while queue:
        ny, nx = queue.popleft()

        for dy, dx in [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < n and 0 <= x < m and board[y][x] != '#' and visited[y][x] == False:
                if board[y][x] == 'H' and visited[y][x] == False:
                    return True
                
                queue.append((y, x))
                visited[y][x] = True
    
    return False

n, m = map(int, input().split())
board = [input() for _ in range(n)]

result = bfs(n, m, board)
print('JA' if result == True else 'NEJ')