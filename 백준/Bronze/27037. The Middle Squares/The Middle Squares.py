import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

seen = set()
cnt = 0

while n not in seen:
    seen.add(n)
    mid = (n // 10) % 100
    n = mid * mid
    cnt += 1

print(cnt)