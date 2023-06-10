from collections import deque

max_val = -1e9
min_val = 1e9

def dfs(n, board, stack, visited):
    global max_val, min_val

    while stack:
        ny, nx, nt = stack.pop()

        if (n - 1, n - 1) == (ny, nx):
            max_val = max(max_val, nt)
            min_val = min(min_val, nt)
        
        for dy, dx in [(1, 0), (0, 1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < n and 0 <= x < n and visited[y][x] == False:
                visited[y][x] = True
                
                if board[y][x] in ('+', '-', '*'):
                    stack.append((y, x, nt))
                    
                else:
                    if board[ny][nx] == '+':
                        stack.append((y, x, nt + int(board[y][x])))
                    elif board[ny][nx] == '-':
                        stack.append((y, x, nt - int(board[y][x])))
                    elif board[ny][nx] == '*':
                        stack.append((y, x, nt * int(board[y][x])))
                    
                dfs(n, board, stack, visited)
                visited[y][x] = False

n = int(input())
board = [list(map(str, input().split())) for _ in range(n)]

stack = deque()
visited = [[False] * n for _ in range(n)]

stack.append((0, 0, int(board[0][0])))
visited[0][0] = True

dfs(n, board, stack, visited)
print(max_val, min_val)