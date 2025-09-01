import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m, k  = map(int, input().split())
board = [list(input()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

def bfs():
    global n, m, k, x1, y1, x2, y2
    
    queue = deque()
    visited = [[1e9] *  m for _ in range(n)]
    
    queue.append((x1 - 1, y1 - 1, 0))
    visited[x1 - 1][y1 - 1] = 0
    
    while queue:
        y, x, t = queue.popleft()
        
        if (y, x) == (x2 - 1, y2 - 1):
            return visited[y][x]
        
        for d in range(4):
            for i in range(1, k + 1):
                ny = y + dy[d] * i
                nx = x + dx[d] * i

                if not (0 <= ny < n and 0 <= nx < m):
                    break
                if board[ny][nx] == '#':
                    break
                if visited[ny][nx] < t + 1:
                    break
                if visited[ny][nx] == t + 1:
                    continue
                queue.append((ny, nx, t + 1))
                visited[ny][nx] = t + 1

    return -1

result = bfs()
print(result)