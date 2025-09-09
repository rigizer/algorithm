import sys
input = lambda: sys.stdin.readline().rstrip()

def key_number(n):
    factors = set()
    x = n
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.add(d)
            while x % d == 0:
                x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        factors.add(x)
    if not factors:
        return 0
    max_prime = max(factors)
    return max_prime - (sum(factors) - max_prime)

result = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    ka = key_number(a)
    kb = key_number(b)
    if ka > kb:
        result.append('a')
    else:
        result.append('b')

print('\n'.join(result))