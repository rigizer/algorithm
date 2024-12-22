num = int(input())
if num < 10:
    print(num)
else:
    n = 1
    while len(str(num)) != n:
        if str(num)[-n] == '5':
            num = (num // (10 ** n) + 1) * (10 ** n)
        else:
            num = round(num, -n)
        n += 1
    print(num)