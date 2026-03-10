import sys
input = lambda: sys.stdin.readline().rstrip()

R, G = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

g = gcd(R, G)

result = []
i = 1

while i * i <= g:
    if g % i == 0:
        result.append(i)
        if i * i != g:
            result.append(g // i)
    i += 1

for n in result:
    print(f'{n} {R//n} {G//n}')