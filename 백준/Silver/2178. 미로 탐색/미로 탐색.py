from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, board):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    queue.append((0, 0, 1)) # 시작 y, 시작 x, 지나간 칸 수
    visited[0][0] = True

    while queue:
        y, x, t = queue.popleft()

        if (y, x) == (n - 1, m - 1):
            return t
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append((ny, nx, t + 1))
                visited[ny][nx] = True

n, m = map(int, input().split())
board = [[int(i) for i in input()] for _ in range(n)]

result = bfs(n, m, board)
print(result)