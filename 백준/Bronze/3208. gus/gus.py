n, m = map(int, input().split())
total = n * m
result = 0
idx = 0
while True:
    if total <= 0:
        break

    if idx % 2 == 0:
        total -= m
        result += 1
        n -= 1
    else:
        total -= n
        result += 1
        m -= 1
    
    idx += 1

print(result - 1)