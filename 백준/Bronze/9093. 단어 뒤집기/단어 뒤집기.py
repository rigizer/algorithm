for _ in range(int(input())):
    n = input().split()

    for i in n:
        print(i[::-1], end=' ')
    print()