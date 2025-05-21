n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]

prev = color[0][:]

for i in range(1, n):
    r = min(prev[1], prev[2]) + color[i][0]
    g = min(prev[0], prev[2]) + color[i][1]
    b = min(prev[0], prev[1]) + color[i][2]
    prev = [r, g, b]

print(min(prev))