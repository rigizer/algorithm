from collections import deque

def bfs(s, t):
    queue = deque()
    visited = []

    queue.append((s, ''))
    visited.append(s)

    while queue:
        nx, calc = queue.popleft()

        if nx == t:
            if calc == '':
                return 0

            return calc

        for d in range(4):
            if d == 0:
                x = nx * nx
                c = '*'
            elif d == 1:
                x = nx + nx
                c = '+'
            elif d == 2:
                x = nx - nx
                c = '-'
            elif d == 3 and nx != 0:
                x = nx // nx
                c = '/'

            if 0 <= x <= max(s, t) and x not in visited:
                queue.append((x, calc + c))
                visited.append(x)

    return -1

s, t = map(int, input().split())
result = bfs(s, t)

print(result)