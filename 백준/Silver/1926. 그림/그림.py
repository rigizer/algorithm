import sys
sys.setrecursionlimit(10 ** 6)

from collections import deque

def dfs(n, m, board, queue, visited):
    global temp_size

    while queue:
        ny, nx = queue.pop()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < n and 0 <= x < m and board[y][x] == 1 and visited[y][x] == False:
                queue.append((y, x))
                visited[y][x] = True
                temp_size += 1

                dfs(n, m, board, queue, visited)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

queue = deque()
cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == False:
            queue.append((i, j))
            visited[i][j] = True
            temp_size = 1

            dfs(n, m, board, queue, visited)

            if max_area < temp_size:
                max_area = temp_size
            
            cnt += 1

print(cnt)
print(max_area)