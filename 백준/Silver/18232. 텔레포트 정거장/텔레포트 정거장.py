from collections import deque

n, m = map(int, input().split())
s, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

def bfs():
    global n, m, s, e

    queue = deque()
    visited = [False] * (n + 1)

    queue.append((s, 0))
    visited[s] = True

    while queue:
        x, t = queue.popleft()

        if x == e:
            return t
        
        for nx in [x - 1, x + 1] + graph[x]:
            if 1 <= nx <= n and visited[nx] == False:
                queue.append((nx, t + 1))
                visited[nx] = True

result = bfs()
print(result)