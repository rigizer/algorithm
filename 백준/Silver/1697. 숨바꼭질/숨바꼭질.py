import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

def bfs(n, k):
    queue = deque()
    visited = [False for _ in range(100_001)]
    
    queue.append([n, 0])
    visited[n] = True
    
    while queue:
        x, t = queue.popleft()
        
        if x == k:
            return t

        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx <= 100_000 and not visited[nx]:
                queue.append([nx, t + 1])
                visited[nx] = True

n, k = map(int, input().split())
result = bfs(n, k)
print(result)