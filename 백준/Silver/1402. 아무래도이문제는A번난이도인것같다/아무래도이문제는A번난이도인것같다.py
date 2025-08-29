import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
result = []
for _ in range(t):
    a, b = map(int, input().split())
    result.append('yes')

print('\n'.join(result))