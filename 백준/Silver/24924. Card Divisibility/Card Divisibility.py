import sys
input = lambda: sys.stdin.readline().rstrip()

l, r = map(int, input().split())

n = r - l + 1
total = (l + r) * n // 2

print(total % 9)