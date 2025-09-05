import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for i in range(n):
    if i == 0:
        print(' ' * (n - 1) + '*')
    else:
        inner = 2 * i - 1
        print(' ' * (n - 1 - i) + '*' + ' ' * inner + '*')