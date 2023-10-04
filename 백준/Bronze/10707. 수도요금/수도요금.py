a, b, c, d, p = int(input()), int(input()), int(input()), int(input()), int(input())

if p > c:
    result = b + (p - c) * d
else:
    result = b

print(min(a * p, result))