import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
for _ in range(int(input())):
    n = int(input())
    x = int(2 ** (n / 2))
    if n % 2 == 0:
        result.append(str(x))
    else:
        result.append(str(0))
print('\n'.join(result))