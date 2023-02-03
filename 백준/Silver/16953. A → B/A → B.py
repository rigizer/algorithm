from collections import deque

a, b = map(int, input().split())

def bfs(a, b):
    queue = deque()
    queue.append((a, 1))

    while queue:
        nx, nt = queue.popleft()

        if nx == b:
            return nt

        for x in [nx * 2, nx * 10 + 1]:
            if x <= b:
                queue.append((x, nt + 1))

    return -1

result = bfs(a, b)
print(result)