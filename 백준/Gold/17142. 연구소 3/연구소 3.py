from itertools import combinations
from collections import deque
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs_init(active_virus, queue, visited):
    for vy, vx in active_virus:
        queue.append((vy, vx))
        visited[vy][vx] = True

def bfs(n, board, active_virus, empty_cnt, result):
    empty_chk = 0
    t = 0

    queue = deque()
    visited = [[False] * n for _ in range(n)]

    bfs_init(active_virus, queue, visited)

    while True:
        queue_size = len(queue)

        if empty_cnt == 0:
            return 0
        
        if empty_chk == empty_cnt:
            return t
        
        if empty_cnt != 0 and queue_size == 0:
            return sys.maxsize
        
        t += 1

        if t > result:
            return sys.maxsize

        for _ in range(queue_size):
            ny, nx = queue.popleft()
            
            for d in range(4):
                y = ny + dy[d]
                x = nx + dx[d]

                if 0 <= y < n and 0 <= x < n and board[y][x] != 1 and visited[y][x] == False:
                    if board[y][x] == 0:
                        queue.append((y, x))
                        empty_chk += 1

                    elif board[y][x] == 2:
                        queue.append((y, x))
                    
                    visited[y][x] = True

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
for active_virus in combinations(virus_list, m):
    r = bfs(n, board, active_virus, empty_cnt, result)
    result = min(result, r)

print(-1 if result == sys.maxsize else result)