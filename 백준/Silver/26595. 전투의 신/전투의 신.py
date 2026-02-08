import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a, pa, b, pb = map(int, input().split())

maxx = n // pa
maxy = n // pb

bestv = -1
bestx = 0
besty = 0

if maxx <= maxy:
    for x in range(maxx + 1):
        rem = n - pa * x
        y = rem // pb
        v = a * x + b * y
        if v > bestv:
            bestv = v
            bestx = x
            besty = y
else:
    for y in range(maxy + 1):
        rem = n - pb * y
        x = rem // pa
        v = a * x + b * y
        if v > bestv:
            bestv = v
            bestx = x
            besty = y

print(f'{bestx} {besty}')