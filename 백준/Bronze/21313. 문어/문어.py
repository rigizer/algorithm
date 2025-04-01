n = int(input())
result = []
for i in range(n):
    if n % 2 == 1 and i == n - 1:
        result.append(3)
    else:
        result.append(1 if i % 2 == 0 else 2)
print(*result)