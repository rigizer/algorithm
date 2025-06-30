import heapq

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: (x[0], x[1]))

busy = []
free = []
cnt = []

for start, end in data:
    while busy and busy[0][0] <= start:
        _, idx = heapq.heappop(busy)
        heapq.heappush(free, idx)
    if free:
        idx = heapq.heappop(free)
    else:
        idx = len(cnt)
        cnt.append(0)
    cnt[idx] += 1
    heapq.heappush(busy, (end, idx))

print(len(cnt))
print(' '.join(map(str, cnt)))