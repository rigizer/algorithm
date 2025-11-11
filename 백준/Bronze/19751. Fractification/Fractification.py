import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import permutations

a, b, c, d = map(int, input().split())
arr = [a, b, c, d]

best_num = None
best_den = None
result = None

for p in permutations(arr, 4):
    x, y, z, w = p
    num = x * w + z * y
    den = y * w
    if best_num is None or num * best_den < best_num * den:
        best_num = num
        best_den = den
        result = p

print(' '.join(map(str, result)))