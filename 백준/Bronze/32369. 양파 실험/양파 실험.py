n, a, b = map(int ,input().split())
p, q = 1, 1

for _ in range(n):
    p += a
    q += b
    
    if p < q:
        p, q = q, p
    
    if p == q:
        q -= 1

print(p, q)