from collections import deque

def bfs(i, j, r, c, board, visited):
    space = 0
    queue = deque()

    queue.append((i, j))
    visited[i][j] = True

    while queue:
        ny, nx = queue.popleft()
        space += 1

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < r and 0 <= x < c and board[y][x] == '.' and visited[y][x] == False:
                queue.append((y, x))
                visited[y][x] = True

    return space

for _ in range(int(input())):
    r, c = map(int, input().split())

    board = [[j for j in input()] for _ in range(r)]
    visited = [[False] * c for _ in range(r)]
    
    section = 0
    space = 0

    for i in range(r):
        if board[i][0] == '.' and visited[i][0] == False:
            bfs(i, j, r, c, board, visited)
        if board[i][c - 1] == '.' and visited[i][c - 1] == False:
            bfs(i, j, r, c, board, visited)
    
    for j in range(c):
        if board[0][j] == '.' and visited[0][j] == False:
            bfs(i, j, r, c, board, visited)
        if board[r - 1][j] == '.' and visited[r - 1][j] == False:
            bfs(i, j, r, c, board, visited)

    # 상자 섹션과 각 공간의 수 확인
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.' and visited[i][j] == False:
                section += 1
                space += bfs(i, j, r, c, board, visited)

    result = ''
    result += f'{section} sections, ' if section != 1 else f'{section} section, '
    result += f'{space} spaces' if space != 1 else f'{space} space'

    print(result)
