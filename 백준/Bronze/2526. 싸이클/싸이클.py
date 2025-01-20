n, p = map(int, input().split())
l = []
a = n
while True:
    r = (a * n) % p
    if r in l:
        print(len(l) - l.index(r))
        break
    l.append(r)
    a = r