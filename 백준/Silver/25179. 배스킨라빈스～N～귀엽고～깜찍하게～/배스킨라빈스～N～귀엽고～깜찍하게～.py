import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

if n % (m + 1) == 1:
    print('Can\'t win')
else:
    print('Can win')