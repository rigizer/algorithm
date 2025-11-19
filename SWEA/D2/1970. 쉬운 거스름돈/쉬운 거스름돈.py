tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    
    r = [0] * 8
    for i, v in enumerate([50000, 10000, 5000, 1000, 500, 100, 50, 10]):
        r[i] = n // v
        n %= v
    
    print(f'#{t}')
    print(*r)