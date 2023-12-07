for _ in range(int(input())):
    n = list(input())
    k = len(n) // 2 - 1
    print('Do-it' if n[k] == n[-k - 1] else 'Do-it-Not')