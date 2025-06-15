from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(input()) for _ in range(m)]

queue = deque()
visited = [[False] * n for _ in range(m)]

result = [0, 0]

for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            cnt = 1
            queue.append((i, j))
            visited[i][j] = True

            while queue:
                y, x = queue.popleft()

                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == board[y][x] and not visited[ny][nx]:
                        cnt += 1
                        queue.append((ny, nx))
                        visited[ny][nx] = True
        
            result[0 if board[i][j] == 'W' else 1] += cnt ** 2

print(*result)