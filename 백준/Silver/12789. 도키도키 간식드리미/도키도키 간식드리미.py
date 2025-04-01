from collections import deque

n = int(input())
queue = deque(map(int, input().split()))
stack = []

number = 1
while queue or stack:
    if queue and queue[0] == number:
        queue.popleft()
        number += 1
    elif stack and stack[-1] == number:
        stack.pop()
        number += 1
    elif queue:
        stack.append(queue.popleft())
    else:
        print('Sad')
        exit()

print('Nice')