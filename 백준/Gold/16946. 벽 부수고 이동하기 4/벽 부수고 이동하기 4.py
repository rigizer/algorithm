from collections import deque

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def bfs(n, m, board):
    result = [[0] * m for _ in range(n)]

    queue = deque()

    group_info = [[0] * m for _ in range(n)]
    group_cnt = {}  # 각 그룹 별 방문 가능한 수 체크
    group_num = 1   # 0이면 방문하지 않음, 1 이상이면 해당하는 그룹 번호

    # 0이 묶여있는 그룹 먼저 확인
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and group_info[i][j] == 0:
                queue.append((i, j))
                group_info[i][j] = group_num
                group_cnt[group_num] = 1

                while queue:
                    y, x = queue.popleft()

                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < n and 0 <= nx < m:
                            if board[ny][nx] == 0 and group_info[ny][nx] == 0:
                                queue.append((ny, nx))
                                group_info[ny][nx] = group_num
                                group_cnt[group_num] += 1
                        
                group_num += 1

    # 벽을 순회하면서 자기 자신과 상하좌우의 그룹에 대해 방문 가능한 수 확인
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                group_check = [] # 같은 그룹을 중복해서 더하지 않기 위함
                visit_cnt = 1

                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]

                    if 0 <= ny < n and 0 <= nx < m:
                        if board[ny][nx] == 0:
                            group_n = group_info[ny][nx]

                            if group_n not in group_check:
                                visit_cnt += group_cnt[group_info[ny][nx]]
                                group_check.append(group_n)
                
                result[i][j] = visit_cnt % 10

    return result

n, m = map(int, input().split())
board = [[int(i) for i in input()] for _ in range(n)]

result = bfs(n, m, board)

for i in range(n):
    for j in range(m):
        print(result[i][j], end='')
    print()