import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]

doors = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '#':
            doors.append((i, j))

sr, sc = doors[0]
er, ec = doors[1]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

dist = [[[1e9] * 4 for _ in range(n)] for _ in range(n)]
dq = deque()

for d in range(4):
    dist[sr][sc][d] = 0
    dq.append((sr, sc, d))

while dq:
    r, c, d = dq.popleft()

    nr = r + dr[d]
    nc = c + dc[d]

    if not (0 <= nr < n and 0 <= nc < n):
        continue
    if board[nr][nc] == '*':
        continue

    if dist[nr][nc][d] > dist[r][c][d]:
        dist[nr][nc][d] = dist[r][c][d]
        dq.appendleft((nr, nc, d))

    if board[nr][nc] == '!':
        for nd in [(d + 1) % 4, (d + 3) % 4]:
            if dist[nr][nc][nd] > dist[r][c][d] + 1:
                dist[nr][nc][nd] = dist[r][c][d] + 1
                dq.append((nr, nc, nd))

result = min(dist[er][ec])
print(result)