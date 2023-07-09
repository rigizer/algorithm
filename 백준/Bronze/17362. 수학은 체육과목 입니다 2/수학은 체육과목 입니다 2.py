n = int(input())
a = n % 8

if a != 0 and a <= 5:
    print(a)
else:
    if a == 0:
        print('2')
    else:
        a = 10 - a
        print(a)