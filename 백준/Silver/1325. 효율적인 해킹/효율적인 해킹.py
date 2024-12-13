from collections import deque

def bfs(i):
    visited = [0] * (n + 1)
    queue = deque([i])
    visited[i] = 1
    cnt = 1

    while queue:
        x = queue.popleft()

        for nx in computer[x]:
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = 1
                cnt += 1

    return cnt

n, m = map(int, input().split())
computer = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int,input().split())
    computer[b].append(a)

answer = []
max_hack = 0
for i in range(1, n + 1):
    result = bfs(i)
    
    if max_hack < result:
        max_hack = result
        answer.clear()
        answer.append(i)
    elif max_hack == result:
        answer.append(i)

print(*answer)