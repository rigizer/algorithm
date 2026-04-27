import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

def bfs():
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return result

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = list(map(int, input().split()))

order = [0] * (n + 1)
for i in range(n):
    order[answer[i]] = i

for i in range(1, n + 1):
    graph[i].sort(key=lambda x: order[x])

result = bfs()
print(int(result == answer))