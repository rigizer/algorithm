while True:
    try:
        line = input()

        if not line:
            break

        l, u, d, s = 0, 0, 0, 0
        for each in line:
            if each.islower():
                l += 1
            elif each.isupper():
                u += 1
            elif each.isdigit():
                d += 1
            elif each.isspace():
                s += 1

        print(l, u, d, s)
    except:
        break