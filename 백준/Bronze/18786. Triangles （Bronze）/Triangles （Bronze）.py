import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_x = {}
max_x = {}
min_y = {}
max_y = {}

for x, y in points:
    if y not in min_x:
        min_x[y] = x
        max_x[y] = x
    else:
        min_x[y] = min(min_x[y], x)
        max_x[y] = max(max_x[y], x)

    if x not in min_y:
        min_y[x] = y
        max_y[x] = y
    else:
        min_y[x] = min(min_y[x], y)
        max_y[x] = max(max_y[x], y)

result = 0

for x, y in points:
    horizontal = max(abs(x - min_x[y]), abs(x - max_x[y]))
    vertical = max(abs(y - min_y[x]), abs(y - max_y[x]))
    result = max(result, horizontal * vertical)

print(result)