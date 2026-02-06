import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

counts = {}

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s = i + j
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1

max_count = max(counts.values())

result = []
for k in counts:
    if counts[k] == max_count:
        result.append(k)

result.sort()

for v in result:
    print(v)