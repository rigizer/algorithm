import sys
input = lambda: sys.stdin.readline().rstrip()

left = list(input())
right = []
m = int(input())

for _ in range(m):
    cmd = input()
    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[2])

left.extend(reversed(right))
print(''.join(left))