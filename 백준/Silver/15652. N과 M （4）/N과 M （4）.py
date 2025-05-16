from collections import deque

n, m = map(int, input().split())
stack = deque()

def func(num, depth):
    global n, m
    if depth == m + 1:
        print(*stack)
        return

    for i in range(num, n + 1):
        stack.append(i)
        func(i, depth + 1)
        stack.pop()

func(1, 1)