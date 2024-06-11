a, b = list(map(int, input().split()))
x, y = list(map(int, input().split()))

n = (b * x + a * y)
d = b * y

def GCD(i, j):
    while j:
        i, j = j, i % j
    return i

gcd = GCD(n, d)

n = int(n / gcd)
d = int(d / gcd)

print(f'{n} {d}')