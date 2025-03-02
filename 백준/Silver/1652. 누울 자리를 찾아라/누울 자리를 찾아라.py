n = int(input())
board = [list(input()) for _ in range(n)]

result = [0, 0]
for i in range(n):
    leng_r, leng_c = 0, 0
    for j in range(n):
        if board[i][j] == '.':
            leng_r += 1
        else:
            leng_r = 0
        if leng_r == 2:
            result[0] += 1
        
        if board[j][i] == '.':
            leng_c += 1
        else:
            leng_c = 0
        if leng_c == 2:
            result[1] += 1
print(*result)