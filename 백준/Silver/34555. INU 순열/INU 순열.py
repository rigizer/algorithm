import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
an = []
bn = []

x = n // 2 + 1
for i in range(x, n + 1):
    an.append(i)
for i in range(x - 1, 0, -1):
    bn.append(i)

for i in range(n // 2):
    print(an[i], bn[i], end=' ')

if n % 2 == 1:
    print(n)