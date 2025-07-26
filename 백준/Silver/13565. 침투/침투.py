import sys
from queue import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, board):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    for i in range(m):
        if board[0][i] == '0':
            queue.append((0, i))
            visited[0][i] = True

    while queue:
        y, x = queue.popleft()
        
        if y == n - 1:
            return 'YES'
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and board[ny][nx] == '0':
                queue.append((ny, nx))
                visited[ny][nx] = True
    
    return 'NO'

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
result = bfs(n, m, board)

print(result)