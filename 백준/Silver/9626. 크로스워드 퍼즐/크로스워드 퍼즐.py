import sys
input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())
puzzle = [list(input()) for _ in range(m)]

board = [['#'] * (n + l + r) for _ in range(m + u + d)]

for i in range(m + u + d):
    for j in range(n + l + r):
        if (i + j) % 2 == 1:
            board[i][j] = '.'

for i in range(m):
    for j in range(n):
        board[i + u][j + l] = puzzle[i][j]

for i in range(m + u + d):
    for j in range(n + l + r):
        print(board[i][j], end='')
    print()