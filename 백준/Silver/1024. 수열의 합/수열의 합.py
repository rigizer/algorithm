def calc(n, l):
    for i in range(l, 101):
        val = n - (i * (i - 1) // 2)
        if val % i != 0:
            continue
        m = val // i
        if m < 0:
            continue
        result = [m + j for j in range(i)]
        print(*result)
        exit()

n, l = map(int, input().split())
result = calc(n, l)
print(-1)