from collections import deque

stack = deque()

n, m = map(int, input().split())
ball = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())

    for x in range(i, j + 1):
        stack.append(ball[x])
    
    for x in range(i, j + 1):
        ball[x] = stack.pop()

print(' '.join(str(ball[i]) for i in range(1, n + 1)))