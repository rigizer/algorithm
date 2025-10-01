m = list(map(int, input().split()))
n = int(input())

result = 0
for _ in range(n):
    b, l, s = input().split()
    b = int(b)
    l = float(l)
    s = int(s)
    
    if s >= 17 and l >= 2.0:
        result += m[b]

print(result)