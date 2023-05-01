a, b, c = map(int, input().split())

find = False
if a == b + c:
    print(f'{a}={b}+{c}')
elif a == b - c:
    print(f'{a}={b}-{c}')
elif a == b * c:
    print(f'{a}={b}*{c}')
elif a == b // c:
    print(f'{a}={b}/{c}')
elif a + b == c:
    print(f'{a}+{b}={c}')
elif a - b == c:
    print(f'{a}-{b}={c}')
elif a * b == c:
    print(f'{a}*{b}={c}')
elif a // b == c:
    print(f'{a}/{b}={c}')