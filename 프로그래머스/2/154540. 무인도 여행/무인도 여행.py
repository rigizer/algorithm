from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    answer = []

    board = [[0 if j == 'X' else int(j) for j in i] for i in maps]
    queue = deque()
    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True
                cnt = board[i][j]

                while queue:
                    ny, nx = queue.popleft()

                    for d in range(4):
                        y = ny + dy[d]
                        x = nx + dx[d]

                        if 0 <= y < n and 0 <= x < m and board[y][x] != 0 and visited[y][x] == False:
                            queue.append((y, x))
                            visited[y][x] = True
                            cnt += board[y][x]

                answer.append(cnt)

    print(answer)

    return [-1] if len(answer) == 0 else sorted(answer)