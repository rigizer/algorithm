from collections import deque

def bfs(i, j, m, n, board, visited):
    queue = deque()
    queue.append((i, j))

    while queue:
        ny, nx = queue.popleft()

        for dy, dx in [(-1, 0) ,(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < m and 0 <= x < n and board[y][x] == '#' and visited[y][x] == False:
                queue.append((y, x))
                visited[y][x] = True

m, n = map(int, input().split())
board = [input() for _ in range(m)]
visited = [[False] * n for _ in range(m)]

result = 0

for i in range(m):
    for j in range(n):
        if board[i][j] == '#' and visited[i][j] == False:
            bfs(i, j, m, n, board, visited)
            result += 1

print(result)