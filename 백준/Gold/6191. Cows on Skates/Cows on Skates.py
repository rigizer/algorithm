from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(r, c, board, visited, before):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        y, x = queue.popleft()

        if (y, x) == (r - 1, c - 1):
            return

        for d in range(4):
            ny = dy[d] + y
            nx = dx[d] + x

            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] == '.' and visited[ny][nx] == False:
                queue.append((ny, nx))
                visited[ny][nx] = True
                before[ny][nx] = [y, x]

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
before = [[None] * c for _ in range(r)]

bfs(r, c, board, visited, before)

result = []
y, x = r - 1, c - 1
while True:
    result.insert(0, [y + 1, x + 1])
    if (y, x) == (0, 0):
        break
    y, x = before[y][x]

print('\n'.join([str(' '.join([str(j) for j in i])) for i in result]))