import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

k = m
print(k)

for i in range(m):
    row = []
    for j in range(n):
        row.append(a[(i + j) % m][j])
    print(*row)