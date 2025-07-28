from collections import deque

def bfs(n, k):
    MAX = 500_000

    if n == k:
        return 0
    
    queue = deque()
    visited = [[False] * (MAX + 1) for _ in range(2)]

    queue.append((n, 0))
    visited[0][n] = True

    while queue:
        x, t = queue.popleft()
        nk = k + t * (t + 1) // 2

        if nk > MAX:
            return -1
        
        if visited[t % 2][nk]:
            return t
        
        nt = t + 1
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= MAX and not visited[nt % 2][nx]:
                queue.append((nx, nt))
                visited[nt % 2][nx] = True
    
    return -1

n, k = map(int, input().split())
result = bfs(n, k)
print(result)