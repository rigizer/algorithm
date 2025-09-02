import sys
input = lambda: sys.stdin.readline().rstrip()

a = input()
b = input()
c = input()

result = []

if c in a and c in b:
    result.append('YES')
else:
    result.append('NO')

print('\n'.join(result))