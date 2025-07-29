def calc(n):
    s = 0
    q = n
    while True:
        r = q % 10
        q //= 10
        s += r
    
        if q == 0:
            break

    s = 9 - (s % 9)
    if s == 9:
        s = 0

    result = []

    o = 0
    while True:
        r = n % (10 ** o)
        q = n // (10 ** o)

        a = (q * (10 ** (o + 1))) + (s * (10 ** o)) + r
        if a % 9 == 0:
            if not (q == 0 and s == 0):
                result.append(a)

        if q == 0:
            break
        
        o += 1
    
    return min(result)

for tc in range(int(input())):
    n = int(input())
    result = calc(n)
    print(f'Case #{tc + 1}: {result}')