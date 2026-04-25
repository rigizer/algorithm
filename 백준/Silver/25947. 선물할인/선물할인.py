import sys
input = lambda: sys.stdin.readline().rstrip()

n, b, a = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()

import heapq

sum_all = 0
sum_disc = 0
disc_heap = []

result = 0

for p in prices:
    sum_all += p
    heapq.heappush(disc_heap, p)
    sum_disc += p

    if len(disc_heap) > a:
        removed = heapq.heappop(disc_heap)
        sum_disc -= removed

    cost = sum_all - (sum_disc // 2)

    if cost <= b:
        result += 1
    else:
        break

print(result)