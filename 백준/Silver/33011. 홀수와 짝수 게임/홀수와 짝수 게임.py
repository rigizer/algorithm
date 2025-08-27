t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd_cnt = sum(1 for x in a if x % 2 != 0)
    even_cnt = n - odd_cnt

    if odd_cnt == even_cnt:
        print('heeda0528')
    else:
        if max(odd_cnt, even_cnt) % 2 == 0:
            print('heeda0528')
        else:
            print('amsminn')