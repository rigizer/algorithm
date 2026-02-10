import sys
input = lambda: sys.stdin.readline().rstrip()

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i:limit + 1:i] = [False] * (((limit - i * i) // i) + 1)
    return [i for i in range(2, limit + 1) if is_prime[i]]

def factor_semiprime(n, primes):
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return p, n // p
    return n, 1

m = int(input())
nums = [int(input()) for _ in range(m)]

primes = sieve(65536)
factors = set()

for x in nums:
    a, b = factor_semiprime(x, primes)
    factors.add(a)
    if a != b:
        factors.add(b)

arr = sorted(factors)

out = []
for i in range(0, len(arr), 5):
    out.append(' '.join(map(str, arr[i:i + 5])))

print('\n'.join(out))