from collections import deque

dy = [-1, -1, 1, 1]
dx = [-1, 1, 1, -1]

def bfs(start_y, start_x, end_y, end_x):
    queue = deque()
    visited = [[None] * 8 for _ in range(8)]

    queue.append((start_y, start_x, 0))
    visited[start_y][start_x] = (start_y, start_x)

    while queue:
        y, x, t = queue.popleft()

        if (y, x) == (end_y, end_x):
            q = deque()
            result = deque()
            
            q.append((y, x))
            result.append((y, x))

            if 0 < t:
                while q:
                    ny, nx = q.popleft()
                    yy, xx = visited[ny][nx]

                    q.append((yy, xx))
                    result.append((yy, xx))

                    if (yy, xx) == (start_y, start_x):
                        break
            
            return [str(t)] + [' '.join([chr(y + 65), str(x + 1)]) for (y, x) in reversed(result)]
        
        if t == 4:
            continue
        
        for d in range(4):
            dd = 0
            while True:
                dd += 1
                ny = y + (dy[d] * dd)
                nx = x + (dx[d] * dd)

                if not (0 <= ny < 8 and 0 <= nx < 8):
                    break
                
                if visited[ny][nx] != None:
                    continue

                queue.append((ny, nx, t + 1))
                visited[ny][nx] = (y, x)
    
    return 'Impossible'

t = int(input())
for _ in range(t):
    start_y, start_x, end_y, end_x = map(str, input().split())
    result = bfs(ord(start_y) - 65, int(start_x) - 1, ord(end_y) - 65, int(end_x) - 1)
    
    if type(result) == str:
        print(result)
    else:
        print(*result)