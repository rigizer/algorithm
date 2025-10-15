import sys
input = lambda: sys.stdin.readline().rstrip()

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

px = (p + t) % (2 * w)
if px > w:
    x = 2 * w - px
else:
    x = px

py = (q + t) % (2 * h)
if py > h:
    y = 2 * h - py
else:
    y = py

print(str(x) + ' ' + str(y), end='')