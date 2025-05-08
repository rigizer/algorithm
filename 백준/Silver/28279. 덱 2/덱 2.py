from collections import deque

result = []
dq = deque()
for _ in range(int(input())):
    s = list(map(int, input().split()))
    n = s[0]
    x = s[1] if n == 1 or n == 2 else None
    size = len(dq)

    if n == 1:
        dq.appendleft(x)
    elif n == 2:
        dq.append(x)
    elif n == 3 or n == 4:
        if size == 0:
            result.append(-1)
        elif size == 1:
            result.append(dq.pop())
        else:
            result.append(dq.popleft() if n == 3 else dq.pop())
    elif n == 5:
        result.append(size)
    elif n == 6:
        result.append(1 if size == 0 else 0)
    elif n == 7 or n == 8:
        if size == 0:
            result.append(-1)
        elif size == 1:
            result.append(dq[0])
        else:
            result.append(dq[0] if n == 7 else dq[-1])

print('\n'.join(str(i) for i in result))