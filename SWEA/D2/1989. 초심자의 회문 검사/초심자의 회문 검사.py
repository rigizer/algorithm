for t in range(1, int(input()) + 1):
    d = input()
    print('#{} {}'.format(t, 1 if d == d[::-1] else 0))