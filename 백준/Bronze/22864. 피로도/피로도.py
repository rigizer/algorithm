a, b, c, m = map(int, input().split())
t = 0
dw = 0

for i in range(24):
    if t > m:
        print(0)
    else:
        if t + a <= m:
            t += a
            dw += b
        else:
            if t - c >= 0:
                t -= c
            else:
                t = 0
print(dw)