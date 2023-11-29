for _ in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    r = 0
    for i in d:
        r += i // k
    print(r)