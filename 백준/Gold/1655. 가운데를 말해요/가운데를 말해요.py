import sys
input = lambda: sys.stdin.readline().rstrip()

import heapq

n = int(input())
left = []
right = []

for _ in range(n):
    x = int(input())
    
    if not left or x <= -left[0]:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)
    
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(left) < len(right):
        heapq.heappush(left, -heapq.heappop(right))
    
    print(-left[0])