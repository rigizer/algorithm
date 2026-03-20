import sys
input = lambda: sys.stdin.readline().rstrip()

p, n = map(int, input().split())
board = [0] * p

for turn in range(n):
    pos = int(input()) - 1
    color = 1 if turn % 2 == 0 else 2
    opp = 2 if color == 1 else 1

    board[pos] = color

    for d in (-1, 1):
        temp = []
        j = pos + d

        while 0 <= j < p:
            if board[j] == opp:
                temp.append(j)
                j += d
            elif board[j] == color:
                if temp:
                    for x in temp:
                        board[x] = 0
                break
            else:
                break

white = board.count(1)
black = board.count(2)

print(white, black)