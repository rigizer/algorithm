import sys
input = sys.stdin.readline

INF = 10**30

n = int(input())

min_x, max_x = -INF, INF
min_y, max_y = -INF, INF

for _ in range(n):
    x, y, d = input().split()
    x = int(x)
    y = int(y)

    if d == 'L':
        max_x = min(max_x, x - 1)
    elif d == 'R':
        min_x = max(min_x, x + 1)
    elif d == 'D':
        max_y = min(max_y, y - 1)
    elif d == 'U':
        min_y = max(min_y, y + 1)

if min_x > max_x or min_y > max_y:
    print(0)
elif min_x == -INF or max_x == INF or min_y == -INF or max_y == INF:
    print('Infinity')
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))