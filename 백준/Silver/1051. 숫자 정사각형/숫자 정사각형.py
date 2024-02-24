n, m = map(int, input().split())
square = []
for _ in range(n):
    square.append(list(input()))

size = min(n, m)
for k in range(size, 0, -1):
    for i in range(n):
        for j in range(m):
            if ((i + k) < n) and ((j + k) < m) and (square[i][j] == square[i][j + k] == square[i + k][j] == square[i + k][j + k]):
                print((k + 1) ** 2)
                exit()
else:
    print(1)