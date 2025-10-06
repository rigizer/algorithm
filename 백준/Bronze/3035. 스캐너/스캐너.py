import sys
input = lambda: sys.stdin.readline().rstrip()

r, c, zr, zc = map(int, input().split())

arr = [input() for _ in range(r)]

for i in range(r):
    line = ''
    for j in range(c):
        line += arr[i][j] * zc
    for _ in range(zr):
        print(line)