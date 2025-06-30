def get_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, v in enumerate(is_prime) if v]

primes = get_primes(2 * 10 ** 6)
t = int(input())
ks = [int(input()) for _ in range(t)]

for k in ks:
    min_product = float('inf')
    for i in range(len(primes)):
        p1 = primes[i]
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            product = p1 * p2
            if product >= k:
                min_product = min(min_product, product)
                break
        if p1 * p1 > k:
            break
    print(min_product)