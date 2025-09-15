import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for x in graph[node]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True
                count += 1
                
    return count

result = 0
for i in range(1, n + 1):
    if visited[i] == False:
        result = max(result, bfs(i))
print(result)