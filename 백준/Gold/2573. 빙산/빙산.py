from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def check(n, m, board):
    cnt = 0

    queue = deque()
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    ny, nx = queue.popleft()

                    for d in range(4):
                        y = ny + dy[d]
                        x = nx + dx[d]

                        if 0 <= y < n and 0 <= x < m and board[y][x] > 0 and visited[y][x] == False:
                            queue.append((y, x))
                            visited[y][x] = True

                cnt += 1

                if cnt == 2:
                    return 2

    return cnt

def bfs(n, m, board):
    year = 0

    while True:
        check_result = check(n, m, board)

        if check_result == 0:
            return 0
        elif check_result >= 2:
            return year
        
        queue = deque()

        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            ny, nx = queue.popleft()

            for d in range(4):
                y = ny + dy[d]
                x = nx + dx[d]

                if 0 <= y < n and 0 <= x < m and board[y][x] > 0:
                    board[y][x] -= 1
        
        year += 1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = bfs(n, m, board)
print(result)