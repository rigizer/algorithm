from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# queue 초기화
def init(n, m, board, queue, visited):
    for i in range(n):
        for j in range(m):
            if board[i][j] == '0':
                # 현재위치 (y, x), 거리, 키 상태 (000000 ~ 111111)
                queue.append((i, j, 0, 0))
                board[i][j] = '.'
                visited[i][j][0] = True
                return

def bfs(n, m, board):
    queue = deque()
    visited = [[[False] * (2 ** 6) for _ in range(m)] for _ in range(n)]

    init(n, m, board, queue, visited)

    while queue:
        ny, nx, nt, nk = queue.popleft()

        # 현재 탐색하고 있는 위치가 탈출가능 하다면 최단거리 (BFS)
        if board[ny][nx] == '1':
            return nt
        
        # 현재 탐색하고 있는 위치로부터 4방향 탐색
        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            # 앞으로 이동할 위치가 미로 범위 내에 있는지 확인
            if 0 <= y < n and 0 <= x < m:
                
                # 키를 들고 있는 상태가 같지 않으면서, 방문한 적이 없었는지 확인
                if visited[y][x][nk] == False:
                    
                    # 현재 위치가 1 혹은 .이라면
                    if board[y][x] == '1' or board[y][x] == '.':
                        queue.append((y, x, nt + 1, nk))
                        visited[y][x][nk] = True
                    
                    # 영문 소문자 a, b, c, d, e, f (키 획득)
                    elif 'a' <= board[y][x] <= 'f':
                        # 현재 획득한 키에 대해 쉬프트 연산 후, or 연산
                        # OR 연산 : 둘 중 하나라도 1이면 1, 아니면 0
                        # 오른쪽에 키가 위치하면 OR 연산을 통해 키 획득
                        tk = nk | (1 << (ord(board[y][x]) - ord('a')))
                        
                        queue.append((y, x, nt + 1, tk))
                        visited[y][x][tk] = True

                    # 영문 대문자 A, B, C, D, E, F (문에 도착)
                    elif 'A' <= board[y][x] <= 'F':
                        
                        # 문에 해당하는 키를 가지고 있는지 확인
                        # AND 연산 : 양쪽 모두 1이면 1, 아니면 0
                        # 문과 비교해서 키를 가지고 있으면 AND 연산을 통해 True 반환
                        if nk & (1 << (ord(board[y][x]) - ord('A'))):
                            # 키를 가지고 있는 경우에만 문을 열고 이동가능
                            queue.append((y, x, nt + 1, nk))
                            visited[y][x][nk] = True

    return -1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

result = bfs(n, m, board)
print(result)