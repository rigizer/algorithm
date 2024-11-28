from collections import deque

BOARD_Y = 10
BOARD_X = 9

dy = [-3, -3, -2, 2, 3, 3, 2, -2]
dx = [-2, 2, 3, 3, 2, -2, -3, -3]

def can_move(y, x, d, b):
    ty = [
        [-1, -2]
        ,[-1, -2]
        ,[0, -1]
        ,[0, 1]
        ,[1, 2]
        ,[1, 2]
        ,[0, 1]
        ,[0, -1]
    ]
    tx = [
        [0, -1]
        ,[0, 1]
        ,[1, 2]
        ,[1, 2]
        ,[0, 1]
        ,[0, -1]
        ,[-1, -2]
        ,[-1, -2]
    ]

    for k in range(2):
        yy = y + ty[d][k]
        xx = x + tx[d][k]

        if (b[0], b[1]) == (yy, xx):
            return False
        
    return True

def bfs(a, b):
    queue = deque()
    visited = [[False] * BOARD_X for _ in range(BOARD_Y)]
    
    queue.append((a[0], a[1], 0))
    visited[a[0]][a[1]] = True

    while queue:
        y, x, t = queue.popleft()

        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            
            if 0 <= ny < BOARD_Y and 0 <= nx < BOARD_X:
                if visited[ny][nx]:
                    continue
                if not can_move(y, x, d, b):
                    continue
                if (ny, nx) == (b[0], b[1]):
                    return t + 1

                queue.append((ny, nx, t + 1))
                visited[ny][nx] = True
    
    return -1

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = bfs(a, b)
print(result)