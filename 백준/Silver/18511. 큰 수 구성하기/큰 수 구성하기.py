from itertools import product

n , k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
leng = len(str(n))

while True:
    cand = list(product(arr,repeat = leng))
    ret = []
    
    for i in cand:
        temp = int(''.join(map(str, i)))
        if temp <= n:
            ret.append(temp)
            
    if len(ret) >= 1:
        print(max(ret))
        break
    else:
        leng -= 1