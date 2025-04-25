n, a, d = map(int, input().split())
ns = list(map(int, input().split()))

i = a
result = 0

for num in ns:
    if num == i:
        result += 1
        i += d

print(result)