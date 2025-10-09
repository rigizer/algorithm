import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
result = []
x = n // 2 + 1

for i in range(n // 2):
    result.append(str(x + i))
    result.append(str(x - 1 - i))

if n % 2 == 1:
    result.append(str(n))

print(' '.join(result), end='')