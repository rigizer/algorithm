for i in range(1, int(input()) + 1):
    a, b, c = map(int, input().split())

    if a == b == c:
        print(f'Case #{i}: equilateral')
    elif max([a, b, c]) < sum([a, b, c]) - max([a, b, c]) and (a == b or b == c or c == a):
        print(f'Case #{i}: isosceles')
    elif max([a, b, c]) < sum([a, b, c]) - max([a, b, c]):
        print(f'Case #{i}: scalene')
    else:
        print(f'Case #{i}: invalid!')