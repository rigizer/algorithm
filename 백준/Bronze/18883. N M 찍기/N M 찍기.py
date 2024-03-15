n, m = map(int, input().split())
for i in range(n):
    print(' '.join([str(x) for x in range((i * m) + 1, ((i + 1) * m) + 1)]))