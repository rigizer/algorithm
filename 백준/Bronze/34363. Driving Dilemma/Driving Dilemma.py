import sys
input = lambda: sys.stdin.readline().rstrip()

s = int(input())
d = float(input())
t = float(input())

speed = s * 5280 / 3600
time_needed = d / speed

if time_needed <= t:
    print('MADE IT')
else:
    print('FAILED TEST')