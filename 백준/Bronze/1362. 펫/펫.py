cnt = 0
while True:
    death = 0
    cnt += 1
    o, w = map(int,input().split())
    if o == w == 0:
        break
    while True:
        a, b = input().split()
        if a == '#' and b == '0':
            break
        b = int(b)
        if a == 'F':
            w += b
        elif a == 'E':
            w -= b
        if w <= 0:
            death = 1
    print(cnt, end=' ')
    if death == 1:
        print('RIP')
    else:
        if w > o / 2 and w < o * 2:
            print(':-)')
        else:
            print(':-(')