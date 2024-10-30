from collections import deque

def bfs(n, graph):
    result = [i for i in range(1, n + 1)]

    queue = deque()
    visited = [False] * (n + 1)

    queue.append(1)
    visited[1] = True
    result.remove(1)

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                result.remove(i)
    
    return result

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

result = bfs(n, graph)
print('\n'.join([str(i) for i in ([0] if len(result) == 0 else result)]))