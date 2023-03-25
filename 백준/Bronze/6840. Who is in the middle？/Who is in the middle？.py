a, b, c = int(input()), int(input()), int(input())
if b <= a <= c or c <= a <= b:
    print(a)
elif a <= b <= c or c <= b <= a:
    print(b)
else:
    print(c)