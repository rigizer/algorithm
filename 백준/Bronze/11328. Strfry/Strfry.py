import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
n = int(input())
for _ in range(n):
    a, b = input().split()
    if sorted(a) == sorted(b):
        result.append('Possible')
    else:
        result.append('Impossible')

print('\n'.join(result))