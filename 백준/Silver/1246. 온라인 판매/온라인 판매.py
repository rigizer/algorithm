n, m = map(int, input().split())
lst = [int(input()) for i in range(m)]

s = 0
price = 0
lst.sort()

for i in lst :
    if (m - lst.index(i)) > n:
        continue
    x = i * (m - lst.index(i))
    if s < x :
        s = x
        price = i
        
print(price, s)