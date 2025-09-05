import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = 1299710
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

primes = [i for i in range(MAX + 1) if is_prime[i]]

t = int(input())
result = []
for _ in range(t):
    k = int(input())
    if is_prime[k]:
        result.append('0')
    else:
        left = right = k
        while not is_prime[left]:
            left -= 1
        while not is_prime[right]:
            right += 1
        result.append(str(right - left))
print('\n'.join(result))