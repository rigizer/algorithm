for i in range(int(input())):
    n = int(input())
    
    mok, nam = n // 5, n % 5
    for _ in range(mok):
        print('++++', end=' ')
    
    for _ in range(nam):
        print('|', end='')
    print()