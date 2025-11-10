import sys
input = lambda: sys.stdin.readline().rstrip()

n, k, l = map(int, input().split())

result = []
count = 0

for _ in range(n):
    x1, x2, x3 = map(int, input().split())
    if x1 >= l and x2 >= l and x3 >= l:
        s = x1 + x2 + x3
        if s >= k:
            count += 1
            result.extend([x1, x2, x3])

print(count)
if count > 0:
    print(' '.join(map(str, result)))