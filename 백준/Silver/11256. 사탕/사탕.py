for _ in range(int(input())):
    j, n = map(int, input().split())
    data = []
    for i in range(n):
        r, c = map(int, input().split())
        data.append(r * c)
    data.sort(reverse=True)
    count = 0
    while j > 0:
        j -= data[count]
        count += 1
    print(count)