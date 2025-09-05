import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for i in range(n):
    for j in range(n * 2):
        if (i + j) % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()