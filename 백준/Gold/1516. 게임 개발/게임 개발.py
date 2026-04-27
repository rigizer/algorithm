import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

result = time[:]
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if result[nxt] < result[cur] + time[nxt]:
            result[nxt] = result[cur] + time[nxt]
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1, n + 1):
    print(result[i])