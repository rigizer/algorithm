n, m = map(int, input().split(':'))
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
a = gcd(n, m)
print('%d:%d' % (n // a, m // a))