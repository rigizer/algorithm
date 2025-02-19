from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(m):
    s, e = map(int, input().split())

    queue = deque()
    visited = [False] * (n + 1)

    queue.append((s, 0))
    visited[s] = True

    while queue:
        x, t = queue.popleft()

        if x == e:
            print(t)
            break

        for nx, nt in graph[x]:
            if visited[nx] == False:
                queue.append((nx, t + nt))
                visited[nx] = True