from collections import deque

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
stack = deque()

def func(num, depth):
    global n, m
    if depth == m + 1:
        print(*stack)
        return

    for i in range(num, n):
        stack.append(data[i])
        func(i, depth + 1)
        stack.pop()

func(0, 1)