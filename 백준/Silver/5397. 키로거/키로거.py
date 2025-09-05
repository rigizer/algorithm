import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
t = int(input())
for _ in range(t):
    keys = input()
    left = []
    right = []
    for k in keys:
        if k == '<':
            if left:
                right.append(left.pop())
        elif k == '>':
            if right:
                left.append(right.pop())
        elif k == '-':
            if left:
                left.pop()
        else:
            left.append(k)
    left.extend(reversed(right))
    result.append(''.join(left))

print('\n'.join(result))