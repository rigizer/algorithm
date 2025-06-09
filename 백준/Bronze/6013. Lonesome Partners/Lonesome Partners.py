n = int(input())
coords = [tuple(map(int, input().split())) for _ in range(n)]
max_dist_sq = -1
result = (0, 0)

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if dist_sq > max_dist_sq:
            max_dist_sq = dist_sq
            result = (i + 1, j + 1)

print(*sorted(result))