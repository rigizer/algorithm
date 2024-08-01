n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ms = [list(map(int, input().split())) for _ in range(m)]

# 누적합 구하기
s = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        s[i][j] = s[i][j-1] + s[i-1][j] - s[i-1][j-1] + board[i-1][j-1]

# 범위별 합 구하기
result = []
for x1, y1, x2, y2 in ms:
    result.append(s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1])

# 결과 출력하기
for i in result:
    print(i)