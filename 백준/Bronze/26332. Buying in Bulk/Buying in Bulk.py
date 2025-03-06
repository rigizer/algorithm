def sol(cnt, price):
    if cnt>1:
        return cnt*price-(cnt-1)*2
    else:
        return price
 
n = int(input())
for _ in range(n):
    cnt, price = map(int, input().split())
    print(cnt, price)
    print(sol(cnt, price))