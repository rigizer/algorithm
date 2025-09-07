import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def bfs(n, l, r, board):
    result = 0
    while True:
        visited = [[False] * n for _ in range(n)]
        is_moved = False
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True
                    union = [(i, j)]
                    total_population = board[i][j]

                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                                if l <= abs(board[x][y] - board[nx][ny]) <= r:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                                    union.append((nx, ny))
                                    total_population += board[nx][ny]

                    if len(union) > 1:
                        is_moved = True
                        new_population = total_population // len(union)
                        for x, y in union:
                            board[x][y] = new_population

        if not is_moved:
            return result
        result += 1

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = bfs(n, l, r, board)
print(result)