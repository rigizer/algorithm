from collections import deque
import math

def bfs(n, k, visited):
    queue = deque()
    queue.append((0, 0))
    visited[0] = True

    while queue:
        nn, nt = queue.popleft()

        if nn == n and nt <= k:
            return 'minigimbob'
        
        now = nn + 1
        if now <= n and visited[now] == False:
            queue.append((now, nt + 1))
            visited[now] = True

        now = nn + math.floor(nn / 2)
        if now <= n and visited[now] == False:
            queue.append((now, nt + 1))
            visited[now] = True
    
    return 'water'

n, k = map(int, input().split())
visited = [False] * (n + 1)

result = bfs(n, k, visited)
print(result)