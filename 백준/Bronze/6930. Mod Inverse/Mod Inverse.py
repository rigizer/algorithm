import sys
input = lambda: sys.stdin.readline().rstrip()

x = int(input())
m = int(input())

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, s, t = egcd(b, a % b)
    return g, t, s - (a // b) * t

g, s, t = egcd(x, m)

if g != 1:
    print('No such integer exists.')
else:
    result = s % m
    print(result)