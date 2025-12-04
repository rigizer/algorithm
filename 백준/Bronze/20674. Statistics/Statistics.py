import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
prev = int(input())
result = 0

for _ in range(n - 1):
    cur = int(input())
    if cur <= prev:
        prev = cur
    else:
        result += cur - prev

print(result)