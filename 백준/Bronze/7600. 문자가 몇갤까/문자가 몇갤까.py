while True:
    s = input()
    if s == '#':
        break
    a = [0] * 26
    for i in s.lower():
        if i.isalpha():
            a[ord(i) - 97] = 1
        else:
            continue
    print(a.count(1))