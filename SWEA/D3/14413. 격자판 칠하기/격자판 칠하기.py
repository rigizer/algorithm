from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def check(n, m, a, queue, visited):
    while queue:
        ny, nx, nt = queue.popleft()

        for d in range(4):
            y = ny + dy[d]
            x = nx + dx[d]

            if 0 <= y < n and 0 <= x < m and visited[y][x] == False:
                    if nt == 0 and a[y][x] == '#':
                        return False
                    elif nt == 1 and a[y][x] == '.':
                        return False
                    
                    queue.append((y, x, 1 if nt == 0 else 0))
                    visited[y][x] = True

    return True

def calc(n, m, a):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if a[i][j] == '#' and visited[i][j] == False:
                queue.append((i, j, 0))
                visited[i][j] = True
                
            elif a[i][j] == '.' and visited[i][j] == False:
                queue.append((i, j, 1))
                visited[i][j] = True

            if check(n, m, a, queue, visited) == False:
                return False

    return True

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]

    result = calc(n, m, a)
    print('#{} {}'.format(t, 'possible' if result else 'impossible'))