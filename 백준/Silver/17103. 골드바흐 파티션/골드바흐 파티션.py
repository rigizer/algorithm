import sys
input = lambda: sys.stdin.readline().rstrip()
MAX = 1_000_000

def get_prime():
    primes = [True] * (MAX + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(MAX**0.5) + 1):
        if primes[i]:
            for j in range(i * i, MAX + 1, i):
                primes[j] = False
    
    return primes    

t = int(input())
primes = get_prime()

answer = []
for _ in range(t):
    n = int(input())
    result = 0
    
    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            result += 1
    
    answer.append(result)

print('\n'.join(map(str, answer)))