from collections import deque

n = int(input())
queue = deque()
queue.append([n])
answer = []

while queue:
    a = queue.popleft()
    x = a[0]
    if x == 1:
        answer = a
        break

    if x % 3 == 0:
        queue.append([x // 3] + a)

    if x % 2 == 0:
        queue.append([x // 2] + a)
    
    queue.append([x - 1] + a)

print(len(answer) - 1)
print(*answer[::-1])