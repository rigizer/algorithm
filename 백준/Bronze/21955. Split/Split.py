n = int(input())
l = n // (10 ** (len(str(n)) // 2))
r = n % (10 ** (len(str(n)) // 2))
print(*[l, r])