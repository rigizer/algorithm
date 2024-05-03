import math

def prim(start):
    global n, line

    visited = set()
    visited.add(start)
    dist = 0

    for _ in range(n - 1):
        min_dist = 1e9
        next_node = -1

        for i in visited:
            for j in range(n):
                if j not in visited and 0 < line[i][j] < min_dist:
                    min_dist = line[i][j]
                    next_node = j
        
        dist += min_dist
        visited.add(next_node)

    return dist

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
line = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        line[i][j] = round(math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2), 2)
        line[j][i] = line[i][j]

print(prim(0))