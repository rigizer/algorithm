h, w = map(int, input().split())
cloud = [list(input()) for _ in range(h)]
result = [[-1] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if cloud[i][j] == 'c':
            result[i][j] = 0
        elif j > 0 and result[i][j - 1] >= 0:
            result[i][j] = result[i][j - 1] + 1

for i in range(h):
    print(*result[i])