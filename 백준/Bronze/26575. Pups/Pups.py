import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for i in range(n):
    d, f, p = map(float, input().split())
    result = d * f * p
    if i == n - 1:
        print(f'${result:.2f}')
    else:
        print(f'${result:.2f}')