import sys
input = lambda: sys.stdin.readline().rstrip()

result = []

while True:
    line = input()
    if not line:
        break

    parts = line.split()
    d = float(parts[0])
    n = int(parts[1])

    if d == 0.0 and n == 0:
        break

    points = []
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))

    d2 = d * d
    sour = [False] * n

    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            dx = xi - xj
            dy = yi - yj
            if dx * dx + dy * dy < d2:
                sour[i] = True
                sour[j] = True

    sour_count = 0
    for v in sour:
        if v:
            sour_count += 1
    sweet_count = n - sour_count

    result.append(f'{sour_count} sour, {sweet_count} sweet')

for line in result:
    print(line)