import sys

n, m = map(int, input().split())
cubes = set()
for _ in range(m):
    i, j, k = map(int, input().split())
    cubes.add((i, j, k))

dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

result = 0
for i, j, k in cubes:
    ok = True
    for di, dj, dk in dirs:
        if (i + di, j + dj, k + dk) not in cubes:
            ok = False
            break
    if ok:
        result += 1

print(result)