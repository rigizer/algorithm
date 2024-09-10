from collections import deque

def bfs(n, s, d, f, b, k, p):
    queue = deque()
    visited = [False] * (n + 1)

    for i in p:
        visited[i] = 'POLICE'

    queue.append((s, 0))
    visited[s] = True

    while queue:
        x, v = queue.popleft()

        if x == d:
            return v
        
        for i in [f, -b]:
            if 1 <= x + i <= n and visited[x + i]  != 'POLICE':
                if visited[x + i] == False:
                    queue.append((x + i, v + 1))
                    visited[x + i] = True

    return 'BUG FOUND'

n, s, d, f, b, k = map(int, input().split())
p = [] if k == 0 else list(map(int, input().split()))

result = bfs(n, s, d, f, b, k, p)
print(result)