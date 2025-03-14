for _ in range(int(input())):
    n = int(input())
    lst = [i for i in range(1, n) if n % i == 0]
    if sum(lst) < n: print(n, 'is a deficient number.')
    elif sum(lst) == n: print(n, 'is a perfect number.')
    else: print(n, 'is an abundant number.')
    print()