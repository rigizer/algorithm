n = int(input())

a, b, c, d = map(int, input().split())
result = ((c - a) + (d - b)) * 2
print(result)

for _ in range(n - 1):
    na, nb, nc, nd = map(int, input().split())
    
    if na < a:
        a = na
    if nb < b:
        b = nb
    if nc > c:
        c = nc
    if nd > d:
        d = nd
    
    result = ((c - a) + (d - b)) * 2
    print(result)