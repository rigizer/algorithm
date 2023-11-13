for _ in range(int(input())) :
    n, m = map(int, input().split())
    u = (m * 2) - n
    t = n - m
    print(u, t)