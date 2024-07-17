n = int(input())
result = 0
for i in range(len(str(n))):
    d = n % 10
    n = n // 10
    
    if d > 4:
        result += (d - 1) * (9 ** i)
    else:
        result += d * (9 ** i)
print(result)