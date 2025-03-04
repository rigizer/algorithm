from collections import deque

dfs_result = []
bfs_result = []

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(i):
    dfs_result.append(i)
    dfs_visited[i] = True

    for x in graph[i]:
        if dfs_visited[x] == False:
            dfs_visited[i] = True
            dfs(x)

def bfs(i):
    queue = deque()
    queue.append(i)
    bfs_result.append(i)
    bfs_visited[i] = True

    while queue:
        x = queue.popleft()
        
        for nx in graph[x]:
            if bfs_visited[nx] == False:
                queue.append(nx)
                bfs_result.append(nx)
                bfs_visited[nx] = True

dfs(v)
bfs(v)

print(*dfs_result)
print(*bfs_result)