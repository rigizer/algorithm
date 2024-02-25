while True:
    n = input()
    if n == '#':
        break
    v = n[0]
    d = n[2::]
    r = d.count(v) + d.count(v.upper())
    print(v, r)