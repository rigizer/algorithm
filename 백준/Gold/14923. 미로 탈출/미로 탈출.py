from collections import deque

LIMIT = 1

def bfs(n, m, sy, sx, ey, ex, board):
    queue = deque()
    visited = [[[False] * m for _ in range(n)] for _ in range(LIMIT + 1)]

    # 출발 좌표 (y, x), 이동시간, 지팡이 사용 횟수
    queue.append((sy - 1, sx - 1, 0, 0))
    visited[0][sy - 1][sx - 1] = True

    while queue:
        ny, nx, nt, nw = queue.popleft()

        if (ny, nx) == (ey - 1, ex - 1):
            return nt
        
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            # 미로 안에서 이동할 수 있는 경우 확인
            if 0 <= y < n and 0 <= x < m:
                # 지팡이를 사용하지 않는 경우
                if board[y][x] == 0 and visited[nw][y][x] == False:
                    queue.append((y, x, nt + 1, nw))
                    visited[nw][y][x] = True

                # 지팡이를 사용하는 경우
                if nw < LIMIT and board[y][x] == 1 and visited[nw + 1][y][x] == False:
                    queue.append((y, x, nt + 1, nw + 1))
                    visited[nw + 1][y][x] = True
    
    return -1

n, m = map(int, input().split())
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = bfs(n, m, sy, sx, ey, ex, board)
print(result)