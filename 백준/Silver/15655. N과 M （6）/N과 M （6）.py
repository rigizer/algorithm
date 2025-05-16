from collections import deque

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
visited = [False] * (n + 1)
stack = deque()

def func(num, depth):
    global n, m
    if depth == m + 1:
        print(*stack)
        return

    for i in range(num, n):
        if not visited[i]:
            visited[i] = True
            stack.append(data[i])
            func(i + 1, depth + 1)
            stack.pop()
            visited[i] = False

func(0, 1)