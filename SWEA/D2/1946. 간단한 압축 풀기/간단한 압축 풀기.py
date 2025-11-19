tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    c = ''
    for _ in range(n):
        a, b = input().split()
        c += a * int(b)
    
    print(f'#{t}')
    for i in range(0, len(c), 10):
        print(c[i:i+10])