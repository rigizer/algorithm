from collections import deque

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = 0

queue = deque()
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and visited[i][j] == False:
            queue.append((i, j))
            visited[i][j] = True

            while queue:
                ny, nx = queue.popleft()

                for d in range(4):
                    y = ny + dy[d]
                    x = nx + dx[d]

                    if y == -1:
                        y = n - 1
                    elif y == n:
                        y = 0
                    
                    if x == -1:
                        x = m - 1
                    elif x == m:
                        x = 0

                    if board[y][x] == 0 and visited[y][x] == False:
                        queue.append((y, x))
                        visited[y][x] = True

            result += 1

print(result)