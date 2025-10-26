import sys
input = lambda: sys.stdin.readline().rstrip()

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

is_prime = sieve(10000)
t = int(input())

for _ in range(t):
    n = int(input())
    a = n // 2
    b = n // 2
    while a > 1:
        if is_prime[a] and is_prime[b]:
            print(a, b)
            break
        a -= 1
        b += 1