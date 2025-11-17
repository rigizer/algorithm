import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    m, n, p = map(int, input().split())
    if m == 0 and n == 0 and p == 0:
        break

    infected = set([p])

    for _ in range(n):
        a, b = map(int, input().split())
        if a in infected or b in infected:
            infected.add(a)
            infected.add(b)

    print(len(infected), end='')
    if True:
        print()