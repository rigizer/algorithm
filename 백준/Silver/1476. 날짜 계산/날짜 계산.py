import sys
input = lambda: sys.stdin.readline().rstrip()

E, S, M = map(int, input().split())

year = 1
e = s = m = 1

while True:
    if e == E and s == S and m == M:
        print(year)
        break

    year += 1

    e += 1
    if e == 16:
        e = 1

    s += 1
    if s == 29:
        s = 1

    m += 1
    if m == 20:
        m = 1