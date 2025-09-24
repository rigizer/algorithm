import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
for _ in range(n):
    list(map(int, input().split()))
print('비와이')