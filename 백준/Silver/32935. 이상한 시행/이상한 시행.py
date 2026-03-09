import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

s = sum(a)
m = min(a)

print(max(s, -m))