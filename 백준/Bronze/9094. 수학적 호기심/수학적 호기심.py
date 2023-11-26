for _ in range(0, int(input())):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n):
            a, b = i, j
            if (a**2 + b**2 + m) % (a * b) == 0:
                cnt += 1
    print(cnt)