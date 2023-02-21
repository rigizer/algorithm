from collections import deque

queue = deque()
n, k = map(int, input().split())

for i in range(1, n + 1):
    queue.append(i)

result = []
idx = 0
while queue:
    idx += 1
    t = queue.popleft()

    if idx % k == 0:
        result.append(t)
    else:
        queue.append(t)

print('<{}>'.format(', '.join(str(i) for i in result)))