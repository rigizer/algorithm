t = int(input())
for _ in range(t):
    d, n, s, p = map(int, input().split())

    if d + n * p < n * s:
        print('parallelize')
    elif d + n * p > n * s:
        print('do not parallelize')
    else:
        print('does not matter')