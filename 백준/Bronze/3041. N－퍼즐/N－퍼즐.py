import sys
input = lambda: sys.stdin.readline().rstrip()

goal = {}
letters = 'ABCDEFGHIJKLMNO'
for i, c in enumerate(letters):
    goal[c] = (i // 4, i % 4)

board = [input() for _ in range(4)]

result = 0
for i in range(4):
    for j in range(4):
        c = board[i][j]
        if c != '.':
            gi, gj = goal[c]
            result += abs(i - gi) + abs(j - gj)

print(result)