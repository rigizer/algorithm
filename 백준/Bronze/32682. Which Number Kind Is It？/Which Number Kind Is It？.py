import sys
from math import isqrt
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())

    is_odd = (n % 2 == 1)
    r = isqrt(n)
    is_square = (r * r == n)

    if is_odd and is_square:
        print('OS')
    elif is_odd:
        print('O')
    elif is_square:
        print('S')
    else:
        print('EMPTY')