for _ in range(int(input())) :
    result = 0
    for i in range(int(input())) :
        i, cnt, price = input().split()
        result += float(cnt) * float(price)
    print('$%.2f' % result)