from collections import deque

max_dist = 0
max_list = [1]

def bfs(n, m, graph):
    global max_dist, max_list

    queue = deque()
    visited = [False] * (n + 1)

    queue.append((1, 0))
    visited[1] = True

    while queue:
        x, t = queue.popleft()

        if max_dist < t:
            max_dist = t
            max_list.clear()
        if max_dist == t:
            max_list.append(x)

        for i in graph[x]:
            if visited[i] == False:
                queue.append((i, t + 1))
                visited[i] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(n, m, graph)
print(sorted(max_list)[0], max_dist, len(max_list))