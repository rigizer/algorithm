import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
a.sort()

l, r = 0, n - 1
park = 0
seongwoo = 0

for turn in range(n):
    if turn % 2 == 0:
        park += a[r]
        r -= 1
    else:
        seongwoo += a[l]
        l += 1

print(seongwoo, park)