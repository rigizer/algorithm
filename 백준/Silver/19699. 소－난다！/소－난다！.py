import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations

n, m = map(int, input().split())
h = list(map(int, input().split()))

max_sum = sum(sorted(h, reverse=True)[:m])

is_prime = [True] * (max_sum + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(max_sum ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_sum + 1, i):
            is_prime[j] = False

result = set()

for comb in combinations(h, m):
    s = sum(comb)
    if is_prime[s]:
        result.add(s)

if result:
    result = sorted(result)
    print(' '.join(map(str, result)))
else:
    print(-1)