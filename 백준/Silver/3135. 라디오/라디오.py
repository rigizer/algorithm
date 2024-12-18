a, b = map(int, input().split())
result = abs(a - b)

for _ in range(int(input())):
    k = int(input())
    if result > abs(k - b):
        result = abs(k - b) + 1

print(result)