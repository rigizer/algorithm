import sys
input = lambda: sys.stdin.readline().rstrip()

a1, b1, a2, b2 = map(int, input().split())
c1, d1, c2, d2 = map(int, input().split())

gunnar_sums = []
for x in range(a1, b1 + 1):
    for y in range(a2, b2 + 1):
        gunnar_sums.append(x + y)

emma_sums = []
for x in range(c1, d1 + 1):
    for y in range(c2, d2 + 1):
        emma_sums.append(x + y)

gunnar_win = 0
emma_win = 0

for g in gunnar_sums:
    for e in emma_sums:
        if g > e:
            gunnar_win += 1
        elif g < e:
            emma_win += 1

if gunnar_win > emma_win:
    print('Gunnar')
elif gunnar_win < emma_win:
    print('Emma')
else:
    print('Tie')