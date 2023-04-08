for _ in range(int(input())):
    s = input()
    r = []

    for i in s:
        if len(r) == 0:
            r.append(i)
        else:
            if r[len(r) - 1] != i:
                r.append(i)

    print(''.join(i for i in r))
