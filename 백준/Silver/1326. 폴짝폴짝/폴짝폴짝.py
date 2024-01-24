from collections import deque

def bfs(n, bridge, a, b):
    queue = deque()
    visited = [False] * n

    queue.append((a, 0))
    visited[a] = True

    while queue:
        nx, nt = queue.popleft()

        if nx == b:
            return nt
        
        for x in range(nx + bridge[nx], n, bridge[nx]):
            if 0 <= x < n and visited[x] == False:
                queue.append((x, nt + 1))
                visited[x] = True

        for x in range(nx - bridge[nx], -1, -bridge[nx]):
            if 0 <= x < n and visited[x] == False:
                queue.append((x, nt + 1))
                visited[x] = True

    return -1

n = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

result = bfs(n, bridge, a - 1, b - 1)
print(result)