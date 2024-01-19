from collections import deque

dy = [-1, -1, 0, 1, 1, 0]
dx = [0, 1, 1, 0, -1, -1]

def init_board():
    global queue, visited, a

    board = [[0] * 1500 for _ in range(1500)]
    y, x = 750, 750
    n, k = 1, 1

    board[y][x] = n

    while True:
        for d in range(0, 6):
            for _ in range(0, k - 1 if d == 1 else k):
                ny = y + dy[d]
                nx = x + dx[d]

                n += 1
                board[ny][nx] = n

                if n == a:
                    queue.append((ny, nx))
                    visited[ny][nx] = 1e9

                if n == 1_000_001:
                    return board
                
                y, x = ny, nx

        k += 1

def bfs(a, b, board, visited, queue):
    while queue:
        ny, nx = queue.popleft()

        if board[ny][nx] == b:
            return (ny, nx)
        
        for d in range(6):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < 1500 and 0 <= x < 1500 and visited[y][x] == None:
                queue.append((y, x))
                visited[y][x] = (ny, nx)

a, b = map(int, input().split())

queue = deque()
visited = [[None] * 1500 for _ in range(1500)]

board = init_board()
result = bfs(a, b, board, visited, queue)

data = []
y, x = result
while True:
    data.insert(0, board[y][x])

    if visited[y][x] == 1e9:
        break

    y, x = visited[y][x]

print(' '.join([str(i) for i in data]))