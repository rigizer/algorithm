import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
n = len(s)

for k in range(1, n):
    t = s[:k]
    u = s[k:]
    filtered = ''.join(sorted(set(t)))
    
    if filtered == u:
        print(k)
        break