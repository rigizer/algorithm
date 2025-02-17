from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(r) for r in graph]

result = [0 for _ in range(n + 1)]
count = 0

queue = deque()
visited = [False] * (n + 1)

queue.append(r)
visited[r] = True
count += 1
result[r] = count

while queue:
    node = queue.popleft()

    for i in graph[node]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
            count += 1
            result[i] = count

print('\n'.join(map(str, [result[i] for i in range(1, n + 1)])))