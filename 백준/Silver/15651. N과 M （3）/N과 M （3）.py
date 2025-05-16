from collections import deque

n, m = map(int, input().split())
stack = deque()

def func(depth):
    global n, m
    if depth == m + 1:
        print(*stack)
        return

    for i in range(1, n + 1):
        stack.append(i)
        func(depth + 1)
        stack.pop()

func(1)