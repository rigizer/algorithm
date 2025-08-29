import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
t = int(input())
for _  in range(t):
    s, p = input().split()
    cnt = len(s)
    s = s.replace(p, '')
    result.append(str(len(s) + (cnt - len(s)) // len(p)))

print('\n'.join(result))