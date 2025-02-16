from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m, k = map(int, input().split())
board = [[False] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = True

def bfs():
    result = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] == 1:
                size = 1

                queue = deque()
                visited = [[False] * (m + 1) for _ in range(n + 1)]

                queue.append((i, j))
                visited[i][j] = True
                
                while queue:
                    y, x = queue.popleft()
                    
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        
                        if 1 <= ny <= n and 1 <= nx <= m and board[ny][nx] == True and visited[ny][nx] == False:
                            size += 1
                            queue.append((ny, nx))
                            visited[ny][nx] = True
                
                result = max(result, size)
    
    return result

result = bfs()
print(result)