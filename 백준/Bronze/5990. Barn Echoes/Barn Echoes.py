import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
t = input()

n = len(s)
m = len(t)

result = 0

for k in range(1, min(n, m) + 1):
    if s[:k] == t[m - k:]:
        if k > result:
            result = k
    if t[:k] == s[n - k:]:
        if k > result:
            result = k

print(str(result))