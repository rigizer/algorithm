n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 1
for n in data:
    result *= n
print(result % m)