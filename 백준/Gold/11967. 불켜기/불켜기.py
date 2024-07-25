from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, board, light_info):
    result = 1
    queue = deque()
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    visited_rooms = [[False] * (n + 1) for _ in range(n + 1)]

    queue.append((1, 1))
    visited[1][1] = True
    visited_rooms[1][1] = True

    while queue:
        y, x = queue.popleft()

        if (y, x) in light_info:
            for ly, lx in light_info[(y, x)]:
                if not board[ly][lx]:
                    board[ly][lx] = True
                    result += 1

                    for d in range(4):
                        ny = ly + dy[d]
                        nx = lx + dx[d]

                        if 1 <= ny <= n and 1 <= nx <= n and visited[ny][nx]:
                            queue.append((ly, lx))
                            visited[ly][lx] = True
                            break

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 1 <= ny <= n and 1 <= nx <= n and board[ny][nx] and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True

    return result

n, m = map(int, input().split())
light_info = {}

board = [[False] * (n + 1) for _ in range(n + 1)]  # 해당 방에 불이 켜져있는지 저장
board[1][1] = True

for _ in range(m):
    x, y, a, b = map(int, input().split())
    if (x, y) in light_info:
        light_info[(x, y)].append((a, b))
    else:
        light_info[(x, y)] = [(a, b)]

result = bfs(n, board, light_info)
print(result)