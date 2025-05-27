def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

n, s = map(int, input().split())
a = [abs(s - i) for i in list(map(int, input().split()))]

result = a[0]
for i in range(1, n):
    result = gcd(result, a[i])
print(result)