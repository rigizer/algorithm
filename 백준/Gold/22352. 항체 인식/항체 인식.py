from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def rollback(b_board, rollback_queue):
    while rollback_queue:
        ny, nx, value = rollback_queue.popleft()

        b_board[ny][nx] = value

def check(n, m, b_board, a_board):
    for i in range(n):
        for j in range(m):
            if b_board[i][j] != a_board[i][j]:
                return False
    
    return True

def bfs(n, m, i, j, b_board, a_board, visited):
    value = b_board[i][j]

    rollback_queue = deque()
    queue = deque()
    
    queue.append((i, j))
    rollback_queue.append((i, j, b_board[i][j]))
    b_board[i][j] = a_board[i][j]
    visited[i][j] = True

    while queue:
        ny, nx = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m and b_board[y][x] == value and visited[y][x] == False:
                queue.append((y, x))
                rollback_queue.append((y, x, b_board[y][x]))
                b_board[y][x] = a_board[i][j]
                visited[y][x] = True

    result = check(n, m, b_board, a_board)
    if result == True:
        return True
    else:
        rollback(b_board, rollback_queue)
        return False

n, m = map(int, input().split())
b_board = [list(map(int, input().split())) for _ in range(n)] # before
a_board = [list(map(int, input().split())) for _ in range(n)] # after
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            result = bfs(n, m, i, j, b_board, a_board, visited)
            if result == True:
                print('YES')
                exit(0)

print('NO')