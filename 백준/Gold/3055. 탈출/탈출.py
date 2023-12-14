from collections import deque

def find_word(r, c, board, queue, visited, word):
    for i in range(r):
        for j in range(c):
            if board[i][j] == word:
                queue.append((i, j, 0))
                visited[i][j] = 0

def bfs_water(r, c, board):
    queue = deque()
    visited = [[1e9] * c for _ in range(r)]

    find_word(r, c, board, queue, visited, '*')

    while queue:
        ny, nx, nt = queue.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < r and 0 <= x < c and board[y][x] != 'X' and board[y][x] != 'D' and visited[y][x] > nt + 1:
                queue.append((y, x, nt + 1))
                visited[y][x] = nt + 1

    return visited

def bfs(r, c, board, visited_water):
    queue = deque()
    visited = [[1e9] * c for _ in range(r)]

    find_word(r, c, board, queue, visited, 'S')

    while queue:
        ny, nx, nt = queue.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < r and 0 <= x < c and board[y][x] != 'X' and visited[y][x] > nt + 1 and visited_water[y][x] > nt + 1:
                if board[y][x] == 'D':
                    return nt + 1

                queue.append((y, x, nt + 1))
                visited[y][x] = nt + 1

    return 'KAKTUS'


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

visited_water = bfs_water(r, c, board)
result = bfs(r, c, board, visited_water)
print(result)