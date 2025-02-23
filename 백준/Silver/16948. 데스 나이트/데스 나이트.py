from collections import deque

dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]

def bfs(n, r1, c1, r2, c2):
    queue = deque()
    visited = [[False] * n for _ in range(n)]

    queue.append((r1, c1, 0))
    visited[r1][c1] = True

    while queue:
        y, x, t = queue.popleft()

        if (y, x) == (r2, c2):
            return t
        
        for d in range(6):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == False:
                queue.append((ny, nx, t + 1))
                visited[ny][nx] = True

    return -1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

result = bfs(n, r1, c1, r2, c2)
print(result)