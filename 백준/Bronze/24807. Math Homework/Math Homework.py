import sys
input = lambda: sys.stdin.readline().rstrip()

b, d, c, l = map(int, input().split())

answers = []

for x in range(0, l // b + 1):
    remain_x = l - b * x
    for y in range(0, remain_x // d + 1):
        remain_y = remain_x - d * y
        if remain_y % c == 0:
            z = remain_y // c
            answers.append((x, y, z))

if not answers:
    print('impossible')
else:
    for x, y, z in answers:
        print(x, y, z)