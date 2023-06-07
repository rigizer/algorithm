from collections import deque

def solution(maps):
    MAP_HEIGHT = len(maps)
    MAP_WIDTH = len(maps[0])
    
    queue = deque()
    visited = [[[False] * MAP_WIDTH for _ in range(MAP_HEIGHT)] for _ in range(2)]
    
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            if maps[i][j] == 'S':
                queue.append((i, j, 0, 0))
                visited[0][i][j] = True
    
    while queue:
        ny, nx, nd, nt = queue.popleft()
        
        if maps[ny][nx] == 'E' and nd == 1:
            return nt
        
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx
            
            if 0 <= y < MAP_HEIGHT and 0 <= x < MAP_WIDTH and maps[y][x] != 'X' and visited[nd][y][x] == False:
                if nd == 0 and maps[y][x] != 'L':
                    queue.append((y, x, 0, nt + 1))
                    visited[0][y][x] = True
                        
                else:
                    queue.append((y, x, 1, nt + 1))
                    visited[1][y][x] = True
    
    return -1