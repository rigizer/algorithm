d, h, m = map(int, input().split())
t1 = d * 24 * 60 + h * 60 + m
t2 = 11 * 24 * 60 + 11 * 60 + 11
t = t1 - t2
if t < 0:
    print(-1)
else:
    print(t)