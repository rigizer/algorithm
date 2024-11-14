from sys import stdin

board = [[False] * 101 for _ in range(101)]
n, m = map(int, stdin.readline().split())

for _ in range(n):
    x1, y1, x2, y2 = map(int, stdin.readline().split())

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] is False:
                board[i][j] = 1
            else:
                board[i][j] += 1

res = 0
for i in range(1, 101):
    for j in range(1, 101):
        if board[i][j] > m:
            res += 1

print(res)