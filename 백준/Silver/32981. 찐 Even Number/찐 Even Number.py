import sys
input = lambda: sys.stdin.readline().rstrip()

mod = 1_000_000_007

q = int(input())
result = []

for _ in range(q):
    n = int(input())
    
    if n == 1:
        result.append('5')
    else:
        v = 4 * pow(5, n - 1, mod) % mod
        result.append(str(v))

print('\n'.join(result))