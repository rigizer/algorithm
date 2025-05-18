from collections import deque

while True:
    data = list(map(int, input().split()))
    if data[0] == 0: break
    stack = deque()

    def func(idx, depth):
        global n
        if depth == 7:
            print(*stack)
            return

        for i in range(idx, len(data)):
            stack.append(data[i])
            func(i + 1, depth + 1)
            stack.pop()

    func(1, 1)
    print()