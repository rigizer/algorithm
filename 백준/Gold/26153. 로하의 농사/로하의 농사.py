from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
i, j, p = map(int, input().split())

stack = deque()
visited = [[False] * m for _ in range(n)]

# y좌표, x좌표, 남은 파이프 재료, 물 누적 최대량, 현재 방향
stack.append((i, j, p, board[i][j], -1))
visited[i][j] = True

result = board[i][j]

def dfs(n, m, board, stack, visited):
    global result

    while stack:
        ny, nx, nt, nw, nd = stack.pop()

        result = max(result, nw)
        if nt == 0:
            continue

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m and visited[y][x] == False:
                if (nd == -1 or d == nd) and nt - 1 >= 0:
                    stack.append((y, x, nt - 1, nw + board[y][x], d))
                elif d != nd and nt - 2 >= 0:
                    stack.append((y, x, nt - 2, nw + board[y][x], d))
                else:
                    continue
                    
                visited[y][x] = True
                dfs(n, m, board, stack, visited)
                visited[y][x] = False

dfs(n, m, board, stack, visited)
print(result)