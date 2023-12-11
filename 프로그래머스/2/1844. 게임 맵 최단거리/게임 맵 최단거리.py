from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(maps):
    n, m = len(maps), len(maps[0])
    
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    while queue:
        ny, nx, nt = queue.popleft()
        
        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]
        
            if 0 <= y < n and 0 <= x < m and maps[y][x] != 0 and visited[y][x] == False:
                if (y, x) == (n - 1, m - 1):
                    return nt + 1
                
                queue.append((y, x, nt + 1))
                visited[y][x] = True
                
    return -1

def solution(maps):
    return bfs(maps)