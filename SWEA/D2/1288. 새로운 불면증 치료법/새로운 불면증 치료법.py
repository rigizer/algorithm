for t in range(1, int(input()) + 1):
    n = int(input())
    i = 1

    number = {
                0: False, 1: False, 2: False, 3: False, 4: False, 
                5: False, 6: False, 7: False, 8: False, 9: False
            }

    while True:
        num = n * i

        temp = list(str(num))
        for a in temp:
            number[int(a)] = True

        if False in number.values():
            i += 1
            continue

        break

    print('#{} {}'.format(t, n * i))