import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    a, d, v = map(int, input().split())
    if a == 0 and d == 0 and v == 0:
        break

    diff = v - a

    if diff % d != 0:
        print('X')
        continue

    n = diff // d + 1

    if n >= 1:
        print(n)
    else:
        print('X')