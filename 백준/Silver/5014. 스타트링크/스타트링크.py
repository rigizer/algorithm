from collections import deque

def bfs(f, s, g, u, d):
    queue = deque()
    visited = [-1] * (f + 1)

    queue.append((s, 0))
    visited[s] = 0

    while queue:
        x, t = queue.popleft()

        if x == g:
            return t

        for dir in [u, -d]:
            nx = x + dir

            if 1 <= nx <= f and visited[nx] == -1:
                queue.append((nx, t + 1))
                visited[nx] = x
    
    return 'use the stairs'

f, s, g, u, d = map(int, input().split())

result = bfs(f, s, g, u, d)
print(result)