n = int(input())
c = list(input())

min_y, min_x = 50, 50
max_y, max_x = 50, 50
y, x = 50, 50
board = [['#'] * 100 for _ in range(100)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dir = 2

board[50][50] = '.'
for command in c:
    if command == 'L':
        dir = ((dir + 4) - 1) % 4
    elif command == 'R':
        dir = ((dir + 4) + 1) % 4
    elif command == 'F':
        y += dy[dir]
        x += dx[dir]
        board[y][x] = '.'

        min_y, min_x = min(min_y, y), min(min_x, x)
        max_y, max_x = max(max_y, y), max(max_x, x)

for i in range(min_y, max_y + 1):
    for j in range(min_x, max_x + 1):
        print(board[i][j], end='')
    print()