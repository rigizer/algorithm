from collections import deque

# h: board의 높이
# w: board의 너비
# n: 치즈 경도의 최대치
h, w, n = map(int, input().split())

# S: 시작지점 (둥지)
board = [[j for j in input().strip()] for _ in range(h)]

def bfs_init(h, w, n, board, queue, visited):
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'S':
                board[i][j] = '.'

                queue.append((i, j, 0, 1))
                visited[0][i][j] = True
                
                return
            
def bfs(h, w, n, board):
    queue = deque()
    visited = [[[False] * w for _ in range(h)] for _ in range(n + 1)]
    bfs_init(h, w, n, board, queue, visited)
    while queue:
        ny, nx, nt, ne = queue.popleft()
        
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < h and 0 <= x < w and board[y][x] != 'X' and board[y][x] != 'S':
                # 치즈를 먹지 않은 경우 주변지역 탐색
                if board[y][x] == '.':
                    # board가 .이면서 방문한 적이 없는 경우
                    if visited[ne][y][x] == False:
                        queue.append((y, x, nt + 1, ne))
                        visited[ne][y][x] = True
                
                elif 1 <= int(board[y][x]) <= n and visited[ne][y][x] == False:
                    # 치즈를 먹고 체력이 1 증가한 경우
                    if int(board[y][x]) == ne:
                        # 모든 치즈를 다 먹은 경우
                        if ne + 1 == n + 1:
                            return nt + 1
                        
                        queue.append((y, x, nt + 1, ne + 1))
                        visited[ne + 1][y][x] = True
                      
                    # 지금 먹어야 할 치즈가 아닌 경우
                    else:
                        queue.append((y, x, nt + 1, ne))
                        visited[ne][y][x] = True

result = bfs(h, w, n, board)
print(result)