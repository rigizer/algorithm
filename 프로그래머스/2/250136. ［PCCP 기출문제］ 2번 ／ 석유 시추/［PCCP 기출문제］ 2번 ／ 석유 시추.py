from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(land, n, m):
    queue = deque()
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    type_list = {}
    type_num = 0
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == False:
                cnt = 1
                type_num += 1
                queue.append((i, j))
                visited[i][j] = True
                board[i][j] = type_num
                
                while queue:
                    y, x = queue.popleft()
                    
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        
                        if 0 <= ny < n and 0 <= nx < m and land[ny][nx] == 1 and visited[ny][nx] == False:
                            queue.append((ny, nx))
                            visited[ny][nx] = True
                            board[ny][nx] = type_num
                            cnt += 1
                
                type_list[type_num] = cnt
    
    return board, type_list

def solution(land):
    answer = 0
    
    n, m = len(land), len(land[0])
    board, type_list = bfs(land, n, m)
    
    for j in range(m):
        temp = 0
        temp_list = []
        for i in range(n):
            if land[i][j] == 1:
                temp_list.append(board[i][j])
        
        temp_list = set(temp_list)
        temp = sum([type_list.get(i) for i in temp_list])
        
        answer = max(answer, temp)
    
    return answer