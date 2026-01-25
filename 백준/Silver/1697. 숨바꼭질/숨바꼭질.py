from collections import deque

def bfs(n, k):
    queue = deque()
    visited = [False for _ in range(100_001)]

    queue.append([n, 0])
    visited[n] = True

    while queue:
        node = queue.popleft()

        x = node[0]
        t = node[1]

        if x == k:
            return t
        
        for d in [-1, 1, x]:
            nx = x + d

            if 0 <= nx <= 100_000:
                if visited[nx] == False:
                    queue.append([nx, t + 1])
                    visited[nx] = True

n, k = map(int, input().split())
result = bfs(n, k)

print(result)