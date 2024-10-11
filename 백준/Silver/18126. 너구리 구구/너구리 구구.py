from collections import deque

def bfs(n, graph):
    result = 0

    queue = deque()
    visited = [False] * (n + 1)

    queue.append((1, 0))
    visited[1] = True

    while queue:
        s, t = queue.popleft()

        if result < t:
            result = t
        
        for e, w in graph[s]:
            if not visited[e]:
                queue.append((e, t + w))
                visited[e] = True

    return result

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

result = bfs(n, graph)
print(result)