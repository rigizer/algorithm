import sys
input = lambda: sys.stdin.readline().rstrip()

board = [list(input()) for _ in range(8)]

rows = set()
cols = set()
diag1 = set()  # r - c
diag2 = set()  # r + c

queen_count = 0
valid = True

for r in range(8):
    for c in range(8):
        if board[r][c] == '*':
            queen_count += 1

            if r in rows or c in cols or (r - c) in diag1 or (r + c) in diag2:
                valid = False
                break

            rows.add(r)
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
    if not valid:
        break

if queen_count != 8:
    valid = False

print('valid' if valid else 'invalid')