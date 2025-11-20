tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    board = [[0] * 10 for _ in range(10)]
    
    count = 0
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if board[i][j] == 0:
                    board[i][j] = color
                elif board[i][j] != color and board[i][j] != 3:
                    board[i][j] = 3
                    count += 1
    
    print(f'#{t} {count}')