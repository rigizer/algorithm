from collections import deque

SIZE = 16
TEST_CASE = 10

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init(board, queue, visited):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = True
                return

def bfs(board):
    queue = deque()
    visited = [[False] * SIZE for _ in range(SIZE)]

    init(board, queue, visited)

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < SIZE and 0 <= nx < SIZE:
                if board[ny][nx] != 1 and visited[ny][nx] == False:
                    queue.append((ny, nx))
                    visited[ny][nx] = True

                    if board[ny][nx] == 3:
                        return 1
    
    return 0

for _ in range(TEST_CASE):
    case_num = int(input())
    board = [list(map(int, input())) for _ in range(SIZE)]

    result = bfs(board)
    print(f'#{case_num} {result}')