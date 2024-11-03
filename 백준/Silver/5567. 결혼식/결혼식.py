from collections import deque

def bfs(n, graph):
    result = 0

    queue = deque()
    visited = [False] * (n + 1)

    queue.append((1, 0))
    visited[1] = True

    while queue:
        x, d = queue.popleft()

        for i in graph[x]:
            if visited[i] == False:
                queue.append((i, d + 1))
                visited[i] = True

                if d + 1 <= 2:
                    result += 1

    return result

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs(n, graph)
print(result)