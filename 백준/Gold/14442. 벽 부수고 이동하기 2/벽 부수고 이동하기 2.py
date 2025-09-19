import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, k, board):
    queue = deque()
    visited = [[[False] * m for _ in range(n)] for _ in range(k + 1)]
    
    queue.append((0, 0, 0, 0))
    visited[0][0][0] = True
    
    while queue:
        y, x, t, b = queue.popleft()
        
        if (y, x) == (n - 1, m - 1):
            return t + 1
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == '0' and not visited[b][ny][nx]:
                    queue.append((ny, nx, t + 1, b))
                    visited[b][ny][nx] = True
                    
                elif board[ny][nx] == '1' and b < k and not visited[b + 1][ny][nx]:
                    queue.append((ny, nx, t + 1, b + 1))
                    visited[b + 1][ny][nx] = True

    return -1

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]

result = bfs(n, m, k, board)
print(result)