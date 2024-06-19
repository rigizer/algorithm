def jinsu(n, m):
    s = 0
    while True:
        if n // m == 0:
            s += n
            break
        s += n%m
        n = n // m
    return s

for i in [2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999]:
    print(i)
for i in range(3000, 10000):
    if sum(list(map(int, list(str(i))))) == jinsu(i, 12) == jinsu(i, 16):
        print(i)