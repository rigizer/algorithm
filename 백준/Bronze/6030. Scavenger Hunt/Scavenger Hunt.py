import sys
input = lambda: sys.stdin.readline().rstrip()

def get_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

P, Q = map(int, input().split())

p_divs = get_divisors(P)
q_divs = get_divisors(Q)

for x in p_divs:
    for y in q_divs:
        print(x, y)