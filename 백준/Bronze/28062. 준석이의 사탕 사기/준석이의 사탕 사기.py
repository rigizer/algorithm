import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
candy = list(map(int, input().split()))

if n == 1 and candy[0] % 2 == 1:
    print(0)
else:
    odd_cnt = sum([1 if i % 2 == 1 else 0 for i in candy])
    
    if odd_cnt % 2 == 0:
        print(sum(candy))
    else:
        min_odd = 1e9
        for i in candy:
            if i % 2 == 1:
                min_odd = min(min_odd, i)
        
        print(sum(candy) - min_odd)