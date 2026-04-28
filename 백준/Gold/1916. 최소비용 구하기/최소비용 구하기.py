import sys
input = lambda: sys.stdin.readline().rstrip()

import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

INF = int(1e15)
dist = [INF] * (n + 1)
dist[start] = 0

pq = []
heapq.heappush(pq, (0, start))

while pq:
    cost, node = heapq.heappop(pq)
    if cost > dist[node]:
        continue
    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

print(dist[end])