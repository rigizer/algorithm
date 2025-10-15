import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
r = list(map(int, input().split()))
result = 0
for _ in range(n - 1):
    s = list(map(int, input().split()))
    for i in range(m):
        s[i] = abs(r[i] - s[i])
    
    result += 1 if 2000 < sum(s) else 0

print('YES' if (n - 1) / 2 <= result else 'NO')