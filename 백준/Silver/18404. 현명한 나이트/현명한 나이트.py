from collections import deque

dy = [-2, -2, -1, -1, 1, 1, 2, 2]
dx = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0
    while queue:
        ny, nx = queue.popleft()
        for d in range(8):
            y, x = ny + dy[d], nx + dx[d]
            if (0 <= y < n) and (0 <= x < n) and graph[y][x] == -1:
                queue.append((y, x))
                graph[y][x] = graph[ny][nx] + 1

n, m = map(int, input().split())
graph = [[-1] * n for _ in range(n)]
sy, sx = map(int, input().split())
location = [list(map(int, input().split())) for _ in range(m)]    

bfs(sy - 1, sx - 1)
for y, x in location:
    print(graph[y - 1][x - 1], end=' ')
print()