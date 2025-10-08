import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    t = int(input())
    t %= 25
    if t < 17:
        print('ONLINE')
    else:
        print('OFFLINE')