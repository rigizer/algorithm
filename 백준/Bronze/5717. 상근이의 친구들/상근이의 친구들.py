while True:
    m, w = map(int, input().split())
    if (m, w) == (0, 0):
        break
    print(m + w)