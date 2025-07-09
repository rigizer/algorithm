for _ in range(int(input())):
    k, n = input().split()
    octa = int(n, 8) if max(map(int, n)) < 8 else 0
    deci = int(n)
    hexa = int(n, 16)
    print(f'{k} {octa} {deci} {hexa}')