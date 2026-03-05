import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
result = []

for _ in range(t):
    x = input()
    
    s = 0
    for c in x:
        s += ord(c) - ord('0')
    
    if s % 9 == 0:
        result.append('YES')
    else:
        result.append('NO')

print('\n'.join(result))