from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, board, active_virus_list, empty_cnt):
    result = 0
    active_empty = 0

    queue = deque()
    visited = [[False] * n for _ in range(n)]

    for i, j in active_virus_list:
        queue.append((i, j, 0))
        visited[i][j] = True
    
    while queue:
        ny, nx, nt = queue.popleft()
        result = nt

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < n and board[y][x] != 1 and visited[y][x] == False:
                queue.append((y, x, nt + 1))
                visited[y][x] = True
                active_empty += 1

    if active_empty == empty_cnt:
        return result

    return sys.maxsize

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

empty_cnt = 0
virus_list = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            empty_cnt += 1
        elif board[i][j] == 2:
            virus_list.append((i, j))

result = sys.maxsize

for active_virus_list in combinations(virus_list, m):
    temp_result = bfs(n, m, board, active_virus_list, empty_cnt + len(virus_list) - m)
    result = min(result, temp_result)

print(-1 if result == sys.maxsize else result)