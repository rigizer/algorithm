import sys
import heapq

input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    x = int(input())

    if x == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, -x)