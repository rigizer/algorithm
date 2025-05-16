from collections import deque

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
stack = deque()

def func(depth):
    global n, m
    if depth == m + 1:
        print(*stack)
        return

    for i in range(n):
        stack.append(data[i])
        func(depth + 1)
        stack.pop()

func(1)