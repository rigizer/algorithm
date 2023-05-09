from collections import deque

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(w, h, board):
    result = 0

    queue = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '.' and visited[i][j] == False:
                cnt = 0

                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    ny, nx = queue.popleft()
                    cnt += 1
                    
                    for d in range(8):
                        y = ny + dy[d]
                        x = nx + dx[d]

                        if 0 <= y < h and 0 <= x < w and board[y][x] == '.' and visited[y][x] == False:
                            queue.append((y, x))
                            visited[y][x] = True
                
                result = max(result, cnt)

    return result

w, h = map(int, input().split())
board = [list(input()) for _ in range(h)]

result = bfs(w, h, board)
print(result)