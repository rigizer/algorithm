import sys
input = lambda: sys.stdin.readline().rstrip()

r, f = map(int, input().split())
x = 180 / r * f

if x < 90:
    print('up')
else:
    x -= 90
    i = 1
    while True:
        if i % 2 == 0:
            answer = 'up'
        else:
            answer = 'down'
        if 180 * (i - 1) <= x <= 180 * i:
            print(answer)
            break
        i += 1