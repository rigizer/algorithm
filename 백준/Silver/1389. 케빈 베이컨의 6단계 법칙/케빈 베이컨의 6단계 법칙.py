from collections import deque

result = [1e9, 1e9]
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    if b not in graph[a]:
        graph[a].append(b)
        graph[b].append(a)

def bfs(n, m, graph, i):
    queue = deque()
    visited = [1e9] * (n + 1)

    queue.append((i, 0))
    visited[i] = 0

    while queue:
        x, t = queue.popleft()

        for nx in graph[x]:
            if visited[nx] == 1e9:
                queue.append((nx, t + 1))
                visited[nx] = t + 1

    return sum(visited[1:])

for i in range(1, n + 1):
    result_i = bfs(n, m, graph, i)

    if result_i < result[1]:
        result = [i, result_i]

print(result[0])