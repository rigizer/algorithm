from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
parent = [0] * (n + 1)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    i = queue.popleft()

    for v in graph[i]:
        if visited[v] == False:
            queue.append(v)
            visited[v] = True
            parent[v] = i

print('\n'.join(map(str, parent[2:n + 1])))