n = int(input())
a = [input() for _ in range(n)]
result = 1
before = a[0]
for i in range(1, n):
    if before != a[i]:
        before = a[i]
        result += 1
print(result + 1)