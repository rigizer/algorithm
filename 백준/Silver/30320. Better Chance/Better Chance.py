import sys
input = lambda: sys.stdin.readline().rstrip()

r1, r2, s1, s2 = map(float, input().split())
r1 = (r1 - 1) / s1
r2 = (r2 - 1) / s2

if abs(r2 - r1) < 1e-9:
    print('SAME')
elif r1 > r2:
    print('JAKARTA')
else:
    print('TAOYUAN')