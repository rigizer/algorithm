from collections import deque

def init_queue(queue, n):
    for i in range(1, n + 1):
        queue.append(i)

queue = deque()
n = int(input())

init_queue(queue, n)

result = 0
while queue:
    now = queue.popleft()

    if len(queue) == 0:
        result = now
    else:
      queue.append(queue.popleft())

print(result)