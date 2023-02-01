from collections import deque

def bfs(n, k):
    queue = deque()
    visited = [1e9] * 100_001

    queue.append((n, 0))
    visited[n] = 0

    while queue:
        nx, nt = queue.popleft()

        if nx == k:
            return nt
        
        # 수빈이가 순간이동 할 때
        x = nx * 2
        if is_move(x, nt, visited):
            queue.append((x, nt))
            visited[x] = nt

        # 수빈이가 걸어갈 때
        for dx in [-1, 1]:
            x = nx + dx
            if is_move(x, nt + 1, visited):
                queue.append((x, nt + 1))
                visited[x] = nt + 1

def is_move(x, t, visited):
    if 0 <= x <= 100_000 and t < visited[x]:
        return True

n, k = map(int, input().split())
result = bfs(n, k)
print(result)