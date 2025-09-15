import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, a, b = map(int, input().split())
need = n * 3

if m >= need:
    result = 0
else:
    result = (need - m) * a + b

print(result)