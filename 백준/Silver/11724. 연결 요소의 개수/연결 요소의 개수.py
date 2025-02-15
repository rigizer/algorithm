from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(i):
    queue = deque()
    queue.append(i)
    visited[i] = True

    while queue:
        node = queue.popleft()

        for v in graph[node]:
            if visited[v] == False:
                queue.append(v)
                visited[v] = True

for i in range(1, n + 1):
    if visited[i] == False:
        result += 1
        bfs(i)

print(result)