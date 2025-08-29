import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t = list(map(int, input().split()))
t.sort()

mid = (n - 1) // 2
res = [t[mid]]

for i in range(1, mid + 1):
    if mid + i < n:
        res.append(t[mid + i])
    res.append(t[mid - i])

if n % 2 == 0:
    res.append(t[-1])

print(' '.join(map(str, res)))