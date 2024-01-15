e, f, c = map(int, input().split())
n = (e + f) // c + (e + f) % c
r = (e + f) // c
while n // c:
    r += n // c
    n = n // c + n % c
print(r)