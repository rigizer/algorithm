while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break
    i = 0
    while i ** n < b:
        i += 1
    print(i if i ** n - b < b - (i - 1) ** n else i - 1)