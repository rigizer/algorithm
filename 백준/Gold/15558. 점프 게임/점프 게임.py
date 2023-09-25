from collections import deque

def bfs(board, n, k):
    queue = deque()
    visited = [[False] * (n + k + 1) for _ in range(2)]

    queue.append((0, 0, 0))
    visited[0][0] = True

    while queue:
        ny, nx, nt = queue.popleft()

        if nx > n:
            return 1
        
        if nx + 1 >= n or (board[ny][nx + 1] == 1 and visited[ny][nx + 1] == False):
            queue.append((ny, nx + 1, nt + 1))
            visited[ny][nx + 1] = True

        if nx - 1 >= 0 and board[ny][nx - 1] == 1 and nx - 1 >= nt + 1 and visited[ny][nx - 1] == False:
            queue.append((ny, nx - 1, nt + 1))
            visited[ny][nx - 1] = True
        
        if nx + k >= n or (board[not ny][nx + k] == 1 and visited[not ny][nx + k] == False):
            queue.append((not ny, nx + k, nt + 1))
            visited[not ny][nx + k] = True

    return 0

n, k = map(int, input().split())
board = [[int(i) for i in input()] for _ in range(2)]
result = bfs(board, n, k)

print(result)