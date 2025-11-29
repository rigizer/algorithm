import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    s = a + b + c
    if s != 180:
        print(f'{a} {b} {c} Check')
    else:
        print(f'{a} {b} {c} Seems OK')