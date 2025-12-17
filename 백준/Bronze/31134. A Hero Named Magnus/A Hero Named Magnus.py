import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    x = int(input())
    print(2 * x - 1)