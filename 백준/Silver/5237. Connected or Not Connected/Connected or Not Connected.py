from collections import deque

def bfs(n, graph):
    result = 0

    queue = deque()
    visited = [False] * n

    queue.append(0)
    visited[0] = True
    result += 1

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                result += 1

    return 'Connected.' if result == n else 'Not connected.'

for _ in range(int(input())):
    data = list(map(int, input().split()))
    n, k = data[0], data[1]
    del data[0:2]

    graph = [[] for _ in range(n)]

    for i in range(0, k * 2, 2):
        a = data[i]
        b = data[i + 1]
        
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(n, graph))