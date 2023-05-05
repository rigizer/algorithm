from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(w, h, board):
    result = 0

    queue = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '*' and visited[i][j] == False:
                cnt = 0

                queue.append((i, j))
                visited[i][j] = True
                cnt += 1

                while queue:
                    ny, nx = queue.popleft()

                    for d in range(4):
                        y = ny + dy[d]
                        x = nx + dx[d]

                        if 0 <= y < h and 0 <= x < w and board[y][x] == '*' and visited[y][x] == False:
                            queue.append((y, x))
                            visited[y][x] = True
                            cnt += 1

                result = max(result, cnt)
    
    return result

w, h = map(int, input().split())
board = [list(input()) for _ in range(h)]

result = bfs(w, h, board)
print(result)