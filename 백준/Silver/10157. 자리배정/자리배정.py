c, r = map(int, input().split())

my_seat = int(input())

if my_seat > c * r:
    print(0)
    exit()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

grid = [[0] * c for _ in range(r)]
d = x = y = 0

for seat in range(1, c * r + 1):
    if seat == my_seat:
        print(y + 1, x + 1)
        break
    else:
        grid[x][y] = seat

        x += dx[d]
        y += dy[d]

        if x < 0 or y < 0 or x >= r or y >= c or grid[x][y]:
            x -= dx[d]
            y -= dy[d]

            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]