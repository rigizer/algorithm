from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque()
visited = [False] * (n + 1)

queue.append((a, 0))
visited[a] = True

while queue:
    i, t = queue.popleft()

    if i == b:
        print(t)
        break
    
    for ni in graph[i]:
        if not visited[ni]:
            queue.append((ni, t + 1))
            visited[ni] = True

else:
    print(-1)