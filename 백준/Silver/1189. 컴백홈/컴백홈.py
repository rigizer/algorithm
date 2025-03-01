dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

result = 0

r, c, k = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

def dfs(y, x, t):
    global r, c, k, result

    if (y, x) == (0, c - 1):
        if t == k:
            result += 1
        return

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < r and 0 <= nx < c and board[ny][nx] == '.' and visited[ny][nx] == False:
            visited[ny][nx] = True
            dfs(ny, nx, t + 1)
            visited[ny][nx] = False
    
visited[r - 1][0] = True
dfs(r - 1, 0, 1)
print(result)