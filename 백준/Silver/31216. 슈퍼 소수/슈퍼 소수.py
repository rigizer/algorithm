MAX = 400000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1) :
    if is_prime[i] :
        for j in range(i * i, MAX + 1, i) :
            is_prime[j] = False

primes = []
for i in range(2, MAX + 1) :
    if is_prime[i] :
        primes.append(i)

super_primes = []
for idx in range(1, len(primes) + 1) :
    if is_prime[idx] :
        super_primes.append(primes[idx - 1])
    if len(super_primes) >= 3000 :
        break

t = int(input())
for _ in range(t) :
    n = int(input())
    print(super_primes[n - 1])