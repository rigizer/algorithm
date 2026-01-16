import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

CP_START = 6 * 60 + 30
CP_END = 19 * 60

times = []

for _ in range(n):
    h, m = map(int, input().split(':'))
    t = h * 60 + m
    if CP_START <= t <= CP_END:
        times.append(t)

if not times:
    print(0)
    sys.exit(0)

first = min(times)
last = max(times)

if first <= 10 * 60:
    if last <= 16 * 60:
        result = 24000
    else:
        result = 36000
else:
    if last <= 16 * 60:
        result = 16800
    else:
        result = 24000

print(result)