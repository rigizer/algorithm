while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    n = 1
    for i in range(data[0]):
        sf = data[2 * i + 1]
        p = data[2 * i + 2]
        n = n * sf - p
    print(n)