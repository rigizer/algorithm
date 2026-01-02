import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = input()

for k in range(1, n + 1):
    seen = set()
    ok = True
    for i in range(n - k + 1):
        part = s[i:i + k]
        if part in seen:
            ok = False
            break
        seen.add(part)
    if ok:
        print(k)
        break