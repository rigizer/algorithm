import sys
input = lambda: sys.stdin.readline().rstrip()

a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

score1 = a1 + a2 * 2 + a3 * 3
score2 = b1 + b2 * 2 + b3 * 3

if score1 > score2:
    print(1)
elif score1 < score2:
    print(2)
else:
    print(0)