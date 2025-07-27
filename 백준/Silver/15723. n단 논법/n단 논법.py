from collections import deque

def bfs(graph, start, end):
    queue = deque()
    visited = set()

    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        
        if current == end:
            return 'T'
        
        if current in graph.keys():
            for nx in graph.get(current):
                if nx not in visited:
                    queue.append(nx)
                    visited.add(nx)
    
    return 'F'

n = int(input())
graph = {}
for i in range(n):
    pr = list(map(str, input().split()))
    if pr[0] not in graph.keys():
        graph[pr[0]] = [pr[2]]
    else:
        graph[pr[0]].append(pr[2])

m = int(input())
for i in range(m):
    cc = list(map(str, input().split()))
    result = bfs(graph, cc[0], cc[2])
    print(result)