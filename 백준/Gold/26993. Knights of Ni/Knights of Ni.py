from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init(w, h, board, queue, visited):
    for i in range(h):
        for j in range(w):
            if board[i][j] == 2:
                queue.append((i, j, 0, False))
                visited[0][i][j] = 0
                return

def bfs(w, h, board):
    queue = deque()
    visited = [[[1e9] * w for _ in range(h)] for _ in range(2)]

    init(w, h, board, queue, visited)

    while queue:
        y, x, t, found = queue.popleft()
        
        if found == True and board[y][x] == 3:
            return t
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < h and 0 <= nx < w and board[ny][nx] != 1 and visited[int(found)][ny][nx] > t + 1:
                if found == False and board[ny][nx] == 3:
                    continue
                
                nFound = found
                if found == False and board[ny][nx] == 4:
                    nFound = True

                queue.append((ny, nx, t + 1, nFound))
                visited[int(nFound)][ny][nx] = t + 1
        
w, h = map(int, input().split())
board = []

if w <= 40:
    for _ in range(h):
        board.append(list(map(int, input().split())))
else:
    temp = []
    rows_needed = h * w
    while len(temp) < rows_needed:
        temp.extend(list(map(int, input().split())))
    
    for i in range(h):
        board.append(temp[i * w:(i + 1) * w])

result = bfs(w, h, board)
print(result)