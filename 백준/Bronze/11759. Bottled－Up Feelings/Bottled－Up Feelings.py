import sys
input = lambda: sys.stdin.readline().rstrip()

s, v1, v2 = map(int, input().split())

result = None
x = s // v1

while x >= 0:
    remain = s - x * v1
    if remain % v2 == 0:
        y = remain // v2
        result = (x, y)
        break
    x -= 1

if result is None:
    print('Impossible')
else:
    print(result[0], result[1])