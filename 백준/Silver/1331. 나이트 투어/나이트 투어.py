board = []
valid = True

for _ in range(36):
    board.append(input())

if len(set(board)) != 36:
    valid = False

for i in range(36):
    diffRow = abs(ord(board[i][0])-ord(board[i-1][0]))
    diffCol = abs(int(board[i][1])-int(board[i-1][1]))
    if (diffRow == 1 and diffCol == 2) or (diffRow == 2 and diffCol == 1):
        continue
    else:
        valid = False

if valid:
    print('Valid')
else:
    print('Invalid')