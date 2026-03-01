import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
rock = set(int(input()) for _ in range(m))

def bfs():
    queue = deque()
    visited = [[False] * (int((2*n)**0.5) + 2) for _ in range(n + 1)]
    
    queue.append((1, 0, 0))
    visited[1][0] = True

    while queue:
        x, v, cnt = queue.popleft()

        if x == n:
            return cnt
        
        for nv in [v - 1, v, v + 1]:
            if nv <= 0:
                continue
            
            nx = x + nv
            
            if nx > n:
                continue
            
            if nx in rock:
                continue
            
            if not visited[nx][nv]:
                queue.append((nx, nv, cnt + 1))
                visited[nx][nv] = True
    
    return -1

print(bfs())