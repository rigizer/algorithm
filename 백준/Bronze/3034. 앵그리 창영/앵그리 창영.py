n, w, h = map(int, input().split())

for _ in range(n):
    leng = int(input())
    m = ((w ** 2) + (h ** 2)) ** 0.5
    
    if m >= leng:
        print('DA')
    else:
        print('NE')