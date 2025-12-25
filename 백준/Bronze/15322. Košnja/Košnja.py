import sys
input = lambda: sys.stdin.readline().rstrip()

k = int(input())
result = []

for _ in range(k):
    n, m = map(int, input().split())
    if n == 1 or m == 1:
        result.append('0')
    else:
        result.append(str(2 * (min(n, m) - 1)))

print('\n'.join(result))